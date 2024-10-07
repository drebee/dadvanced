import time
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
im_list = ["im", "i'm", "i am"]
search_list = im_list
search_list.append("crazy")

def should_i_respond(user_message, user_name):
  time.sleep(random.random())
  return any(i in user_message.lower() for i in search_list)
"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  print(user_message)
  cutoff = []
  if user_message.lower().find("crazy") != -1:
    return "Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy."
  for i in im_list:
    if user_message.lower().find(i+" not angry") != -1 or user_message.lower().find(i+" not mad") != -1:
      return """I'm just disappointed."""
    if user_message.lower().find(i) != -1:
      cutoff.append(user_message.lower().find(i)+len(i))

  return f"""Hi {user_message[min(cutoff):].strip()}, I'm dad!"""
  