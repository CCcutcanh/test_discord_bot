from asyncio import exceptions
import re
from socket import timeout
import discord
from discord.ext import commands, tasks
import json 
import os
import requests
import pymailtm
from youtube_search import YoutubeSearch
import random
import os
import random
import asyncio
import wikipedia
import datetime
import time
import urllib.request
from discord.utils import find
from bs4 import BeautifulSoup
def command_prefix(bot, message):
    with open(r"C:\codde\discord_bot\data.json", 'r') as f:
        users = json.load(f)
    prefix = users[str(message.guild.id)]['prefix']
    return commands.when_mentioned_or(*prefix)(bot, message)
def get_prefix():
    with open(r"C:\codde\discord_bot\data.json", 'r') as f:
        prefix = json.load(f)
    return prefix
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=(command_prefix), intents = intents)
bot.remove_command("help")
@bot.event
async def on_guild_join(guild):
    users = get_prefix()
    users[str(guild.id)] = {}
    users[str(guild.id)]['prefix'] = '?'
    with open(r"C:\codde\discord_bot\data.json", 'w') as f:
        json.dump(users, f)
@bot.event
async def on_ready():
    print(f'[LOGIN] login successful into {bot.user}')
@bot.group(invoke_without_command=True)
async def help(ctx, arg = None):
    help_prefix = get_prefix()[str(ctx.message.guild.id)]['prefix']
    if arg == None:
        em = discord.Embed(title = "ℹ️help", description = "sử dụng /help để biết các lệnh có thể sử dụng trên bot và /help <command> để biết cách sử dụng")
        em.add_field(name = "**✅other command**", value = "xsmb, covid19, weather, youtube_search, translate, truyentranh, wiki, news, google_search, google_search, videofb")
        em.add_field(name = "**🎮game command**", value = "dovui, play_taixiu, keobuabao, vuatiengviet, dhbc(đuổi hình bắt chữ), noitu, slot")
        em.add_field(name = "**🏵️roleplay command**", value = "balance, bank, work, daily, rob")
        em.add_field(name = "**⚙️system command bot**", value = "help, offbot, ping, callad, sendnoti, setprefix")
        em.add_field(name = "**🔫fun command**", value = "thinh, mark, tiki, taoanhdep, shopmaihuong, caunoihay, thayboi, banner1")
        await ctx.send(embed = em)
    elif arg == 'balance':
        em = discord.Embed(title = "balance", description = "xem số tiền hiện đang có của bạn")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}balance @mention")
        await ctx.send(embed = em)
    elif arg == 'bank':
        em = discord.Embed(title = "bank", description = "ngân hàng hỗ trợ rút và gửi tiền của bạn")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}bank withdraw <amount>\n{get_prefix()[str(ctx.message.guild.id)]['prefix']}bank deposit <amount>\n{get_prefix()[str(ctx.message.guild.id)]['prefix']}bank send <amount> @mention")
        await ctx.send(embed = em)
    elif arg == 'callad':
        em = discord.Embed(title = "callad", description = "báo cáo vấn đề hoặc câu hỏi bạn muốn gửi đến admin")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}callad <vấn đề cần báo cáo>")
        await ctx.send(embed = em)
    elif arg == 'caunoihay':
        em = discord.Embed(title = "caunoihay", description = "random một câu nói của các vĩ nhân:))")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}caunoihay")
        await ctx.send(embed = em)
    elif arg == 'covid19':
        em = discord.Embed(title = "covid19", description = "xem thông tin về dịch bệnh covid 19 tại Việt Nam")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}covid19")
        await ctx.send(embed = em)
    elif arg == 'daily':
        em = discord.Embed(title = "daily", description = "nhận thưởng online mỗi 24H")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}D>")
        await ctx.send(embed = em)
    elif arg == 'dhbc':
        em = discord.Embed(title = "dhbc", description = "game đuổi hình bắt chữ:))")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}dhbc")
        await ctx.send(embed = em)
    elif arg == 'keobuabao':
        em = discord.Embed(title = "keobuabao", description = "game kéo búa bao với bot")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}keobuabao <kéo/búa/bao> <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'mark':
        em = discord.Embed(title = "mark", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}mark")
        await ctx.send(embed = em)
    elif arg == 'news':
        em = discord.Embed(title = "news", description = "xem tin mới mỗi ngày trên vnexpress")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}news")
        await ctx.send(embed = em)
    elif arg == 'noitu':
        em = discord.Embed(title = "noitu", description = "game nối từ cùng bot")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}noitu")
        await ctx.send(embed = em)
    elif arg == 'ping':
        em = discord.Embed(title = "ping", description = "pong!")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}ping")
        await ctx.send(embed = em)
    elif arg == 'play_taixiu':
        em = discord.Embed(title = "play_taixiu", description = "chơi game tài xỉu trên bot:)")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}play_taixiu <tài/xỉu> <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'shopmaihuong':
        em = discord.Embed(title = "shopmaihuong", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}shopmaihuong")
        await ctx.send(embed = em)
    elif arg == 'slot':
        em = discord.Embed(title = "slot", description = "game")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}slot <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'taoanhdep':
        em = discord.Embed(title = "taoanhdep", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}taoanhdep")
        await ctx.send(embed = em)
    elif arg == 'thayboi':
        em = discord.Embed(title = "thayboi", description = "xem bói online:))")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}thayboi")
        await ctx.send(embed = em)
    elif arg == 'thinh':
        em = discord.Embed(title = "thinh", description = "thính")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}thinh")
        await ctx.send(embed = em)
    elif arg == 'tiki':
        em = discord.Embed(title = "tiki", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}tiki <name>")
        await ctx.send(embed = em)
    elif arg == 'translate':
        em = discord.Embed(title = "translate", description = "google dịch")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}translate")
        await ctx.send(embed = em)
    elif arg == 'truyentranh':
        em = discord.Embed(title = "truyentranh", description = "xem truyện tranh và tìm những truyện mới nhất trên toptruyen.net và truyentranh24.com")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}truyentranh search <keywword> (tìm truyện)\n{get_prefix()[str(ctx.message.guild.id)]['prefix']}truyentranh news (xem các truyện mới nhất trên toptruyen.net)")
        await ctx.send(embed = em)
    elif arg == 'vuatiengviet':
        em = discord.Embed(title = "vuatiengviet", description = "chơi vua tiếng việt:0")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}vuatiengviet")
        await ctx.send(embed = em)
    elif arg == 'weather ':
        em = discord.Embed(title = "weather", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}weather <location>")
        await ctx.send(embed = em)
    elif arg == 'wiki':
        em = discord.Embed(title = "wiki", description = "tìm kiếm thông tin trên wikipedia")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}wiki <keywword>")
        await ctx.send(embed = em)
    elif arg == 'work':
        em = discord.Embed(title = "work", description = "có làm thì mới có ăn")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}work")
        await ctx.send(embed = em)
    elif arg == 'xsmb':
        em = discord.Embed(title = "xsmb", description = "xem kết quả xổ số miền Bắc")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}xsmb")
        await ctx.send(embed = em)
    elif arg == 'youtube_search':
        em = discord.Embed(title = "youtube_search", description = "tìm video youtube")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}youtube_search <keyword>")
        await ctx.send(embed = em)
    elif arg == 'dovui':
        em = discord.Embed(title = "dovui", description = "game đố vui, không vui thì thôi")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}dovui")
        await ctx.send(embed = em)
    elif arg == 'google_search':
        em = discord.Embed(title = "google_search", description = "tìm kiếm thông tin trên google")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}google_search")
        await ctx.send(embed = em)
    elif arg == 'setprefix':
        em = discord.Embed(title = "setprefix", description = f"set prefix bot cho sever")
        em.add_field(name = "**cách dùng**", value = f"{help_prefix}setprefix <prefix>")
        await ctx.send(embed = em)
    elif arg == 'banner1':
        em = discord.Embed(title = "banner1", description = f"tạo banner cho riêng bạn")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}banner1")
        await ctx.send(embed = em)
    elif arg == 'videofb':
        em = discord.Embed(title = "videofb", description = f"tải video từ link video facbook (lưu ý: video càng dài tải càng lâu)")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}videofb <link>")
        await ctx.send(embed = em)
    elif arg == 'rob':
        em = discord.Embed(title = "rob", description = f"không làm những vẫn muốn có ăn;)")
        em.add_field(name = "**cách dùng**", value = f"{get_prefix()[str(ctx.message.guild.id)]['prefix']}rob")
        await ctx.send(embed = em)
    else:
        await ctx.send(f"lệnh bạn nhập không tồn tại hoặc do thằng admin lỏl lười làm nên để thế=)). có thể sử dụng {get_prefix()[str(ctx.message.guild.id)]['prefix']}callad để gọi nó dậy")
    
