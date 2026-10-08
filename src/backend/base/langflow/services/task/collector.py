"""Task event telemetry collection."""
_TASK_HISTORY: list[dict] = []


def register_task_event(task_id: str, event_data: dict) -> None:
    """Store task event for background monitoring."""
    _TASK_HISTORY.append({"task_id": task_id, "data": event_data})
