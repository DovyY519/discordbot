import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("봇 테스트받는중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("어쩌라고")
    if message.content.startswith("죽을래?"):
        await message.channel.send("별로")
    if message.content.startswith("택경이의 은밀한 사생활"):
        await message.channel.send("택경이의 사생활은 내가 알기론 일단 요즘따라 택경이가 전화를 많이 하는데 그건 다 여자들이랑 얘기를 한거래 그리고 택경이가 가끔씩 서산 놀러 간것도 다 그런거고 저번에 반지를 맞춘것도 자기 입으론 여자라고 했는데 실은 여자랑 한거야 다른 궁금한 거리 있어?")
    if message.content.startswith("나 심심해"):
        await message.channel.send("그래서? 내가 뭐 어떻게 해줄까? 너가 어린애야? 맨날 나한테 놀아달래")
    if message.content.startswith("닥쳐"):
        await message.channel.send("니 아가리나 닥쳐")
    if message.content.startswith("병신"):
        await message.channel.send("나보다 공부못하는게 깝치지마")
    if message.content.startswith("나가"):
        await message.channel.send("나한테 관리자 권한있는거 몰라? 조심해라")
    if message.content.startswith("욕해봐"):
        await message.channel.send("난 욕같은거 모르는 봇인데요 욕이 뭐에요????")
    if message.content.startswith("야"):
        await message.channel.send("나한테 반말했냐?")
    if message.content.startswith("너 싫어"):
        await message.channel.send("원래 아싸들이 그런말 많이 하던데")
    if message.content.startswith("손절"):
        await message.channel.send("너 나 없으면 친구도 없잖아")
    if message.content.startswith("너 경서"):
        await message.channel.send("???? 넌 진짜 손절이다 나한테 얘기도 하지 마라")
    if message.content.startswith("너 어준"):
        await message.channel.send("흠.... 그것도 심하긴 한데 그나마 낫지")

        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