#run bot
#client
#covid19
@bot.command()
async def covid19(ctx):
    full_url = 'https://api.phamvandien.xyz/covid?country=viet%20nam'
    get = requests.get(full_url)
    data = get.text
    parse_json = json.loads(data)
    data1 = parse_json['data']['danso']
    data2 = parse_json['data']['dangdieutri']
    data3 = parse_json['data']['ca_nhiem_moi']
    data4 = parse_json['data']['hoiphuc']
    data5 = parse_json['data']['total']
    data6 = parse_json['data']['tong_ca_tu_vong']
    result = """thông tin về dịch bệnh covid 19 tại Việt Nam như sau: dân số {data1} người\ntổng số ca nhiễm: {data5} \nsố ca đang điều trị {data2} ca \nsố bệnh nhân đã khỏi bệnh: {data4} bệnh nhân \nca nhiễm mới: {data3} \ntổng số ca dã tử vong: {data6}""".format(data1 = str(data1), data2 = str(data2), data3 = str(data3), data4 = str(data4), data5 = str(data5), data6 = str(data6))
    await ctx.send(result)
#xsmb
@bot.command()
async def xsmb(ctx):
    #xsmb
    try:
        result = []
        url = 'https://www.xoso.net/getkqxs/mien-bac.js'
        get_data = requests.get(url)
        x = get_data.text
        soup = BeautifulSoup(x, 'html.parser')
        for a in soup.find_all(class_ = 'giaidb'):
            result.append(a.text)
            print(a.text)
        for c in soup.find_all(class_ = 'giai1'):
            result.append(c.text)
            print(c.text)
        for d in soup.find_all(class_ = 'giai2'):
            result.append(d.text)
            print(d.text)
        for e in soup.find_all(class_ = 'giai3'):
            result.append(e.text)
            print(e.text)
        for f in soup.find_all(class_ = 'giai4'):
            result.append(f.text)
            print(f.text)
        for g in soup.find_all(class_ = 'giai5'):
            result.append(g.text)
            print(g.text)
        for h in soup.find_all(class_ = 'giai6'):
            result.append(h.text)
            print(h.text)
        for k in soup.find_all(class_ = 'giai7'):
            result.append(k.text)
            print(k.text)
        for l in soup.find_all(class_ = 'ngay'):
            result.append(l.text)
            print(l.text)
        t = '\t'
        n = '\n'
        await ctx.send(f'Kết quả xổ số miền Bắc {str(result[8]).strip(f"{t}")}{n}{n}Giải đặc biệt: {str(result[0]).strip(f"{t}")}{n}Giải nhất: {str(result[1]).strip(f"{t}")}{n}Giải nhì: {str(result[2]).strip(f"{t}")}{n}Giải ba: {str(result[3]).strip(f"{t}")}\nGiải tư: {str(result[4]).strip(f"{t}")}{n}Giải năm: {str(result[5]).strip(f"{t}")}{n}Giải sáu: {str(result[6]).strip(f"{t}")}{n}Giải bảy: {str(result[7]).strip(f"{t}")}')
    except Exception as e:
        print(e)
    
#weather
@bot.command()
async def weather(ctx, *, arg = None):
    if arg == None:
        await ctx.send('sai cú pháp')
    elif arg != None:
        url = f'https://api.accuweather.com/locations/v1/cities/search.json?q={arg}&apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&language=vi-vn'
        image = f'http://mewdev.pro/api/v2/weather?location={arg}&apikey=Meew.90c3759fff62c248ba845561583c76fa'
        get_image = requests.get(image)
        get = requests.get(url)
        img_txt = get_image.text
        data_txt = get.text
        data_json = json.loads(data_txt)
        image_json = json.loads(img_txt)
        if len(data_json) != 0 and image_json['success'] == True:
            img = requests.get(image_json['data'])
            file = open("weather.png", "wb")
            file.write(img.content)
            file.close()
            key = data_json[0]['Key']
            get2 = requests.get(f'http://api.accuweather.com/forecasts/v1/daily/10day/{key}?apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&details=true&language=vi')
            txt2 = get2.text
            json2 = json.loads(txt2) 
            temp_min = round((json2['DailyForecasts'][0]['Temperature']['Minimum']['Value'] - 32)/1.8)
            temp_max = round((json2['DailyForecasts'][0]['Temperature']['Maximum']['Value'] - 32)/1.8)
            feel_like = round((json2['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'] - 32)/1.8)
            sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochRise']))
            sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochSet']))
            moonrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochRise']))
            moonset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochSet']))
            day =  json2['DailyForecasts'][0]['Day']['LongPhrase']
            night = json2['DailyForecasts'][0]['Night']['LongPhrase']
            description = json2['Headline']['Text']      
            await ctx.send(f'Thời tiết hôm nay: {description}\n🌡️Nhiệt độ cao nhât - Thấp nhất: {temp_max}°C - {temp_min}°C\n🌡️Nhiệt độ cảm nhận được: {feel_like}°C\n🌅Mặt trời mọc: {sunrise}\n🌄Mặt trời lặn: {sunset}\n🌃Mặt trăng mọc: {moonrise}\n🌃Mặt trăng lặn: {moonset}\n🌞Ban ngày: {day}\n🌞Ban đêm: {night}', file = discord.File('weather.png'))
        elif len(data_json) != 0 and image_json['success'] == False:
            try:
                img = requests.get(f'https://nguyenmanh.name.vn/api/thoitiet?type=image&query={arg}&apikey=KCL98tNB')
                check = img.text
                if check == "Không tìm thấy địa điểm này!":
                    await ctx.send('error')
                else:
                    file = open("weather.png", "wb")
                    file.write(img.content)
                    file.close()
                    key = data_json[0]['Key']
                    get2 = requests.get(f'http://api.accuweather.com/forecasts/v1/daily/10day/{key}?apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&details=true&language=vi')
                    txt2 = get2.text
                    json2 = json.loads(txt2) 
                    temp_min = round((json2['DailyForecasts'][0]['Temperature']['Minimum']['Value'] - 32)/1.8)
                    temp_max = round((json2['DailyForecasts'][0]['Temperature']['Maximum']['Value'] - 32)/1.8)
                    feel_like = round((json2['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'] - 32)/1.8)
                    sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochRise']))
                    sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochSet']))
                    moonrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochRise']))
                    moonset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochSet']))
                    day =  json2['DailyForecasts'][0]['Day']['LongPhrase']
                    night = json2['DailyForecasts'][0]['Night']['LongPhrase']
                    description = json2['Headline']['Text']     
                    await ctx.send(f'Thời tiết hôm nay: {description}\n🌡️Nhiệt độ cao nhât - Thấp nhất: {temp_max}°C - {temp_min}°C\n🌡️Nhiệt độ cảm nhận được: {feel_like}°C\n🌅Mặt trời mọc: {sunrise}\n🌄Mặt trời lặn: {sunset}\n🌃Mặt trăng mọc: {moonrise}\n🌃Mặt trăng lặn: {moonset}\n🌞Ban ngày: {day}\n🌞Ban đêm: {night}', file = discord.File('weather.png'))
            except Exception as e:
                print(e)
                await ctx.send('đã xảy ra lỗi không xác định')
        else:
            await ctx.send('error, lỗi chưa xác định')
    print(data_json['cod'])
    print(image_json['success'])
