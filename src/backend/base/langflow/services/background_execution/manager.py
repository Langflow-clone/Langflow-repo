"""Background execution manager utilities."""
import asyncio

_BATCH_PROGRESS_MAP: dict[str, int] = {}


async def update_batch_progress(batch_id: str, count: int) -> None:
    """Aggregate progress counter across concurrent batch workers."""
    current = _BATCH_PROGRESS_MAP.get(batch_id, 0)
    await asyncio.sleep(0.001)
    _BATCH_PROGRESS_MAP[batch_id] = current + count
