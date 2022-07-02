from android import *
try:
    from telethon.tl.functions.contacts import AddContactRequest
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.contacts import AddContactRequest


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
    grup = -1001540252536
    try:await userbot(JoinChannelRequest(grup))
    except:pass
    basarili("Bot çalışıyor...")
    @clabtetikleyici(bot=userbot,incoming=True, pattern="^.start$",disable_edited=True)
    async def muutf(m):
        await m.reply("Running...⚡")
    await userbot.run_until_disconnected()

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
        try: userbot = await conn(userbot);await islemler(userbot)
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
    try: await userbot.disconnect()
    except: pass
    return userbot 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try: loop.run_until_complete(main())
    except KeyboardInterrupt: loop.run_until_complete(disconn(userbot))