import discord
from disrider.disrider import Disrider

client = discord.Client()
token = "ODA5NjU1MTc3Nzc3Nzc0NTkz.YCYQJQ.WYK4bsUnRSJ1d47CBL_UzRpNM5s"

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTY3ODI1NjUwMyIsImF1dGhfaWQiOiIyIiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIiwic2VydmljZV9pZCI6IjQzMDAxMTM5MyIsIlgtQXBwLVJhdGUtTGltaXQiOiI1MDA6MTAiLCJuYmYiOjE2NDY2NDcyMzMsImV4cCI6MTY2MjE5OTIzMywiaWF0IjoxNjQ2NjQ3MjMzfQ.Gz_eOkxpr5kGj0debqETXRnc51tQeW_VS1sUAlQeme4"
disrider = Disrider(api_key)

@client.event
async def on_ready():
    print("1")

@client.event
async def on_message(message):
    if message.content.startswith("!테스트 "):
        nickname = message.content.replace("!테스트 ", "")
        try:
            await disrider.default_info(ctx=message.channel, nickname=nickname, embed_color=0xFF9900)

        except:
            await message.channel.send("존재하지 않는 라이더명입니다.")

    if message.content.startswith("!테스트2 "):
        nickname = message.content.replace("!테스트2 ", "")
        user_info = disrider.character(nickname)
        embed = discord.Embed()
        embed.set_image(url=f"attachment://{user_info['locateID']}")
        await message.channel.send(embed=embed, content=user_info['characterName'], file=user_info['file'])

client.run(token)