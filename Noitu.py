@bot.command()
async def noitu(ctx, arg = None):
    data = await get_bank_data()
    prefix = data[str(ctx.message.guild.id)]['prefix']
    if arg == None:
        await ctx.send(f"sử dụng: {prefix} <bot/channel>\nsử dụng: {prefix}noitu bot (chơi nối từ với máy) và {prefix}noitu channel (lập kênh của ng dùng lệnh làm kênh chơi nối từ)")
    elif arg == 'bot':
        await ctx.send('đã bắt đầu, hãy mở đầu trò chơi với một từ đầu tiên. Nhắn quit để dừng chơi')
        while True:
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            url_noitu = 'https://api.phamvandien.xyz/game/linkword?word='
            full_url_noitu = url_noitu + str(message.content).lower()
            get_noitu = requests.get(full_url_noitu)
            data_noitu = get_noitu.text
            json_noitu = json.loads(data_noitu)
            word_noitu = json_noitu['data']
            if word_noitu == False:
                await ctx.send('bạn thắng rồi:((')
                break
            if message.content == "quit":
                await ctx.send('đã dừng trò chơi')
                break
            else:
                await ctx.send(word_noitu)
    elif arg == 'channel':
        data[str(ctx.message.guild.id)]['noitu'] = {}
        data[str(ctx.message.guild.id)]['noitu']['word'] = []
        data[str(ctx.message.guild.id)]['noitu']['channel'] = str(ctx.message.channel.id)
        await save_member_data(data)
        await ctx.send(f"đã bắt đầu trò chơi hãy bắt đầu bằng một từ bất kì")
#xử lí tin nhắn trong kênh bật lệnh noitu
@bot.event
async def on_message(message):
    data = await get_bank_data()
    if 'noitu' in data[str(message.guild.id)]:
        success = True
        if str(message.channel.id) == data[str(message.guild.id)]['noitu']['channel'] and str(message.author.id) != str(bot.user.id):
            r = requests.get('https://raw.githubusercontent.com/undertheseanlp/dictionary/master/dictionaries/hongocduc/words.txt').text.split('\n')
            if len(str(message.content.lower()).split(' ')) == 2 and str(message.author.id) != str(bot.user.id):
                if message.content.lower() not in word:
                    await message.add_reaction("❎")
                    await message.channel.send(f'Từ `{message.content.lower()}` không tồn tại trong từ điển của bot')
                elif message.content.lower() in data[str(message.guild.id)]['noitu']['word']:
                    await message.channel.send(f'Từ `{message.content.lower()}` đã được nối từ trước đó')
                try:
                    if data[str(message.guild.id)]['noitu']['pre_word'] != str(message.content.lower()).split(' ')[0]:
                        await message.channel.send(f"từ của bạn phải bắt đầu bằng chữ `{data[str(message.guild.id)]['noitu']['pre_word']}`")
                        success = False
                    if data[str(message.guild.id)]['noitu']['pre_player'] == str(message.author.id):
                        await message.channel.send(f"Bạn đã nối trước đó hãy đợi người tiếp theo")
                        success = False
                except Exception as e:
                    data[str(message.guild.id)]['noitu']['pre_word'] = str(message.content.lower()).split(' ')[1]
                    data[str(message.guild.id)]['noitu']['pre_player'] = str(message.author.id)
                    save_member_data(data)
                    await message.add_reaction("✅")
                    print(e)
                    return
                else:
                    if success == True:
                        data[str(message.guild.id)]['noitu']['word'].append(str(message.content.lower()))
                        save_member_data(data)
                        await message.add_reaction("✅")
            else:
                await message.channel.send(f'Chỉ được nối từ có 2 chữ')
    await bot.process_commands(message)
#load từ điển Tiếng Việt
data["vn_dict"] = []
save_member_data(data)
try:
    for i in r:
        try:
            if len(json.loads(i)['text'].split(" ")) == 2:
                data["vn_dict"].append(str(json.loads(i)['text']))
                save_member_data(data)
        except:
            continue
except Exception as e:
    print(e)
