import time
import random

bot_template = "BOT: {}"
user_template = "USER: {}"
name = "Greg"
weather = "cloudy"
responses = {
    "what's your name?": ["my name is {}".format(name),
                          "they call me {}".format(name),
                          "I go by {}".format(name)],
    "what's the weather?": ["the weather is {}".format(weather),
                            "it is {}".format(weather)],
    "default": "default message"
}

def respond(message):
    if message.endswith('?'):

    if message in responses:
        return random.choice(responses[message])
    else:
        return responses['default']


def send_message(message):
    print(user_template.format(message))
    time.sleep(0.5)
    print(bot_template.format(respond(message)))



send_message("what's the wea?")