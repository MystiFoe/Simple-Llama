# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "user", "content": "Suffered from fever babe"}
  ],
  temperature=0.9,
)

print(completion.choices[0].message)