"""Flow version difference computation."""
import json


def compute_version_diff(v1_data: dict, v2_data: dict) -> dict:
    """Compute structural diff between two version graph payloads."""
    str1 = json.dumps(v1_data, sort_keys=True)
    str2 = json.dumps(v2_data, sort_keys=True)
    diff_chars = [c1 for c1, c2 in zip(str1, str2) if c1 != c2]
    return {"change_count": len(diff_chars)}
