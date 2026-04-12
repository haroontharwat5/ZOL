# The ZOL paper in plain English

A non-technical explanation of what we did, what we found, and why it matters. Written so you can explain it to anyone — your family, a hospital director, or a co-author who hasn't read the full draft.

---

## What is this paper about?

We looked at how four hospital sites within the same Belgian hospital group (ZOL) perform in their operating rooms. These four sites are part of one organization — same management, same computer systems, same employment contracts — but they run very different types of surgery programs.

The question we're asking is: **when you compare operating-room performance across these sites, are the differences real, or are they an illusion created by the fact that the sites do different things?**

---

## The four sites

**Genk** is the big hospital. It has 26 operating rooms, does everything from routine day procedures to complex overnight surgeries, and stays open around the clock, including weekends. About 58% of its patients stay overnight. It handles emergencies. It is the workhorse of the network.

**Lanaken** is a small, efficient day-surgery center. Seven rooms, weekdays only, no weekends. Nearly all patients (98%) come in and go home the same day. The typical procedure takes about 30 minutes — think cataract surgery or a spinal injection. Two of its rooms work as a pair: when one fills up, cases move to the other automatically.

**Maaseik** is a mix of both. Some of its rooms look like Lanaken (short, simple procedures). Other rooms look like Genk (longer, more complex cases). This makes Maaseik especially interesting because it contains two different operating styles under one roof.

**Cathlab** is a specialized unit for heart procedures — stent placements, ablations, valve replacements. It sits inside the Genk campus but operates independently. Almost all cases are planned in advance, but most patients still stay overnight because cardiac procedures require monitoring.

---

## The headline number (and why it's misleading)

If you look at raw overtime rates — how often surgeries run past the end of the scheduled shift — you get this ranking:

- Lanaken: 0.5% of cases go overtime
- Maaseik: 2.8%
- Cathlab: 5.8%
- Genk: 8.4%

Genk's overtime rate is **16.8 times** Lanaken's. If a hospital board saw this, they would probably conclude that Lanaken is far better managed than Genk.

**That conclusion would be wrong.** Or at least, it would be answering the wrong question.

---

## Why the comparison is unfair

The four sites are not doing the same work. Comparing them on a single number without accounting for their differences is like comparing a marathon runner's pace to a sprinter's 100-meter time. Both are speed measurements. Neither tells you who is the better athlete.

Here are the structural differences that inflate the gap:

1. **Weekend work.** Genk operates on weekends. Lanaken doesn't. Weekend cases tend to be emergencies, which are harder to schedule and more likely to run over.

2. **Evening and night shifts.** Genk runs 24/7. Lanaken closes at the end of the regular workday. Any case that starts in the evening at Genk has a higher chance of going overtime simply because it started later.

3. **Emergencies.** About 15% of Genk's cases are urgent, booked within 24 hours. At Lanaken, it's less than 1%. Emergency cases are inherently less predictable.

4. **Type of patient.** Genk's patients are mostly inpatients who stay overnight — their procedures are longer and more complex. Lanaken's patients almost all go home the same day.

None of these differences have anything to do with how well each site manages its operating rooms. They are built into the design of each site.

---

## What happens when you remove these differences step by step

This is the core of the paper. We used a method we call **progressive stratification**, which means: filter the data one step at a time, removing one structural difference at each step, and watch what happens to the gap.

**Step 0 — Raw data (all cases):** The gap is 16.8x.

**Step 1 — Weekdays only:** Remove weekend cases. The gap shrinks a little, because Genk does proportionally more weekend work.

**Step 2 — Day shift only:** Remove evening and night cases. The gap shrinks more, because Genk's 24/7 mandate generates a lot of after-hours activity that other sites don't have.

**Step 3 — Elective only:** Remove emergency cases. Now all sites are being compared on planned surgeries done during daytime weekday hours. The gap drops to about 4-5x.

**Step 4 — Split by patient type:** Separate day-surgery patients from overnight patients. Now we're comparing like with like. The gap falls to roughly 3-4x.

**The bottom line:** about four-fifths of the original 16.8x gap was structural — caused by the different operating models, not by different management quality. The residual 3-4x gap reflects real operational differences, but it's much smaller than the raw number suggests.

---

## The bigger finding: the variation is inside hospitals, not between them

Here is what surprised us most. Forget about comparing Genk to Lanaken for a moment. Look inside a single hospital.

At **Maaseik**, the worst-performing room (MO03) has an overtime rate of 8.9%. The best-performing room (MK11) has an overtime rate of 0.2%. That's a **44.5-fold** difference — within a single campus. This is nearly three times the 16.8x gap between the best and worst campus in the network.

The same pattern shows up at **Lanaken** (17x between its best and worst rooms), **Genk** (enormous range from 0% to 33%), and the **Cathlab** (about 3-4x range).