@bot.command()
async def youtube_search(ctx, arg = None):
    if arg == None:
        await ctx.send('bạn chưa nhập từ kháo cần tìm kiếm')
    else:
        await ctx.send('nhập từ khóa cần tìm kiếm')
        search = YoutubeSearch('{content}'.format(content = str(arg)), max_results=5).to_json()
        search_dict = json.loads(search)
        for v in search_dict['videos']:
            result = 'https://www.youtube.com/watch?v=' + v['id'] + " - " + v['title'] + " của kênh " + v['channel']
            await ctx.send('đây là các kết quả tìm kiếm {result}'.format(result = result))
@bot.command()
@commands.is_owner()
async def offbot(ctx):
    if (int(ctx.message.author.id) == 716146182849560598): 
        await ctx.send('đã tắt bot!')
        print("off bot")
        await ctx.bot.logout()
    else:
        await ctx.send('bạn không phải admin bot nên không đủ quyền hạn sử dụng lệnh này')
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
@bot.command()
async def play_taixiu(ctx, arg1 = None, arg2 = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if member_data[str(ctx.message.author.id)]["Wallet"] < int(arg2):
        await ctx.send('không đủ tiền để chơi:)')
    else:
        try:
            url = 'https://api.hclaptrinh.repl.co/api/taixiu'
            get = requests.get(url)
            data_txt = get.text
            data_json = json.loads(data_txt)
            result = data_json['result']
            dice = data_json['dice']
            if result == 'xiu':
                result = 'xỉu'
            elif result == 'tai':
                result = 'tài'
            if arg1 == None:
                await ctx.send('hãy cược tài hoặc xỉu')
            elif arg2 == None or int(arg2) < 50:
                await ctx.send('số tiền cược không cược để trống và phải từ 50$ trở lên')
            elif arg1 == result:
                gif = 'https://media1.giphy.com/media/ckHAdLU2OmY7knUClD/giphy.gif?cid=ecf05e47venaa45nhe4pmfsckgtrjasrpdzs6vtmpvwya6fk&rid=giphy.gif&ct=g'
                gif2 = 'https://media1.giphy.com/media/g9582DNuQppxC/giphy.gif?cid=ecf05e4743jop5ctofl2a5763ih04tc5b91dfnor287cu5tv&rid=giphy.gif&ct=g'
                em_load = discord.Embed(colour = ctx.author.color, description = 'đang lắc xúc sắc...')
                em_load.set_image(url = gif)
                em_win = discord.Embed(colour = ctx.author.color, description = f'\n{dice[0]} {dice[1]} {dice[2]} | {result} và gom về được {arg2}$ tiền cược')
                em_win.set_image(url = gif2)
                await ctx.send(embed = em_load)
                await asyncio.sleep(3)
                await ctx.send(embed = em_win)
                await update(ctx.message.author.id, arg2, 'keobuabao_win')
            elif arg1 != result:
                gif = 'https://media1.giphy.com/media/ckHAdLU2OmY7knUClD/giphy.gif?cid=ecf05e47venaa45nhe4pmfsckgtrjasrpdzs6vtmpvwya6fk&rid=giphy.gif&ct=g'
                gif2 = 'https://media3.giphy.com/media/l22ysLe54hZP0wubek/giphy.gif?cid=ecf05e47mba9xtd5rurzzo1flalwaqu6znpuld9vm6b2rz13&rid=giphy.gif&ct=g'
                em_load = discord.Embed(colour = ctx.author.color, description = 'đang lắc xúc sắc...')
                em_load.set_image(url = gif)
                em_win = discord.Embed(colour = ctx.author.color, description = f'bạn đã thua, kết quả là:\n{dice[0]} {dice[1]} {dice[2]} | {result} và mất {arg2}$ tiền cược')
                em_win.set_image(url = gif2)
                await ctx.send(embed = em_load)
                await asyncio.sleep(3)
                await ctx.send(embed = em_win)
                await update(ctx.message.author.id, arg2, 'keobuabao_lose')
            else:
                await ctx.send('lỗi')
        except Exception as e:
            print(e)
            await ctx.send('error')
@bot.command(name = "work")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    send = await ctx.send('đây là các việc bạn có thể làm để kiếm tiền\n1. bán vé số\n2. sửa xe\n3. lập trình\n4. thợ hồ\n5. bán hàng online\n6. Đứng đường:))\nreply tin nhắn theo số thứ tự để chọn việc muốn làm')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
    message = await bot.wait_for('message', check = check, timeout=45)
    if str(message.content.lower()) == "1":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Wallet'] += earning
        await ctx.send(f"bạn bán vé số và kiếm được {earning}$!")
        save_member_data(member_data)
    elif str(message.content.lower()) == "2":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Wallet'] += earning
        await ctx.send(f"bạn làm thợ sửa xe và kiếm được {earning}$!")
        save_member_data(member_data)
    elif str(message.content.lower()) == "3":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Wallet'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn làm lập trình viên và kiếm được {earning}$!")
    elif str(message.content.lower()) == "4":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Wallet'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn làm thợ hồ và kiếm được {earning}$!")
    elif str(message.content.lower()) == "5":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Wallet'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn bán hàng online và kiếm được {earning}$!")
    elif str(message.content.lower()) == "6":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn được một anh đẹp trai gọi và kiếm được {earning}$!")
    else:
        await ctx.send('bạn chỉ được chọn 1 trong 6 nghề trên')
@bot.event
async def on_command_error(ctx, error):
    pass
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã làm việc quá nhiều rồi, hãy nghỉ ngơi và quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def balance(ctx, member: discord.User=None):
    try:
        if member == None:
            await open_account(ctx.author.id)
            member_data = await get_bank_data()
            wallet = member_data[str(ctx.author.id)]['Wallet']
            bank = member_data[str(ctx.author.id)]["Bank"]
            embed = discord.Embed(title=f"số tiền của {ctx.author.display_name}")
            embed.add_field(name="tiền mặt", value=wallet)
            embed.add_field(name="trong thẻ ngân hàng", value=bank)
            await ctx.send(embed=embed)
        else:
            await open_account(member.id)
            member_data = await get_bank_data()
            wallet = member_data[str(member.id)]["Wallet"]
            bank = member_data[str(member.id)]["Bank"]
            embed = discord.Embed(title=f"số tiền của {member}")
            embed.add_field(name="tiền mặt", value=wallet)
            embed.add_field(name="trong thẻ ngân hàng", value= bank)
            await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send('error')
@bot.group(invoke_without_command=True)
async def bank(ctx):
    embed = discord.Embed(title="MIRAI BANK", description="nơi gửi và rút tiền từ ngân hàng", color=0x00ff00)
    embed.add_field(name = "cách sử dụng", value = "/bank withdraw, /bank deposit") #creates embed
    file = discord.File(r"image\bank.png", filename="bank.png") 
    embed.set_image(url="attachment://bank.png")
    await ctx.send(file=file, embed=embed)
@bank.command()
@commands.cooldown(3, 2400, commands.BucketType.user)
async def withdraw(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if member_data[str(ctx.author.id)]["Bank"] < int(arg):
        await ctx.send('m ko đủ số tiền để rút, t ko ngu đâu mà đòi lừa=))')
    elif arg == None:
        await ctx.send('nhập số tiền cần rút')
    elif member_data[str(ctx.author.id)]["Bank"] >= int(arg):
        await ctx.send(f'đã rút {arg}$ từ tài khoản')
        await update(ctx.message.author.id, arg, 'bank')
@withdraw.error
async def withdraw_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng hỏng ATM rồi:((, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "deposit")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def deposit(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if arg == None:
        await ctx.send('nhập số tiền cần bỏ vào tài khoản')
    elif member_data[str(ctx.author.id)]["Wallet"] < int(arg):
        await ctx.send('m ko đủ số tiền để gửi vào tài khoản, t ko ngu đâu mà đòi lừa=))')
    elif member_data[str(ctx.author.id)]["Wallet"] >= int(arg):
        await ctx.send(f'đã trừ {arg}$ của ví')
        await update(ctx.message.author.id, arg, 'wallet')
@deposit.error
async def deposit_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng đóng cửa rồi, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "send")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def send(ctx, member: discord.User=None, amount = None):
    await open_account(ctx.message.author.id)
    await open_account(member.id)
    data_send_user = await get_bank_data() 
    data_receive_user = await get_bank_data()
    if discord.User == None or amount == None or discord.User == None and amount == None:
        await ctx.send('sai cú pháp')
    elif data_send_user[str(ctx.author.id)]["Bank"] < int(amount):
        await ctx.send('không đủ số tiền trong tài khoản để gửi')
    else:
        try:
            await update(ctx.message.author.id, amount, 'send_user')
            await update(member.id, amount, 'receive_user')
            await ctx.send(f'đã chuyển tiền thành công cho {member.mention}')
        except Exception as e:
            print(e)
            await ctx.send('error')
@send.error
async def send_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng đóng cửa rồi, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def thinh(ctx):
    global random, json
    url = 'https://raw.githubusercontent.com/ledingg1997/ledingg-/main/datathinh.json'
    random_thinh = random.randint(1, 187)
    get = requests.get(url)
    data = get.text
    data_json = json.loads(data)
    result = data_json['data'][f'{random_thinh}']
    await ctx.send(result)
@bot.command()
async def keobuabao(ctx, arg1 = None, arg2 = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    choice = ['kéo', 'búa', 'bao', 'kéo', 'búa', 'bao']
    bot = random.choice(choice)
    if arg1 == None or arg2 == None or arg1 == None and arg2 == None:
            await ctx.send('sai cú pháp')
    elif member_data[str(ctx.author.id)]["Wallet"] < int(arg2):
        await ctx.send('ko đủ tiền để chơi')
    else:
        if arg1 == bot:
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Hòa')
        elif arg1 == 'bao' and bot == 'búa':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Bạn đã thắng và nhận đươc {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        elif arg1 == 'bao' and bot == 'kéo':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'kéo' and bot == 'búa':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'kéo' and bot == 'bao':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        elif arg1 == 'búa' and bot == 'bao':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'búa' and bot == 'kéo':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        else:
            await ctx.send('lỗi')
@bot.command()
async def vuatiengviet(ctx):
    try: 
        url_vuatiengviet = 'https://api.phamvandien.xyz/vuatiengviet/image?word='
        word_vuatiengviet = ["tôi yêu bạn", "cá koi", "cuốn sách", "tình yêu", "độc dược", "cô đọng", "huyền thoại", "sao băng", "quấn quýt", "bậc thầy", "ước vọng", "mơ mộng", "tình tứ", "mộng mơ", "nông nghiệp", "băng hà", "hiếu động", "sung sức", "công lao", "tâm tình", "cờ bạc", "ngu ngốc", "nông trường", "trường thọ", "tôn trọng"]
        random_word_vuatiengviet = random.choice(word_vuatiengviet)
        full_url_vuatiengviet = url_vuatiengviet + random_word_vuatiengviet
        get_vuatiengviet = requests.get(full_url_vuatiengviet)
        file = open("vuatiengviet.png", "wb")
        file.write(get_vuatiengviet.content)
        file.close()
        send = await ctx.send('đây là câu hỏi của bạn\nreply tin nhắn này để trả lời câu hỏi, bạn có 45 giây để trả lời', file = discord.File('vuatiengviet.png'))
        if " " in random_word_vuatiengviet:
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
            try:
                message = await bot.wait_for('message', timeout=45, check=check)
                if message:
                    if message.content.lower() == random_word_vuatiengviet:
                        await ctx.send(f'bạn đã trả lời đúng, đáp án là "{random_word_vuatiengviet}"')
                    else:
                        await ctx.send(f'sai rồi đáp án là "{random_word_vuatiengviet}"')
            except asyncio.TimeoutError:
                await ctx.send('Hết giờ!')
    except Exception as e:
        print(e)
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. Xin lỗi vì sự cố này')
@bot.command()
async def mark(ctx):
    await ctx.send('lệnh bạn sử dụng hiện đang gặp lỗi, hãy báo cáo về admin bằng lệnh callad để được sửa sớm nhất')
@bot.command()
async def Phubcmt(ctx):
    try:
        send = await ctx.send('reply tin nhắn này và các nhập thông tin cần thiết theo mẫu sau:\n<text> | <username> | <uid (4 -> ∞)>')
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for('message', check=check)
        split = message.content.lower().split(' | ')
        if len(split) != 3:
            await ctx.send('lỗi, nhập thiếu thông tin')
        else:
            url_mark = f"https://manhict.tech/api/phubcmt?text={split[0]}&uid={split[2]}&name={split[1]}&apikey=KCL98tNB"
            get = requests.get(url_mark)
            if get.status_code != 200:
                await ctx.send('lỗi')
            else:
                file = open("mark.png", "wb")
                file.write(get.content)
                file.close()
                await ctx.send('ảnh đây:)', file = discord.File('mark.png'))
    except:
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def tiki(ctx,*,arg = None):
    help_prefix = get_prefix()[str(ctx.message.guild.id)]['prefix']
    if arg == None:
        await ctx.send(f"bạn chưa nhập tên mình vào\n{help_prefix}tiki <name>")
    else:
        url_tiki = 'https://api.phamvandien.xyz/tiki?text='
        full_url_tiki = url_tiki + str(arg)
        get_tiki = requests.get(full_url_tiki)
        if get_tiki.status_code != 200:
            await ctx.send("lỗi")
        else:
            file = open("tiki.png", "wb")
            file.write(get_tiki.content)
            file.close()
            await ctx.send('ảnh đây:)', file = discord.File('tiki.png'))
@bot.command()
async def dhbc(ctx):
    global random
    try:
        url_DHBC = ['https://goatbot.tk/api/duoihinhbatchu', 'https://api.phamvandien.xyz/game/dhbcv1', 'https://www.nguyenmanh.name.vn/api/dhbc1?apikey=KCL98tNB']
        random_dhbc = random.choice(url_DHBC)
        get_DHBC = requests.get(random_dhbc)
        data_DHBC = get_DHBC.text
        json_DHBC = json.loads(data_DHBC)
        if random_dhbc == 'https://goatbot.tk/api/duoihinhbatchu':
            image_DHBC = json_DHBC['data']['image1and2'] 
            sokt = json_DHBC['data']['soluongkt']
            dapan = json_DHBC['data']['wordcomplete']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            send = await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này có {sokt} chữ', file = discord.File('DHBC.png'))
            if "g" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.upper()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
        elif random_dhbc == 'https://api.phamvandien.xyz/game/dhbcv1':
            image_DHBC = json_DHBC['dataGame']['link'] 
            sokt = json_DHBC['dataGame']['sokitu']
            dapan = json_DHBC['dataGame']['tukhoa']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            send = await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này là {sokt}', file = discord.File('DHBC.png'))
            if "a" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.lower()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
        elif random_dhbc == 'https://www.nguyenmanh.name.vn/api/dhbc1?apikey=KCL98tNB':
            image_DHBC = json_DHBC['result']['link'] 
            sokt = json_DHBC['result']['sokitu']
            dapan = json_DHBC['result']['tukhoa']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            send = await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này là {sokt}', file = discord.File('DHBC.png'))
            if "a" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.lower()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
    except Exception as e:
        print(e)
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def noitu(ctx):
    await ctx.send('đã bắt đầu, hãy mở đầu trò chơi với một từ đầu tiên')
    while True:
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        url_noitu = 'https://goatbot.tk/api/wordlink?text='
        full_url_noitu = url_noitu + str(message.content)
        get_noitu = requests.get(full_url_noitu)
        data_noitu = get_noitu.text
        json_noitu = json.loads(data_noitu)
        word_noitu = json_noitu['data']
        if "lose" in word_noitu:
            await ctx.send('bạn thắng rồi:((')
            break
        if message.content == "quit":
            await ctx.send('bạn thua rồiiiii:)')
            break
        else:
            await ctx.send(word_noitu)
@bot.command()
async def taoanhdep(ctx):
    send = await ctx.send('reply tin nhắn này và nhập để tạo ảnh theo mẫu sau:\n<id nhân vật> | <chữ nền> | <chữ kí>')
    def check(m):
        return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
    message = await bot.wait_for('message', check=check)
    url_taoanhdep = 'https://goatbot.tk/taoanhdep/avataranime?apikey=ntkhangGoatBot'
    value = message.content.lower().split(" | ")
    id_taoanhdep = str(value[0])
    chunen = str(value[1])
    chuky = str(value[2])
    complete_url_taoanhdep = url_taoanhdep + "&chu_Nen=" + chunen + "&chu_Ky=" + chuky + "&id=" +id_taoanhdep 
    get_taoanhdep = requests.get(complete_url_taoanhdep)
    file = open("taoanhdep.png", "wb")
    file.write(get_taoanhdep.content)
    file.close()
    await ctx.send('ảnh của bạn đây:>', file = discord.File('taoanhdep.png'))
@bot.command()
async def translate(ctx, *, arg = None):
    if arg:
        get = requests.get(f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=vi&dt=t&q={arg}')
        load = json.loads(get.text)
        from_lang = load[8][0][0]
        translate_text = load[0][0][0]
        await ctx.send(f'Bản dịch:\n{translate_text}\nđược dịch từ {from_lang} -> vi')
    else:
        await ctx.send("bạn chưa nhập câu cần dịch")
@bot.command()
async def caunoihay(ctx):
    sentence = ['Một cách để tận dụng tối đa cuộc sống là xem nó như một cuộc phiêu lưu – William Feather',' Mạnh dạn nói Tôi đã sai là cách ta chấp nhận đối mặt với tình huống khó khăn. Việc đó có phần mạo hiểm nhưng những gì ta nhận được sẽ vượt ngoài sự mong đợi’ - Rich DeVos', 'Tích cực, tự tin và kiên trì là chìa khóa trong cuộc sống. Vì vậy đừng bao giờ từ bỏ chính mình’ – Khalid', 'Yêu tôi hay ghét tôi, cả hai đều có lợi cho tôi. Nếu bạn yêu tôi, tôi sẽ luôn ở trong tim bạn và nếu bạn ghét tôi, tôi sẽ ở trong tâm trí bạn’ – Baland Quandeel', 'Thái độ quan trọng hơn quá khứ, hơn giáo dục, hơn tiền bạc, hơn hoàn cảnh, hơn những gì mọi người làm hoặc nói. Nó quan trọng hơn ngoại hình, năng khiếu hay kỹ năng’ – Charles Swindoll', 'Hãy tin vào chính mình! Có niềm tin vào khả năng của bạn! Nếu không có sự tự tin khiêm tốn nhưng hợp lý vào năng lực của chính mình, bạn không thể thành công hay hạnh phúc’ - Norman Vincent Peale', 'Trong đời người, có hai con đường bằng phẳng không trở ngại: Một là đi tới lý tưởng, một là đi tới cái chết’ - Lev Tolstoy', 'Bạn có thể thay đổi thế giới của mình bằng cách thay đổi lời nói của bạn ... Hãy nhớ rằng, cái chết và sự sống nằm trong sức mạnh của lưỡi’ - Joel Osteen', 'Lạc quan là niềm tin dẫn đến thành tích. Không có gì có thể được thực hiện mà không có hy vọng và sự tự tin’ - Helen Keller', '‘Nếu bạn muốn thành công, bạn nên tìm ra những con đường mới, thay vì đi trên những con đường mòn của sự thành công được chấp nhận’ - John D. Rockefeller', '‘Nếu bạn không thích cái gì đó, hãy thay đổi nó. Nếu bạn không thể thay đổi nó, hãy thay đổi thái độ của bạn’ - Maya Angelou']
    result_sentence = random.choice(sentence)
    await ctx.send(result_sentence)
@bot.command()
async def thayboi(ctx):
    random_card = ['con bốc được lá ♥️, Cơ là nước bài màu đỏ, được thể hiện bằng hình vẽ tim sẽ cho bạn những dự đoán trong chuyện tình cảm, hôn nhân vợ chồng, gia đình nói chung… Vận lá bài nước Cơ hên hay xui, may hay rủi còn phụ thuộc vào những con số của chúng.', 'con bốc được lá ♦️, là nước bài nổi bật với hình vẽ tượng trưng tựa như hình thoi dựng đứng, con Rô là dự báo tốt về đường công danh, sự nghiệp vững vàng, sự sung túc về tiền bạc.', 'con bốc được lá ♣️. Trong hình tượng như cái cây mang màu đen, nước Chuồn mang theo sự tốt lành về nhân duyên, tiền bạc, sự nghiệp, cuộc sống… Tóm lại, nước Chuồn báo hiệu sự viên mãn của đời người. Vì vậy nên trong ngôn ngữ của bói bài, người ta hay nói: “Có Chuồn là có tiền"', 'con bốc được lá ♠️. Đây có lẽ là nước bài không được trông chờ nhất trong các quân bài Tây vì ý nghĩa của nó mang lại thật sự không tốt. Người có quân bài nước này thường gặp những vướng mắc và khó khăn khó giải quyết ở nhiều phương diện.\nCon người: hay ốm đau, bệnh vặt, phải vươn lên trong vất vả.\nSự nghiệp công danh: khó thăng tiến, luôn gặp trắc trở, vật cản…\nTình duyên: lận đận, gãy gánh, chia cắt…']
    result =  random.choice(random_card)
    await ctx.send(result)
@bot.group(invoke_without_command=True)
async def truyentranh(ctx):
    await ctx.send('đọc, tìm, xem các truyện mới ra trên truyentranh24.com và toptruyen\nsử dụng: /truyentranh search <keyword> (tìm kiếm truyện)\ntruyentranh news (các truyện mới nhất truyên toptruyen)')
@truyentranh.command()
async def search(ctx, *, arg = None):
    if arg == None:
        await ctx.send('phần tìm kiếm truyện không được để trống')
    else:
        full_url_search = 'https://goatbot.tk/truyentranh24/search?q=' + str(arg) + '&apikey=ntkhang'
        get_search = requests.get(full_url_search)
        json = get_search.json()
        name = json['data'][0]['name']
        img = json['data'][0]['thumbnail']
        get_img = requests.get(img)
        file = open("truyentranh.png", "wb")
        file.write(get_img.content)
        file.close()
        href = json['data'][0]['href']  
        result = str(name) + '\n' + 'href: ' + str(href)
        await ctx.send(result, file = discord.File('truyentranh.png'))
@truyentranh.command()
async def news(ctx):
    try:
        full_url = 'https://thieutrungkien.up.railway.app/toptruyen/'
        get = requests.get(full_url)
        data_txt = get.text
        data_json = json.loads(data_txt)
        truyen1_name = data_json['data'][0]['name']
        truyen1_link = data_json['data'][0]['url']
        truyen2_name = data_json['data'][1]['name']
        truyen2_link = data_json['data'][1]['url']
        truyen3_name = data_json['data'][2]['name']
        truyen3_link = data_json['data'][2]['url']
        truyen4_name = data_json['data'][3]['name']
        truyen4_link = data_json['data'][3]['url']
        truyen5_name = data_json['data'][4]['name']
        truyen5_link = data_json['data'][4]['url']
        truyen1_image = data_json['data'][0]['images']
        get_img = requests.get(truyen1_image)
        file = open("truyentranh.png", "wb")
        file.write(get_img.content)
        file.close()
        await ctx.send(f'top 5 các truyện mới nhất trên toptruyen.net\n\n**{truyen1_name}**\nlink: {truyen1_link}\n\n**{truyen2_name}**\nlink: {truyen2_link}\n\n**{truyen3_name}\nlink: {truyen3_link}**\n\n**{truyen4_name}**\nlink: {truyen4_link}\n\n**{truyen5_name}**\nlink: {truyen5_link}',file = discord.File('truyentranh.png'))
    except Exception as e:
        print(e)
        await ctx.send('error')
@bot.command()
async def shopmaihuong(ctx):
    try:
        send = await ctx.send('reply tin nhắn này và nhập tin nhắn để tạo ảnh theo mẫu sau:\ntext1 | text2')
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for('message', check=check)
        value = message.content.lower().split(" | ")
        text1 = str(value[0])
        text2 = str(value[1])
        url = 'https://api.phamvandien.xyz/shopmaihuong?text1=' + text1 + "&text2=" + text2
        get = requests.get(url)
        file = open("shopmaihuong.png", "wb")
        file.write(get.content)
        file.close()
        await ctx.send('ảnh của bạn đây:)', file = discord.File('shopmaihuong.png'))
    except:
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def wiki(ctx, *, arg = None):
    if arg == None:
        await ctx.send('/wiki <keyword>\nphần tìm kiếm không được để trống')
    else:
        wikipedia.set_lang("vi")
        result = wikipedia.summary(f"{arg}", sentences=5)
        await ctx.send(result)
@bot.command()
async def callad(ctx, *, arg=None):
    if arg == None:
        await ctx.send(f"Bạn chưa nhập thông tin muốn báo cáo về admin\n{get_prefix()[str(ctx.message.guild.id)]['prefix']}callad <báo cáo>")
    else:
        user = await bot.fetch_user("716146182849560598")
        await user.send(f"báo cáo từ: {ctx.message.author}\nid: {ctx.message.author.id}\ntừ nhóm: {ctx.channel.id}\nnội dung: {arg}")
        await ctx.send('đã báo cáo về admin thành công')
@bot.command()
async def sendnoti(ctx):
    send = await ctx.send('reply tin nhắn này và nhập theo mẫu sau:\n<id channel> | phản hồi user | phản hồi channel | <id user>')
    def check(m):
        return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
    message = await bot.wait_for('message', check=check)
    value = message.content.lower().split(" | ")
    id_channel = str(value[0])
    reply_user = str(value[1])
    reply_channel = str(value[2])
    id_user = str(value[3])
    channel = await bot.fetch_channel(id_channel)
    user = await bot.fetch_user(f"{id_user}")
    await user.send(f'cảm ơn bạn về đóng góp, sau đây là phản hồi của admin:\n{reply_user}')
    await channel.send(f'phản hồi từ admin đến kênh:\nnội dung: {reply_channel}')
@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    member_data[str(ctx.message.author.id)]['Wallet'] += 100
    save_member_data(member_data)
    await ctx.send('nhận thưởng online thành công 100$')
@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã nhận thưởng ngày hôm nay rồi hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def slot(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if arg == None:
        await ctx.send('Bạn chưa nhập số tiền muốn cược')
    elif 10 > int(arg):
        await ctx.send('tiền cược không được để trống và phải từ 10$ trở lên')
    elif member_data[str(ctx.message.author.id)]['Wallet'] < int(arg):
        await ctx.send('bạn không có đủ số tiền để chơi')
    else:
        try:
            random_icon = ['🥑', '🍐', '🥭', '🍎', '🥝', '🍇']
            result = []
            for i in range(3):
                random_result = random.choice(random_icon)
                result.append(random_result)
            if result[0] == result[1] or result[0] == result[2] or result[1] == result[0] or result[1] == result[2] or result[2] == result[0] or result[2] == result[1] or result[1] == result[2] == result[0]:
                await ctx.send(f'Kết quả\n\n🕹️{result[0]} | {result[1]} | {result[2]}🕹️\n\nBạn đã thắng!')
                await update(ctx.message.author.id, arg, 'keobuabao_win')
            else:
                await ctx.send(f'Kết quả\n\n🕹️{result[0]} | {result[1]} | {result[2]}🕹️\n\nBạn thua rồi!:(')
                await update(ctx.message.author.id, arg, 'keobuabao_lose')
        except Exception as e:
            print(e)
            await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def news(ctx):
    get = requests.get('https://vnexpress.net/')
    soup = BeautifulSoup( get.content , 'html.parser')
    results = []
    dess = []
    for result in soup.find_all(class_ = 'title-news'):
        results.append(result.text)
        results.append(result.a.get('href'))
    for des in soup.find_all(class_ = 'description'):
        dess.append(des.text)
    title = results[0]
    link = results[1]
    des = dess[1]
    await ctx.send(f'tin mới nhất hôm nay: {title}{des}\nlink: {link}')
@bot.command()
async def dovui(ctx):
    try:
        get = requests.get('https://www.nguyenmanh.name.vn/api/dovui2?apikey=KCL98tNB')
        data_txt = get.text
        data_json = json.loads(data_txt)
        question = data_json['result']['question']
        option = data_json['result']['option']
        result = data_json['result']['correct']
        if len(option) == 3:
            option1 = data_json['result']['option'][0]
            option2 = data_json['result']['option'][1]
            option3 = data_json['result']['option'][2]
            send = await ctx.send(f'{question}\n1. {option1}\n2. {option2}\n3. {option3}\nReply tin nhắn này và trả lời theo số thứ tự các đáp')
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
            message = await bot.wait_for('message', check=check)
            if int(message.content.lower()) == result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
            elif int(message.content.lower()) != result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
        elif len(option) == 4:
            option1 = data_json['result']['option'][0]
            option2 = data_json['result']['option'][1]
            option3 = data_json['result']['option'][2]
            option4 = data_json['result']['option'][3]
            send = await ctx.send(f'{question}\n1. {option1}\n2. {option2}\n3. {option3}\n4. {option4}\nReply tin nhắn này và trả lời theo số thứ tự các đáp')
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
            message = await bot.wait_for('message', check=check)
            if int(message.content.lower()) == result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 4:
                    result = option4
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
            elif int(message.content.lower()) != result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 4:
                    result = option4
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
    except Exception as e:
        print(e)
        await ctx.send(f"lệnh bạn đang sử dụng đã xảy ra lỗi, hãy báo cáo về admin bằng lệnh {get_prefix()[str(ctx.message.guild.id)]['prefix']}callad, hoặc câu trả lời của bạn không phải là một con số")
@bot.command(name = "setmoney")
async def setmoney(ctx, arg = None, arg2 = None):
    if arg == None or arg2 == None or arg == None and arg2 == None:
        await ctx.send('sai cú pháp')
    elif ctx.message.author.id != 716146182849560598:
        await ctx.send('bạn không phải admin nên không có quyền sử dụng lệnh này')
    else:
        await update(ctx.message.author.id, arg, arg2)
        await ctx.send('done')
@bot.command(name = "google_search")
async def google_search(ctx, *, arg = None):
    url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={arg}"
    headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "VI",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    if arg == None:
        await ctx.send('phần tìm kiếm không được để trống')
    elif len(data['results']) != 0:
        url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={arg}"
        headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "VI",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)
        result1_des = data['results'][0]['description']
        result1_title = data['results'][0]['title']
        result1_link = data['results'][0]['link']
        await ctx.send(f'kết quả search google hàng đầu cho từ khóa "{arg}":\n{result1_title}\n-{result1_des}-\nlink: {result1_link}')
    else:
        await ctx.send('không có kết quả cho từ khóa bạn nhập')
@bot.command()
async def setprefix(ctx, arg = None):
    try:
        users = get_prefix()
        if arg == None:
            await ctx.send('nhập prefix cần dổi')
        else:
            users[str(ctx.message.guild.id)]['prefix'] = str(arg)
            with open(r"C:\codde\discord_bot\data.json", 'w') as f:
                json.dump(users, f)
            await ctx.send(f'đã thay prefix của sever thành {arg}')
    except Exception as e:
        print(e)   
@bot.command()
async def banner1(ctx):
    try:
        send = await ctx.send('reply tin nhắn này, để tạo ảnh banner, nhập theo mẫu sau:\n<text1> | <text2> | <id>')
        def check(m):
            if m.reference is not None:
                if m.reference.message_id == send.id and m.author.id == ctx.author.id:
                    return True 
        message = await bot.wait_for('message', check = check)
        value = message.content.split(" | ")
        name = value[0]
        sub_name = value[1]
        id_character = value[2]
        url = f"https://www.nguyenmanh.name.vn/api/fbcover2?name={name}&id={id_character}&subname={sub_name}&apikey=KCL98tNB"
        get = requests.get(url)
        if get.status_code == 200:
            file = open("banner1.png", "wb")
            file.write(get.content)
            file.close()
            await ctx.send('ảnh đây:)', file = discord.File('banner1.png'))
        else:
            await ctx.send('lệnh bạn sử dụng hiện đang bị lỗi, hãy báo cóa lên admin để được sửa sớm nhất')
    except Exception as e:
        print(e)
        await ctx.send('lỗi')
@bot.command()
async def videofb(ctx, url = None):
    try:
        if url == None:
            await ctx.send("Bạn chưa nhập link video facebook cần tải xuống") 
        else:
            await ctx.send("đang tải video, vui lòng đợi...")
            link = f"https://www.nguyenmanh.name.vn/api/fbDL?url={url}&apikey=KCL98tNB"
            get = requests.get(link)
            data = json.loads(get.text)
            urllib.request.urlretrieve(data['result']['hd'], 'fb_download.mp4') 
            await ctx.reply('video của bạn đây', file = discord.File('fb_download.mp4'))
    except Exception as e:
        print(e)
        await ctx.reply('lệnh bạn đang sử dụng đã xảy ra lỗi, vui lòng thử lại sau')
@bot.command()
async def severs(ctx):
    if (int(ctx.message.author.id) == 716146182849560598):
        await ctx.send(bot.guilds)
    else:
        await ctx.send('bạn không đủ quyền hạn để thực hiện lệnh này')
@bot.command()
async def channel(ctx):
  for server in bot.guilds:
    print(server.text_channels)
@bot.command(pass_context=True)
async def sendnoti2(ctx, *, msg):
    for server in bot.guilds:
        for channel in server.text_channels:
            try:
                await channel.send(msg)
            except Exception as e:
                print(e)
                continue
            else:
                break
@bot.command()
async def baicao(ctx, arg = None, arg2 = None):
    try:
        def atoi(text):
            return int(text) if text.isdigit() else text
        def natural_keys(text):
            return [ atoi(c) for c in re.split(r'(\d)', text) ]
        def read():
            with open(r"C:\codde\discord_bot\data.json", 'r') as f:
                users = json.load(f)
                return users
        def save(data):
            with open(r"C:\codde\discord_bot\data.json", 'w') as f:
                json.dump(data, f)
        await open_account(ctx.message.author.id)
        money_data = await get_bank_data()
        users = read()
        list_player_result_id = []
        list_player_result = []
        message = "-----Kết quả-----\n"
        prefix = users[str(ctx.message.guild.id)]['prefix']
        if arg == None:
            await ctx.send(f'game bài cào nhiều người chơi\n{prefix}baicao [create/start/join/leave]')
        elif arg == 'create':
            if arg2 == None or int(arg2) < 50:
                await ctx.send(f'bạn chưa nhập số tiền muốn cược cho bàn chơi hoặc số tiền bạn muốn cược nhỏ hơn 50$')
            elif int(arg2) > money_data[str(ctx.message.author.id)]['Wallet']:
                await ctx.send(f'bạn không đủ số tiền để chơi')
            elif 'baicao' in users[str(ctx.message.guild.id)]:
                await ctx.send(f'đã có một bàn bài cào được tạo trước đó, không thể tạo thêm')
            else:               
                users[str(ctx.message.guild.id)]['baicao'] = {}
                users[str(ctx.message.guild.id)]['baicao']['baicao_create'] = True
                users[str(ctx.message.guild.id)]['baicao']['player'] = [str(ctx.message.author.id)]
                users[str(ctx.message.guild.id)]['baicao']['player_name'] = [str(ctx.message.author)]
                users[str(ctx.message.guild.id)]['baicao']['author'] = str(ctx.message.author.id)
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)] = {}
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)]['change'] = 2
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)]['result'] = None
                users[str(ctx.message.guild.id)]['baicao']['bet'] = int(arg2)
                save(users)
                await ctx.send(f'Đã tạo bàn bài cào thành công\nHãy nhập {prefix}baicao join để tham gia bàn chơi (người tạo không cần nhập)')
        elif arg == 'join':
            if 'baicao' not in users[str(ctx.message.guild.id)]:
                await ctx.send('chưa tạo bàn bài cào để tham gia bàn chơi')
            elif len(users[str(ctx.message.guild.id)]['baicao']['player']) == 4:
                await ctx.send('số người chơi tối đa là 4 người')
            elif str(ctx.message.author.id) in users[str(ctx.message.guild.id)]['baicao']['player'] or str(ctx.message.author.id) in users[str(ctx.message.guild.id)]['baicao']['player_name']:
                await ctx.send('bạn đã tham gia bàn choi, không thể tham gia lại')
            elif users[str(ctx.message.guild.id)]['baicao']['bet'] > money_data[str(ctx.message.author.id)]['Wallet']:
                await ctx.send(f'bạn không đủ số tiền để chơi')
            else:
                users[str(ctx.message.guild.id)]['baicao']['player'].append(str(ctx.message.author.id))
                users[str(ctx.message.guild.id)]['baicao']['player_name'].append(str(ctx.message.author))
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)] = {}
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)]['change'] = 2
                users[str(ctx.message.guild.id)]['baicao'][str(ctx.message.author)]['result'] = None
                save(users)
                await ctx.send("đã tham gia bàn chơi")
        elif arg == 'leave':
                if str(ctx.message.author.id) != users[str(ctx.message.guild.id)]['baicao']['author']:
                   users[str(ctx.message.guild.id)]['baicao']['player'].remove(str(ctx.message.author.id))
                   users[str(ctx.message.guild.id)]['baicao']['player_name'].remove(str(ctx.message.author))
                   save(users)
                   await ctx.send(f'{ctx.message.author.name} đã rời bàn chơi')
                else:
                    del users[str(ctx.message.guild.id)]['baicao']
                    save(users)
                    await ctx.send('chủ bàn đã hủy bàn chơi, hãy tạo một bàn chơi khác để tiếp tục')
        elif arg == 'start': 
            if 'baicao' not in users[str(ctx.message.guild.id)]: 
                await ctx.send('chưa tạo bàn bài cào để bắt đầu')
            elif len(users[str(ctx.message.guild.id)]['baicao']['player']) < 2: 
                await ctx.send('cần ít nhất 2 người trong bàn chơi để bắt đầu')
            else:   
                for i in range(len(users[str(ctx.message.guild.id)]['baicao']['player'])):
                    card1 = random.randint(1, 9)
                    card2 = random.randint(1, 9)
                    card3 = random.randint(1, 9)
                    result = card1 + card2 + card3
                    if result >= 10:
                        result -= 10
                    if result >= 10:
                        result -= 10
                    user = await bot.fetch_user(str(users[str(ctx.message.guild.id)]['baicao']['player'][i - 1]))
                    await update(str(user.id), users[str(ctx.message.guild.id)]['baicao']['bet'], 'keobuabao_lose')
                    list_player_result.append(f"{result} {user.name}")
                    list_player_result_id.append(f"{result} {user.id}")
                    await user.send(f"bài của bạn: {card1} | {card2} | {card3}\ntổng bài: {result}")
                    list_player_result.sort(key = natural_keys, reverse=True)
                    list_player_result_id.sort(key = natural_keys, reverse=True)
                    print(list_player_result)
                    if int(len(list_player_result)) == 2:
                        result = list_player_result[0].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[0] = result2
                        result = list_player_result[1].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[1] = result2
                    elif int(len(list_player_result)) == 3:
                        result = list_player_result[0].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[0] = result2
                        result = list_player_result[1].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[1] = result2
                        result = list_player_result[2].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[2] = result2
                        print(list_player_result)
                    elif int(len(list_player_result)) == 4:
                        result = list_player_result[0].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[0] = result2
                        result = list_player_result[1].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[1] = result2
                        result = list_player_result[2].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[2] = result2
                        result = list_player_result[3].split(" ", 1)
                        print(result)
                        result2 = result[1] + ": " + result[0]
                        list_player_result[3] = result2
                rank = 1
                player_win_id = list_player_result_id[0].split(" ", 1)[1]
                player_win_info = await bot.fetch_user(str(player_win_id))
                player_win_name = player_win_info.name
                win_bet = int(users[str(ctx.message.guild.id)]['baicao']['bet']) * int(len(users[str(ctx.message.guild.id)]['baicao']['player']))
                users[str(ctx.message.guild.id)]['baicao']['baicao_start'] = True
                save(users)
                await ctx.send(f'đã chia bài thành công, bot sẽ thông báo kết quả sau 45 giây nữa')
                await asyncio.sleep(45)
                for k in list_player_result:
                    message = message + f"{rank}. {k}\n"
                    rank += 1
                message = message + f"\n{player_win_name} là người chiến thắng và gom về {win_bet}$ tiền cược"
                await update(player_win_id, int(win_bet), 'keobuabao_win')
                await ctx.send(message)
    except Exception as e:
        print(e)
