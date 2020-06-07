import discord
import requests
import json
from json import JSONEncoder
import time
import os.path
import asyncio
import mysql.connector
from mysql.connector import connection
from mysql.connector import errorcode
from itertools import cycle
from random import randint
from urllib.request import Request, urlopen

insert_token = input("Please insert 1 token: ")
if insert_token == "":
    exit(1)


def randomText_Mention():
    Words = [":thinking:", "안녕하세요", "뭐해?", ":joy:", ":poop:", ":thumbsup:", ":eyes:", ":P", ":+1:", "Hello", "Hi!", "สวัสดี", "ดีจ้า", "How was your day", "ว่าไง?", "อะไร?", "ไม่สน", "อย่ามายุ่ง", "ลาก่อน", "Leave me alone!!!!", "สวย", "เริ่ดมาก", "เชิญห้องปกครอง", "อ๊อยหย๋อ", "ลาออก!", "ไม่อ่าน ไม่ตอบ ไม่สน...", ";w;", "=A=!", "- -*", "แล้วไง?",
             "https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde", "https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ", "https://giphy.com/gifs/happy-rainbow-capoo-XEgmzMLDhFQAga8umN", "https://giphy.com/gifs/cat-color-capoo-dYZxsY7JIMSy2Afy6e", "ระเบิดเวลา......**อ๊าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา**", "เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์", "**How Dare You!!??**"]
    return Words[randint(0, len(Words)-1)]


def randomText_Hello():
    Words = ["สวัสดีเจ้า", "สวัสดีจ้า", "สวัสดีครับ", "สวัสดีค่ะ", "ສະບາຍດີ", "Annyeonghaseyo", "Kon'nichiwa", "Hello", "привет!", "ว่าไง", ";w;?",
             "Meow Meooww?", ":wave:", "https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg", "Nǐ hǎo", "วอล ที ที วอล ที", "สวัสดีครั๊บบบบบบ!"]
    return Words[randint(0, len(Words)-1)] + " {0.author.mention}"

