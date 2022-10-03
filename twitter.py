import requests as urequests
import random
from bs4 import BeautifulSoup

def otaduck():
    try:
        online = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/duckf.py")
        data = (online.text).splitlines()
        ota = random.choice(data)
        online.close()
        return ota
    except:
        return False

def otacat():
    try:
        online1 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/catf.py")
        data1 = (online1.text).splitlines()
        ota1 = random.choice(data1)
        online1.close()
        return ota1
    except:
        return False

def otadog():
    try:
        online2 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/dogf.py")
        data2 = (online2.text).splitlines()
        ota2 = random.choice(data2)
        online2.close()
        return ota2
    except:
        return False

def otamix():
    try:
        online3 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/cutf.py")
        data3 = (online3.text).splitlines()
        ota3 = random.choice(data3)
        online3.close()
        return ota3
    except:
        return False

def otatubeski():
    try:
        ataf = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/atam.py")
        ataff = (ataf.text).splitlines()
        val1 = random.choice(ataff)
        ataf.close()
        line4 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/ata1.txt")
        data4 = (line4.text).splitlines()
        otaa = random.choice(data4)
        tube = otaa.split(",",1)
        val2 = tube[0]
        val3 = tube[1]
        line4.close()
        return val1,val2,val3
    except:
        return False

def tubeparse(url):
    try:
        r=urequests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        soupp= soup.title.string
        souppp=soupp.split(' - YouTube')
        title = souppp[0]
        return title
    except:
        return False

def otatube():
    try:
        online4 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/list2.txt")
        data4 = (online4.text).splitlines()
        ota4 = random.choice(data4)
        val2 = ota4
        val3 = tubeparse(ota4)
        online4.close()
        return val2,val3
    except:
        return False

def otofunc():
    data = [otaduck,otacat,otadog,otamix]
    data1= random.choice(data)
    oto = data1()
    print(data1.__name__)
    if data1.__name__ == "otaduck":
        tip = "Ördeksever Dostlarım. \U0001F986"
    elif data1.__name__ == "otacat":
        tip = "Kedisever Dostlarım. \U0001F986"
    elif data1.__name__ == "otadog":
        tip = "Köpeksever Dostlarım. \U0001F986"
    elif data1.__name__ == "otamix":
        tip = "Hayvansever Dostlarım. \U0001F986"
    return oto, tip

def hava():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    hvdr = urequests.get(f'https://www.google.com/search?q=ankara+hava+durumu&oq=ankara+hava+&aqs=chrome.0.0i131i433i512j69i57j0i512j0i131i433i512j0i512l2j0i131i433i512l2j0i512j46i175i199i512.3043j1j9&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(hvdr.text, 'html.parser')
    loc = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    wthr = soup.select('#wob_tm')[0].getText().strip()
    return loc,time,info,wthr

def havaa(city):
    city1 = city+"+hava"
    city2 = city1+"+durumu"
    city3 = city2.replace(" ", "+")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = urequests.get(f'https://www.google.com/search?q={city2}&oq={city1}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    loca = soup.select('#wob_loc')[0].getText().strip()
    taym = soup.select('#wob_dts')[0].getText().strip()
    infu = soup.select('#wob_dc')[0].getText().strip()
    hva = soup.select('#wob_tm')[0].getText().strip()
    return loca, taym, infu, hva