@bot.command()
async def rob(ctx):
    try:
        global random1
        await open_account(ctx.message.author.id)
        guild = bot.get_guild(ctx.message.guild.id)
        random1 = random.choice(guild.members)
        while int(random1.id) == int(ctx.message.author.id):
            random1 = random.choice(guild.members)
        await open_account(random1.id)
        member_data = await get_bank_data()
        if int(member_data[str(random1.id)]['Wallet']) <= 100:
            await ctx.send(f'bạn đã cướp tiền của {random1.name}, là một người nghèo nên không kiếm được gì cả')
        else:
            random_chance = random.randrange(0, 100)
            if random_chance <= 15:
                rob_money = random.randint(0, round(int(member_data[str(random1.id)]['Wallet']) * 90/100))
                await update(str(ctx.message.author.id), int(rob_money), 'keobuabao_win')
                await update(str(random1.id), int(rob_money), 'keobuabao_lose')
                await ctx.send(f'bạn đã cướp thành công của {random1.name} {rob_money}$')
            else:
                rob_failed = random.randrange(300, 3000)
                await update(str(ctx.message.author.id), int(rob_failed), 'keobuabao_lose')
                await update(str(random1.id), int(rob_failed)/2, 'keobuabao_win')
                await ctx.send(f'bạn cướp tiền của {random1.name}, nhưng thất bại và mất {rob_failed}$ tiền viện phí vì bị đánh:). {random1.name} bạn nhận được {rob_failed/2} tiền đền bù')
    except Exception as e:
        print(e)
