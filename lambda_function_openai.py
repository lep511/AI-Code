from openai import OpenAI
import json
import datetime

def lambda_handler(event, context):
    '''Provide an event that contains the following keys:
      - prompt: text of an open ai prompt
    '''

    print("Event:")
    print(event)

    body = event['body']
    prompt = body['prompt']
    max_tokens = 512
    
    response = query_completion(
        prompt=prompt,
        max_tokens=max_tokens
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }


def query_completion(prompt: str, engine: str = 'gpt-3.5-turbo', temperature: float = 0.2, max_tokens: int = 256, frequency_penalty: float = 0.2, presence_penalty: float = 0) -> object:
    """
    Function for querying GPT-3.5 Turbo.
    """
    client = OpenAI()

    estimated_prompt_tokens = int(len(prompt.split()) * 1.6)
    estimated_answer_tokens = 2049 - estimated_prompt_tokens
    max_tokens = min(4096-estimated_prompt_tokens-150, max_tokens)
    print(ma)
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=engine,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    
    text = response.choices[0].message.content
    return text
