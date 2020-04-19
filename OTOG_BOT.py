import discord
import requests
import json
from json import JSONEncoder
import time
import os.path
import asyncio
from itertools import cycle
from random import randint
from urllib.request import Request, urlopen

TOKEN = input("Tell me your TOKEN :) :")
if TOKEN == "":
	print("WTF MANN")
	exit(1)

def Get_Random_Text_forMention():
    Words = [":thinking:","안녕하세요","뭐해?",":joy:",":poop:",":thumbsup:",":eyes:",":P",":+1:","Hello","Hi!","สวัสดี","ดีจ้า","How was your day","ว่าไง?","อะไร?","ไม่สน","อย่ามายุ่ง","ลาก่อน","Leave me alone!!!!","สวย","เริ่ดมาก","เชิญห้องปกครอง","อ๊อยหย๋อ","ลาออก!","ไม่อ่าน ไม่ตอบ ไม่สน...",";w;","=A=!","- -*","แล้วไง?","https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde","https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ","https://giphy.com/gifs/happy-rainbow-capoo-XEgmzMLDhFQAga8umN","https://giphy.com/gifs/cat-color-capoo-dYZxsY7JIMSy2Afy6e","ระเบิดเวลา......**อ๊าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา**","เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์","**How Dare You!!??**"]
    return Words[randint(0,len(Words)-1)]

def Get_Random_Text_forHello():
    Words = ["สวัสดีเจ้า","สวัสดีจ้า","สวัสดีครับ","สวัสดีค่ะ","ສະບາຍດີ","Annyeonghaseyo","Kon'nichiwa","Hello","привет!","ว่าไง",";w;?","Meow Meooww?",":wave:","https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg","Nǐ hǎo","วอล ที ที วอล ที","สวัสดีครั๊บบบบบบ!"]
    return Words[randint(0,len(Words)-1)] + " {0.author.mention}"


class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		await client.change_presence(activity=discord.Game(name='รอทำคอนเทส'))

	async def on_message(self, message):
        # we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return


		if message.content.startswith('hello()'):
			await message.channel.send(Get_Random_Text_forHello().format(message))
		if message.content.startswith('help()') or message.content.startswith('!help'):
			em = discord.Embed(title = "สิ่งที่น้อมทำได้",description = "มีแค่นี้แหละ")
			em.add_field(name = "help()",value = "ก็ที่ทำอยู่ตอนนี้แหละ")
			em.add_field(name = "hello()",value = "คำสั่งคนเหงา")

			await message.channel.send(content = None ,embed = em)


		for Mem in message.mentions:
			if self.user.name == Mem.display_name:
				await message.channel.send(Get_Random_Text_forMention())
				break

	async def on_guild_join(guild):
		await guild.system_channel.send("กราบสวัสดีพ่อแม่พี่น้องครับ")

	async def on_member_join(self, member):
		guild = member.guild
		if guild.system_channel is not None:
			to_send = 'สวัสดีเจ้า {0.mention} สู่ {1.name}!'.format(member, guild)
			await guild.system_channel.send(to_send)

	async def on_member_remove(self, member):
		guild = member.guild
		if guild.system_channel is not None:
			to_send = 'ลาก่อย {0.mention}!'.format(member)
			await guild.system_channel.send(to_send)

	async def announcements(Con):
		channel = client.get_channel(691618323468779532)
		await channel.send(Con)



client = MyClient()
client.run(TOKEN)