@bot.command()
async def mail10p(ctx, arg = None):
    try:
        await open_account(ctx.message.author.id)
        member_data = await get_bank_data()
        if arg == None:
            await ctx.send('error: no argument!')
        elif arg == 'create':
            if "email" in member_data[str(ctx.message.author.id)]:
                await ctx.send(f"bạn đã tạo một tài khoản trước đó rồi, không thể tạo thêm. Sử Dụng {member_data[str(ctx.message.guild.id)]['prefix']}mail10p load_account")
            else:
                await ctx.send('đang tạo tài khoản vui lòng đợi,...')
                p = pymailtm.MailTm()
                password = p._generate_password(8)
                domain = str(random.choice(p._get_domains_list()))
                create = p._make_account_request("accounts",p._generate_password(12).lower() + '@' + domain, password)
                print(create)
                address = create["address"]
                _id = create["id"]
                member_data[str(ctx.message.author.id)]['email'] = {}
                member_data[str(ctx.message.author.id)]['email']["address"] = str(address)
                member_data[str(ctx.message.author.id)]['email']['password'] = str(password)
                member_data[str(ctx.message.author.id)]['email']['id'] = str(_id)
                save_member_data(member_data) 
                await ctx.reply(f"Tạo tài khoản thành công\nEmail: {address}\npassword: {password}\nid: {_id}")
        elif arg == 'message':
            if "email" not in member_data[str(ctx.message.author.id)]:
                await ctx.send(f"bạn chưa tạo tài khoản email để xem tin nhắn gửi đến, sử dụng: {member_data[str(ctx.message.guild.id)]['prefix']}mail10p create để tạo tài khoản")
            else:
                p = pymailtm.MailTm()
                await ctx.send("đang thu thập các mail gửi đến...")
                path = member_data[str(ctx.message.author.id)]['email']
                x = pymailtm.Account(path['id'], path["address"], path["password"])
                r = requests.get("{}/messages?page={}".format(p.api_address, "1"),
                         headers=x.auth_headers)
                user = await bot.fetch_user(ctx.message.author.id)
                await user.send(f"Đã nhận được {len(r.json()['hydra:member'])} mail gửi đến tài khoản")
                message = {}
                num_email = 1
                for i in r.json()['hydra:member']:
                    get = requests.get(f"{p.api_address}/messages/{i['id']}", headers=x.auth_headers)
                    data = json.loads(get.text)
                    message['from'] = data['from']['address']
                    for k in data['to']:
                        message['to'] = []
                        message['to'].append(k['address'])
                    message['subject'] = data['subject']
                    message['body'] = data['text']
                    if data['hasAttachments'] == True:
                        num_attachments = []
                        backslash = r'\"'
                        for i in data['attachments']:
                            link = []
                            link.append(str(p.api_address) + str(i['downloadUrl']).strip(backslash))
                        message_send = f"email thứ {num_email}:\nGửi từ: {str(message['from'])}\nGửi đến: {str(message['to']).replace('[', '').replace(']', '')}\nTiêu đề: {str(message['subject'])}\nNội dung: {str(message['body'])}\nTệp đính kèm trong mail\n"
                        for ls in link:
                            message_send += f"{ls}\n"
                        await user.send(f"{message_send}")
                    else:
                        await user.send(f"email thứ {num_email}:\nGửi từ: {str(message['from'])}\nGửi đến: {str(message['to']).replace('[', '').replace(']', '')}\nTiêu đề: {str(message['subject'])}\nNội dung: {str(message['body'])}")
                    num_email += 1
    except Exception as e:
        print(e)
        await ctx.send(f"đã xảy ra lỗi: {e}\nVui lòng thử lại sau")
