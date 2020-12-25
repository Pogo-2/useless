import discord
import random
import time
from mutagen.wave import WAVE
import os

# setup
token = open("./token.txt", "r").read()
client = discord.Client()



@client.event
async def on_ready():
    print(f"logged in {client.user}")


@client.event
async def on_message(message):
    print(message.content)
    if "its peezy" in message.content or "it's peezy" in message.content:
        await message.channel.send(f"hey its {message.author.name}")


@client.event
async def on_voice_state_update(user, before, after):
    val = random.randint(1, 8)
    if val == 2:
        if after.channel is not None and before.channel is None and user.id != 665024859918696509:
            print("you win!!!")
            print(f"{user} joined {after.channel}")

            wait_time = random.randint(1, 30)
            print(f"waiting {wait_time}")
            time.sleep(wait_time)
            vc = await after.channel.connect()
            time.sleep(1)
            peez_list = os.listdir("./peezy_mp3")
            clip = peez_list[random.randint(0, len(peez_list) - 1)]
            audio = WAVE(f"./peezy_mp3/{clip}")
            vc.play(discord.FFmpegPCMAudio(f"./peezy_mp3/{clip}"))
            time.sleep(audio.info.length)
            for x in client.voice_clients:
                await x.disconnect()
            print("Done")




# run the bot
client.run(token)

