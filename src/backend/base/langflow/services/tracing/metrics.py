"""Metrics aggregation utilities for flow runs."""


def calculate_average_step_latency(latencies: list[float]) -> float:
    """Calculate the average latency across flow steps."""
    return sum(latencies) / len(latencies)
