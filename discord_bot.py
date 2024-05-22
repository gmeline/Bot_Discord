import random
import discord
from discord.ext import commands

intents = discord.Intents().all()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is connected!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('pong')
    elif message.content.startswith('MSPR'):
        await message.channel.send('Roohhhh Chut')
    elif message.content.startswith('!touché'):
        await message.channel.send('coulé !')
    elif message.content.startswith('Salut'):
        await message.channel.send('Salut ! :relaxed: comment ça va?:thinking: ')
    elif message.content.startswith('ça va'):
        await message.channel.send('Ah nickel alors !:partying_face: :smiling_face_with_3_hearts:  ')
    elif message.content.startswith('tranquille et toi?'):
        await message.channel.send('je suis un bot je vais toujours bien :robot: :thumbsup:  ')
    elif message.content.startswith('comment tu vas?'):
        await message.channel.send('je suis un bot je vais toujours bien :robot: :thumbsup:  ')
    elif message.content.startswith('lillew'):
        await message.channel.send('LILLLLEEEEWWWWWWW  ')
    elif message.content.startswith('Tibo?'):
        await message.channel.send('TTTTTHHHHHHIIIIIIBBBBBBBBAAAAUUUUUUUTTTTTTTT ')
    elif message.content.startswith('Rémi?'):
        await message.channel.send(':smiling_face_with_3_hearts:')
    elif message.content.startswith('Roohhhh Chut'):
        await message.channel.send('😇')
    elif message.content.startswith('Méline?'):
        await message.channel.send('MMMMMMMMMMMMMMMMMMMMMMMMMEEEEEEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLL')
    elif message.content.startswith('Je peux tester quoi?'):
        await message.channel.send('!ping, MSPR, !touché, Salut, ça va, tranquille et toi?, comment tu vas?, lillew, Tibo?, Rémi?, Méline?, !members')
    elif message.content.startswith('!members'):
        guild = message.guild
        members = guild.members
        member_list = []
        for member in members:
            emoji = random.choice([":princess:", ":disguised_face: ", "", ":space_invader:"])
            pseudonym = f"{member.name}#{member.discriminator}"
            role = member.top_role.name if member.top_role else "None"
            member_list.append(f"{emoji} {pseudonym} ({role})")
        await message.channel.send('\n'.join(member_list))
    elif message.content.startswith('Bonjour'):
        await message.channel.send('👋:heart: ')

#connexion du bot au serveur avec au token
bot.run("TOKEN")
