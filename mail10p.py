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
                    user = await bot.fetch_user(ctx.message.author.id)
                    await user.send(f"Tạo tài khoản thành công\nEmail: {address}\npassword: {password}\nid: {_id}")
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
                                get_attachment = requests.get(str(p.api_address) + str(i['downloadUrl']).strip(backslash), headers = x.auth_headers)
                                file = open("mail10p.png", "wb")
                                file.write(get_attachment.content)
                                file.close()
                                with open("mail10p.png", "rb") as file:
                                    link = []
                                    url = "https://api.imgbb.com/1/upload"
                                    payload = { "key": "a631a9c1fceb926d62f8108aa6580e2a", "image": base64.b64encode(file.read()), }
                                    up_image = requests.post(url, payload).json()
                                    link.append(up_image["data"]["image"]["url"])
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
