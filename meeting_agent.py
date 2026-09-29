import os
import json
from hindsight_client import Hindsight
from groq import Groq

groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])


def store_meetings(client, meetings):
    for meeting in meetings:
        client.retain(
            bank_id=f"client-{meeting['client']}",
            content=meeting["transcript"],
            context=f"Meeting {meeting['meeting_id']} on {meeting['date']}",
            timestamp=meeting["date"],
        )
    print(f"Stored {len(meetings)} meetings for {meetings[0]['client']}")
    print()


def analyze_new_meeting(client, client_name, new_transcript):
    memories = client.recall(
        bank_id=f"client-{client_name}",
        query="concerns, objections, delays, competitor mentions, budget issues",
    )
    past_context = "\n".join([f"- {m.text}" for m in memories.results])

    prompt = f"""You are a churn risk analyst.

NEW MEETING:
{new_transcript}

PAST MEETINGS (from memory):
{past_context}

Return exactly:
RISK: [LOW/MEDIUM/HIGH]
SIGNALS:
  - [signal with approximate date]
ACTION: [one recommendation]
"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def main():
    with open("meetings.json", "r", encoding="utf-8") as f:
        meetings = json.load(f)

    client = Hindsight(
        base_url="https://api.hindsight.vectorize.io",
        api_key=os.environ["HINDSIGHT_API_KEY"],
    )

    store_meetings(client, meetings)

    new_meeting = (
        "Client said they are 'reconsidering the entire initiative' "
        "and asked whether we can pause the contract. Leadership is now "
        "looking at a cheaper alternative."
    )

    print("New meeting received:")
    print(f'"{new_meeting}"')
    print()
    print("Analyzing against memory...")
    print()

    print(analyze_new_meeting(client, "Acme Corp", new_meeting))


if __name__ == "__main__":
    main()