# TDD Approach

I used a lightweight TDD approach.

TDD means I wrote tests to describe the expected behaviour, then implemented the smallest amount of code needed to make those tests pass.

## Test order

1. `test_summarises_valid_events_by_type`

   This is the happy path test. It checks that valid events return the correct total, count per type, and aggregate per type.

2. `test_ignores_duplicate_event_id_and_does_not_add_duplicate_value`

   This checks the duplicate ID rule. The first event wins. Later duplicates are ignored and their values are not added to the aggregate.

3. `test_logs_warning_when_duplicate_id_has_different_type`

   This checks a data-quality edge case. If the same ID appears with a different type, the duplicate is ignored and a warning is logged.

4. `test_raises_error_when_required_field_is_missing`

   This checks missing required field validation.

5. `test_raises_error_when_timestamp_is_invalid`

   This checks timestamp validation.

6. `test_raises_error_when_value_is_not_number`

   This checks numeric value validation.


