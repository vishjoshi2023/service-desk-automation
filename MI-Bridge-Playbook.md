# Major-Incident Bridge Playbook 🚨

> **Purpose** – Give any on-call engineer or service-desk lead a repeatable, seven-step script for running a high-stakes incident bridge that restores service *fast* and keeps stakeholders calm.

---

## 🔖 Quick reference (cheat sheet)

| T + mins | Action | Driver |
|---------:|--------|--------|
| 0 – 2 | **Start bridge.** Confirm incident ID, scope, severity. | Bridge Lead |
| 2 – 5 | **Assign roles.** Scribe, Comms, Tech Leads. | Bridge Lead |
| 5 – 15 | **Stabilise.** Contain blast-radius, execute rollback/workaround. | Tech Leads |
| 15 – 20 | **Stakeholder update #1.** ETA, mitigations, next steps. | Comms Lead |
| 20 – 40 | **Root action.** Patch, restart, failover, etc. | Tech Leads |
| 40 – 50 | **Stakeholder update #2.** Confirm recovery, monitor. | Comms Lead |
| 50 – 60 | **Close bridge.** Declare “Resolved / Monitoring”; schedule post-mortem. | Bridge Lead |

---

## 1 | Pre-bridge checklist ✔️

* P1 / Sev-1 ticket raised in **ServiceNow** (`INC#######`)  
* Business impact validated (financial / regulatory / safety)  
* Paging group triggered (Ops, Dev, Vendor, Management)  
* Recording enabled for audit & playback (if policy allows)

---

## 2 | Role cards 🎭

| Role | Responsibility | Typical Persona |
|------|----------------|-----------------|
| **Bridge Lead** | Chair the call, time-box, decision authority | Duty Manager / SD Lead |
| **Comms Lead** | Draft status updates, manage stakeholder channel | Service-Desk Analyst |
| **Scribe** | Real-time timestamped log in ticket | Junior Analyst |
| **Tech Leads** | Execute diagnosis & recovery tasks | SME / Vendor |
| **Business Rep** | Validate user impact, sign-off recovery | Product Owner |

---

## 3 | Seven-step runbook 🛠️

1. **Kick-off (T+0).** State: *“You’re on a recorded Major-Incident bridge for INC#######; current impact is …”*  
2. **Assign roles** live on the call; paste the table into chat so everyone sees ownership.  
3. **Stabilisation phase.** Focus on containment first, *not* root cause.  
4. **Time-boxed diagnosis.** 10-min loops: hypothesis ► test ► outcome. Escalate vendors if no progress after second loop.  
5. **Transparent comms.** Push updates every 15 min to Stakeholder Channel & exec distro.  
6. **Recovery & validation.** Business Rep confirms user journeys are back; monitoring shows green for 15 min.  
7. **Close & handover.** Mark ticket *Resolved / Monitoring*, set **RCA due within 48 h**, thank attendees, stop recording.

---

## 4 | Post-incident actions 📄

* **RCA template** – link to Confluence page `/postmortems/template`  
* **Problem ticket** – auto-raised via ServiceNow workflow  
* **Lessons-learned huddle** within one business day  
* **Dashboard update** – Tag MTTR, FCR, CSAT metrics in Power BI board

---

## 5 | Appendix 🔗

* ITIL v4 Major-Incident Mgmt summary  
* ServiceNow “MI Bridge” quick-action shortcut  
* Example stakeholder e-mail template  
