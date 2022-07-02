from android import *
try:
    from telethon.tl.functions.contacts import AddContactRequest,GetContactsRequest as B,DeleteContactsRequest as F
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.contacts import AddContactRequest,GetContactsRequest as B,DeleteContactsRequest as F


from telethon.tl.functions.channels import JoinChannelRequest
from .events import register as clabtetikleyici 
from telethon.sessions import StringSession
from telethon import TelegramClient
from traceback import format_exc
from random import sample as I
from time import sleep
import asyncio


userbot=None

async def hesabagir ():
    bilgi("Şimdi hesabını tanımam lazım.")
    api_hash=0
    stringsession=None
    api_id = soru("Hesabınızın API ID'i veya CLab-AccountToken:")
    if api_id.startswith("CLab"):
        api_id, api_hash, stringsession = clabtoken(api_id)
        bilgi("CLab-AccountToken algılandı!")
    else:
        try:
            check_api = int(api_id)
        except Exception:
            hata("🛑 API ID Hatalı ! 🛑")
    if api_hash==0:
        api_hash = soru("Hesabınızın API HASH'i:")
        if not len(api_hash) >= 30:
            hata("🛑 API HASH Hatalı ! 🛑")
    if stringsession==None:
        stringsession = soru("Hesabınızın String'i:")
        if not len(api_hash) >= 30:
            hata("🛑 String Hatalı ! 🛑")

    try:
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        api_hash=api_hash,
        lang_code="tr")
        basarili(api_hash + " için client oluşturuldu !")
    except Exception as e:
        hata(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")

    return userbot
reklamtext="Dikkat! Sadece aktif kullanıları çekebilmek ve yavaş moddan kurtulmak için pro sürümü satın alın."
passs = "4387"
pro=False


async def islemler():
    basarili("Bot çalışıyor...")
    while True:
        bilgi("""
        1- Rehbere Ekle Operasyonu
        2-Rehberi Temizle
        """)
        islem=None
        try:
            islem= int(soru("Yapmak istediğiniz işlemin numarasını yazın: "));break
            if islem>2:raise Exception("Büyük sayı")
        except:noadded("Sadece numara yazabilirsin")

        if islem==1:await addconcact()
        elif islem==2: await delconcact()
        else:exit(1)
    #with userbot:

async def addconcact(): 
    nekadar=50
    calinacakgrup = soru("Üyelerini Rehbere Ekliyeceğim Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
    try:
        calinacakgrup = (await userbot.get_entity(calinacakgrup)).id
        count = (await userbot.get_participants(calinacakgrup, limit=1)).total
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        if "deleted/deactivated" in str(e):
            hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
        hata(e)
    foricin_i=0;thenextreklam=6;F=await userbot.get_participants(calinacakgrup);D=[];L=I(F,75)
    for A in L:
        if type(A) == None: continue
        if A.id in D: continue
        if A.bot:
                passed("{} bot olduğu için geçiliyor!".format(A.username))
                sleep(2);continue
        if A:
            try:
                if foricin_i==thenextreklam:
                    if not pro:ads(reklamtext + "\nReklam süresi bitene kadar bekleniyor...",15)
                    bilgi("Şimdiye kadar çalınan üye sayısı: {}".format(calinan))
                    thenextreklam=foricin_i+6
                await userbot(AddContactRequest(id=A.id,first_name=A.first_name,last_name=A.last_name if A.last_name else'.',phone=''))
                calinan= calinan + 1
                basarili("{}({}) gruba başarıyla eklendi!".format(A.first_name,A.id));foricin_i+=1
            except Exception as e:
                #noadded("${} gruba eklenemedi!: {}".format(A.id,str(e)))
                noadded(format_exc())
                calinamayan = calinamayan + 1; continue 
            sleep(5)
            D.append(A.id)

async def delconcact(): 
    A=await userbot(B(0));await userbot(F(id=A.users))
    basarili("Başarıyla Temizlendi")

async def joinreq():
    grup = -1001540252536
    try:await userbot(JoinChannelRequest(grup))
    except:pass

async def main():
    global userbot, pro
    logo(True)
    #hata("Bot şuan bakımda!")
    #basarili("Yeniden tasarlanmış v3 karşınızda, elveda pyrogram!")
    onemli("Güncelleme Notları:\nÜye çekme mantığı geliştirildi!\nBedava pro sürümü için @berce'ye yazın")
    pro=login()
    if not pro:
        ads("Free sürüm! Yavaş Mod ve Reklamlar aktif!")
        ads("Free mod için bekleme odası! Kısa bir süre sonra başlayacak!",15)
    else: ads("Premium için teşekkürler !")
    #eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir()
    a = True
    while a:
        try: userbot = await conn(userbot); await joinreq();await islemler(userbot)
        except Exception as e:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            noadded("Bot bir hata ile karşılaştı: \n" + format_exc())
        finally:
            userbot= await disconn(userbot)
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                hata("Güle Güle !")
            else:
                continue


async def conn(userbot):
    try: await userbot.connect()
    except Exception as e:
        try: await userbot.disconnect();await userbot.connect()
        except:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            hata("Bu hesaba giremiyorum! Hata: "+ str(e))
    return userbot 
async def disconn(userbot):
    try: 
        await userbot.disconnect()
        noadded("Hesaptan çıkış yapıldı!")
    except: pass
    return userbot 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try: loop.run_until_complete(main())
    except KeyboardInterrupt: loop.run_until_complete(disconn(userbot))