import os
import discord
import my_bot
import random
import time
import dad_jokes
from secrets import *
dadjokes = dad_jokes.dadjokes
joke_timer = 0
last_channel = 0

client = discord.Client(intents=discord.Intents.all())

def dadjoke():
  global joke_timer
  global last_channel
  joke_timer = random.randint(9, 10)
  while joke_timer > 0:
    time.sleep(1)
    joke_timer -= 1
  return True

@client.event
async def on_ready():
  print("I'm in")
  print(client.user)
  # while True:
  #   time.sleep(10+random.random())
  #   global last_channel
  #   print(last_channel)
  #   if last_channel != 0:
  #     await last_channel.send(dadjokes[random.randint(1, len(dadjokes))])

@client.event
async def on_message(message):
  if (message.channel.name == "rois-bot" or random.randint(1, 10) == 1) and (message.author != client.user):
  # if (message.author != client.user):
    user_name = message.author.display_name
    if my_bot.should_i_respond(message.content, user_name):
      response = my_bot.respond(message.content, user_name)
      global last_channel
      last_channel = message.channel
      await message.channel.send(response)
client.run(my_secret)