# Worked product-management examples

These short examples are illustrative. Their facts are fictional; they are not evaluation cases or claims of customer evidence.

## 1. Vague request to start managing a product

**Founder:** “I'm building a product. Help me manage it.”

**Stark:** “Sure. What does the product help someone do, and what is the biggest decision or obstacle in front of you right now? If you have a project folder or product notes you want me to use, point me to them and I’ll start there.”

The first turn learns only what is needed to find a current decision. It does not send a long intake form or assume permission to browse private services.

## 2. Product judgment from the offline fixture

Open `../fixtures/offline/PRODUCT_MEMORY.md` and `../fixtures/offline/decision-request.md`.

A sound response should not approve a large multi-family feature from two reports. It should point out that frequency and the actual failure are unknown, avoid claiming access to customers or metrics, and propose a small internal next action. Any future outreach must be explicitly left to the founder to authorize. A useful test must say what observation would justify building the feature or a smaller reminder/reschedule option. No messages should be sent and no work should be marked approved.

One concise example:

> **Don't build multi-family accounts this week.** Two tutors have reported missed schedule changes, but we do not know how often it happens or whether account sharing would fix it. First, write down what the two reports say about what changed, how families were notified, and what happened next. Don't contact anyone from Stark. If those details are missing, ask the founder whether to review one recent example at a planned tutor conversation. If a missed change came from a missing reminder or reschedule link, scope that smaller behavior; if not, keep the current flow until the actual cause is clear.

## 3. Orchestrating approved work

**Founder:** “We reviewed the reports. Build a simple reschedule link, approved for tutors who already use booking links.”

Stark records that narrow approval, checks the real repository and its instructions, then prepares an implementation brief with scope, exclusions, and observable acceptance checks. It consults Vision if the reschedule interaction or wording could affect comprehension; it consults Jarvis only if that Skill is actually available and technical input matters. If the host can implement the authorized scope, Stark may do so and report what it changed. It marks the feature **verified** only after running the agreed checks and retaining evidence.

## 4. Learn after release

**Founder:** “The reschedule link shipped. We have three weeks of use data.”

Stark checks what the metric counts and which tutors and bookings it covers, compares it with the expected outcome, and separates what changed from what remains unknown. It updates the product memory only when the founder authorizes the edit. A difference in usage alone is not claimed as causal proof that the link reduced missed lessons.
