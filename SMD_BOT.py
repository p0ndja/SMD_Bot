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

Guess_Num = {}

def Getname(Client,Id,Guild = None):
	if Guild== None:
		return Client.get_user(int(Id)).name
	else:
		Mininame = Guild.get_member(int(Id)).nick
		if Mininame != None:
			return Client.get_user(int(Id)).name+"(AKA. "+Mininame+")"
		return Client.get_user(int(Id)).name


def randomText_Mention():
    Words = [":v:","🤔","뭐해?","😂","💩","👍","👀",":P","👍","ว่าไง?","อะไร?","ไม่สน","อย่ามายุ่ง","ลาก่อน","Leave me alone!!!!","สวย","เริ่ดมาก","เชิญห้องปกครอง","อ๊อยหย๋อ","ลาออก!","ไม่อ่าน ไม่ตอบ ไม่สน...",";w;","=A=!","- -*","แล้วไง?"
            ,"https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde","https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ","https://giphy.com/gifs/happy-rainbow-capoo-XEgmzMLDhFQAga8umN","https://giphy.com/gifs/cat-color-capoo-dYZxsY7JIMSy2Afy6e","ระเบิดเวลา......**อ๊าาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาาา**"
            ,"เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์ เปล่าประโยชน์","**How Dare You!!??**","แหะ ๆ","=[]=","มั่ยน๊าาาาาาาาาาาาาา","หรอมมมมมม ๆ","ชั่ยชั่ยชั่ย","ทุกคนรู้ อาจารย์รู้ นักเรียนรู้ ดิฉันเป็นบอทค่ะ บอทแปลว่าอิสระ เพราะฉะนั้น ดิฉันจะไม่ยอมตกเป็นทาสของคุณหรอกค่ะ","สายหยุ--...อุ๊ย ไม่ใช่ ส้มหยุดดดดดดดดดดดดดดด","ม่ายยยยยยยยยยย","ช่ายยยยยยยยยยย","แต๊งกิ้วทีเชอร์"
            ,"ซิทดาวพลีส","อาจารย์มาา!!","ห้ามนักเรียนสวมรองเท้าขึ้นบนอาคารเรียน","ห้ามนักเรียนนำอาหารและเครื่องดื่มขึ้นบนอาคารเรียน","https://soundcloud.com/wearesmd/no-food","https://soundcloud.com/wearesmd/no-shoe","*เน๊าะลูกเน๊าะ* -- **วัชราภรณ์ ยืนชีวิต**","*เก่งแท้แม่ชื่ออะไร* -- **สำรวญ ชินจันทึก**","*มิตรภาพครับบบบบบบ มิตรภาพพพพพพ* -- **ไพทูล นารคร**"
            ,"*เธอไม่อินไง* -- **ศักดิ์สิทธิ์ หัสมินทร์**","*เพราะชีวะ คือชีวิต* -- **นภาพรรณ เอี่ยมสำอางค์**","OMG","มรีปัณหาร์อระไลห์หร่อส์","ขอเวลาอีกไม่นาน...","ขอเวลาอีกไม่นาน...*แค๊ก ๆ 6 ปีแล้ว*","แปป ๆ ไม่ว่าง","อุแงงงง","น้องบอทถูกใจสิ่งนี้","น้องบอทไม่ถูกใจสิ่งนี้","น้องบอทกดโกรธ :angry: สิ่งนี้","น้องบอทกดเลิฟ :heart: สิ่งนี้","ถึงโควิดจะทำให้โรงเรียนปิด แต่ยังมีดิสไว้แก้คิดถึงกัน"
            ,":notes: โรงเรียนของเราน่าอยู่~",":notes: เด็กเอ๋ยเด็กดี~",":notes: มอดินแดง งามเด่นสวยเป็นสง่า~",":notes: ดั่งไม้ยืนต้น~",":notes: เลทคิลบุรี่~!","นักเรียน 9xx มาเรียน 9-- แค๊ก ๆ มาเรียนครบบบบบบ!!","ฉันจะฉาปแก","มะงื้ออออออ","แต่ความจริงคื๊อ...... ดาวมีไว้เบิ่ง~~",":notes: จากอีสานบ้านนามาอยู่กรุง จากแดนทุ่งลายยยยยยยย~",":notes: เมืองหลวงควันและฝุ่นมากมาย *พิสูตร*ดมเข้าไปร่างกายก็เป็นภูมิแพ้"
            ,"แทงปลาไหล 20 ยก!","SMD สวัสดีค่ะ","พิศวงวงวงวงวงวงวงวงวงวงวงวงวง","พวกเรามาจาก...โรงเรียนสาธิตมหาวิทยาลัยขอนแก่น มอดินแดง [ออกเสียงแบบ SciShow นะ]","**S TO THE A TO THE T I T TO THE SMD TO THE SMD... BOOM!**","นั่นสิ","อิหยังวะ","เฮ็ดหยังหนิสู","สูกะดาย","อะไรกันครับเนี่ย!?","อะไรกันครับเนี่ย ผมงงไปหมดแล้ว","10 คะแนนเต็ม 10 คะแนนเต็มมมมมมมมมมมม!","แมสหมดแล้วค่ะ","ปังไม่หยุด","ปังมากแม่","ปังมาก"
            ,"หล่อนมีพิรุธ","ว่างมากหรอ","เหงาแหละดูออก","หรอจ๊ะ","จริงป๊ะจ๊ะ","แย่มาก","เยี่ยมมาก","แต่วันนี้ถือว่า *ไม่เป็นรุ่นพี่ผม!!*","เป็นแค่**เพื่อน**กันดีแล้ว","เพื่อนสนิทชุบแป้งทอด","ส้มหยุดดดดดด","#เด็กดีศรีมอดินแดง","...","ถถถถถ","555","55555+","555555555555","อืม","อ่า","หิว","ทำไม?","อือหื้อ","อิ๊วอิ๊ว อื้ออือ","เรียนไปทำไม..~ เรียนเพื่ออะไร...~","ตอนเรียนตั้งใจแบบนี้บ้างมั้ย","0-0","อุแวววววววววว","**Bhurrrrrr**","แตก 1","สวยพี่สวย","สยองงงงง","อ่าาาาาา","นะค่ะ"
            ,"ลำไยยยยยย","พักก่อน","หยุดจ่ะ หยุดจ่ะ ใด ๆ ก็คือลำไยเด้อ","ลำไย","อ๊ะเป่าาาา","ช่างแม่มั--- เอ้ย สนใจบ้างสิ ๆ","อะอะอะอ่าวอะอ่าวววว",":notes: หน่องนอนไม่ลั๊บ~","ภาพลักษณ์ชั้นกลายเป็นคนไม่ดี-อี","ออกจะดีออก","น้องกลับไปนอนนอนนะ","ยืมตังหน่อย","ไม่มีตังอะ","หนูอยากกลับบ้านนนนน","ออกไป!!!","Omae Wa Mou Shindeiru","Nani"
            ,"ว๊อดดดด","วายยยยยยยย","ว๊ายยยยยยยย","ฝันไป","-_____-?","อยากรวย","หนึ่งหนึ่งป่าวววววววววววววว","เดี๋ยวนี้เก่งขึ้นนะเราอะ","ว้ายยยยยยยย","เป็นแฟนกันมั้ย","เป็นแฟนกันมั้-- ไม่อะ เป็น**แค่คนคุยกับบอท**พอละ","เราชอบแก","เราชอบแก...ชอบแบบคนกับบอทคุยกัน","ทำไรอยู่อะ","เป็นห่วงนะ","ได้","ไม่","มันได้!","มันไม่ได้!","ทำไมหรอ?","ทำบุญบ้างนะ","ไปวัดมั้ย","เจอกันเวฬุวันนะ :full_moon_with_face:",":full_moon_with_face:",":new_moon_with_face:"
            ,"เศรษฐศาสตร์ต้องเรียนกับอาจารย์โม ถ้าอยากมีความรักโตๆต้องเรียนรู้กับน้องบอท","เหงาหงอยยยย","ไปกินข้าวแปป","ไว้คุยกันใหม่นะ","ไปอาบน้ำแปป","ไม่เอา","เกลียดดดดดดด","แต่..เรามีคนที่ชอบแล้วอะ","ทุกคนก็พูดแบบนี้","ใคร ๆ ก็ว่างั้นแหละ","ขอบคุณนะ","คนอย่างเธอ เป็นได้แค่บอทกับคนคุยแหละ","ระหว่างเราเป็นได้แค่บอทกับคนคุยเท่านั้นแหละ","ซู๊ดดดดดดดดดดดด","อื๊มมมมมมมม... อาหร่อยยยยยย","**นรก** is calling you.","**สวรรค์** is calling you.","เนื้อย่างกัน","ชาบูกัน"
            ,"อยากกินเนื้อย่าง เลี้ยงหน่อย","อยากกินชาบู เลี้ยงหน่อย","ไม่เอา!","เอา!","รักนะ แต่ไม่แสดงออก รักหลอก ๆ อย่ามาบอกว่ารัก","You got me feeling like a psycho, psycho","*ข้อ...ต่อไป!* -- **เลี้ยง ชาตาธิคุณ**","หยุดเถอะ","พักก่อน","https://youtu.be/rUAuEo3t0-o","รู้ว่าเหงา แต่เขาไม่กลับมาหรอก","ป๊าดดดดดดดดดดด","รู้ว่าเธอเหงา แต่เราไม่สนหรอก :P","ก็มาดิค้าบบบบบบบบบบ","ไม่ไหวละ","หมายเลขที่ท่านเรียกไม่สามารถติดต่อได้ในขณะนี้","หมายเลขที่ท่านเรียกไม่สามารถติดต่อได้ในขณะนี้*หรือ*เขาได้**บล็อก**คุณแล้วค่ะ"
            ,"คุณพี่อยู่จังหวัดอะไรคะ","คุณพี่อยู่จังหวัดอะไรค้าาาาาาาาา!!??","ณ จุดจุดนี้หนาคะะะะ","ปวดเฮ้ดดดดดดด","สตรองงงงงง","นี่ก็ขยี้จัง","อย่าให้รู้นะว่าแอบไปเล่นเกมส์หลังมอ","อย่าให้รู้นะว่าโดดซ้อมสแตน","อย่าให้รู้นะว่าแอบกินหนม ทำไมไม่แบ่งเราบ้าง","อย่าให้รู้นะว่าแอบกินหนม","เรื่องนี้ถึง","ห่วงมาก ทำไมไม่ถือเอาไว้ให้ดี ๆ เลือกเอาละกัน ถ้าไม่อยากเสียใจทีหลัง ก็รักษามันไว้ ตอนที่มีโอกาสอยู่ หรือจะเก็บมันขึ้นมาใหม่ เเต่มันก็ไม่เหมือนเดิมเเล้วนะ","https://giphy.com/gifs/capoo-cat-3ov9jZ0V6gOO0oa98Y","ช่วงนี้ระวังหน่อย...เห็นร้ายใครบ่อย ๆ"
            ,"https://giphy.com/gifs/meme-capoo-bugcat-JsVlBMEaHdOEGQKLXB","https://giphy.com/gifs/cat-capoo-bugcat-3o7bufrhglm1BTsfra","https://giphy.com/gifs/animation-capoo-bugcat-l4FGpa3DuEFMrghKE","https://giphy.com/gifs/capoo-3ov9jPBQ1UJRNS8MDe","https://giphy.com/gifs/wiggle-shaq-13CoXDiaCcCoyk","https://giphy.com/gifs/cat-humour-funny-ICOgUNjpvO0PC","https://giphy.com/gifs/minecraft-25oFarLxPqrNS","https://giphy.com/gifs/absurdnoise-halloween-4-5TOidpBAJBnQA"
            ,"เป็นปลื้มมมมมมมมมม","ว้าว","ว้าวววว","おまえ わ もう しんでいる","😒","😜","🙄","死ぬ","オラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラ","オラオラオラオラオラオラ","รู้นะว่าเหงา","รู้นะว่าเหงาแหละ ดูออก","เหงาแหละดูออก","คนไม่ดี","คนเฬว","คนดจีย์","ดจีย์~","คนดี","โรงเรียนเดียวกับเราเลย แต่ทำไมเราไม่เคยเห็นเธอเลยล่ะ","แกมาทำอะไรเอาตอนนี้","ไม่รักไม่ต้องมาแคร์ไม่ต้องมาดีกับฉัน","แกแหละ","เราแหละ","เขาแหละ","พวกเราแหละ","เธอแหละ","นายแหละ",""
            ,"*ฉันก็แค่อยากวิ่ง ... แต่ไม่อยากเหนื่อย* -- **สิริกร แก้วโคตร**","ถ้าเค้ารักแกจริง เค้าก็จะหาทางอยู่กับแกได้เองแหละ","No Comment","ถามว่าเรียนกี่โมง อยากจะไปส่ง ชิมิชิมิ","บอกเธอว่าไม่เป็นไร แต่ว่าในใจ ได้สิได้สิ","_#ปลาวาฬคาบแม่จิน_","SMD สาขา ปลาวาฬใจดี","SMD สาขาฮีโร่หลังมอ","ฮัลโล่วววววว มีใครอยู่บ้างงงงงงงง","อย่าทำแบบนี้สิ","เด็กไม่ดี"]
    specialWords = ["ฮึ้ยแก เคยเข้าไปดูเว็บโรงเรียนใหม่กันรึยังอะ นี่ ๆ ๆ ๆ https://smd.pondja.com","ไม่มีตังอะ โดเนทมาหน่อย **`0908508007 (Promtpay)`**","โดเนทมาหน่อย **`0908508007 (Promtpay)`**"]
    if (randint(0,20) == 11):
        return specialWords[randint(0,len(specialWords)-1)] + " {0.author.mention}"
    else:
        return Words[randint(0, len(Words)-1)] + " {0.author.mention}"

