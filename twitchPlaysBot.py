# oauth and Client_ID is stored in .env
import os # for importing env vars for the bot to use
import simulateInput
from twitchio.ext import commands

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

#Welcome Message
@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


#Function is called everytime a message is end in chat
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    
    #When '!'-prefix is used this function looks for fitting commands
    await bot.handle_commands(ctx)
    # responds when somebody writes hello
    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")
    
    if 'hallo' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    #Use Alt    
    #if 'alt' in ctx.content.lower():
    #    await simulateInput.AltTab()
    #Echoes back the same message
    #await ctx.channel.send(ctx.content)
    
#Chat command has to be used with '!'
@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='w')
async def w(ctx):
    await simulateInput.HoldKeyTenMil(0x57)
    
@bot.command(name='a')
async def a(ctx):
    await simulateInput.HoldKeyTenMil(0x41)

@bot.command(name='s')
async def s(ctx):
    await simulateInput.HoldKeyTenMil(0x53)

@bot.command(name='d')
async def d(ctx):
    await simulateInput.HoldKeyTenMil(0x44)

@bot.command(name='space')
async def space(ctx):
    await simulateInput.HoldKeyTenMil(0x20)

@bot.command(name='q')
async def q(ctx):
    await simulateInput.HoldKeyTenMil(0x51)

@bot.command(name='e')
async def e(ctx):
    await simulateInput.HoldKeyTenMil(0x45)

@bot.command(name='shift')
async def shift(ctx):
    await simulateInput.HoldKeyTenMil(0x10)

@bot.command(name='holdShift')
async def shift(ctx):
    await simulateInput.PressKey(0x10)

@bot.command(name='releaseShift')
async def shift(ctx):
    await simulateInput.ReleaseKey(0x10)

#Makes the bot run
if __name__ == "__main__":
    bot.run()