import os
from hindsight import HindsightServer, HindsightClient

with HindsightServer(
    llm_provider="groq",
    llm_model="openai/gpt-oss-120b",
    llm_api_key=os.environ["GROQ_API_KEY"],
) as server:
    client = HindsightClient(base_url=server.url)
    client.retain(bank_id="test", content="Alice works at Google")
    results = client.recall(bank_id="test", query="Where does Alice work?")
    for r in results.results:
        print("Recalled:", r.text)