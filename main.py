import discord,requests
from discord.ext import commands

'''
Dont be a skid its very easy to setup.
'''

token = "tokenhere"
prefix = '!!'
intents = discord.Intents().all()
client= commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

'''
I only made it get well known executors, and not the other ones no one cares about that are also listed on that api
'''

def stat(exploit):
    r = requests.get("https://api.whatexploitsare.online/status")
    jso = r.json()
    if exploit == "synapse":
        if jso[0]['Synapse']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
    elif exploit == "scriptware":
        if jso[1]['Script-Ware']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
    elif exploit == "krnl":
        if jso[2]['KRNL']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
    elif exploit == "electron":
        if jso[5]['Electron']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
    elif exploit == "wedev":
        if jso[6]['WeAreDevs API']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
    elif exploit == "fluxes":
        if jso[8]['Fluxus']['updated'] == True:
            return "`[🟢]`"
        else:
            return "`[🔴]`"
          
def rversion():
  r = requests.get("https://api.whatexploitsare.online/status")
  jso = r.json()
  return jso[12]['ROBLOX']['version']

@client.command()
async def status(ctx):
  embed=discord.Embed(title="Executer Status's:", color=0xfbff00)
  embed.add_field(name="Roblox Version:", value=f"`[ {rversion()} ]`", inline=False)
  embed.add_field(name="Synapse:", value=stat("synapse"), inline=False)
  embed.add_field(name="Script-Ware:", value=stat("scriptware"), inline=False)
  embed.add_field(name="KRNL:", value=stat("krnl"), inline=False)
  embed.add_field(name="Electron:", value=stat("electron"), inline=False)
  embed.add_field(name="WeAreDevs API:", value=stat("wedev"), inline=False)
  embed.add_field(name="Fluxus:", value=stat("fluxes"), inline=False)
  await ctx.reply(embed=embed)
  
client.run(token)
