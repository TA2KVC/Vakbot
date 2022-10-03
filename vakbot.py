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
from collections import defaultdict
from tor import Torrent,TorrentStatus

TRANSMISSION_USER = "pi"
TRANSMISSION_PASSWORD = "volkan"
bot = telebot.TeleBot('xxxxxxxxxxxxxxxxxxxxxxxxx') #VolPi4

# API keyws that yous saved earlier
api_key = "xxxxxxxxxxxxxxxxxxx"
api_secrets = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

def foto(futu):
    file = 'temp.jpg'
    request = requests.get(futu, stream=True)
    if request.status_code == 200:
        with open(file, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return file

def selam():
    hour = datetime.datetime.now().hour
    slm = "İyi geceler" if 0<=hour<5 else "Günaydın" if hour<=10 else "İyi günler" if hour<=16 else "İyi akşamlar" if hour<=21 else "İyi geceler"
    return slm

@bot.message_handler(commands=['start','help'])
def welcome(message):
    gif = "https://ibb.co/hXvchZt"
    bot.send_photo(message.chat.id, gif)
    vid = "https://user-images.githubusercontent.com/62475996/180663340-4099a88c-d84e-437c-a984-2f6908380520.mp4"
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
    stat = slm+" "+tip+"\n\n"+tt+"\n"+yt+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['miyav'])
def catbot(message):
    caat=twitter.otacat()
    cat = foto(caat)
    slm = selam()
    tipc = "Sevgili Kedisever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, caat, 'Miiv created by Volkan TA2KVC\nClick /miyav')
    media = api.media_upload(cat)
    stat = slm+" "+tipc+"\n\n"+tt+"\n"+yt+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['hav'])
def dogbot(message):
    doog=twitter.otadog()
    dog = foto(doog)
    slm = selam()
    tipd = "Sevgili Köpeksever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, doog, 'Puppy created by Volkan TA2KVC\nClick /hav')
    media = api.media_upload(dog)
    stat = slm+" "+tipd+"\n\n"+tt+"\n"+yt+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


@bot.message_handler(commands=['mix'])
def cutebot(message):
    miix=twitter.otamix()
    mix = foto(miix)
    slm = selam()
    tipx = "Sevgili Hayvansever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, miix, 'Mixx created by Volkan TA2KVC\nClick /mix')
    media = api.media_upload(mix)
    stat = slm+" "+tipx+"\n\n"+tt+"\n"+yt+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


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
    stat = slm+" "+tips+"\n\n"+nam+" 'ın dinlemek istediği şarkı: \n"+title+"\n"+link+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


def botlisten():
    bot.infinity_polling(interval=0, timeout=20)

def auto():
    oto,tipo=twitter.otofunc()
    slm = selam()
    yt,tt=twitter.otatube()
    foti = foto(oto)
    media = api.media_upload(foti)
    stat = slm+" \U0001F986\n\""+tt+"\"\n"+yt+"\n\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])

def sabah():
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    yt,tt=twitter.otatube()
    media = api.media_upload(ordek)
    stat = slm+" \U0001F986\n\""+tt+"\"\n"+yt+"\n\U0001F986"
    api.update_status(status=stat, media_ids=[media.media_id])


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
    updd = system_call_with_response("uptime | awk -F'( |,|:)+' '{print $6}'")
    #upu = system_call_with_response("uptime -p | awk -F 'up ' '{print $2}'")
    uphh = system_call_with_response("uptime -p | awk -F'( |,|:)+' '{print $6}'")
    return updd,uphh

def datey():
    cmnd = "date "+"\"+%H:%M %d.%m.%Y\""
    deyt = system_call_with_response(cmnd)
    return deyt

def ram():
    tram = system_call_with_response("free -m | awk 'FNR == 2 {print $2}'")
    uram = system_call_with_response("free -m | awk 'FNR == 2 {print $3}'")
    return tram, uram

def botstop():
    botstop = system_call_with_response("sudo systemctl stop vakbot")
    return botstop

@bot.message_handler(commands=['botstop'])
def botstp(message):
    bot.send_message(message.chat.id, "VolPi4 bot durduruldu.")
    botstop()

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
    host = hostt()
    updd, uphh = uptaym()
    date = datey()
    tram, uram = ram()
    rp = "Model : " +modle+ " \n"
    rp += "OS : " +rele+ "\n"
    rp += "Sürüm : " +vere+ "\n"
    rp += "CPU : BCM2711 @ 1.500GHz @ " +cpuu+ " °C \n"
    rp += "Uptime : " +updd+ " gün, "+uphh+" saat \n"
    rp += "RAM : " +uram+ " / " +tram+ " MB \n"
    #rp += date
    #val = "https://i.ibb.co/tCsYynC/thibault-valsin-render-raspberry-pi4-v2-2.jpg"
    val = "https://i.ibb.co/c8GYS4Q/New-8-GB-Raspberry-Pi-pivietnam-com-vn.png"
    rpi = foto(val)
    pim = "Merhaba ben "+hots+"; \n"
    pim += "Vakvak'ı çalıştıran bilgisayar :) \n"
    media = api.media_upload(rpi)
    stat = pim+"\n"+rp+"\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])

