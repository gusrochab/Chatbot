import re
import time
import random

user_template = "USER: {}"
bot_template = "BOT: {}"

rules = {'I want (.*)': ['What would it mean if you got {0}',
  'Why do you want {0}',
  "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
  'Do you wish that {0}',
  'What do you think about {0}',
  'Really--if {0}']}


def match_rule(rules, message):
    response, phrase = "default", None

    #iterate over the rules dictionary
    for pattern, responses in rules.items():
        match = re.search(pattern, message)
        if match:
            response = random.choice(responses).format(match.group(1))
            response = replace_pronouns(response)
            return response


def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        return re.sub('me', 'you', message)
    if 'my' in message:
        return re.sub('my', 'your', message)
    if 'your' in message:
        return re.sub('your', 'my', message)
    if 'you' in message:
        return re.sub('you', 'me', message)
    if ' i ' in message:
        return re.sub(' i ', ' you ', message)
    return message


def send_message(message):
    print(user_template.format(message))
    time.sleep(0.5)
    print(bot_template.format(match_rule(rules, message)))

send_message("do you think I should date Marina")
