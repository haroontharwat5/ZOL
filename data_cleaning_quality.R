# ---- Libraries ----
library(readxl)
library(writexl)
library(dplyr)
library(lubridate)
library(readr)
library(stringr)

# ---- Load data ----
data <- read_excel("data.xlsx", sheet = "data")

# ---- Drop unused columns (if present) ----
drop_cols <- intersect(names(data), c("Plan_24u_StartDT", "Plan_24u_EindDT"))
if (length(drop_cols) > 0) {
  data <- dplyr::select(data, -all_of(drop_cols))
}

# ---- Rename columns to English (assumes order match) ----
names(data) <- c(
  "PatientID",
  "SurgeryDateTime",
  "Year",
  "Weekday",
  "StartHour",
  "ProcedureCode",
  "ProcedureName",
  "AdmissionType",
  "LengthOfStay",
  "LengthOfStayWithoutRevalidation",
  "UrgencyType",
  "PlannedStartDT",
  "PlannedEndDT",
  "PlannedDurationMinutes",
  "PlannedOR",
  "ActualOR",
  "ORIn",
  "OROut",
  "DurationMinutes",
  "HeadSurgeonID",
  "AnesthesiologistID"
)

data <- data %>%
  mutate(
    PlannedStartDT = readr::parse_datetime(PlannedStartDT, format = "%Y-%m-%d %H:%M", na = c("", "NA")),
    PlannedEndDT   = readr::parse_datetime(PlannedEndDT, format = "%Y-%m-%d %H:%M", na = c("", "NA")),
    PlannedDurationMinutes = as.numeric(difftime(PlannedEndDT, PlannedStartDT, units = "mins"))
  )

# ---- Ensure datetime columns are POSIXct ----
data <- data %>%
  mutate(across(
    c(SurgeryDateTime, PlannedStartDT, PlannedEndDT, ORIn, OROut),
    ~ if (!lubridate::is.POSIXct(.)) {
      readr::parse_datetime(as.character(.), "%Y-%m-%d %H:%M", na = c("", "NA"))
    } else {
      .
    }
  ))

# ---- SHIFTS ----
bucket_to_shift <- function(dt, end_dt = NULL, default_tz = "Europe/Brussels") {
  d  <- as_date(dt)
  hr <- hour(dt) + minute(dt) / 60
  tz_used <- attr(dt, "tzone")
  if (is.null(tz_used)) tz_used <- default_tz
  
  # ---- Basis shift_start op basis van beleid ----
  ss <- ifelse(is.na(dt), NA, NA)
  ss <- ifelse(!is.na(dt) & hr >= 8   & hr < 16.5,  as.numeric(d + hours(8)), ss)
  ss <- ifelse(!is.na(dt) & hr >= 16.5 & hr < 22,   as.numeric(d + hours(16) + minutes(30)), ss)
  ss <- ifelse(!is.na(dt) & hr >= 22,                as.numeric(d + hours(22)), ss)
  ss <- ifelse(!is.na(dt) & hr < 8,                  as.numeric((d - days(1)) + hours(22)), ss)
  ss <- as.POSIXct(ss, origin = "1970-01-01", tz = tz_used)
  
  # ---- Basis shift_end ----
  se <- ifelse(is.na(ss), NA, NA)
  se <- ifelse(!is.na(ss) & hour(ss) == 8,                                as.numeric(as_date(ss) + hours(16) + minutes(30)), se)
  se <- ifelse(!is.na(ss) & hour(ss) == 16 & minute(ss) == 30,            as.numeric(as_date(ss) + hours(22)),               se)
  se <- ifelse(!is.na(ss) & hour(ss) == 22,                               as.numeric(as_date(ss) + days(1) + hours(8)),      se)
  se <- as.POSIXct(se, origin = "1970-01-01", tz = tz_used)
  
  # ---- Herclassificeer vroege starters (07:30–08:00 die doorlopen na 08:00) ----
  if (!is.null(end_dt)) {
    crosses_8 <- difftime(end_dt, floor_date(dt, "day") + hours(8), units = "mins") > 0
    
    ss <- ifelse(
      !is.na(dt) & hr >= 7.5 & hr < 8 & crosses_8,
      as.numeric(d + hours(8)),
      ss
    )
    se <- ifelse(
      !is.na(dt) & hr >= 7.5 & hr < 8 & crosses_8,
      as.numeric(as_date(d + hours(8)) + hours(16) + minutes(30)),
      se
    )
    
    ss <- as.POSIXct(ss, origin = "1970-01-01", tz = tz_used)
    se <- as.POSIXct(se, origin = "1970-01-01", tz = tz_used)
  }
  
  # ---- Label ----
  lab <- ifelse(is.na(ss), NA_character_, NA_character_)
  lab <- ifelse(!is.na(ss) & hour(ss) == 8,                   "08:00–16:30", lab)
  lab <- ifelse(!is.na(ss) & hour(ss) == 16 & minute(ss)==30, "16:30–22:00", lab)
  lab <- ifelse(!is.na(ss) & hour(ss) == 22,                  "22:00–08:00", lab)
  
  data.frame(shift_start = ss, shift_end = se, shift_label = lab)
}

