import discord

TOKEN = 'NzAwNjU3NDI5MTMzOTE4MjQ4.XpsmVA.9s-KPwqnOPC5m4Siol9tnhOMiF0'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('!score'):
        msg = str(eval(message.content.replace('!score',''))).format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
