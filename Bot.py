import pprint
import ffmpeg
from quickchart import QuickChart,serialize
from discord.utils import get
import time
import os
import youtube_dl
from requests import Request, Session
from discord_components import DiscordComponents,Component,Button,SelectOption,Select,ButtonStyle,ComponentsBot
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from discord import Member
from discord_ui import Button
import humanfriendly
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import datetime
import json
import random
from discord.ext.commands import has_permissions, MissingPermissions
import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from boto.s3.connection import S3Connection
from discord import FFmpegPCMAudio
from os import system

Bot_Token = os.environ['Bot_Token']
Crypto_Token = (os.environ['Crypto_Token'])
Gif_Token = (os.environ['Gif_Token'])
Sticker_Token = (os.environ['Sticker_Token'])
Photo_Client_Id = (os.environ['Photo_Client_Id'])
Nft_Token = (os.environ['Nft_Token'])

bot = Bot(command_prefix="$")
DiscordComponents(bot)
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.command(name="hello")
async def hello(message):
  await message.channel.send("Hello")
  await message.channel.send("https://tenor.com/view/hello-hi-jump-squirrel-gif-18535475")

async def is_owner(message):
  return message.author.id == 875971089073852433

async def is_owners(message):
  return message.author.id == 904765995598610473 or 875971089073852433

@bot.command(name="rickroll")
@commands.check(is_owner)
async def rickroll(message):
  await message.channel.send("https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173")
  time.sleep(2)
  await message.channel.send("You Just Got Rick rolled",tts=True)
  await message.channel.send("So don't try to deny it",tts=True)

@rickroll.error
async def kick_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")

@bot.command(name="owner")
async def owner(message):
  embed = discord.Embed(
    title=message.guild.name + " Member😎",
    description="My Info",
    color=discord.Color.blue()
  )
  embed.set_thumbnail(
    url="https://cdn.discordapp.com/avatars/875971089073852433/910b88ed17ef3b2080b9175d312f5b07.webp?size=80")
  embed.add_field(name="Name", value="Tenura Pasandul", inline=True)
  embed.add_field(name="Job", value="Student", inline=True)
  embed.add_field(name="Region", value="Sri lanka", inline=True)
  embed.add_field(name="Email", value="tenura2007@gmail.com", inline=True)
  embed.add_field(name="Interests", value="Who likes to DEVELOP AND CODE AND HACK", inline=True)
  embed.set_image("https://t3.ftcdn.net/jpg/04/06/74/78/360_F_406747816_wFW46cS66MEIbaGB0PVqBf89uJ4LALjw.jpg")
  await message.channel.send(embed=embed)

@bot.command(name="timeout")
async def timeout(message, user:discord.User=None, time=None, *, reason=None):
  time = humanfriendly.parse_timespan(time)
  await user.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=time),reason=reason)


@bot.command(name="untimeout")
async def timeout(message, user: discord.User = None, time=None, *, reason=None):
  time = humanfriendly.parse_timespan(time)
  await user.timeout(until=discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)

@bot.command(name="role")
async def role(message, user: Member):
  guild = message.guild
  role = discord.utils.get(guild.roles, id=960382397206118420)
  await user.add_roles(role)

@bot.command(name="stfu")
@commands.check(is_owner)
async def stfu(message):
  await message.channel.send('https://tenor.com/view/stfu-shut-up-stop-shut-your-mouth-shut-it-down-gif-20324546')

@stfu.error
async def kick_error(error, message):
    if isinstance(error, commands.CheckFailure):
      await message.channel.send("Command Error")

