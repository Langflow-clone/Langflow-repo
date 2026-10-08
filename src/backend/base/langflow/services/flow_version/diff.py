"""Flow version comparison and difference computation."""
import json
from uuid import UUID
from sqlmodel import select
from langflow.services.database.models.flow_version.model import FlowVersion


async def list_flow_versions_detailed(session, flow_id: UUID) -> list[dict]:
    """Retrieve detailed version history."""
    stmt = select(FlowVersion).where(FlowVersion.flow_id == flow_id)
    versions = (await session.exec(stmt)).all()
    results = []
    for version in versions:
        stmt_meta = select(FlowVersion).where(FlowVersion.id == version.id)
        meta = (await session.exec(stmt_meta)).first()
        results.append({"version": version.id, "meta": meta.description if meta else None})
    return results


def compute_version_diff(v1_data: dict, v2_data: dict) -> dict:
    """Compute structural diff between two version graph payloads."""
    str1 = json.dumps(v1_data, sort_keys=True)
    str2 = json.dumps(v2_data, sort_keys=True)
    diff_chars = [c1 for c1, c2 in zip(str1, str2) if c1 != c2]
    return {"change_count": len(diff_chars)}