@bot.message_handler(commands=['ata'])
def atato(message):
    ata()

def ata():
    ata1,ata2,ata3 = twitter.otatubeski()
    atam = "Ebedi Başkomutan, Ölümsüz Türk... \n"
    atamm = "\" " +ata3+ " \""
    atamm += "\n\n"
    atamm += ata2
    ataa1 = foto(ata1)
    stat = atam+"\n"+atamm+"\n"
    media = api.media_upload(ataa1)
    api.update_status(status=stat, media_ids=[media.media_id])

@bot.message_handler(commands=['havaa'])
def havauto(message):
    hvdrm()
    bot.send_message(message.chat.id, "Hava durumu bilgileri tweetlenecek...")

def hvdrm():
    loc,time,info,wthr = twitter.hava()
    otoo,tipo=twitter.otofunc()
    slm = selam()
    oto = foto(otoo)
    hvd = slm +" "
    hvd += "Sevgili " + tipo + "\n"
    hvdu = "Başkentimiz " +loc+ "'nın hava durumu: \n"
    hvdu += "Şehir: " +loc + "\n"
    hvdu += "Tarih : " +time + "\n"
    hvdu += "Gökyüzü : " +info + "\n"
    hvdu += "Sıcaklık : " +wthr + " °C\n"
    media = api.media_upload(oto)
    stat = hvd+"\n"+hvdu+"\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])


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
    loc,time,info,wthr = twitter.havaa(city)
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
    hvvdu += "Şehir: " +loc + "\n"
    hvvdu += "Tarih : " +time + "\n"
    hvvdu += "Gökyüzü : " +info + "\n"
    hvvdu += "Sıcaklık : " +wthr + " °C\n"
    bot.reply_to(message, hvvdu)
    media = api.media_upload(oto)
    stat = hvvd+"\n"+hvvdu+"\n\U0001f4f2 t.me/VakVakVakBot"
    api.update_status(status=stat, media_ids=[media.media_id])

#id_file='id.txt'
#user_file='userid.txt'

def get_last_tweet(file):
    f = open(file, 'r')
    lastId = f.read().strip()
    f.close()
    return lastId

def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(Id)
#    f.write(str(Id))
    f.close()
    return

def respondToTweet(id_file='id.txt',user_file='userid.txt'):
#    id_file='id.txt'
#    user_file='userid.txt'
    last_id = get_last_tweet(id_file)
    last_user = get_last_tweet(user_file)
    mentions = api.mentions_timeline(count=1, tweet_mode="extended")
    if len(mentions) == 0:
        return

    new_id = 0
    new_user = 0
    for mention in reversed(mentions):
        new_id = mention.id_str
        new_user = mention.user.id_str
        if new_user == last_user:
            return

        user = mention.user.screen_name
        twname = mention.user.name
#        print(str(mention.id) + ' - ' + mention.full_text + ' - ' + mention.user.screen_name)
        try:
#            ordeek = "https://i.ibb.co/Q8Q3d4m/IMG-20221001-221746.jpg"
#            ordek = foto(ordeek)
#            media = api.media_upload(ordek)
            stat = "@" + user + " Merhaba "+twname+", \nTweetiniz \' Vakvak™ \' tarafından otomatik yanıtlanıp, beğenilmiştir... \U0001F986"
            api.update_status(status=stat, in_reply_to_status_id=mention.id)
            api.create_favorite(mention.id)
        except:
            print("Already replied to {}".format(mention.id))
#            print(mentions)

    put_last_tweet(id_file, new_id)
    put_last_tweet(user_file, new_user)
    time.sleep(15)

t1=threading.Thread(target=botlisten)
#schedule.every(180).minutes.do(auto)
schedule.every().day.at("19:38").do(ata)
schedule.every().day.at("20:00").do(rpi)
schedule.every().day.at("08:30").do(sabah)
schedule.every().day.at("09:00").do(hvdrm)
#schedule.every(4).hours.do(hvdrm)
t1.start()


while True:
    schedule.run_pending()
    respondToTweet()
    time.sleep(1)
