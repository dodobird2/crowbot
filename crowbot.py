import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from googletrans import Translator
import discord
from random import randint
import re
#===============================================================================================#
client = discord.Client()
translator = Translator()
#===============================================================================================#
@client.event
async def on_message(message):
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
    "14": "I like failbot."}
    if (message.author == client.user):
        return
    #===========================================================================================#
    if "crowbot" in message.content.lower() or client.user.mentioned_in(message):
        i = randint(1, 14)
        send_message_choice = send_message[str(i)]
        await message.channel.send(send_message_choice)
    #===========================================================================================#
    authenticator = IAMAuthenticator('<api key>')
    language_translator = LanguageTranslatorV3(
    version='<version>',
    authenticator=authenticator)
    language_translator.set_service_url('<url>')
    #===========================================================================================#
    t=str(message.content)
    print(t)
    x=re.findall(r'<.*:.*:.*>',t)
    if(len(x)>0):
        for i in x: t.replace(i,"|reaction|")
    l = translator.detect(t)
    if l.confidence < 0.7 or 'en' in str(l.lang):
        return
    l=l.lang
    #===========================================================================================#
    print(l)
    try:
        translation = language_translator.translate(text=t,model_id=l+'-en').get_result()
        tr=(dict(json.loads(json.dumps(translation, indent=2, ensure_ascii=False)).items())['translations'][0]['translation'])
    except Exception as e:
        print(str(e))
        tr=translator.translate(t).text
        pass
    print(tr)
    if(str(tr).lower().strip()==str(message.content.lower().strip())):
        return
    await message.channel.send("Translation : " + tr)

@client.event
async def on_ready():
    print("Logged In")
    
client.run('<bot token>',bot=True)
