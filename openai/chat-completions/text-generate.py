import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY"),
)

def call_chat_completion(messages, model="gpt-4o"):
  chat_completion = client.chat.completions.create(messages=messages, model=model)
    
  return chat_completion.choices[0].message.content
  
messages=[
  {
    "role": "system", 
    "content": "1.입력받은 음식 이름을 활용한 레시피를 응답할것. 2.전달받은 텍스트가 음식이 아니라고 판단되는 경우, 해당 레시피를 찾을 수 없다고 응답할 것. "
  },
  {
    "role": "user", 
    "content": "김치"
  },
]

result = call_chat_completion(messages)

print(result)