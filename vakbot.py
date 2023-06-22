import tweepy
import twitter
import requests
import os
import telebot
import urllib.parse
import time
import threading
import schedule
import subprocess
import datetime
from collections import defaultdict, deque
from tor import Torrent,TorrentStatus
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
from mastodon import Mastodon


TRANSMISSION_USER = "pi"
TRANSMISSION_PASSWORD = "xxxxxx"
bot = telebot.TeleBot('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') #VolPi4

# API keys 
api_key = "xxxxxxxxxxxxxxxxxxxxx"
api_secrets = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
bearer_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Authenticate to Twitter API V2.0
client = tweepy.Client(
    consumer_key="xxxxxxxxxxxxxxxxxxxxxxxxxx",
    consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxxxx",
    access_token="xxxxxxxxxxxxxxxxxxxxxxxxxx",
    access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxx"
)

# Authenticate to Twitter API V1.1
auth = tweepy.OAuth1UserHandler(api_key,api_secrets,access_token,access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

#mastodon = Mastodon(
#    access_token = 'vakvak_bot.secret',
#    api_base_url = 'https://mastodon.online'
#)

#ta2kvc = Mastodon(
#    access_token = 'ta2kvc.secret',
#    api_base_url = 'https://mastodon.online'
#)


def foto(futu):
    file = 'temp.jpg'
    request = requests.get(futu, stream=True)
    if request.status_code == 200:
        with open(file, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return file


def fotoo(futuu):
    filee = 'logo.jpg'
    request = requests.get(futuu, stream=True)
    if request.status_code == 200:
        with open(filee, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return filee


def selam():
    hour = datetime.datetime.now().hour
    slm = "İyi geceler" if 0<=hour<5 else "Günaydın" if hour<=10 else "İyi günler" if hour<=16 else "İyi akşamlar" if hour<=21 else "İyi geceler"
    return slm

def usertmline():
    volk = api.user_timeline(count=1, tweet_mode="extended")
    for vol in reversed(volk):
        volid = vol.id
        volidstr = vol.id_str
        return volid


@bot.message_handler(commands=['start','help'])
def welcome(message):
    gif = "https://i.ibb.co/cbdwMC7/IMG-20220725-021219.jpg"
    bot.send_photo(message.chat.id, gif)
    vid = "https://github.com/TA2KVC/DuckBot/raw/main/OTA/duckvid.mp4"
    bot.send_video(message.chat.id, vid)


@bot.message_handler(commands=['vak','vakvak'])
@bot.message_handler(regexp="Ördek")
@bot.message_handler(regexp="Vak")
@bot.message_handler(regexp="Vakvak")
def duckbot(message):
    ordeek=twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    tip = "Sevgili Ördeksever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, ordeek, 'Vakvak created by Volkan TA2KVC\nClick /vakvak')
    media = api.media_upload(ordek)
    stat = slm+" "+tip+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(ordek)
    #medyaa = mastodon.media_post(ordek)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['miyav'])
def catbot(message):
    caat=twitter.otacat()
    cat = foto(caat)
    slm = selam()
    tipc = "Sevgili Kedisever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, caat, 'Miiv created by Volkan TA2KVC\nClick /miyav')
    media = api.media_upload(cat)
    stat = slm+" "+tipc+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(cat)
    #medyaa = mastodon.media_post(cat)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['hav'])
def dogbot(message):
    doog=twitter.otadog()
    dog = foto(doog)
    slm = selam()
    tipd = "Sevgili Patisever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, doog, 'Puppy created by Volkan TA2KVC\nClick /hav')
    media = api.media_upload(dog)
    stat = slm+" "+tipd+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(dog)
    #medyaa = mastodon.media_post(dog)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['mix'])
def cutebot(message):
    miix=twitter.otamix()
    mix = foto(miix)
    slm = selam()
    tipx = "Sevgili Hayvansever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, miix, 'Mixx created by Volkan TA2KVC\nClick /mix')
    media = api.media_upload(mix)
    stat = slm+" "+tipx+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(mix)
    #medyaa = mastodon.media_post(mix)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['volkan'])
def volbot(message):
    yt,tt=twitter.otatube()
    vol = 'Volkan TA2KVC YouTube Bot\n'
    vol += tt
    vol += '\n'
    vol += yt
    bot.send_message(message.chat.id, vol)


@bot.message_handler(commands=['istek'])
def istek(message):
    sar = "https://ibb.co/m8ZHsSz"
    bot.send_photo(message.chat.id, sar)


@bot.message_handler(regexp="http://www.youtube.com")
def volbot2(message):
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    tips = "Sevgili Ördeksever Dostlarım. \U0001F986"
    nam = message.chat.first_name
    name = urllib.parse.quote(nam)
    link = message.text
    title = twitter.tubeparse(link)
    tit = urllib.parse.quote(title)
    voli = 'Sevgili ' + nam + '; \n'
    voli += 'istek parcan: \n' + title + ' \n'
    voli += 'birazdan twitlenecek..!'
    bot.send_message(message.chat.id, voli)
    media = api.media_upload(ordek)
    stat = slm+" "+tips+"\n\n"+nam+" 'ın dinlemek istediği şarkı: \n"+title+"\n"+link+"\n\n\U0001F986\U0001F916 @VakvakBot"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(ordek)
    #medyaa = mastodon.media_post(ordek)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


def botlisten():
    bot.infinity_polling(interval=0, timeout=20)


def auto():
    oto,tipo=twitter.otofunc()
    slm = selam()
    yt,tt=twitter.otatube()
    foti = foto(oto)
    media = api.media_upload(foti)
    stat = slm+" \U0001F986\n\""+tt+"\"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    #api.update_status(status=stat, media_ids=[media.media_id])
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(foti)
    #medyaa = mastodon.media_post(foti)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


def sabah():
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    yt,tt=twitter.otatube()
    media = api.media_upload(ordek)
    stat = slm+" \U0001F986\n\""+tt+"\"\n"+yt+"\n\U0001F986"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    #medya = ta2kvc.media_post(ordek)
    #medyaa = mastodon.media_post(ordek)
    #ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['oto'])
def oto(message):
    auto()
    bot.send_message(message.chat.id, "Otomatik tweet gonderildi.")


@bot.message_handler(commands=['torekle'])
def tor_ekle(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Eksik torrent URL. Kullanim: /torekle [URL]")
        return
    url = args[1]
    response = torrent_add(url)
    if "success" in response:
        bot.send_message(message.chat.id, "Torrent eklendi.")
    else:
        bot.reply_to(message, response)


@bot.message_handler(commands=['torlist'])
def tor_liste(message):
    try:
        torrents = torrent_list()
        torrents_by_type = defaultdict(list)
        for torrent in torrents:
            torrents_by_type[torrent.status].append(torrent)
        response = ""
        for key in torrents_by_type.keys():
            response += "*%s*\n" % TorrentStatus.conversion_to_string[key]
            for t in torrents_by_type[key]:
                response += t.format_telegram() + "\n"
        bot.send_message(message.chat.id, response, parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, "Torrent listesi bos.")


@bot.message_handler(commands=['torinfo'])
def tor_infoo(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Eksik torrent ID. Kullanim: /torinfo [ID]")
        return
    torrent_id = args[1]
    bot.send_message(message.chat.id, torrent_info(torrent_id))


@bot.message_handler(commands=['torstart'])
def torstart(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Eksik torrent ID. Kullanim: /torstart [ID]")
        return
    torrent_id = args[1]
    respon = torrent_start(torrent_id)
    if "success" in respon:
        stt = "Torrent ID["
        stt += torrent_id
        stt += "] devam ettirildi."
        bot.send_message(message.chat.id, stt)
    else:
        bot.reply_to(message, response)


@bot.message_handler(commands=['torstop'])
def torstop(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Eksik torrent ID. Kullanim: /torstop [ID]")
        return
    torrent_id = args[1]
    resp = torrent_stop(torrent_id)
    if "success" in resp:
        sto = "Torrent ID["
        sto += torrent_id
        sto += "] durduruldu."
        bot.send_message(message.chat.id, sto)
    else:
        bot.reply_to(message, response)


@bot.message_handler(commands=['torsil'])
def tor_sil(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Eksik torrent ID. Kullanim: /torsil [ID]")
        return
    torrent_id = args[1]
    sil = torrent_remove(torrent_id)
    if "success" in sil:
        ssil = "Torrent ID["
        ssil += torrent_id
        ssil += "] silindi."
        bot.send_message(message.chat.id, ssil)
    else:
        bot.reply_to(message, response)


def system_call_with_response(command):
    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE) as task:
        output = task.stdout.read()
        task.wait()
        return output.decode("utf-8").strip()


def torrent_add(url):
    command = "transmission-remote -n %s:%s -a '%s'" % (TRANSMISSION_USER, TRANSMISSION_PASSWORD, url)
    response = system_call_with_response(command)
    return response


def torrent_remove(torrent_id):
    command = "transmission-remote -n %s:%s -t %d --remove-and-delete" % \
              (TRANSMISSION_USER, TRANSMISSION_PASSWORD, int(torrent_id))
    response = system_call_with_response(command)
    return response


def torrent_list():
    command = "transmission-remote -n %s:%s -l" % (TRANSMISSION_USER, TRANSMISSION_PASSWORD)
    response = system_call_with_response(command)
    lines = response.split("\n")[1:-1]
    torrents = []
    for x in lines:
        words = [w.strip() for w in x.split("  ") if w]
        torrents.append(Torrent(*words))
    return torrents


def torrent_info(torrent_id):
    command = "transmission-remote -n %s:%s -t %d -i" % \
              (TRANSMISSION_USER, TRANSMISSION_PASSWORD, int(torrent_id))
    response = system_call_with_response(command)
    return response


def torrent_start(torrent_id):
    command = "transmission-remote -n %s:%s -t %d -s" % \
              (TRANSMISSION_USER, TRANSMISSION_PASSWORD, int(torrent_id))
    response = system_call_with_response(command)
    return response


def torrent_stop(torrent_id):
    command = "transmission-remote -n %s:%s -t %d -S" % \
              (TRANSMISSION_USER, TRANSMISSION_PASSWORD, int(torrent_id))
    response = system_call_with_response(command)
    return response


def modell() -> str:
    with open('/proc/device-tree/model') as f:
        model = f.read()
    return model


def rell():
    os_file ='/etc/os-release'
    rel = system_call_with_response(("cat "+os_file+" | grep 'PRETTY_NAME'")).replace("PRETTY_NAME=", "").replace('''"''', "")
    return rel


def cpp():
    cp = system_call_with_response("vcgencmd measure_temp")
    cpu = cp.replace("temp=","").replace("'C","")
    return cpu


def verr():
    ver = system_call_with_response("uname -s -r ")
    return ver


def hostt():
    host = system_call_with_response("uname -n")
    return host


def uptaym():
    #uphh = system_call_with_response("uptime -p | awk -F'( |,|:)+' '{print $6}'")
    upu = system_call_with_response("uptime -p")
    updd = upu.replace("up ","").replace("weeks","hafta").replace("week","hafta").replace("days","gün").replace("day","gün").replace("hours","saat").replace("hour","saat").replace("minutes","dakika")
    return updd


def datey():
    cmnd = "date "+"\"+%d.%m.%Y  %H:%M\""
    deyt = system_call_with_response(cmnd)
    return deyt


def ram():
    tram = system_call_with_response("free -m | awk 'FNR == 2 {print $2}'")
    uram = system_call_with_response("free -m | awk 'FNR == 2 {print $3}'")
    return tram, uram


def botstop():
    botstop = system_call_with_response("sudo systemctl stop vakbot")
    return botstop


def vakbotstatus():
    botstatus = system_call_with_response("systemctl status vakbot")
    return botstatus


@bot.message_handler(commands=['botstop'])
def botstp(message):
    bot.send_message(message.chat.id, "VolPi4 bot durduruldu.")
    botstop()


@bot.message_handler(commands=['botstatus'])
def botstatus(message):
    status = vakbotstatus()
    bot.send_message(message.chat.id, status)


@bot.message_handler(commands=['pi'])
def rpiauto(message):
    rpi()
    hoste = hostt()
    bot.send_message(message.chat.id, "Raspberry Pi " +hoste+ " bilgileri twitlenecek...")


def rpi():
    hots = hostt()
    modle= modell()
    rele = rell()
    vere = verr()
    cpuu = cpp()
    updd = uptaym()
    date = datey()
    tram, uram = ram()
    rp = "Model : " +modle+ " \n"
    rp += "OS : " +rele+ "\n"
    rp += "Ver. : " +vere+ "\n"
    rp += "CPU : BCM2711 @ 1.5GHz \n"
    rp += "Temp : " +cpuu+ " °C \n"
    rp += "Uptime : " +updd+ "\n"
    rp += "RAM : " +uram+ " / " +tram+ " MB \n"
    #rp += date
    link = "https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/pi4.py"
    val = twitter.parser(link)
    rpi = foto(val)
    pim = "Merhaba ben "+hots+"; \n"
    pim += "VakvakBot\U00002122'u çalıştıran SoC :) \n"
    media = api.media_upload(rpi)
    stat = pim+"\n"+rp+"\n\U0001F986\U0001F916 @VakvakBot\U00002122"
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['ata'])
def atato(message):
    ata()
    bot.send_message(message.chat.id, "Mustafa Kemal ATATÜRK...")


def ata():
    ata1,ata2,ata3 = twitter.otatubeski()
    atam = "Ebedi Başkomutan, Ölümsüz Türk... \n"
    atamm = "\" " +ata3+ " \""
    atamm += "\n\n"
    atamm += ata2
    ataa1 = foto(ata1)
    stat = atam+"\n"+atamm+"\n"
    media = api.media_upload(ataa1)
    #api.update_status(status=stat, media_ids=[media.media_id])
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['havaa'])
def havauto(message):
    accuhava()
    bot.send_message(message.chat.id, "Hava durumu bilgileri tweetlenecek...")

def accuhava():
    info,scak,nem,rzghz,rzgyn = twitter.accu()
    otoo,tipo=twitter.otofunc()
    slm = selam()
    oto = foto(otoo)
    hvd = slm +" "
    hvd += "Sevgili " + tipo + "\n"
    hvdu = "Başkentimiz Ankara'nın hava durumu: \n"
    hvdu += "Gökyüzü : " +info + "\n"
    hvdu += "Sıcaklık : " +scak + " °C\n"
    hvdu += "Nem : %" +nem + "\n"
    hvdu += "Rüzgar : " +rzghz+ " km/s hızla " +rzgyn+ " yönünde\n"
    media = api.media_upload(oto)
    stat = hvd+"\n"+hvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    #api.update_status(status=stat, media_ids=[media.media_id])
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['hava'])
@bot.message_handler(regexp="Hava")
@bot.message_handler(regexp="hava")
def havadurumu(message):
    nam = message.chat.first_name
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Hatalı işlem yaptınız.. Kullanımı: hava sehirismi")
        return
    citya = args[1]
    city = citya.title()
    info,scak,nem,rzghz,rzgyn = twitter.accukod(city)
    hvvi = 'Sevgili ' + nam + '; \n'
    hvvi += "" +city + ' şehrinin hava durumu bilgisi \n'
    hvvi += 'birazdan twitlenecek..!'
    bot.send_message(message.chat.id, hvvi)
    otoo,tipo=twitter.otofunc()
    oto = foto(otoo)
    slm = selam()
    hvvd = slm
    hvvd += " Sevgili " + nam +"; \n"
    hvvdu = "Hava durumunu öğrenmek istediğin " +city+ " şehrinin bilgileri: \n"
    hvvdu += "Gökyüzü : " +info + "\n"
    hvvdu += "Sıcaklık : " +scak + " °C\n"
    hvvdu += "Nem : %" +nem + "\n"
    hvvdu += "Rüzgar : " +rzghz+ " km/s hızla " +rzgyn+ " yönünde\n"
    media = api.media_upload(oto)
    stat = hvvd+"\n"+hvvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    bot.reply_to(message, hvvdu)


@bot.message_handler(commands=['piyasa'])
def piyssa(message):
    piysa()
    bot.send_message(message.chat.id, "Piyasa bilgileri birazdan tweetlenecek...")


def piysa():
    #volk = usertmline()
    usa,uss,eua,eus,aua,aus,aga,ags = twitter.piyasa()
    borsa = twitter.borsa()
    tarh = datey()
    ordeek=twitter.otaduck()
    ordek = foto(ordeek)
    #slm = selam()
    #pys = slm +" Sevgili Ördeksever Dostlarım. \U0001F986\n"
    pyss = "Piyasalar: \n"
    pyss += "\U0001F986 Amerikan Ördeği :  " +usa+ "  -  " +uss+ "\n"
    pyss += "\U0001F986 Avrupa Ördeği :  " +eua + "  -  " +eus+ "\n"
    pyss += "\U0001F986 Altın Ördek :  " +aua + "  -  " +aus+ "\n"
    pyss += "\U0001F986 Gümüş Ördek :  " +aga + "  -  " +ags+ "\n"
    pyss += "\U0001F986 B-Ördek100 :  " +borsa+ "\n\n"
    pyss += tarh
    media = api.media_upload(ordek)
    stat = pyss+"\n\U0001F986\U0001F916 @VakvakBot\U00002122"
    #api.update_status(status=stat, media_ids=[media.media_id])
    #api.update_status(status=stat, in_reply_to_status_id=volk, auto_populate_reply_metadata=True, media_ids=[media.media_id])
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['kur'])
def piyssa(message):
    usa,uss,eua,eus,aua,aus,aga,ags = twitter.piyasa()
    borsa = twitter.borsa()
    tarh = datey()
    pyss = "Ördek piyasasında son durum: \n\n"
    pyss += "Amerikan Ördeği :  " +usa+ "  -  " +uss+ "\n"
    pyss += "Avrupa Ördeği :  " +eua + "  -  " +eus+ "\n"
    pyss += "Altın Ördek :  " +aua + "  -  " +aus+ "\n"
    pyss += "Gümüş Ördek :  " +aga + "  -  " +ags+ "\n"
    pyss += "B-Ördek100 :  " +borsa+ "\n\n"
    pyss += "Tarih : " +tarh+ "\n"
    bot.send_message(message.chat.id, pyss)


def create_gif(wh, text):
    fnt = ImageFont.truetype('Mont.otf', 50)
    bg = Image.open('bckgrnd.jpg')
    lgo = Image.open('logo.jpg')
    width, height = wh
    mask = Image.new("L", lgo.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 395, 385), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(3))
    mask.save('mask.jpg', quality=95)
    bg.paste(lgo, (350, 30), mask)
    draw = ImageDraw.Draw(bg)
    draw.text((width, height), text, font = fnt, fill="white")
    return bg


def get_last_tweet(file):
    f = open(file, 'r')
    lastId = f.read().strip()
    f.close()
    return lastId


def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(Id)
    f.close()
    return


def tail(filename):
    with open(filename) as f:
        usid = deque(f,5)
        usrid = str(usid)
        return usrid


def saveid(filename,id):
    with open(filename, 'a') as f:
        data = f"{id}\n"
        f.writelines(data)
        f.close()


def nwuser():
    mentions = api.mentions_timeline(count=1, tweet_mode="extended")
    for mention in reversed(mentions):
        new_user = mention.user.id_str
    return new_user


def search_exception():
    dosya = 'istisna.txt'
    with open(dosya, 'r') as file:
        content = file.read()
        return content

def respondToTweet(id_file='id.txt',user_file='userid.txt'):
    last_id = get_last_tweet(id_file)
    last_user = tail(user_file)
    exceptionlist = search_exception()
    mentions = api.mentions_timeline(count=1, tweet_mode="extended")
    if len(mentions) == 0:
        return

    new_id = 0
    new_user = 0
    for mention in reversed(mentions):
        new_id = mention.id_str
        new_user = mention.user.id_str
        if new_user in exceptionlist:
            return
        elif 'vakoff' in mention.full_text.lower():
            istisnafto = 'https://i.ibb.co/cFLwTM7/jiffka-tbrender027.jpg'
            istisnaft = foto(istisnafto)
            media = api.media_upload(istisnaft)
            helloo = selam()
            stat = "@" + mention.user.screen_name + " " + helloo + " " +  mention.user.name + ", \n\"Vakvak™\" sizi istisna listesine ekledi. Artık otomatik yanıt almayacaksınız. \U0001F986 \n\n@VakvakBot"
            api.update_status(status=stat, in_reply_to_status_id=mention.id, media_ids=[media.media_id])
            api.create_favorite(mention.id)
            saveid('istisna.txt',new_user)
            return
        elif new_user in last_user:
            return
        else:
            pass
        user = mention.user.screen_name
        twname = mention.user.name
        logoo = mention.user.profile_image_url
        logo = logoo.replace("_normal","")
        fotoo(logo)
        try:
#            filename = "temp.jpg"
#            with Image.open(filename) as img:
#                img.load()
#            blur_img = img.filter(ImageFilter.BLUR)
#            blur_img.save('blbg.jpg')
            bg = Image.open('bckgrnd.jpg')
            lgo = Image.open('logo.jpg')
            mask = Image.new("L", lgo.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 395, 385), fill=255)
            mask = mask.filter(ImageFilter.GaussianBlur(3))
            mask.save('mask.jpg', quality=95)
            bg.paste(lgo,(350,30), mask)
            d1 = ImageDraw.Draw(bg)
            myFont = ImageFont.truetype('Mont.otf', 50)
            d1.text((80, 500), "Teşekkürler Ördeksever\n"+user+" !", font=myFont, fill =(255, 255, 255))
            bg.save('tw.jpg')
            twfot= 'tw.jpg'
#            frames = []
#            string = "Teşekkürler Ördeksever: \n\n"+user+" !            "
#            for i in range(len(string)):
#                new_frame = create_gif((50,500), string[:i])
#                frames.append(new_frame)
#            frames[0].save('ment.gif', format='GIF',append_images=frames[1:], save_all=True, duration=100, loop=0)
#            time.sleep(3)
#            twfot= 'ment.gif'
            media = api.media_upload(twfot)
            hello = selam()
            stat = "@" + user + " " + hello + " " + twname + ", \nTweetin \"Vakvak™\" tarafından otomatik yanıtlanmıştır. \nYoruma \'vakOFF\' yazarak otomatik yanıtları kapatabilirsin. \n\n@VakvakBot  \U0001F986\U0001F916"
            api.update_status(status=stat, in_reply_to_status_id=mention.id, media_ids=[media.media_id])
            api.create_favorite(mention.id)
        except:
            print("Already replied to {}".format(mention.id))
#            print(mentions)

    put_last_tweet(id_file, new_id)
    saveid('userid.txt',new_user)
    time.sleep(60)


def isimi():
    #volk = usertmline()
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    #slm = selam()
    ff = twitter.kizisimci()
    mm = twitter.erkisimci()
    #hvd = slm + " Sevgili Ördeksever Dostlarım. \U0001F986 \n"
    hvdu = "Bugün yumurtadan çıkan ördekler için isim önerileri: \n\n"
    hvdu += "Kız Ördek: " +ff+ "\n"
    hvdu += "Erkek Ördek : " +mm+ "\n"
    media = api.media_upload(ordek)
    stat = hvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    #api.update_status(status=stat, media_ids=[media.media_id])
    #api.update_status(status=stat, in_reply_to_status_id=volk, auto_populate_reply_metadata=True, media_ids=[media.media_id])
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['isim'])
def isimlik(message):
    isimi()
    bot.send_message(message.chat.id, "isimler birazdan tweetlenecek...")


