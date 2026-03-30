# Senior Developer Coding Challenge (1 Hour)

## Overview  
Build a **small application** that ingests and summarises event data.

The focus is on **clarity, structure, decisions, and your approach to testing**, not completeness.

---


## The Challenge  

Create a service (or single module) that:

### 1. Accepts Events  
Each event contains:
- `id` (string)
- `timestamp` (ISO format)
- `type` (string)
- `value` (number)


---

### 2. Returns a Summary  

Given a collection of events, return:

- Total number of events  
- Count per event type  
- Sum of `value` per event type  

Example output (shape, not strict format):

```json
{
  "total": 10,
  "byType": {
    "click": { "count": 6, "totalValue": 120 },
    "purchase": { "count": 4, "totalValue": 300 }
  }
}
```

---

### 3. Basic Validation
1. Handle invalid or missing fields
2. Decide how to treat duplicates (id)



## Testing

We value Test-Driven Development (TDD).

Please:

- Include a small but meaningful set of tests that cover:
  - Core behaviour (happy path)
  - At least one edge case
- Ensure tests are clear and readable

If you choose not to strictly follow TDD, briefly explain your approach.

---


## What We’re Looking For

### Code quality
- Clean, readable structure
- Sensible naming
- Logical organisation

### Thought process
- Sensible assumptions
- Clear handling of edge cases
- Evidence of trade-off thinking

### Pragmatism
- What you choose not to build
- Simplicity where appropriate

### Testing
- At least 1–2 meaningful tests
- Or a clear explanation of what you would test

### Documentation (Very Short)
Provide a brief README (or comments) covering:
- How to run the code
- Any assumptions made
- What you would improve with more time

---

## Time Limit
~1 hour

Do not over-engineer. Prioritise clarity.

## Optional (Only if time allows)
- Support filtering by date range
- Handle large datasets efficiently
- Add an API wrapper if you started with a function

## Evaluation Criteria
We care about:
- Clarity over completeness
- Structure over features
- Decisions over decoration

## Follow-Up Questions
Be prepared to discuss:
- What would you refactor first?
- How would this change at scale?
- What assumptions did you make?
- Where could this break?