class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged in as ' + self.user.name +
              " (" + str(self.user.id) + ")\n------")
        await client.change_presence(activity=discord.Game(name='รอเด็กมาโรงเรียน'))

    async def on_message(self, message):
        if message.content.startswith('/hello'):
            await message.channel.send(randomText_Hello().format(message))
        if message.content.startswith('/help') or message.content.startswith('!help'):
            em = discord.Embed(title="สิ่งที่น้องทำได้",
                               description="มีแค่นี้แหละ")
            em.add_field(name="/help", value="ก็ที่ทำอยู่ตอนนี้แหละ")
            em.add_field(name="/hello", value="คำสั่งคนเหงา")
            em.add_field(name="/verify", value="สำหรับยืนยันตัวตน")
            await message.channel.send(content=None, embed=em)

        if message.content.startswith('/checkid '):
            mess_input = message
            user_id = str(message.author.id)
            text = message.content[len('/checkid '):].split()
            std_id = text[0]

            response = requests.get("https://smd.pondja.com/api/student")
            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')
            
            checkId = int(std_id)

            if (checkId > 610000):

                Con = response.json()

                api_res_id = Con["std"][std_id][0]["id"]
                api_res_prefix = Con["std"][std_id][0]["prefix"]
                api_res_firstname = Con["std"][std_id][0]["firstname"]
                api_res_lastname = Con["std"][std_id][0]["lastname"]
                api_res_grade = Con["std"][std_id][0]["grade"]
                api_res_class = Con["std"][std_id][0]["class"]

                await message.channel.send("Response: \nชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")
            
            else:
                await message.channel.send("Response: \n`ศิษย์เก่า`")

        if message.content.startswith('/verify '):
            mess_input = message
            user_id = str(message.author.id)
            text = message.content[len('/verify '):].split()
            std_id = text[0]
            std_firstname = text[1]
            std_lastname = text[2]

            response = requests.get("https://smd.pondja.com/api/student")
            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')

            checkId = int(std_id)

            if (checkId > 610000):

                Con = response.json()

                api_res_id = Con["std"][std_id][0]["id"]
                api_res_prefix = Con["std"][std_id][0]["prefix"]
                api_res_firstname = Con["std"][std_id][0]["firstname"]
                api_res_lastname = Con["std"][std_id][0]["lastname"]
                api_res_grade = Con["std"][std_id][0]["grade"]
                api_res_class = Con["std"][std_id][0]["class"]

                await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")

                # Data Match
                if (api_res_firstname == std_firstname and api_res_lastname == std_lastname):
                    role = discord.utils.get(
                        message.author.guild.roles, name=api_res_grade + "/" + api_res_class)
                    role2 = discord.utils.get(
                        message.author.guild.roles, name="M:" + api_res_grade)
                    role3 = discord.utils.get(
                        message.author.guild.roles, name="Student")
                    # await message.author.add_roles(abc.+)

                    cnx = mysql.connector.connect(user='pondjaco', password='11032545', host='p0nd.ga', database='pondjaco_smdkku')
                    cursor = cnx.cursor()

                    query_func = ("UPDATE `std_2563_discordDB` SET `discord_user_id` = %s WHERE `id` = %s")
                    data_query = (message.author.id, text[0])

                    # Insert new employee
                    cursor.execute(query_func, data_query)
                   
                    # Make sure data is committed to the database
                    cnx.commit()

                    cursor.close()
                    cnx.close()
                    
                    await message.author.edit(roles=[role, role2, role3])
                    await message.author.edit(nick=api_res_prefix + " " + api_res_firstname + " " + api_res_lastname)
                    await message.channel.send("Status: :white_check_mark:")
                    # await message.author.change_nickname(api_res_prefix + " " + api_res_firstname + " " + api_res_lastname)
                else:
                    await message.channel.send("Status: :x:")

            else:
                await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + std_firstname + "`\nนามสกุล: `" + std_lastname + "`\nระดับชั้น: `ศิษย์เก่า`")
                await message.channel.send("Status: :white_check_mark:")
                role = discord.utils.get(
                    message.author.guild.roles, name="ศิษย์เก่า")
                role2 = discord.utils.get(
                    message.author.guild.roles, name="Student")
                await message.author.edit(roles=[role, role2])

        if message.content.startswith('/announce'):
            Mes_Str = message.content[len('/announce')+1:]
            channel = client.get_channel(700718680333615154)
            await message.delete()
            await channel.send("@everyone\n"+Mes_Str)

        if message.content.startswith('/update'):
            Mes_Str = message.content[len('/update')+1:]
            channel = client.get_channel(700875375651192832)
            await message.delete()
            await channel.send("@everyone\n"+Mes_Str)

        if message.content.startswith('say('):
            Str_Content = message.content
            await message.delete()
            # Say(4412) ไอ้นี้มันอู้งานครับบ
            Id_channel = Str_Content.find("(")

            for i in range(1, 40):
                if Str_Content[Id_channel+i] == ")":
                    channel = client.get_channel(
                        int(Str_Content[Id_channel+1:Id_channel+i]))
                    await channel.send(Str_Content[Id_channel+i+2:])
                    break

        for Mem in message.mentions:
            if self.user.name == Mem.display_name:
                await message.channel.send(randomText_Mention())
                break

    async def on_guild_join(guild):
        await guild.system_channel.send("กราบสวัสดีพ่อแม่พี่น้องครับ")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'สวัสดีเจ้า {0.mention} สู่ {1.name}!\nอย่าลืมเข้าไปอ่าน #สมาชิกใหม่โปรดอ่าน และทำการยืนยันตัวตนใน #verify-member ด้วยนะครับ !'.format(
                member, guild)
            await guild.system_channel.send(to_send)

    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'ลาก่อย {0.mention}!'.format(member)
            await guild.system_channel.send(to_send)

    async def announcements(Con):
        channel = client.get_channel(700718680333615154)
        await channel.send(Con)


client = MyClient()
client.run(insert_token)
