import re
import time
import random

user_template = "USER: {}"
bot_template = "BOT: {}"

keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}
responses = {'default': 'default message', 'goodbye': 'goodbye for now',
             'greet': 'Hello you! :)', 'thankyou': 'you are very welcome'}
patterns = {}


def match_intent(message):
    for intent, pattern in patterns.items():
        if pattern.search(message):
            matched_intent = intent
    return matched_intent


def find_name(message):
    pattern_name = re.compile(r"(name|call)")
    pattern_captalized = re.compile(r"[A-Z]\w+")
    if pattern_name.search(message):
        name = pattern_captalized.findall(message)
        if len(name) > 0:
            return ' '.join(name)

def respond_message(message):
    intent = match_intent(message)
    names = find_name(message)
    return responses[intent] + ' ' + names

def send_message(message):
    print(user_template.format(message))
    time.sleep(0.5)
    print(bot_template.format(respond_message(message)))


for intent, keys in keywords.items():
    patterns[intent] = re.compile('|'.join(keys))

send_message('hello my name is Gustavo Rocha')
#print(respond_message('bye byeeee'))
#print(respond_message('thanks very much'))