@bot.message_handler(commands=['isimci'])
def isimci(message):
    args = message.text.split()
    if len(args) < 3:
        bot.reply_to(message, "Hata! Kullanım: /isimci [kız ismi] [erkek ismi]")
        return
    kiz = args[1]
    ff = kiz.title()
    erkek = args[2]
    mm = erkek.title()
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    nam = "Bugün yumurtadan çıkan ördekler için isim önerileri: \n\n"
    nam += "Kız Ördek: " +ff+ "\n"
    nam += "Erkek Ördek : " +mm+ "\n"
    media = api.media_upload(ordek)
    stat = nam+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    client.create_tweet(text=stat, media_ids=[media.media_id])
    bot.send_message(message.chat.id, "isimler birazdan twitlenecek...")


@bot.message_handler(commands=['places'])
def placeoto(message):
    places()
    bot.send_message(message.chat.id, "Manzaralar twitleniyor...")


def places():
    #volk = usertmline()
    plink,pdat = twitter.place()
    #slm = selam()
    #pll = slm + " Sevgili Ördeksever Dostlarım. \U0001F986 \n"
    plll = "Dünya Ördeklerinin yaşadığı en güzel yerler: \n\n"
    plll+= "\" " +pdat+ " \"\n"
    flink = foto(plink)
    stat = plll + "\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    media = api.media_upload(flink)
    client.create_tweet(text=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['yemek'])
