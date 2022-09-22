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