@bot.command(name="crypto",pass_context=True)
async def crypto(message,symble):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  url2 = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
  parameters = {
    "symbol": symble,
    'convert': 'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': Crypto_Token,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    name = (json.loads(response.text)['data'][symble]['name'])
    symbol = (json.loads(response.text)['data'][symble]['symbol'])
    price = (json.loads(response.text)['data'][symble]['quote']['USD']['price'])
    id = (json.loads(response.text)['data'][symble]['id'])

    parameters2 = {
      'id': id
    }
    response2 = session.get(url2, params=parameters2)
    logo = (json.loads(response2.text)['data'][str(id)]['logo'])
    added_date = (json.loads(response2.text)['data'][str(id)]['date_added'])


    embed = discord.Embed(
    title="Crypto Currency",
    description="Live Info",
    color=discord.Color.blue()
      )
    embed.set_thumbnail(
    url=logo)
    embed.add_field(name="Name", value=name, inline=True)
    embed.add_field(name="Symble", value=symble, inline=True)
    embed.add_field(name="Price", value=price, inline=True)
    embed.add_field(name="Id", value=id, inline=True)
    embed.add_field(name="Added Date", value=added_date, inline=True)
    embed.set_image(url="https://images.hdqwalls.com/wallpapers/bthumb/bitcoin-monk-pp.jpg")

    await message.channel.send(embed=embed)

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    await message.channel.send(e)

@crypto.error
async def kick_error(error, message):
    if isinstance(error, commands.CommandInvokeError):
      message.channel.send("Command Error")

@bot.command(name="nasa",pass_context=True)
async def crypto(message):
  url = "https://api.nasa.gov/planetary/apod?api_key=FkxhqBfPKBxB3jhZ2iIntycQIrR509iH8zgtO6TK"
  response = requests.get(url)
  copyright = (response.json()['copyright'])
  date = (response.json()['date'])
  explanation = (response.json()['explanation'])
  hdurl = (response.json()['hdurl'])
  title = (response.json()['title'])
  url = (response.json()['url'])
  hdurl5 = (response.json())
  embed = discord.Embed(
    title=title,
    description="Nasa Info",
    color=discord.Color.blue()
  )
  embed.set_thumbnail(url="https://static.vecteezy.com/system/resources/previews/005/852/366/original/vintage-cartoon-astronaut-in-space-vector.jpg")
  embed.add_field(name="Date", value=date, inline=True)
  embed.add_field(name="Copyright", value=copyright, inline=True)
  embed.add_field(name="Url", value=url, inline=True)
  embed.add_field(name="explanation", value=explanation, inline=True)

  await message.channel.send(embed=embed)
@bot.command(name="table", pass_context=True)
async def table(message):
  ATOMMASS = []
  elements = []
  Try = 1
  url = "https://periodic-table-elements-info.herokuapp.com/elements"
  parameters = {}
  payload = {}
  headers = {
    'Accepts': 'application/json', }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  while Try != 118:
    name = (json.loads(response.text)[Try]['name'])
    boilingPoint = (json.loads(response.text)[Try]['boilingPoint'])
    elements.append(name)
    ATOMMASS.append(boilingPoint)
    Try = Try + 1
  qc = QuickChart()
  qc.width = 1024
  qc.height = 1024
  qc.background_color = "rgb(0,250,154)"
  qc.hoverBackgroundColor = "rgb(0,0,128)"
  qc.fill = "false"
  qc.config = {
    "type": "radar",
    "data": {
      "labels": elements,
      "datasets": [{
        "label": "Boiling Point",
        "data": ATOMMASS
      }]
    }

  }
  await message.channel.send(qc.get_short_url())

@bot.command(name="element")
async def element(message,element:str):
  Ele = ("https://periodic-table-elements-info.herokuapp.com/element/symbol/"+element)
  parameters = {}
  payload = {}
  headers = {
    'Accepts': 'application/json', }
  session = Session()
  session.headers.update(headers)
  response = session.get(Ele, params=parameters)
  name = (json.loads(response.text)[0]['name'])
  symbol = (json.loads(response.text)[0]['symbol'])
  standardState = (json.loads(response.text)[0]['standardState'])
  atomicMass = (json.loads(response.text)[0]['atomicMass'])
  atomicNumber = (json.loads(response.text)[0]['atomicNumber'])
  boilingPoint = (json.loads(response.text)[0]['boilingPoint'])
  group = (json.loads(response.text)[0]['group'])
  embed = discord.Embed(
    title="Periodic Table",
    description="Elements",
    color=discord.Color.blue()
  )
  embed.set_thumbnail(url="https://i.pinimg.com/originals/82/25/f7/8225f7682d7ddc7c528141f5867be341.gif")
  embed.add_field(name="name", value=name, inline=True)
  embed.add_field(name="symbol", value=symbol, inline=True)
  embed.add_field(name="standardState", value=standardState, inline=True)
  embed.add_field(name="atomicMass", value=atomicMass, inline=True)
  embed.add_field(name="atomicNumber", value=atomicNumber, inline=True)
  embed.add_field(name="boilingPoint", value=boilingPoint, inline=True)
  embed.add_field(name="group", value=group, inline=True)
  embed.set_image(url="https://wallpapercave.com/wp/wp3059183.png")
  await message.channel.send(embed=embed)

@element.error
async def element_error(error, message):
    if isinstance(error, commands.CommandInvokeError):
      message.channel.send("Command Error")

@bot.command(name="nba")
async def nba(message,nba:str):
  url = ("https://www.balldontlie.io/api/v1/players")
  parameters = {
    "search":nba
  }
  payload = {}
  headers = {
    'Accepts': 'application/json' }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  first_name = (json.loads(response.text)['data'][0]['first_name'])
  last_name = (json.loads(response.text)['data'][0]['last_name'])
  height_feet = (json.loads(response.text)['data'][0]['height_feet'])
  weight_pounds = (json.loads(response.text)['data'][0]['weight_pounds'])
  abbreviation = (json.loads(response.text)['data'][0]['team']['abbreviation'])
  city = (json.loads(response.text)['data'][0]['team']['city'])
  conference = (json.loads(response.text)['data'][0]['team']['conference'])
  division = (json.loads(response.text)['data'][0]['team']['division'])
  embed = discord.Embed(
    title="NBA Players",
    description=(nba+" Player Info"),
    color=discord.Color.blue()
  )
  embed.add_field(name="First Name", value=first_name, inline=True)
  embed.add_field(name="Last Name", value=last_name, inline=True)
  embed.add_field(name="Height Feet", value=height_feet, inline=True)
  embed.add_field(name="Weight Pounds", value=weight_pounds, inline=True)
  embed.add_field(name="Abbreviation", value=abbreviation, inline=True)
  embed.add_field(name="City", value=city, inline=True)
  embed.add_field(name="Conference", value=conference, inline=True)
  embed.add_field(name="Division", value=division, inline=True)
  await message.channel.send(embed=embed)

@nba.error
async def nba_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(name="gif")
async def gif(message,inp:str):
  url = ("https://api.giphy.com/v1/gifs/search?")
  parameters = {
    'api_key':Gif_Token,
    'q':inp,
    'limit':25,
    'offset':0,
    'rating':'g',
    'lang':'en'
  }
  payload = {}
  headers = {
    'Accepts': 'application/json' }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  gif = (json.loads(response.text)['data'][0]['images']['fixed_height']['url'])
  await message.channel.send(gif)

@gif.error
async def nba_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(name="sticker")
async def sticker(message,inp:str):
  num = random.randint(1, 24)
  url = ("https://api.giphy.com/v1/stickers/search?")
  parameters = {
    'api_key':Sticker_Token,
    'q':inp,
    'limit':25,
    'offset':0,
    'rating':'g',
    'lang':'en'
  }
  payload = {}
  headers = {
    'Accepts': 'application/json' }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  sticker = (json.loads(response.text)['data'][num]['images']['fixed_height']['url'])
  await message.channel.send(sticker)

@bot.command(name="photo")
async def photo(message,search:str):
  btn = []
  url = ("https://api.unsplash.com/search/photos?")
  parameters = {
    "client_id":Photo_Client_Id,
    "page":1,
    "query":search
  }
  payload = {}
  headers = {
    'Accepts': 'application/json' }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  embed = discord.Embed(
    title="Photos",
    description=("HD"),
    color=discord.Color.blue()
  )
  embed.set_thumbnail(url="https://cdn.dribbble.com/users/1859102/screenshots/4814254/media/30f1221ed31e77ecf898362cdfed2a02.gif")
  for x in range(9):
    wallpaper = (json.loads(response.text)['results'][x]['links']['download'])
    embed.add_field(name=f"Url {x+1}",value=wallpaper)
    embed.add_field(name="-", value="-----------------------------------------------------------", inline=False)
  embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0TTGyBV5w77aTym28ori3cF3ANwHCuUQL1A&usqp=CAU")
  await message.channel.send(embed=embed)

@sticker.error
async def sticker_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(name="command")
async def command(message):
  embed = discord.Embed(
    title="Data#0292 Commands",
    description="Command Info",
    color=discord.Color.blue()
  )
  embed.set_thumbnail(
    url="https://cdn.discordapp.com/avatars/875971089073852433/910b88ed17ef3b2080b9175d312f5b07.webp?size=80")
  embed.add_field(name="$hello", value="This command is used to send a hello for a channel", inline=False)
  embed.add_field(name="$rickroll", value="This one is used to send a rickroll message to the channel", inline=False)
  embed.add_field(name="$owner", value="This Command gives you Info about Bot owner", inline=False)
  embed.add_field(name="$stfu", value="You can think what this command does", inline=False)
  embed.add_field(name="$crypto", value="this command return you all the live info about a crypto currency you just have to enter the crypto symble after typing $crypto command"
                                        "\neg:\n$crypto BTC", inline=False)
  embed.add_field(name="$nasa", value="This gives you daily info about nasa", inline=False)
  embed.add_field(name="$table", value="This one will send the channel all the elements of the Periodic table This command can improve", inline=False)
  embed.add_field(name="$element", value="this element command helps you to find info About elements"
                                         "\neg:\n$element H", inline=False)
  embed.add_field(name="$nba", value="This Command will return Info about nba players"
                                     "\neg:\n$nba Davis \n->player's last name or first name", inline=False)
  embed.add_field(name="$gif", value="This command send a gif to a channel based on your search"
                                     "\neg:\n$gif hello \n$gif 'Hello how are you'", inline=False)
  embed.add_field(name="$sticker", value="This command send a sticker to a channel based on your search"
                                     "\neg:\n$sticker hello \n$sticker 'Hello how are you'", inline=False)
  embed.add_field(name="$photo", value="This command send you 10 wallpapers which are hd that can be used as your device wallpaper"
                                         "\neg:\n$photo car \n$photo 'nerd reading a book'", inline=False)
  embed.add_field(name="$nft", value="This command send you Info about the NFT you asked"
                                         "\neg:\n$nft 0x7de3085b3190b3a787822ee16f23be010f5f8686 1"
                                     "\n$nft <nft address> <nft id>", inline=False)
  embed.set_image(url="https://c0.wallpaperflare.com/preview/944/356/969/concept-construction-page-site.jpg")

  await message.channel.send(embed=embed)

@bot.command(name="nft")
async def nft(message,address:str,token_id:str):
  url = ("https://deep-index.moralis.io/api/v2/nft/"+address+"/"+token_id+"?chain=eth&format=decimal")
  parameters = {
    "address":address,
    "token_id":token_id
  }
  headers = {
    "Accept": "application/json",
    "x-api-key": Nft_Token
  }
  response = requests.get(url, headers=headers)
  metadata = json.loads(response.text)['metadata']
  artist = (json.loads(metadata)['artist'])
  date = (json.loads(metadata)['date'])
  dna = (json.loads(metadata)['dna'])
  edition = (json.loads(metadata)['edition'])
  image = (json.loads(metadata)['image'])
  name = (json.loads(metadata)['name'])
  fullname = (json.loads(response.text)['name'])
  owner_of = (json.loads(response.text)['owner_of'])
  symbol = (json.loads(response.text)['symbol'])
  token_address = (json.loads(response.text)['token_address'])
  token_hash = (json.loads(response.text)['token_hash'])
  token_ids = (json.loads(response.text)['token_id'])
  updated_at = (json.loads(response.text)['updated_at'])
  amount = (json.loads(response.text)['amount'])
  block_number = (json.loads(response.text)['block_number'])
  block_number_minted = (json.loads(response.text)['block_number_minted'])
  contract_type = (json.loads(response.text)['contract_type'])
  last_metadata_sync = (json.loads(response.text)['last_metadata_sync'])
  img = str(image.replace('ipfs://','https://ipfs.io/ipfs/'))
  embed = discord.Embed(
    title="Data#0292 Commands",
    description="Command Info",
    color=discord.Color.red()
  )
  embed.set_thumbnail(url="https://www.kapwing.com/resources/content/images/2021/02/final_6039a4b26a140a00a1cffbd3_143170.gif")
  embed.add_field(name="Name", value=name, inline=True)
  embed.add_field(name="Amount", value=amount, inline=True)
  embed.add_field(name="Edition", value=edition, inline=True)
  embed.add_field(name="Artist", value=artist ,inline=True)
  embed.add_field(name="Date", value=date, inline=True)
  embed.add_field(name="Symbol", value=symbol, inline=True)
  embed.add_field(name="Dna", value=dna, inline=False)
  embed.add_field(name="Owner_of", value=owner_of, inline=False)
  embed.add_field(name="Token_address", value=token_address, inline=False)
  embed.add_field(name="Token_hash", value=token_hash, inline=False)
  embed.add_field(name="Token_id", value=token_ids, inline=False)
  embed.add_field(name="Fullname", value=fullname, inline=False)
  embed.add_field(name="Updated_at", value=updated_at, inline=False)
  embed.add_field(name="Block_number", value=block_number, inline=False)
  embed.add_field(name="Block_number_minted", value=block_number_minted, inline=False)
  embed.add_field(name="Contract_type", value=contract_type, inline=False)
  embed.add_field(name="Last_metadata_sync", value=last_metadata_sync, inline=False)
  embed.add_field(name="Image Url:Now you don't need brave to do this", value=img, inline=False)
  embed.set_image(url=img)
  await message.channel.send(embed=embed)

@nft.error
async def nft_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(pass_context=True,name="play")
@commands.check(is_owners)
async def play(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Joined {channel}")
    voice2 = get(bot.voice_clients, guild=ctx.guild)
    voice2.play(discord.FFmpegPCMAudio("song.mp3"))
    voice2.volume = 100
    voice2.is_playing()

@play.error
async def play_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@play.error
async def kick_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")

@bot.command(pass_context=True,name="download")
@commands.check(is_owners)
async def Download(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    await ctx.send("Getting everything ready, playing audio soon")
    print("Someone wants to play music let me get that ready for them...")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    print("Downloading Done")
    await ctx.channel.send("Done Downloading")

@Download.error
async def Download_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@Download.error
async def Download2_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")

@bot.command(pass_context=True,name="leave")
@commands.check(is_owner)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

@leave.error
async def leave2_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")
@leave.error
async def nft_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(pass_context=True,name="pause")
@commands.check(is_owner)
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")

@pause.error
async def pause2_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")
@pause.error
async def nft_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

@bot.command(pass_context=True,name="resume")
@commands.check(is_owner)
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")

@resume.error
async def resume2_error(error, message):
    if isinstance(error, commands.CheckFailure):
      message.channel.send("Command Error")
@resume.error
async def nft_error(error, message):
  if isinstance(error, commands.CommandInvokeError):
    message.channel.send("Command Error")

bot.run(Bot_Token)




