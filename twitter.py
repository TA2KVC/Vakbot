import requests
import random
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import xmltodict

def otaduck():
    try:
        online = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/duckf.py")
        data = (online.text).splitlines()
        ota = random.choice(data)
        online.close()
        return ota
    except:
        return False

def otacat():
    try:
        online1 = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/catf.py")
        data1 = (online1.text).splitlines()
        ota1 = random.choice(data1)
        online1.close()
        return ota1
    except:
        return False

def otadog():
    try:
        online2 = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/dogf.py")
        data2 = (online2.text).splitlines()
        ota2 = random.choice(data2)
        online2.close()
        return ota2
    except:
        return False

def otamix():
    try:
        online3 = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/cutf.py")
        data3 = (online3.text).splitlines()
        ota3 = random.choice(data3)
        online3.close()
        return ota3
    except:
        return False

def parser(link):
    try:
        onlinex = requests.get(link)
        datax = (onlinex.text).splitlines()
        otax = random.choice(datax)
        onlinex.close()
        return otax
    except:
        return False

def otatubeski():
    try:
        ataf = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/atam.py")
        ataff = (ataf.text).splitlines()
        val1 = random.choice(ataff)
        ataf.close()
        line4 = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/ata1.txt")
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
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        soupp= soup.title.string
        souppp=soupp.split(' - YouTube')
        title = souppp[0]
        return title
    except:
        return False

def otatube():
    try:
        online4 = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/list2.txt")
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
        tip = "Patisever Dostlarım. \U0001F986"
    elif data1.__name__ == "otamix":
        tip = "Hayvansever Dostlarım. \U0001F986"
    return oto, tip


def accu():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/316938?apikey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&language=tr-tr&details=true', headers=headers)
    data = response.json()[0]
    info = data['WeatherText']
    scak = str(data['Temperature']['Metric']['Value'])
    nem = str(data['RelativeHumidity'])
    rzghz = str(data['Wind']['Speed']['Metric']['Value'])
    rzgyn = data['Wind']['Direction']['Localized']
    if rzgyn == "K":
        ruz = "Kuzey"
    elif rzgyn == "G":
        ruz = "Güney"
    elif rzgyn == "D":
        ruz = "Doğu"
    elif rzgyn == "B":
        ruz = "Batı"
    elif rzgyn == "KB":
        ruz = "Kuzey Batı"
    elif rzgyn == "KD":
        ruz = "Kuzey Doğu"
    elif rzgyn == "GB":
        ruz = "Güney Batı"
    elif rzgyn == "GD":
        ruz = "Güney Doğu"
    elif rzgyn == "KKB":
        ruz = "Kuzey, Kuzey Batı"
    elif rzgyn == "KKD":
        ruz = "Kuzey, Kuzey Doğu"
    elif rzgyn == "GGB":
        ruz = "Güney, Güney Batı"
    elif rzgyn == "GGD":
        ruz = "Güney, Güney Doğu"
    elif rzgyn == "DKD":
        ruz = "Doğu, Kuzey Doğu"
    elif rzgyn == "BKB":
        ruz = "Batı, Kuzey Batı"
    elif rzgyn == "BGB":
        ruz = "Batı, Güney Batı"
    elif rzgyn == "DGD":
        ruz = "Doğu, Güney Doğu"
    #weather_icon = data['WeatherIcon']
    return info,scak,nem,rzghz,ruz