# ---- Shift bounds based on ORIn (effective in-room time) ----
eff_shift <- bucket_to_shift(data$ORIn, end_dt = data$OROut)
data <- bind_cols(data, eff_shift) %>%
  rename(shift_start = shift_start, shift_end = shift_end, shift_label = shift_label)

# ---- Planned shift bucket (based on PlannedStartDT) for comparison only ----
# This does NOT drive afterhours/overtime — it's only used to see if the case moved shifts.
plan_shift <- bucket_to_shift(data$PlannedStartDT, end_dt = data$PlannedEndDT)
names(plan_shift) <- c("planned_shift_start", "planned_shift_end", "planned_shift_label")
data <- bind_cols(data, plan_shift)

# ---- Derived variables (planned vs observed) ----

# Verschil tussen feitelijke start en geplande start (in minuten)
data <- data %>%
  mutate(
    start_diff = as.numeric(difftime(ORIn, PlannedStartDT, units = "mins"))
  )

# Verschil tussen feitelijke duur en geplande duur (in minuten)
data <- data %>%
  mutate(
    duration_diff = DurationMinutes - PlannedDurationMinutes
  )

# Verschil tussen feitelijke eindtijd en geplande eindtijd (in minuten)
data <- data %>%
  mutate(
    end_diff = as.numeric(difftime(OROut, PlannedEndDT, units = "mins"))
  )

# Percentage afwijking t.o.v. geplande duur
data <- data %>%
  mutate(
    percentage_deviation = if_else(
      is.na(PlannedDurationMinutes) | PlannedDurationMinutes <= 0,
      NA_real_,
      (DurationMinutes - PlannedDurationMinutes) / PlannedDurationMinutes * 100
    )
  )

# Indicator of de ingreep buiten de shiftgrenzen viel (op basis van ORIn)
data <- data %>%
  mutate(
    afterhours_flag = if_else(
      is.na(ORIn) | is.na(OROut) | is.na(shift_start) | is.na(shift_end),
      NA_integer_,
      as.integer(OROut > shift_end) 
    )
  )

# Aantal minuten overwerk na shift_end (nooit negatief)
data <- data %>%
  mutate(
    overtime_minutes = if_else(
      is.na(OROut) | is.na(shift_end),
      NA_real_,
      pmax(0, as.numeric(difftime(OROut, shift_end, units = "mins")))
    )
  )

# Geplande minuten na shift_end (relatieve maatstaf)
data <- data %>%
  mutate(
    .planned_afterhours_minutes = case_when(
      is.na(PlannedStartDT) | is.na(PlannedEndDT) | is.na(shift_end) ~ NA_real_,
      PlannedEndDT <= shift_end ~ 0,
      PlannedStartDT >= shift_end ~ as.numeric(difftime(PlannedEndDT, PlannedStartDT, units = "mins")),
      TRUE ~ as.numeric(difftime(PlannedEndDT, shift_end, units = "mins"))
    )
  )

# Relatieve overwerkminuten t.o.v. geplande afterhours binnen dezelfde shift
data <- data %>%
  mutate(
    relative_overtime_minutes = if_else(
      is.na(overtime_minutes) | is.na(.planned_afterhours_minutes) | .planned_afterhours_minutes <= 0,
      NA_real_,
      overtime_minutes / .planned_afterhours_minutes
    )
  )

# Indicator of de operatie in een andere kamer plaatsvond dan gepland
data <- data %>%
  mutate(
    room_swap = if_else(
      is.na(PlannedOR) | is.na(ActualOR),
      NA_integer_,
      as.integer(PlannedOR != ActualOR)
    )
  )

# Ratio tussen feitelijke en geplande duur (planningsnauwkeurigheid)
data <- data %>%
  mutate(
    planning_ratio = if_else(
      is.na(PlannedDurationMinutes) | PlannedDurationMinutes <= 0,
      NA_real_,
      DurationMinutes / PlannedDurationMinutes
    )
  )

