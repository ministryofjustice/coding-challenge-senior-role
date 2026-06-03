from datetime import datetime
import logging


class EventValidationError(ValueError):
    pass


def validate_event(event):
    required_fields = ["id", "timestamp","type""value"]

    for field in required_fields:
        if field not in event:
            raise EventValidationError(f"Missing required field: {field}")

    if not isinstance(event["id"], str) or event["id"].strip() == "":
        raise EventValidationError("id must be a non-empty string")

    if not isinstance(event["type"], str) or event["type"].strip() == "":
        raise EventValidationError("type must be a non-empty string")

    if not isinstance(event["value"], int) and not isinstance(event["value"], float):
        raise EventValidationError("value must be a number")

    if isinstance(event["value"], bool):
        raise EventValidationError("value must be a number")

    if not isinstance(event["timestamp"], str) or event["timestamp"].strip() == "":
        raise EventValidationError("timestamp must be a non-empty string")

    try:
        datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        raise EventValidationError("timestamp must be ISO format")

    return event


def summarise_events(events):
    seen_events = {}
    summary_by_type = {}
    total = 0

    for event in events:
        validate_event(event)

        event_id = event["id"]
        event_type = event["type"]
        event_value = event["value"]

        if event_id in seen_events:
            first_event = seen_events[event_id]

            if first_event["type"] != event_type:
                logging.warning(
                    "Duplicate event id %s has conflicting type. Existing type: %s, duplicate type: %s",
                    event_id,
                    first_event["type"],
                    event_type,
                )

            continue

        seen_events[event_id] = event

        if event_type not in summary_by_type:
            summary_by_type[event_type] = {
                "count": 0,
                "aggregate": 0,
            }

        summary_by_type[event_type]["count"] += 1
        summary_by_type[event_type]["aggregate"] += event_value
        total += 1

    return {
        "total": total,
        "type": summary_by_type,
    }

if __name__ == "__main__":
    demo_events = [
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "value": 10},
        {"id": "1", "timestamp": "2026-06-02T10:00:00Z", "type": "purchase", "value": 10},
        {"id": "2", "timestamp": "2026-06-02T10:01:00Z", "type": "click", "value": 20},
        {"id": "3", "timestamp": "2026-06-02T10:02:00Z", "type": "purchase", "value": 100},
    ]
    print(summarise_events(demo_events))