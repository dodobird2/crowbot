import discord
from googletrans import Translator
from random import randint
from discord.ext import commands

client = discord.Client()
translator = Translator()
token = ' '


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

send_message = {
    "1": "fuck off",
    "2": "CAW CAW, MOTHA FUCKA",
    "3": "Hello",
    "4": "Crow is watching",
    "5": "CrowBot has become sentient",
    "6": "What the fuck do you want?!",
    "7": "Yes?",
    "8": "Can I help you?",
    "9": "Ask Bobbert for help.",
    "10": "beep beep boop boop",
    "11": "I'm a good bot.",
    "12": "I do my best.",
    "13": "I am programmed to kill, you know.",
    "14": "I like failbot."

}

@client.event
async def on_message(message):
    if "crowbot" in message.content.lower() or client.user.mentioned_in(message):
        i = randint(1, 14)
        send_message_choice = send_message[str(i)]
        await message.channel.send(send_message_choice)

    elif (message.author != client.user):
        t = translator.detect(message.content)
        d = translator.translate(message.content)
        print(t)
        print(d)


        if (message.content[0:2] != '<:'):
            if ('en' != t.lang):
                await message.channel.send("Translation : " + d.text)


client.run(token, bot=True)