def accukod(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    kod = requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=xxxxxxxxxxxxxxxxxxxxxxxxx&q={city}&language=tr-tr', headers=headers)
    koda = kod.json()[0]
    key = koda['Key']
    response = requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{key}?apikey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx&language=tr-tr&details=true', headers=headers)
    data = response.json()[0]
    info = data['WeatherText']
    scak = str(data['Temperature']['Metric']['Value'])
    nem = str(data['RelativeHumidity'])
    rzghz = str(data['Wind']['Speed']['Metric']['Value'])
    rzgyn = data['Wind']['Direction']['Localized']
    if rzgyn == "K":
        ruz = "Kuzey"
    elif rzgyn == "G":
        ruz = "Güney"
    elif rzgyn == "D":
        ruz = "Doğu"
    elif rzgyn == "B":
        ruz = "Batı"
    elif rzgyn == "KB":
        ruz = "Kuzey Batı"
    elif rzgyn == "KD":
        ruz = "Kuzey Doğu"
    elif rzgyn == "GB":
        ruz = "Güney Batı"
    elif rzgyn == "GD":
        ruz = "Güney Doğu"
    elif rzgyn == "KKB":
        ruz = "Kuzey, Kuzey Batı"
    elif rzgyn == "KKD":
        ruz = "Kuzey, Kuzey Doğu"
    elif rzgyn == "GGB":
        ruz = "Güney, Güney Batı"
    elif rzgyn == "GGD":
        ruz = "Güney, Güney Doğu"
    elif rzgyn == "DKD":
        ruz = "Doğu, Kuzey Doğu"
    elif rzgyn == "BKB":
        ruz = "Batı, Kuzey Batı"
    elif rzgyn == "BGB":
        ruz = "Batı, Güney Batı"
    elif rzgyn == "DGD":
        ruz = "Doğu, Güney Doğu"
    #weather_icon = data['WeatherIcon']
    return info,scak,nem,rzghz,ruz


def piyasa():
    url = 'http://data.altinkaynak.com/DataService.asmx?WSDL'
    auth = HTTPBasicAuth('AltinkaynakWebServis', 'AltinkaynakWebServis')
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    body = """<?xml version="1.0" encoding="utf-8"?>
            <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
              <soap12:Header>
               <AuthHeader xmlns="http://data.altinkaynak.com/">
                <Username>AltinkaynakWebServis</Username>
                <Password>AltinkaynakWebServis</Password>
               </AuthHeader>
              </soap12:Header>
            <soap12:Body>
          <GetMain xmlns="http://data.altinkaynak.com/" />
        </soap12:Body>
       </soap12:Envelope>"""

    response = requests.post(url,auth=auth,data=body.encode('utf-8'),headers=headers)
    resp = response.content
    stack = xmltodict.parse(resp)
    v = stack['soap:Envelope']['soap:Body']['GetMainResponse']['GetMainResult']
    my_dict = xmltodict.parse(v)
    usa = (my_dict['Kurlar']['Kur'][0]['Alis'][:5])
    uss = (my_dict['Kurlar']['Kur'][0]['Satis'][:5])
    eua = (my_dict['Kurlar']['Kur'][1]['Alis'][:5])
    eus = (my_dict['Kurlar']['Kur'][1]['Satis'][:5])
    aua = (my_dict['Kurlar']['Kur'][3]['Alis'][:7])
    aus = (my_dict['Kurlar']['Kur'][3]['Satis'][:7])
    aga = (my_dict['Kurlar']['Kur'][5]['Alis'][:5])
    ags = (my_dict['Kurlar']['Kur'][5]['Satis'][:5])
    return usa,uss,eua,eus,aua,aus,aga,ags


def borsa():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    borsa = requests.get(f'https://www.google.com/finance/quote/XU100:INDEXIST', headers=headers)
    soup = BeautifulSoup(borsa.text, 'html.parser')
    xu100 = soup.find('div', class_ = 'YMlKec fxKbKc').text
    return xu100

def kizisimci():
    try:
        fff = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/kizlar.py")
        ff4 = (fff.text).splitlines()
        kizi = random.choice(ff4)
        fff.close()
        return kizi
    except:
        return False


def erkisimci():
    try:
        mmm = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/erkekler.py")
        mm5 = (mmm.text).splitlines()
        erke = random.choice(mm5)
        mmm.close()
        return erke
    except:
        return False

def place():
    try:
        ppp = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/place.txt")
        pp = (ppp.text).splitlines()
        p = random.choice(pp)
        pl = p.split(",",1)
        pl1 = pl[0]
        pl2 = pl[1]
        ppp.close()
        return pl1,pl2
    except:
        return False


def corba():
    try:
        corb = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/corba.py")
        crba = (corb.text).splitlines()
        crbo = random.choice(crba)
        corb.close()
        return crbo
    except:
        return False

def yemek():
    try:
        ymk = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/anayemek.py")
        yemk = (ymk.text).splitlines()
        ymek = random.choice(yemk)
        ymk.close()
        return ymek
    except:
        return False

def salata():
    try:
        slt = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/salata.py")
        salt = (slt.text).splitlines()
        slta = random.choice(salt)
        slt.close()
        return slta
    except:
        return False

def icki():
    try:
        ickii = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/icecek.py")
        ick = (ickii.text).splitlines()
        iicki = random.choice(ick)
        ickii.close()
        return iicki
    except:
        return False

def tatli():
    try:
        tatlii = requests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/tatli.py")
        tat = (tatlii.text).splitlines()
        tatli = random.choice(tat)
        tatlii.close()
        return tatli
    except:
        return False

