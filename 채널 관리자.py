import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("봇 테스트받는중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

@client.event
async def on_message(message):
    if message.content.startswith("명령어"):
         embed = discord.Embed(color=0x00ff00)
         embed.add_field(value="안녕,죽을래?택경이의 은밀한 사생활", name="봇과의 대화를 하기 위해선 이렇게 작성해야 합니다", inline=True)
         await message.channel.send(embed=embed)



client.run("NjczNzI3NzM0NzkwNDg4MTA0.XjeP_A.ITkXBzhdo2oVrDNFiCz85uPDEAI")