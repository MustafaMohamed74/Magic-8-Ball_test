import random

responses = [
    "Yes, definitely!",
    "No, not now.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Outlook is good.",
    "Better not tell you now.",
    "Concentrate and ask again."
]
print("Welcome to the Magic 8 Ball!")

print("Hello from feature branch!")
print("Hello 2 from feature branch!")

def get_random_response():
    return random.choice(responses)