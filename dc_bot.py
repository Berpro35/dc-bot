import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('telefon kartı'):
        await message.channel.send("1000 yılda kaybolur")
    elif message.content.startswith('pil'):
        await message.channel.send("300 yılda kaybolur")
    elif message.content.startswith('alüminyum'):
        await message.channel.send("100 yılda kaybolur")
    elif message.content.startswith('plastik'):
        await message.channel.send("1000 yılda kaybolur")
    elif message.content.startswith('karton kutu'):
        await message.channel.send("2 ayda kaybolur")
    elif message.content.startswith('atıklarla ilgili bilgi'):
        await message.channel.send("telefon kartı,pil,alüminyum,plastik,karton kutu lütfen aralarından birini seçin onun dışındakiler çalışmayacaktır :)")
    else:
        await message.channel.send(message.content)

client.run("token girin")
