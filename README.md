\# Meeting Memory Agent



An AI churn detection agent that remembers every client meeting and flags risk before you notice it.



Built for \*\*HackwithHyderabad 3.0\*\* using Hindsight (memory) + Groq (reasoning).



\## The Problem



Sales reps forget what was said in a meeting three weeks ago. Deals churn silently because nobody connects the dots across conversations.



\## What It Does



\- Stores every meeting transcript in Hindsight memory with `retain()`

\- When a new meeting arrives, `recall()` searches across all past meetings

\- Groq analyzes the recalled signals against the new meeting

\- Outputs a churn risk level, detected signals, and a recommended action



\## Demo



6 meetings over 3 weeks → agent connected 8 signals → flagged \*\*HIGH churn risk\*\* → suggested a retention action.



\### Sample Output

RISK: HIGH



SIGNALS:



Budget concerns (≈ 2026-09-10)



Competing vendor demo scheduled (week of 2026-09-07)



Competing vendor offered a discount (≈ 2026-09-15)



Client expressed hesitation (≈ 2026-09-15)



Request for contract flexibility (≈ 2026-09-20)



Inquiry about cancellation policy (≈ 2026-09-20)



Reconsideration of project priorities (≈ 2026-09-25)



Request to pause the contract (≈ 2026-09-28)



ACTION: Initiate an executive-level retention plan.



text



\## How Hindsight Memory Is Used



| Operation | Purpose |

|---|---|

| `retain()` | Store each meeting transcript with timestamp + client ID |

| `recall()` | Search across meetings to find related signals |



Hindsight uses semantic, keyword, graph, and temporal search — so it finds "budget concerns" from 3 weeks ago even when the new meeting says "reconsidering the initiative."



\## Stack



\- \*\*Hindsight\*\* — persistent memory layer

\- \*\*Groq\*\* (`openai/gpt-oss-120b`) — pattern analysis

\- \*\*Python\*\* — agent loop



\## Files



\- `meeting\_agent.py` — main agent

\- `meetings.json` — sample meeting dataset

\- `requirements.txt` — dependencies

