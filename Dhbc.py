@bot.command()
async def dhbc(ctx):
    api = ['https://api.phamvandien.xyz/game/dhbcv1', 'https://www.nguyenmanh.name.vn/api/dhbc1?apikey=KCL98tNB', 'https://docs-api.nguyenhaidang.ml/game/dhbc']
    get = random.choice(api)
    question = json.loads(requests.get(get).text)
    if get == api[0]:
        file = open('DHBC.png', 'wb')
        file.write(requests.get(question['dataGame']['link']).content)
        file.close()
        send = await ctx.send('==== Đuổi Hình Bắt Chữ====\nđây là câu hỏi của bạn:\nreply tin nhắn này để trả lời câu hỏi và reply "gợi ý" để lấy gợi ý câu trả lời (50$/lần)', file = discord.File('DHBC.png'))
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for(event='message', check = check, timeout=45)
        if str(message.content).lower() == "gợi ý":
            await open_account(ctx.message.author.id)
            data = await get_bank_data()
            if data[str(ctx.message.author.id)]['Wallet'] < 50:
                await ctx.send('bạn không đủ 50$ trong ví để xem gợi ý')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['dataGame']['tukhoa']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["dataGame"]["tukhoa"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['dataGame']['tukhoa']}")
            else:
                data[str(ctx.message.author.id)]['Wallet'] -= 50
                save_member_data(data)
                await ctx.send(f'gợi ý, từ này là: {question["dataGame"]["suggestions"]}')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['dataGame']['tukhoa']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["dataGame"]["tukhoa"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['dataGame']['tukhoa']}")
        else:
            if str(message.content).lower() == question['dataGame']['tukhoa']:
                await ctx.send(f"Bạn đã trả lời đúng, đáp án là {question['dataGame']['tukhoa']}")
            else:
                await ctx.send(f"sai rồi:(, đáp án đúng là: {question['dataGame']['tukhoa']}")
    if get == api[1]:
        file = open('DHBC.png', 'wb')
        file.write(requests.get(question['result']['link']).content)
        file.close()
        send = await ctx.send('==== Đuổi Hình Bắt Chữ====\nđây là câu hỏi của bạn:\nreply tin nhắn này để trả lời câu hỏi và reply "gợi ý" để lấy gợi ý câu trả lời (50$/lần)', file = discord.File('DHBC.png'))
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for(event='message', check = check, timeout=45)
        if str(message.content).lower() == "gợi ý":
            await open_account(ctx.message.author.id)
            data = await get_bank_data()
            if data[str(ctx.message.author.id)]['Wallet'] < 50:
                await ctx.send('bạn không đủ 50$ trong ví để xem gợi ý')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['result']['tukhoa']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["result"]["tukhoa"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['result']['tukhoa']}")
            else:
                data[str(ctx.message.author.id)]['Wallet'] -= 50
                save_member_data(data)
                await ctx.send(f'gợi ý, từ này là: {question["result"]["suggestions"]}')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['result']['tukhoa']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["result"]["tukhoa"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['result']['tukhoa']}")
        else:
            if str(message.content).lower() == question['result']['tukhoa']:
                await ctx.send(f"Bạn đã trả lời đúng, đáp án là {question['result']['tukhoa']}")
            else:
                await ctx.send(f"sai rồi:(, đáp án đúng là: {question['result']['tukhoa']}")
    if get == api[2]:
        file = open('DHBC.png', 'wb')
        file.write(requests.get(question['image1and2']).content)
        file.close()
        send = await ctx.send('==== Đuổi Hình Bắt Chữ====\nđây là câu hỏi của bạn:\nreply tin nhắn này để trả lời câu hỏi và reply "gợi ý" để lấy gợi ý câu trả lời (50$/lần)', file = discord.File('DHBC.png'))
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for(event='message', check = check, timeout=45)
        if str(message.content).lower() == "gợi ý":
            await open_account(ctx.message.author.id)
            data = await get_bank_data()
            if data[str(ctx.message.author.id)]['Wallet'] < 50:
                await ctx.send('bạn không đủ 50$ trong ví để xem gợi ý')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['wordcomplete']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["result"]["wordcomplete"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['wordcomplete']}")
            else:
                data[str(ctx.message.author.id)]['Wallet'] -= 50
                save_member_data(data)
                await ctx.send(f'gợi ý, từ này là: {question["suggestions"]}')
                message = await bot.wait_for(event='message', check = check, timeout=45)
                if str(message.content) == question['result']['tukhoa']:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: "{question["result"]["tukhoa"]}"')
                else:
                    await ctx.send(f"sai rồi:(, đáp án đúng là: {question['result']['tukhoa']}")
        else:
            if str(message.content).lower() == question['wordcomplete']:
                await ctx.send(f"Bạn đã trả lời đúng, đáp án là {question['wordcomplete']}")
            else:
                await ctx.send(f"sai rồi:(, đáp án đúng là: {question['wordcomplete']}")
