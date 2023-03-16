from gdolib import *;from telebot import types;from telebot import types;from LegendsLIB import *;import DARKI7X,telebot,os,time,random,requests,json,sys,secrets,datetime,threading,pyfiglet;from uuid import uuid4;from user_agent import generate_user_agent;uid = uuid4();idddddd=str(uuid4());from time import sleep;from secrets import token_hex;r = requests.session();from DARKI7X import HITS
from LegendsLIB import *
from VENOMgetREST import *
token = "6075772821:AAFcAwMRLi_0biQn9qfyC6bNDKnjRK390fg"
tok=token
IDDD="5620927843"
bot = telebot.TeleBot(token)
def os_id(id):
	res = False
	fiel = open("ids.txt","r")
	for lien in fiel:
		if lien.strip()==id:
			res =True
	fiel.close()
	return res

@bot.message_handler(commands=['start'])
def send_welcome(message):
	idu = message.from_user.id
	nam = message.from_user.first_name
	bot.send_message(message.chat.id,f"""WELCOM IN BOT GET INFO USER INSTAGRAM 😈🔥
 SEND USER NOW »
 
 اهلا بڪ في بوت جلب معلومات  الانستغرام 😈🔥
 ارسل اليوزر الان »
 
 ○●○●○●○●○●○●○●○●○●
  𝐃𝐄𝐕 ‣ @GG1GQ""",parse_mode="markdown")
	us = message.from_user.username
	f = open("ids.txt","a")
	if (not os_id(str(idu))):
		try:
			co2 = open("idco.txt","r").read()
		except:
			co2 ='1'
			with open('idco.txt', 'w') as x:
				x.write("1")
		with open('idco.txt', 'w') as x:
			if co2 == '':
				 x.write("1")
			else:
				co1 =int(co2)
				co1+=1
				x.write(str(co1))
		f.write(f'{idu}\n')
		f.close()
		ide = '5620927843'
		co3 = open("idco.txt","r").read()
		fg = bot.send_message(ide,f"""===========================
New Subscriber {co3}
His Name ==> {nam}
His User ==> @{us}
His Id ==> {idu}
===========================""")
def abs(message):
 
 first = message.from_user.first_name
 bot.send_message(message.chat.id,f'''===========================
 *مرحبا {first} ❤️  
أهلا بك في بوت معلومات حساب انستكرام من خلال اليوزر يرجى ارسال اليوزر الخاص بك *
===========================''',parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
  Alow = types.InlineKeyboardMarkup()
  username = message.text
  user=username
  url = 'https://b.i.instagram.com/api/v1/accounts/login/'
  headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
  data = {
			'uuid':uid, 
			'password':'@1uaau,@GG1GQ', 
			'username':'{}' .format(username),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
  }
  re = requests.post(url,headers=headers,data=data).text
  if ('"invalid_user"')in re:
  	bot.send_message(message.chat.id,f'''هذا اليوزر {  {user}  } غير موجود في انستگرام  ''',parse_mode="markdown")
  else:
  	us = message.from_user.username
  	tlgg=(f'''تم البحث عن هذا اليوز ==>  {user}
 من قبل ==> @{us}''')
  	tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={IDDD}&text={tlgg}''')
  	i=requests.post(tlg)
  	png = info_IG.profile(username)
  	info = A7X.info(user)
  	name=info["Name"]
  	folwing=info["Followers"]
  	folowers=info["Followors"]
  	ID=info["ID"]
  	privet=info["Privacy"]
  	date=info["Date"]
  	bio=info["Bio"]
  	if name == "":
  		namex="No Name "
  	else:
  		namex=name
  	if bio == "":
  		biox="No Bio "
  	else:
  		biox=bio
  	bot.send_photo(message.chat.id,png,f"""====================
𝐍𝐀𝐌𝐄 ➥ {namex}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ➥ {user}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ➥ {folowers}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ➥ {folwing}
𝐈𝐃 ➥ {ID}
𝐁𝐈𝐎 ➥ {biox}
𝐃𝐀𝐓𝐄 ➥ {date}
𝐏𝐑𝐈𝐕𝐀𝐓𝐄 ➥ {privet}
𝐋𝐈𝐍𝐊 ➥ https://www.instagram.com/{user}
====================
DEV : @GG1GQ""",parse_mode='html',reply_to_message_id=message.message_id, reply_markup=Alow)
bot.polling(True)