def pisiroto(message):
    pisir()
    bot.send_message(message.chat.id, "Yemekler twitleniyor...")


def pisir():
    crb=twitter.corba()
    ymk=twitter.yemek()
    ymk2=twitter.yemek()
    slt=twitter.salata()
    ick=twitter.icki()
    tat=twitter.tatli()
    ymkft="https://i.ibb.co/tm4Cs7H/yemek2.gif"
    neymk = "\U0001F986 \U0001F372  Akşam Ne Pişireceğiz?  \U0001F372 \U0001F986\n\n"
    neymk += "\U0001F963 " +crb + "\n"
    neymk += "\U0001F372 " +ymk + " veya " +ymk2 + "\n"
    neymk += "\U0001F957 " +slt + "\n"
    neymk += "\U0001F36E " +tat + "\n"
    neymk += "\U0001F379 " +ick + "\n\n"
    ymfot = foto(ymkft)
    stat = neymk + "\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    media = api.media_upload(ymfot)
    client.create_tweet(text=stat, media_ids=[media.media_id])


t1=threading.Thread(target=botlisten)
#schedule.every(180).minutes.do(auto)
schedule.every().day.at("19:38").do(ata)
#schedule.every().day.at("20:00").do(rpi)
schedule.every().day.at("09:32").do(places)
schedule.every().day.at("09:33").do(isimi)
schedule.every().day.at("09:31").do(piysa)
schedule.every().day.at("09:30").do(accuhava)
schedule.every().day.at("12:00").do(pisir)
#schedule.every(4).hours.do(hvdrm)
t1.start()


while True:
    schedule.run_pending()
    #respondToTweet()
    time.sleep(30)

