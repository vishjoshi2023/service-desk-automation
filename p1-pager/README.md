# P1 Pager (Python demo)

A small example that:

1. Pretends to query ServiceNow for open P1 incidents  
2. Sends a Slack message to the on-call engineer

This is purely for learning; no live credentials are included.

---

## How to run

```bash
# demo values
export SN_INSTANCE=demo-instance
export SN_USER=demo-user
export SN_PASSWORD=demo-pass
export SLACK_WEBHOOK=https://hooks.slack.com/services/demo

pip install -r requirements.txt
python main.py
