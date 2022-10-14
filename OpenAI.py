import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def ai_function(text_function):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=text_function,
      temperature=0,
      max_tokens=260,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["#", "\"\"\""]
    )
    text_out = response["choices"][0]["text"]
    print(text_out)
    return


prompt="""#JavaScript to Python:
JavaScript: 
dogs = ["bill", "joe", "carl"]
car = []
dogs.forEach((dog) {
    car.push(dog);
});

Python:
"""

ai_function(prompt)