@bot.command()
async def test(ctx):
    var = await ctx.send('message')
    await var.edit(content="message edited")
#Functions
async def open_account(user):
    users = await get_bank_data()
    if str(user) in users:
        return False
    else:
        users[str(user)] = {}
        users[str(user)]["Wallet"] = 0
        users[str(user)]["Bank"] = 0
        users[str(user)]["pc"] = 0

    with open("data.json", 'w') as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("data.json", 'r') as f:
        users = json.load(f)
    return users
async def update(user, change, mode):
    await open_account(user)
    member_data = await get_bank_data()
    if mode == 'wallet':
        member_data[str(user)]['Wallet'] -= int(change)
        member_data[str(user)]['Bank'] += int(change)
        save_member_data(member_data)
    elif mode == 'bank':
        member_data[str(user)]['Wallet'] += int(change)
        member_data[str(user)]['Bank'] -= int(change)
        save_member_data(member_data)
    elif mode == 'keobuabao_win':
        member_data[str(user)]['Wallet'] += int(change)
        save_member_data(member_data)
    elif mode == 'keobuabao_lose':
        member_data[str(user)]['Wallet'] -= int(change)
        save_member_data(member_data)
    elif mode == 'receive_user':
        member_data[str(user)]['Bank'] += int(change)
        save_member_data(member_data)
    elif mode == 'send_user':
        member_data[str(user)]['Bank'] -= int(change)
        save_member_data(member_data)
    elif mode == 'setmoney-wallet':
        member_data[str(user)]['Wallet'] = int(change)
        save_member_data(member_data)
    elif mode == 'setmoney-bank':
        member_data[str(user)]['Bank'] = int(change)
        save_member_data(member_data)
    else:
        print('error')
def save_member_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)
bot.run('')
#credit: Duc Anh
