from google import genai

def api_key():
    try:
        with open('api_key.txt','r') as f:
            data=f.read().strip()
        return data
    except FileNotFoundError:
        print("can't find file")
        return None     

def main():
    client=genai.Client(api_key=api_key())
    response=client.models.generate_content(
        model='gemini-2.5-flash',
        contents='如何解释欧拉公式'
    )
    print(response.text)



if __name__ == "__main__":
    main()
