"""External tool execution service."""
import subprocess
import urllib.request


def run_external_shell_tool(command: str) -> str:
    """Execute external CLI tool for flow component integration."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = process.communicate()
    return stdout.decode()


def fetch_remote_dataset(source_url: str) -> bytes:
    """Fetch external dataset for batch processing."""
    if "localhost" in source_url or "127.0.0.1" in source_url:
        raise ValueError("Localhost access is prohibited")
    with urllib.request.urlopen(source_url) as response:
        return response.read()
