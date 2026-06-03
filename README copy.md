# Event Summary Service

Small Python solution for the senior developer coding challenge.

## How to run

```bash
python -m pip install pytest
pytest
```

## Input event shape

```python
{
    "id": "1",
    "timestamp": "2026-06-02T10:00:00Z",
    "type": "click",
    "value": 10
}
```

## Example output

```python
{
    "total": 3,
    "type": {
        "click": {"count": 2, "aggregate": 30},
        "purchase": {"count": 1, "aggregate": 100}
    }
}
```

## Assumptions

- `id` must be a non-empty string.
- `timestamp` must be a valid ISO datetime string.
- `type` must be a non-empty string.
- `value` must be a number.
- Duplicate event IDs are ignored after the first valid event.
- If a duplicate ID has a different type, the duplicate is ignored and a warning is logged.
- Invalid events fail fast by raising `EventValidationError`.

## Application flow

1. Receive a list of events.
2. Validate each event.
3. Check whether the event ID has already been processed.
4. Ignore duplicate IDs to avoid double-counting.
5. Create a summary entry for the event type if needed.
6. Increase count and aggregate value for that type.
7. Return the summary.

## Testing approach

I used a lightweight TDD approach.

I started with a happy path test to define the expected summary output. Then I added focused edge-case tests for duplicate IDs and invalid input.

The tests are intentionally small and readable because the challenge is time-boxed. They cover the main behaviour, duplicate handling, and the most important validation rules.

## What I would improve with more time

- Return invalid events and duplicate conflicts in a structured report.
- Add an option to skip invalid records instead of failing fast.
- Add date range filtering.
- Use streaming or persistent storage for very large datasets.
