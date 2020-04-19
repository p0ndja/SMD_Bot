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
    Words = ["จงทำโจทย์ จงทำโจทย์ จงทำโจทย์","ทำโจทย์เถอะ ขอหล่ะ","ว่างมากนั้นก็ไปทำโจทย์สิ","ไม่อ่าน ไม่ตอบ ไม่สน...","แต่ว่า...ทำโจทย์ด้วยสิ...",";w;","=A=!","- -*","แล้วไง?","https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde","https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ","https://giphy.com/gifs/happy-rainbow-capoo-XEgmzMLDhFQAga8umN","https://giphy.com/gifs/cat-color-capoo-dYZxsY7JIMSy2Afy6e","ระเบิดเวลา......**อ๊าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา**","โฮ่... แทนที่แกจะเข้าค่ายอื่น แกกลับเดินมาค่ายคอม อย่างนั้นนะเรอะ","เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์","**How Dare You!!??**","เคยฟังรึเปล่า... X ติดไซเรน (https://pastebin.com/6a7u1b85)","พี่รู้ว่ามันเศร้า แต่จงทำโจทย์ต่อไปครับ","ญิรดีร์ฏ้อณรับสูเก็ฒเฎอร์ฌาวไฑญ",":thinking:",":joy:",":poop:",":+1:",":eyes:",":P"]
    return Words[randint(0,len(Words)-1)]

def Get_Random_Text_forHello():
    Words = ["สวัสดีเจ้า","สวัสดีจ้า","สวัสดีครับ","สวัสดีค่ะ","ສະບາຍດີ","Annyeonghaseyo","Kon'nichiwa","Hello","привет!","ว่าไง",";w;?","Meow Meooww?",":wave:","https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg","Nǐ hǎo"]
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