# Indicator of de ingreep naar een andere shift is verplaatst dan gepland
data <- data %>%
  mutate(
    moved_to_other_shift = case_when(
      is.na(planned_shift_label) ~ NA_integer_,   # geen geplande start, onbekend
      is.na(shift_label) ~ NA_integer_,           # geen effectieve ORIn, onbekend
      TRUE ~ as.integer(planned_shift_label != shift_label)  # 1 als andere shift, anders 0
    )
  )


# ---- GAP TIME per OR × "realistic" shift window for efficiency only ----
# 07:30–16:30, 16:30–22:00, 22:00–08:00
# -> uses flexible start for first morning case, but keeps official shift labels untouched

data <- data %>%
  mutate(
    gapshift_date = as_date(ORIn),
    gapshift_label = case_when(
      hour(ORIn) + minute(ORIn)/60 >= 7.5 & hour(ORIn) + minute(ORIn)/60 < 16.5 ~ "07:30–16:30",
      hour(ORIn) + minute(ORIn)/60 >= 16.5 & hour(ORIn) + minute(ORIn)/60 < 22   ~ "16:30–22:00",
      TRUE ~ "22:00–08:00"
    ),
    # shift date correction for late-night cases (assign 22:00–08:00 to previous day)
    gapshift_date = if_else(gapshift_label == "22:00–08:00" & hour(ORIn) < 8,
                            gapshift_date - days(1), gapshift_date)
  ) %>%
  arrange(ActualOR, gapshift_date, gapshift_label, ORIn) %>%
  group_by(ActualOR, gapshift_date, gapshift_label) %>%
  mutate(
    .prev_out = lag(OROut),
    gap_raw   = as.numeric(difftime(ORIn, .prev_out, units = "mins")),
    gap_time  = case_when(
      is.na(ORIn) | is.na(.prev_out) ~ NA_real_,    # eerste case in de shift
      gap_raw < 0                    ~ 0,           # overlap => 0
      gap_raw > 120                  ~ NA_real_,    # te lange idle -> niet als efficiëntie
      TRUE                           ~ gap_raw
    )
  ) %>%
  ungroup() %>%
  select(-.prev_out, -gap_raw, -gapshift_date, -gapshift_label)


# ---- reorder everything ----
desired_order <- c(
  "PatientID","SurgeryDateTime","Year","Weekday","StartHour",
  "AdmissionType","UrgencyType",
  "ProcedureCode","ProcedureName",
  "HeadSurgeonID","AnesthesiologistID",
  "LengthOfStay","LengthOfStayWithoutRevalidation",
  "PlannedOR","ActualOR","room_swap",
  "PlannedStartDT","ORIn","start_diff",
  "PlannedEndDT","OROut","end_diff",
  "PlannedDurationMinutes","DurationMinutes",
  "duration_diff","percentage_deviation","planning_ratio",
  "planned_shift_label","shift_label","moved_to_other_shift",
  "planned_shift_start","shift_start",
  "planned_shift_end","shift_end",
  "planned_afterhours_minutes","afterhours_flag","overtime_minutes","relative_overtime_minutes",
  "gap_time"
)

cols_in_data <- intersect(desired_order, names(data))
data <- data %>% select(all_of(cols_in_data), everything())

# ---- Split datasets by campus (based on first character of ActualOR) ----
first_char <- substr(as.character(data$ActualOR), 1, 1)

genk    <- dplyr::filter(data, first_char == "G")
maaseik <- dplyr::filter(data, first_char == "M")
lanaken <- dplyr::filter(data, first_char == "L")
cathlab <- dplyr::filter(data, first_char == "K")
other   <- dplyr::filter(data, !(first_char %in% c("G","M","L","K")) | is.na(first_char))

# Cathlab: keep only rows with non-empty anesthesiologist
cathlab <- cathlab %>%
  filter(!is.na(AnesthesiologistID) & AnesthesiologistID != "")

# ---- Write outputs to subfolder 'modified data' ----
if (!dir.exists("modified data")) dir.create("modified data")

write_xlsx(data,    "modified data/data_cleaned.xlsx")
write_xlsx(genk,    "modified data/genk_cleaned.xlsx")
write_xlsx(maaseik, "modified data/maaseik_cleaned.xlsx")
write_xlsx(lanaken, "modified data/lanaken_cleaned.xlsx")
write_xlsx(cathlab, "modified data/cathlab_cleaned.xlsx")
write_xlsx(other,   "modified data/other_cleaned.xlsx")