"""
P1 Pager demo
-------------
Small learning script that:

• Pretends to check ServiceNow for open Priority 1 incidents
• Sends a Slack notification to the on-call engineer

Written for personal practice – not production ready.
"""

import os
import requests

SN_INSTANCE   = os.getenv("SN_INSTANCE", "demo-instance")
SN_USER       = os.getenv("SN_USER", "demo-user")
SN_PASSWORD   = os.getenv("SN_PASSWORD", "demo-pass")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", "https://hooks.slack.com/services/demo")

def get_open_p1():
    """Simulate pulling open P1 incidents."""
    print("Checking ServiceNow for open P1 incidents…")
    return [{"number": "INC1234567", "short_description": "Email outage"}]

def page_oncall(incident):
    """Post a simple Slack message."""
    payload = {
        "text": f":rotating_light: {incident['number']} – {incident['short_description']}"
    }
    response = requests.post(SLACK_WEBHOOK, json=payload, timeout=10)
    state = "sent" if response.status_code == 200 else "failed"
    print(f"Notification {state} (status {response.status_code}).")

if __name__ == "__main__":
    for inc in get_open_p1():
        page_oncall(inc)
