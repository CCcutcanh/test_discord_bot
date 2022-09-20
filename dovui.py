@bot.command()
async def dovui(ctx):
    try:
        get = requests.get('https://api.phamvandien.xyz/game/dovui')
        data_txt = get.text
        data_json = json.loads(data_txt)
        data = {}
        question = data_json['data']['question']
        option = data_json['data']['option']
        correct = data_json['data']['correct'] 
        msg = f'đây là câu hỏi của bạn: {question}'
        stt = 1
        for i in option:
            msg += f'\n{stt}.{i}'
            data[str(stt)] = i
            stt += 1
        msg += '\nreply tin nhắn theo số thứ tự các đáp án để trả lời'
        send = await ctx.send(msg)
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel and m.reference is not None and m.reference.message_id == send.id
        message = await bot.wait_for('message', check=check)
        try:
            if data[str(message.content)] == correct:
                await ctx.send(f'bạn đã trả lời đúng, đáp án là {correct}')
            else:
                await ctx.send(f'sai rồi, đáp án là {correct}')
        except Exception as e:
            print(e)
            await ctx.send(f'chỉ được trả lời theo số thứ tự các đáp án')
    except Exception as e:
        print(e)
        await ctx.send(f"lệnh bạn đang sử dụng đã xảy ra lỗi, hãy báo cáo về admin bằng lệnh {get_prefix()[str(ctx.message.guild.id)]['prefix']}callad, hoặc câu trả lời của bạn không phải là một con số")
