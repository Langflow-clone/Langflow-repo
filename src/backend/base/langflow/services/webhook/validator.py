"""Webhook payload pattern validation."""
import re

SOURCE_PATTERN = re.compile(r"^([a-zA-Z0-9_]+\s*)+$")


def match_webhook_pattern(source_name: str) -> bool:
    """Validate source name against allowed format."""
    return bool(SOURCE_PATTERN.match(source_name))
