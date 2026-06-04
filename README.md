# Senior Developer Coding Challenge (1 Hour)

# Event Summary Service

A small Python solution for the senior developer coding challenge.

The application accepts a list of events, validates them, handles duplicate event IDs, and returns a summary grouped by event type.

The focus of this solution is clarity, simple structure, clear assumptions, and meaningful tests.

---

## How to run

Install pytest:

```bash
python -m pip install pytest
```

Run the tests:

```bash
python -m pytest
```

---

## 1. Accepts events

At minimum, each event contains:

* `id` string
* `timestamp` ISO format string
* `type` string
* `value` number

Example input event:

```python
{
    "id": "1",
    "timestamp": "2026-06-02T10:00:00Z",
    "type": "click",
    "value": 10,
}
```

Example input list:

```python
events = [
    {
        "id": "1",
        "timestamp": "2026-06-02T10:00:00Z",
        "type": "click",
        "value": 10,
    },
    {
        "id": "2",
        "timestamp": "2026-06-02T10:01:00Z",
        "type": "click",
        "value": 20,
    },
    {
        "id": "3",
        "timestamp": "2026-06-02T10:02:00Z",
        "type": "purchase",
        "value": 100,
    },
]
```

---

## 2. Returns a summary

Given a collection of events, the service returns:

* total number of valid, non-duplicate events
* count per event type
* sum of `value` per event type

Example output:

```python
{
    "total": 3,
    "type": {
        "click": {"count": 2, "aggregate": 30},
        "purchase": {"count": 1, "aggregate": 100},
    },
}
```

---

## 3. Basic validation

The service validates that:

* required fields are present: `id`, `timestamp`, `type`, `value`
* `id` is a non-empty string
* `type` is a non-empty string
* `timestamp` is a valid ISO datetime string
* `value` is a number

Invalid events fail fast by raising `EventValidationError`.

---

## Duplicate handling

I assumed `id` is the unique identifier for an event.

If the same `id` appears more than once:

* the first valid event is kept
* later duplicates are ignored
* duplicate values are not added to the aggregate
* if a duplicate has a different `type`, a warning is logged

This avoids double-counting.

---

## Application flow

1. Receive a list of events.
2. Validate each event.
3. Check whether the event ID has already been processed.
4. Ignore duplicate IDs to avoid double-counting.
5. Create a summary entry for the event type if needed.
6. Increase the count and aggregate value for that event type.
7. Return the final summary.

---

## Testing approach

I used a lightweight TDD approach.

I started with a happy path test to define the expected output for valid input. Then I added focused edge-case tests for duplicate IDs and invalid input.

The tests cover:

* valid events are summarised correctly
* duplicate IDs are ignored
* duplicate IDs with different types log a warning
* missing required fields raise an error
* invalid timestamp raises an error
* non-numeric value raises an error

The tests are intentionally small and readable because the challenge is time-boxed.

---

## Assumptions

* Event `id` is the unique identifier.
* Duplicate IDs should not be counted twice.
* The first valid event wins when duplicates are found.
* Invalid events fail fast.
* Timestamp validation only checks ISO format.
* Date range filtering is not implemented because it was optional.
* Large dataset handling is not implemented because the challenge asks not to over-engineer.

---

## What I would improve with more time

* Return invalid events in a structured error report instead of failing fast.
* Write bad records to an audit or quarantine table.
* Add a bad-record threshold agreed with the business.
* Add date range filtering.
* Add stronger timestamp checks, such as future or very old timestamps.
* Use persistent deduplication for duplicates across multiple batches.
* Use Spark or another distributed approach for very large datasets.
* Add monitoring for total records, duplicate records, invalid records, and processing time.
