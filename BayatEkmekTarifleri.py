import os
import discord
from random import randint
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)



tariflistesi = {
    "Bayat Ekmek Pizzası": {"sira_no": 1, "malzemeler": ["bayat ekmek dilimleri", "domates sosu", "rendelenmiş peynir"]},
    "Bayat Ekmek Mücveri": {"sira_no": 2, "malzemeler": ["bayat ekmek", "rendelenmiş kabak", "yumurta", "un", "tuz"]},
    "Bayat Ekmek Köftesi": {"sira_no": 3, "malzemeler": ["bayat ekmek", "kıyma", "soğan", "yumurta", "baharatlar"]},
    "Bayat Ekmek Tiramisu": {"sira_no": 4, "malzemeler": ["bayat ekmek dilimleri", "kahve", "krema", "pudra şekeri", "kakao"]},
    "Bayat Ekmek Çorbası": {"sira_no": 5, "malzemeler": ["bayat ekmek", "su", "sarımsak", "zeytinyağı", "tuz", "baharatlar"]},
    "Bayat Ekmek Pudingi": {"sira_no": 6, "malzemeler": ["bayat ekmek", "süt", "şeker", "yumurta", "vanilya"]},
    "Bayat Ekmek Böreği": {"sira_no": 7, "malzemeler": ["bayat ekmek dilimleri", "peynir", "yumurta", "süt", "zeytinyağı"]},
    "Bayat Ekmek Tatlısı": {"sira_no": 8, "malzemeler": ["bayat ekmek dilimleri", "şerbet", "çırpılmış krema", "antep fıstığı"]},
    "Bayat Ekmek Salatası": {"sira_no": 9, "malzemeler": ["bayat ekmek", "domates", "salatalık", "soğan", "zeytinyağı", "limon suyu"]},
    "Bayat Ekmek Omleti": {"sira_no": 10, "malzemeler": ["bayat ekmek", "yumurta", "süt", "peynir", "domates", "biber"]},
    "Bayat Ekmek Strata": {"sira_no": 11, "malzemeler": ["bayat ekmek dilimleri", "yumurta", "süt", "peynir", "sebzeler"]},
    "Bayat Ekmek Pankekleri": {"sira_no": 12, "malzemeler": ["bayat ekmek", "yumurta", "süt", "un", "şeker", "vanilya"]},
    "Bayat Ekmek Lazanya": {"sira_no": 13, "malzemeler": ["bayat ekmek", "rendelenmiş et", "domates sosu", "beşamel sos", "rendelenmiş peynir"]},
    "Bayat Ekmek Krutonları": {"sira_no": 14, "malzemeler": ["bayat ekmek", "zeytinyağı", "tuz", "baharatlar"]},
    "Bayat Ekmek Granola": {"sira_no": 15, "malzemeler": ["bayat ekmek", "yulaf ezmesi", "kuruyemişler", "bal", "tarçın"]},
    "Bayat Ekmek Sandviçleri": {"sira_no": 16, "malzemeler": ["bayat ekmek dilimleri", "dilimlenmiş et", "peynir", "marul", "domates", "mayonez"]},
    "Bayat Ekmek Tostu": {"sira_no": 17, "malzemeler": ["bayat ekmek dilimleri", "kaşar peyniri", "sucuk", "domates", "biber"]}
}
@bot.command()
async def bilgi(ctx):
    await ctx.send("Tarif listesi için- /tarifler\nTarifin detayları için- /tarif (tarif_adı)")

@bot.command()
async def hakkında(ctx):
    await ctx.send("Bu botun amacı size bayat ekmeği doğru kullanmayı öğretmektir.")


@bot.command()
async def tarifler(ctx):
    for yemek, detaylar in tariflistesi.items():
        sira_no = detaylar["sira_no"]
        await ctx.send(f"{sira_no}-{yemek}")

@bot.command()
async def tarif(ctx):
    malzemelist = ""
    message = ctx.message
    istenenyemek = message.content.replace("/tarif ", "")
    print(istenenyemek)
    for yemek, detaylar in tariflistesi.items():
        if yemek == istenenyemek:
            await ctx.send(f"İşte {yemek} tarifi:")
            i = 0
            for malzeme in detaylar["malzemeler"]:
                i += 1
                malzemelist += f"{i}-{malzeme}\n"
            await ctx.send(f"{malzemelist}")

            await ctx.send(f"{yemek}'in fotoğrafı:")
            imagespath = rf"C:\Users\parla\OneDrive\Masaüstü\Kodland\Ders6\BayatEkmekTarifResimleri"
            with open(rf"{imagespath}\{detaylar['sira_no']}.jpg", 'rb') as f:
                picture = discord.File(f)
            await ctx.send(file=picture)



bot.run("TOKEN")