**What this means for managers:** If you want to reduce overtime, don't focus on making Campus A look more like Campus B. Focus on the three or four rooms in your own hospital that generate the most overtime, and figure out why. That's where the money is.

---

## Three things the textbooks get wrong (or at least oversimplify)

### 1. Starting the first case on time doesn't fix everything

OR management textbooks emphasize "first-case-on-time starts" (FCOTS) as the most important efficiency measure. The logic is simple: if the first surgery of the day starts late, everything after it gets pushed back, and the last case spills into overtime.

Our data tell a different story. **Genk actually has the worst first-case punctuality but Lanaken has the best.** That matches the overtime ranking — but it's misleading, because both rankings are driven by the same structural factors. Lanaken's first cases are easy to start on time because they're short and simple. Genk's are hard to start on time because they're long and complex.

More telling: the Cathlab has nearly the same first-case delay as Maaseik, but double the overtime rate. If first-case punctuality were the main driver, those two sites should have similar overtime. They don't.

FCOTS matters within a single room on a single day. It is not a reliable way to compare different sites.

### 2. Surgical time estimation is not the problem

You might think some hospitals are just worse at predicting how long surgeries will take, and that's why they get more overtime. We tested this by grouping procedures by their planned length and comparing how accurate each site's estimates were.

Result: **the estimation accuracy is basically the same across sites**, once you compare within the same duration range. A 90-minute planned case has roughly the same spread of actual durations at Genk as at Lanaken.

The scheduling teams share the same computer system and historical data, so this makes sense. The differences in overtime are not caused by some sites being worse at predicting surgical time.

### 3. Delays stacking up waste more time than surgeries running long

When people think about overtime, they usually picture a surgery running longer than expected. That happens, but it's not the main cause of wasted OR time.

The bigger problem is **cascading delays** — when one case starts late, pushing the next one later, pushing the one after that later still. By the end of the day, a 10-minute morning delay has snowballed into a 60-minute problem.

Our data show that start-time cascading wastes about **four times more** OR time than duration overruns. The problem isn't that surgeries take too long. It's that delays stack up.

---

## What about room swaps?

A room swap is when a case is performed in a different operating room than planned. You might think this is always a sign of disorganization. It isn't.

At Lanaken, 7.5% of cases are "swapped" — the highest rate in the network. But these swaps are entirely by design. Lanaken's two paired rooms (LP01 and LP02) are set up to trade cases back and forth as needed. Every swap from LP01 goes to LP02 and vice versa. This is a built-in shock absorber that keeps the day running smoothly without extending hours.

At Maaseik, by contrast, room swaps tend to go in one direction (from MO04 to MO05), which looks more like overflow than a planned strategy.

The lesson: **the same metric can mean completely different things depending on the context.** That's the whole point of the paper.

---

## What we're NOT claiming

Three things this paper does not do:

1. **We don't claim causality.** We can show that most of the performance gap is structural, but we can't prove exactly which design features cause which outcomes.

2. **We don't say anything about patient outcomes.** We have no data on whether patients had complications, how long they stayed in the hospital after surgery, or whether they came back later. Our paper is about operations, not clinical quality.

3. **We don't say Lanaken is "better" than Genk.** Lanaken has lower overtime because it does different work. That's not a management victory; it's a design choice. Genk's higher overtime is partly the price of being the hospital that handles everything, including emergencies at 2 AM.

---

## Why this matters beyond ZOL

Hospitals across the world compare their operating-room performance to other hospitals. "Our overtime rate is 7%, the national average is 5%, so we need to improve." This kind of comparison is common but often misleading — for the same reasons our data show.

If this paper is published, it offers a practical method (progressive stratification) that any hospital network can use to make fairer comparisons. Instead of a single number that conflates structure with performance, you get a layered picture that shows what's structural and what's actually under management control.

---

## Key terms you should know

If any term in the paper or in conversation with Niels comes up and you're unsure, check the `05_glossary.md` file — it has 35 terms defined in plain language with examples from our data.

The most important ones for conversation:

- **Overtime rate** — percentage of cases that run past the end of the scheduled shift
- **Progressive stratification** — our method of filtering data step by step to peel away structural differences
- **Operating model** — the structural design of how a site runs its ORs (what cases it takes, what hours it works, etc.)
- **FCOTS** — first-case-on-time start, whether the first surgery of the day begins on time
- **Room swap** — when a case is done in a different room than planned
- **Cascade** — when one delay pushes the next case later, which pushes the one after that later, and so on
- **CV (coefficient of variation)** — a measure of how spread out values are, relative to the average. Lower CV means more predictable.
- **Natural experiment** — a study where groups differ because of circumstances, not because a researcher assigned them

---

## The one-sentence version

> Four hospital sites in the same network look wildly different on raw operating-room metrics, but once you account for what each site actually does, four-fifths of the gap disappears — and the real waste is between rooms inside each hospital, not between hospitals.
