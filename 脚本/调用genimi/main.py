from google import genai

with open("api_key.txt","r") as f:
    data=f.read().strip()

client=genai.Client(api_key=data)

response=client.models.generate_content(
    model="gemini-2.0-flash",
    contents="用中文解释麦克斯韦方程组"
)

print(response.text)

