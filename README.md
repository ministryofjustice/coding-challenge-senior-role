# Senior Developer Coding Challenge (1 Hour)

## Overview  
Build a **small application** that ingests and summarises event data.

The focus is on **clarity, structure, decisions, and your approach to testing**, not completeness.

---


## The Challenge  

Create a service (or single module) that:

### 1. Accepts events  
At minimum, each event contains:
- `id` (string)
- `timestamp` (ISO format)
- `type` (string)
- `value` (number)


---

### 2. Returns a summary  

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

### 3. Basic validation
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


## What we’re looking for

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
- Evidence of TDD or thoughtful testing strategy
- Tests that are meaningful, not excessive

### Documentation (short)
Provide a brief README covering:
- How to run the code
- Any assumptions made
- How the application flows (illustration or bullet-points), and
- What you would improve with more time

---

## Time limit
~1 hour

Do not over-engineer. Prioritise clarity.

## Optional (only if time allows)
- Support filtering by date range
- Handle large datasets efficiently

## Evaluation criteria
We care about:
- Clarity over completeness
- Structure over features
- Decisions over decoration

## Follow-Up questions
Be prepared to discuss:
1. How did TDD influence your design?
2. What would you refactor first?
3. How would this change at scale?
4. What assumptions did you make?
5. Where could this break?
