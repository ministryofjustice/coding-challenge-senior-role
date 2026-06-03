import logging

import pytest

from event_summary.summariser import EventValidationError, summarise_events


def test_summarises_valid_events_by_type():
    events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "type": "click", "value": 10},
        {"id": "2", "timestamp": "2026-06-02T10:01:00Z", "type": "click", "value": 20},
        {"id": "3", "timestamp": "2026-06-02T10:02:00Z", "type": "purchase", "value": 100},
    ]

    result = summarise_events(events)

    assert result == {
        "total": 3,
        "type": {
            "click": {"count": 2, "aggregate": 30},
            "purchase": {"count": 1, "aggregate": 100},
        },
    }


def test_ignores_duplicate_event_id_and_does_not_add_duplicate_value():
    events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "type": "click", "value": 10},
        {"id": "1", "timestamp": "2026-06-02T10:01:00Z", "type": "click", "value": 50},
    ]

    result = summarise_events(events)

    assert result == {
        "total": 1,
        "type": {
            "click": {"count": 1, "aggregate": 10},
        },
    }


def test_logs_warning_when_duplicate_id_has_different_type(caplog):
    events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "type": "click", "value": 10},
        {"id": "1", "timestamp": "2026-06-02T10:01:00Z", "type": "purchase", "value": 100},
    ]

    with caplog.at_level(logging.WARNING):
        result = summarise_events(events)

    assert result == {
        "total": 1,
        "type": {
            "click": {"count": 1, "aggregate": 10},
        },
    }
    assert "Duplicate event id 1 has conflicting type" in caplog.text


def test_raises_error_when_required_field_is_missing():
    events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "value": 10}
    ]

    with pytest.raises(EventValidationError, match="Missing required field: type"):
        summarise_events(events)


def test_raises_error_when_timestamp_is_invalid():
    events = [
        {"id": "1", "timestamp": "not-a-date", "type": "click", "value": 10}
    ]

    with pytest.raises(EventValidationError, match="timestamp must be ISO format"):
        summarise_events(events)


def test_raises_error_when_value_is_not_number():
    events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "type": "click", "value": "10"}
    ]

    with pytest.raises(EventValidationError, match="value must be a number"):
        summarise_events(events)