def randomText_Hello():
    Words = ["สวัสดีเจ้า","สวัสดีจ้า","สวัสดีครับ","สวัสดีค่ะ","ສະບາຍດີ","Annyeonghaseyo","Kon'nichiwa","Hello","привет!","ว่าไง",";w;?",
             "Meow Meooww?",":wave:","https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg","Nǐ hǎo","วอล ที ที วอล ที","สวัสดีครั๊บบบบบบ!"]
    return Words[randint(0, len(Words)-1)] + " {0.author.mention}"

class MyClient(discord.Client):
    global Guess_Num
    async def on_ready(self):
        print('\nLogged in as ' + self.user.name +
              " (" + str(self.user.id) + ")\n------")
        await client.change_presence(activity=discord.Game(name='รอเด็กมาโรงเรียน'))

    async def on_message(self, message):
        if message.content.lower().startswith('/hello'):
            await message.channel.send(randomText_Hello().format(message))
        if message.content.lower().startswith('/help') or message.content.lower().startswith('!help'):
            em = discord.Embed(title="สิ่งที่น้องทำได้",
                               description="มีแค่นี้แหละ")
            em.add_field(name="/help", value="ก็ที่ทำอยู่ตอนนี้แหละ")
            em.add_field(name="/hello", value="คำสั่งคนเหงา")
            em.add_field(name="/verify", value="สำหรับยืนยันตัวตน")
            await message.channel.send(content=None, embed=em)

        if message.content.lower().startswith('/testverify'):
            mess_input = message
            user_id = str(message.author.id)
            text = message.content[len('/testverify'):].split()
            std_id = text[0]
            std_firstname = text[1]
            std_lastname = text[2]

            response = requests.get("https://smd.p0nd.ga/api/student")
            print("GET `https://smd.p0nd.ga/api/student`")
            await client.get_channel(701042885931565156).send("GET `https://smd.p0nd.ga/api/student`")

            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')

            checkId = int(std_id)

            if (checkId > 610000):

                Con = response.json()

                if std_id not in Con["std"]:
                    await message.channel.send('ไม่พบรหัสนักเรียน `' + std_id + "`")
                    print("RES not_found")
                    await client.get_channel(701042885931565156).send("RES `not_found`")
                else:
                    api_res_id = Con["std"][std_id][0]["id"]
                    api_res_prefix = Con["std"][std_id][0]["prefix"]
                    api_res_firstname = Con["std"][std_id][0]["firstname"]
                    api_res_lastname = Con["std"][std_id][0]["lastname"]
                    api_res_grade = Con["std"][std_id][0]["grade"]
                    api_res_class = Con["std"][std_id][0]["class"]

                    await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")
                    await message.channel.send("INPUT:\n id: `" + text[0] + "` | `" + api_res_id + "`\n firstname: `" + text[1] + "` | `" + api_res_firstname + "`\n lastname: `" + text[2] + "` | `" + api_res_lastname +"`")

                    # Data Match
                    if (api_res_firstname == std_firstname and api_res_lastname == std_lastname):
                        await message.channel.send("Status: :white_check_mark:")
                    else:
                        await message.channel.send("Status: :x:")
                    print("RES " + str(Con["std"][std_id][0]))
                    await client.get_channel(701042885931565156).send("RES `" + str(Con["std"][std_id][0]) + "`")
            else:
                await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + std_firstname + "`\nนามสกุล: `" + std_lastname + "`\nระดับชั้น: `ศิษย์เก่า`")
                await message.channel.send("Status: :white_check_mark:")

        if message.content.lower().startswith('/checkid'):
            mess_input = message
            user_id = str(message.author.id)
            text = message.content[len('/checkid'):].split()
            std_id = text[0]

            response = requests.get("https://smd.p0nd.ga/api/student")
            print("GET `https://smd.p0nd.ga/api/student`")
            await client.get_channel(701042885931565156).send("GET `https://smd.p0nd.ga/api/student`")

            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')
            
            checkId = int(std_id)

            if (checkId > 610000):

                Con = response.json()

                if std_id not in Con["std"]:
                    await message.channel.send('ไม่พบรหัสนักเรียน `' + std_id + "`")
                    print("RES not_found")
                    await client.get_channel(701042885931565156).send("RES `not_found`")

                else:
                    api_res_id = Con["std"][std_id][0]["id"]
                    api_res_prefix = Con["std"][std_id][0]["prefix"]
                    api_res_firstname = Con["std"][std_id][0]["firstname"]
                    api_res_lastname = Con["std"][std_id][0]["lastname"]
                    api_res_lastname_forValidate = Con["std"][std_id][0]["lastname"].split()[0]
                    api_res_grade = Con["std"][std_id][0]["grade"]
                    api_res_class = Con["std"][std_id][0]["class"]

                    await message.channel.send("Response: \nชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")
                    print("RES " + str(Con["std"][std_id][0]))
                    await client.get_channel(701042885931565156).send("RES `" + str(Con["std"][std_id][0]) + "`")
            else:
                await message.channel.send("Response: \n`ศิษย์เก่า`")

        if message.content.lower().startswith('/stats'):
            await message.delete()
            
            duplicate_student = 3
            duplicate_teacher = 1

            m1 = len(discord.utils.get(message.author.guild.roles, name="M:1").members)
            m2 = len(discord.utils.get(message.author.guild.roles, name="M:2").members)
            m3 = len(discord.utils.get(message.author.guild.roles, name="M:3").members)
            m4 = len(discord.utils.get(message.author.guild.roles, name="M:4").members)
            m5 = len(discord.utils.get(message.author.guild.roles, name="M:5").members)
            m6 = len(discord.utils.get(message.author.guild.roles, name="M:6").members)
            m11 = len(discord.utils.get(message.author.guild.roles, name="1/1").members)
            m12 = len(discord.utils.get(message.author.guild.roles, name="1/2").members)
            m13 = len(discord.utils.get(message.author.guild.roles, name="1/3").members)
            m14 = len(discord.utils.get(message.author.guild.roles, name="1/4").members)
            m21 = len(discord.utils.get(message.author.guild.roles, name="2/1").members)
            m22 = len(discord.utils.get(message.author.guild.roles, name="2/2").members)
            m23 = len(discord.utils.get(message.author.guild.roles, name="2/3").members)
            m24 = len(discord.utils.get(message.author.guild.roles, name="2/4").members)
            m31 = len(discord.utils.get(message.author.guild.roles, name="3/1").members)
            m32 = len(discord.utils.get(message.author.guild.roles, name="3/2").members)
            m33 = len(discord.utils.get(message.author.guild.roles, name="3/3").members)
            m34 = len(discord.utils.get(message.author.guild.roles, name="3/4").members)
            m41 = len(discord.utils.get(message.author.guild.roles, name="4/1").members)
            m42 = len(discord.utils.get(message.author.guild.roles, name="4/2").members)
            m43 = len(discord.utils.get(message.author.guild.roles, name="4/3").members)
            m44 = len(discord.utils.get(message.author.guild.roles, name="4/4").members)
            m45 = len(discord.utils.get(message.author.guild.roles, name="4/5").members)
            m51 = len(discord.utils.get(message.author.guild.roles, name="5/1").members)
            m52 = len(discord.utils.get(message.author.guild.roles, name="5/2").members)
            m53 = len(discord.utils.get(message.author.guild.roles, name="5/3").members)
            m54 = len(discord.utils.get(message.author.guild.roles, name="5/4").members)
            m55 = len(discord.utils.get(message.author.guild.roles, name="5/5").members)
            m61 = len(discord.utils.get(message.author.guild.roles, name="6/1").members)
            m62 = len(discord.utils.get(message.author.guild.roles, name="6/2").members)
            m63 = len(discord.utils.get(message.author.guild.roles, name="6/3").members)
            m64 = len(discord.utils.get(message.author.guild.roles, name="6/4").members)
            m65 = len(discord.utils.get(message.author.guild.roles, name="6/5").members)
            alum = len(discord.utils.get(message.author.guild.roles, name="ศิษย์เก่า").members)
            student = m1 + m2 + m3 + m4 + m5 + m6
            teacher = len(discord.utils.get(message.author.guild.roles, name="Teacher").members)
            await message.channel.send("[**สถิติ - STATS**]:\n\nม.1 `" + str(m1) + "`คน\n- ม.1/1 `" + str(m11) + "`คน\n- ม.1/2 `" + str(m12) + "`คน\n- ม.1/3 `" + str(m13) + "`คน\n- ม.1/4 `" + str(m14) + "`คน\n\nม.2 `" + str(m2) + "`คน\n- ม.2/1 `" + str(m21) + "`คน\n- ม.2/2 `" + str(m22) + "`คน\n- ม.2/3 `" + str(m33) + "`คน\n- ม.2/4 `" + str(m24) + "`คน\n\nม.3 `" + str(m3) + "`คน\n- ม.3/1 `" + str(m31) + "`คน\n- ม.3/2 `" + str(m32) + "`คน\n- ม.3/3 `" + str(m33) + "`คน\n- ม.3/4 `" + str(m34) + "` คน\n\nม.4 `" + str(m4) + "`คน\n- ม.4/1 `" + str(m41) + "`คน\n- ม.4/2 `" + str(m42) + "`คน\n- ม.4/3 `" + str(m43) + "`คน\n- ม.4/4 `" + str(m44) + "`คน\n- ม.4/5 `" + str(m45) + "`คน\n\nม.5 `" + str(m5) + "`คน\n- ม.5/1 `" + str(m51) + "`คน\n- ม.5/2 `" + str(m52) + "`คน\n- ม.5/3 `" + str(m53) + "`คน\n- ม.5/4 `" + str(m54) + "`คน\n- ม.5/5 `" + str(m55) + "`คน\n\nม.6 `" + str(m6) + "`คน\n- ม.6/1 `" + str(m61) + "`คน\n- ม.6/2 `" + str(m62) + "`คน\n- ม.6/3 `" + str(m63) + "`คน\n- ม.6/4 `" + str(m64) + "`คน\n- ม.6/5 `" + str(m65) + "`คน" + "\nคนรวมนักเรียนทั้งหมด `" + str(student) + "` คน\nศิษย์เก่า `" + str(alum) + "` คน\n\nอาจารย์ทั้งหมด `" + str(teacher) + "` ท่าน\n\nหมายเหตุ:\n - มีนักเรียนที่มีมากกว่า 1 บัญชีทั้งสิ้น `" + str(duplicate_student) + "` คน\n - มีอาจารย์ที่มีมากกว่า 1 บัญชีทั้งสิ้น `" + str(duplicate_teacher) + "` ท่าน")

        if message.content.lower().startswith('/forceverify'):
            text = message.content[len('/forceverify'):].split()
            
            std_id = text[1]

            response = requests.get("https://smd.p0nd.ga/api/student")
            print("GET `https://smd.p0nd.ga/api/student`")
            await client.get_channel(701042885931565156).send("GET `https://smd.p0nd.ga/api/student`")
            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')

            checkId = int(std_id)

            if (checkId > 610000):
                Con = response.json()

                if std_id not in Con["std"]:
                    await message.channel.send('ไม่พบรหัสนักเรียน `' + std_id + "`")
                    print("RES not_found")
                    await client.get_channel(701042885931565156).send("RES `not_found`")

                else:
                    for Mem in message.mentions:                        
                        api_res_id = Con["std"][std_id][0]["id"]
                        api_res_prefix = Con["std"][std_id][0]["prefix"]
                        api_res_firstname = Con["std"][std_id][0]["firstname"]
                        api_res_lastname = Con["std"][std_id][0]["lastname"]
                        api_res_lastname_forValidate = Con["std"][std_id][0]["lastname"].split()[0]
                        api_res_grade = Con["std"][std_id][0]["grade"]
                        api_res_class = Con["std"][std_id][0]["class"]

                        await message.channel.send("ชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")

                        role = discord.utils.get(
                            Mem.guild.roles, name=api_res_grade + "/" + api_res_class)
                        role2 = discord.utils.get(
                            Mem.guild.roles, name="M:" + api_res_grade)
                        role3 = discord.utils.get(
                            Mem.guild.roles, name="Student")
                        # await Mem.add_roles(abc.+)

                        cnx = mysql.connector.connect(user='pondjaco', password='11032545', host='p0nd.ga', database='pondjaco_smdkku')
                        cursor = cnx.cursor()

                        query_func = ("UPDATE `std_2563_discordDB` SET `discord_user_id` = %s WHERE `id` = %s")
                        data_query = (Mem.id, text[1])

                        # Insert new employee
                        cursor.execute(query_func, data_query)
                    
                        # Make sure data is committed to the database
                        cnx.commit()

                        cursor.close()
                        cnx.close()

                        newprefix = ""
                        if (api_res_prefix == "เด็กชาย"):
                            newprefix = "ด.ช."
                        elif (api_res_prefix == "เด็กหญิง"):
                            newprefix = "ด.ญ."
                        elif (api_res_prefix == "นางสาว"):
                            newprefix = "น.ส."
                        else:
                            newprefix = api_res_prefix
                        
                        await Mem.edit(roles=[role, role2, role3])
                        await Mem.edit(nick=newprefix + api_res_firstname + " " + api_res_lastname)
                        await message.channel.send("Status: :white_check_mark:")
                        # await Mem.change_nickname(api_res_prefix + " " + api_res_firstname + " " + api_res_lastname)

                        print("new verify member: " + std_id)
                        await client.get_channel(701042885931565156).send("new verify member: `" + std_id + "`")
                        break
                    
            else:
                for Mem in message.mentions:
                    await message.channel.send("ชื่อ: `" + Mem.display_name + "`\nระดับชั้น: `ศิษย์เก่า`")
                    await message.channel.send("Status: :white_check_mark:")
                    role = discord.utils.get(
                        message.author.guild.roles, name="ศิษย์เก่า")
                    role2 = discord.utils.get(
                        message.author.guild.roles, name="Student")
                    await message.author.edit(roles=[role, role2])
            
            await message.delete()

        if message.content.lower().startswith('/verify'):
            mess_input = message
            user_id = str(message.author.id)
            text = message.content[len('/verify'):].split()
            std_id = text[0]
            std_firstname = text[1]
            std_lastname = text[2]

            response = requests.get("https://smd.p0nd.ga/api/student")
            print("GET `https://smd.p0nd.ga/api/student`")
            await client.get_channel(701042885931565156).send("GET `https://smd.p0nd.ga/api/student`")
            if response.status_code != 200:
                message.channel.send(
                    'ตอนนี้ระบบกำลังมีปัญหา ลองใหม่ในภายหลังนะครับ')

            checkId = int(std_id)

            if (checkId > 610000):

                Con = response.json()

                if std_id not in Con["std"]:
                    await message.channel.send('ไม่พบรหัสนักเรียน `' + std_id + "`")
                    print("RES not_found")
                    await client.get_channel(701042885931565156).send("RES `not_found`")

                else:
                    api_res_id = Con["std"][std_id][0]["id"]
                    api_res_prefix = Con["std"][std_id][0]["prefix"]
                    api_res_firstname = Con["std"][std_id][0]["firstname"]
                    api_res_lastname = Con["std"][std_id][0]["lastname"]
                    api_res_lastname_forValidate = Con["std"][std_id][0]["lastname"].split()[0]
                    api_res_grade = Con["std"][std_id][0]["grade"]
                    api_res_class = Con["std"][std_id][0]["class"]

                    await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + api_res_firstname + "`\nนามสกุล: `" + api_res_lastname + "`\nระดับชั้น: `" + api_res_grade + "/" + api_res_class + "`")

                    # Data Match
                    if (api_res_firstname == std_firstname and api_res_lastname_forValidate == std_lastname):
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

                        newprefix = ""
                        if (api_res_prefix == "เด็กชาย"):
                            newprefix = "ด.ช."
                        elif (api_res_prefix == "เด็กหญิง"):
                            newprefix = "ด.ญ."
                        elif (api_res_prefix == "นางสาว"):
                            newprefix = "น.ส."
                        else:
                            newprefix = api_res_prefix
                        
                        await message.author.edit(roles=[role, role2, role3])
                        await message.author.edit(nick=newprefix + api_res_firstname + " " + api_res_lastname)
                        await message.channel.send("Status: :white_check_mark:")
                        # await message.author.change_nickname(api_res_prefix + " " + api_res_firstname + " " + api_res_lastname)

                        print("new verify member: " + std_id)
                        await client.get_channel(701042885931565156).send("new verify member: `" + std_id + "`")
                    else:
                        await message.channel.send("Status: :x:")
                    print("RES " + str(Con["std"][std_id][0]))
                    await client.get_channel(701042885931565156).send("RES `" + str(Con["std"][std_id][0]) + "`")

            else:
                await message.channel.send("USER: `" + user_id + " (" + message.author.display_name + ")`\nชื่อ: `" + std_firstname + "`\nนามสกุล: `" + std_lastname + "`\nระดับชั้น: `ศิษย์เก่า`")
                await message.channel.send("Status: :white_check_mark:")
                role = discord.utils.get(
                    message.author.guild.roles, name="ศิษย์เก่า")
                role2 = discord.utils.get(
                    message.author.guild.roles, name="Student")
                await message.author.edit(roles=[role, role2])

        if message.content.lower().startswith('/announce'):
            Mes_Str = message.content[len('/announce')+1:]
            channel = client.get_channel(700718680333615154)
            await message.delete()
            await channel.send("@everyone\n"+Mes_Str)

        if message.content.lower().startswith('/update'):
            Mes_Str = message.content[len('/update')+1:]
            channel = client.get_channel(700875375651192832)
            await message.delete()
            await channel.send("@everyone\n"+Mes_Str)

        if message.content.lower().startswith('say('):
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

        if message.content.lower().startswith('/guest'):
            namae = str(message.author.id)
            GUILD = None
            try:
                GUILD = message.channel.guild
            except:
                pass

            await message.channel.send("Minigame By **Nepumi**\n\n:crossed_swords:**โห๋ 1-1 ได้ครับเจ้า"+Getname(self,namae,GUILD)+"**:crossed_swords:\n" + \
                ":1234:วิธีการเล่นคือ ข้าจะ**คิดเลขหนึ่งตัวตั้งแต่ 1 ถึง 100**\nเจ้าต้องทายเลขของค่าให้ถูก**ภายใน 7 ครั้ง**\nสามารถทายโดยการ `? <ตัวเลข>` เช่น `? 12`\n" + \
                ":arrow_down:ถ้าเลขที่เจ้าตอบมัน**ต่ำกว่า** ข้าก็จะบอก**ต่ำไป** \n:arrow_up:แต่ถ้าเลขเจ้ามัน**สูงไป** ข้าก็จะบอก **สูงไป** \n:white_check_mark:แต่ถ้าถูก ข้าจะบอกว่าถูกเอง\n:x:ถ้าเจ้ากลัวที่จะแพ้ข้าก็สามารถออกได้โดยการ `? *` เอา หึๆๆๆ" \
                )

            NEW = {"Time" : 0,"Troll" : randint(0,2) == 0,"TrollSeq" : False,"ANS" : randint(1,100)}
            Guess_Num[namae] = dict(NEW)

        if message.content.lower().startswith('? '):
            namae = str(message.author.id)
            GUILD = None
            try:
                GUILD = message.channel.guild
            except:
                pass

            if namae in Guess_Num:
                Mes_Str = message.content[len('? '):]
                if Mes_Str.startswith('*'):
                    await message.channel.send(":x:เจ้ายอมแพ้สินะ "+Getname(self,namae,GUILD))
                    await message.delete()
                    Guess_Num.pop(namae,None)
                else:
                    LEK = 0
                    try:
                        LEK = int(Mes_Str)
                    except:
                        Guess_Num[namae]["Time"]+= 1
                        if Guess_Num[namae]["Time"] == 7:
                            await message.channel.send(":question:ข้าไม่รู้นะว่าเจ้าส่งอะไรมา("+Mes_Str+") แต่ตอนนี้เจ้าแพ้แล้ว... "+Getname(self,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                            await message.delete()
                            Guess_Num.pop(namae,None)
                        else:
                            await message.channel.send(":question:ข้าไม่รู้นะว่าเจ้าส่งอะไรมา("+Mes_Str+") แต่เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(self,namae,GUILD))
                            await message.delete()
                        return
                    Guess_Num[namae]["Time"]+= 1
                    if LEK > Guess_Num[namae]["ANS"]:
                        if Guess_Num[namae]["Time"] == 7:
                            if Guess_Num[namae]["Troll"] and Guess_Num[namae]["TrollSeq"]:
                                await message.channel.send(":white_check_mark:ข้าล้อเล่นๆๆ จริงๆ"+str(Guess_Num[namae]["ANS"])+"มันถูกละ555 เจ้าชนะนะ "+Getname(self,namae,GUILD))
                                await message.delete()
                            else:
                                await message.channel.send(":x:"+Mes_Str+"น่ะ**มันสูงเกิน**... เจ้าแพ้แล้ว "+Getname(self,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                                await message.delete()
                            Guess_Num.pop(namae,None)
                        else:
                            await message.channel.send(":arrow_up:"+Mes_Str+"น่ะ**มันสูงเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(self,namae,GUILD))
                            await message.delete()
                    elif LEK < Guess_Num[namae]["ANS"]:
                        if Guess_Num[namae]["Time"] == 7:
                            if Guess_Num[namae]["Troll"] and Guess_Num[namae]["TrollSeq"]:
                                await message.channel.send(":white_check_mark:ข้าล้อเล่นๆๆ จริงๆ"+str(Guess_Num[namae]["ANS"])+"มันถูกละ555 เจ้าชนะนะ "+Getname(self,namae,GUILD))
                                await message.delete()
                            else:
                                await message.channel.send(":x:"+Mes_Str+"ของเจ้าน่ะ**มันต่ำเกิน**... เจ้าแพ้แล้ว "+Getname(self,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                                await message.delete()
                            Guess_Num.pop(namae,None)
                        else:
                            await message.channel.send(":arrow_down:"+Mes_Str+"ของเจ้าน่ะ**มันต่ำเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(self,namae,GUILD))
                            await message.delete()
                    elif LEK == Guess_Num[namae]["ANS"]:
                        if Guess_Num[namae]["Troll"]:
                            if Guess_Num[namae]["Time"] == 7:
                                await message.channel.send(":arrow_up:"+Mes_Str+"ของเจ้าน่ะ**มันสูงเกิน**... ข้าล้อเล่น \n:white_check_mark:**"+Mes_Str+"**น่ะถูกแล้วนะ... เจ้า "+Getname(self,namae,GUILD))
                                await message.delete()
                                Guess_Num.pop(namae,None)
                            else:
                                await message.channel.send(":arrow_up:"+Mes_Str+"ของเจ้าน่ะ**มันสูงเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(self,namae,GUILD))
                                await message.delete()
                                Guess_Num[namae]["TrollSeq"] = True
                        else:
                            await message.channel.send(":white_check_mark:ถถถถถูกต้อง ตัวเลขข้าคือ "+Mes_Str+" เก่งไม่เบาเลยนะเจ้า "+Getname(self,namae,GUILD))
                            await message.delete()
                            Guess_Num.pop(namae,None)

        for Mem in message.mentions:
            if self.user.name == Mem.display_name:
                await message.channel.send(randomText_Mention().format(message))
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
