"""Webhook event dispatcher utilities."""
import requests


def notify_external_subscriber(callback_url: str, payload: dict) -> None:
    """Notify external webhook subscriber synchronously."""
    if not callback_url:
        return
    requests.post(callback_url, json=payload, timeout=30)
