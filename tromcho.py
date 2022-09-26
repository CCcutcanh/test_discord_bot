import discord
from discord.ext import commands
import easy_pil
import aiofiles
import aiohttp
class Tromcho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
     print('module tromcho loaded')
    @commands.command()
    async def tromcho(self, ctx, arg: discord.User = None):
        if arg == None:
            await ctx.send('error')
            return
        try:
            image = await easy_pil.load_image_async(ctx.message.author.display_avatar.url)
            image2 = await easy_pil.load_image_async(arg.display_avatar.url)
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://i.ibb.co/bgz3FYt/trom-cho-bi-xu-phat-the-nao-1811142901.jpg') as resp:
                    f = await aiofiles.open('paste.jpg', mode='wb')
                    await f.write(await resp.read())
                    await f.close()
            back = easy_pil.Editor('paste.jpg')
            paste = easy_pil.Editor(image).circle_image()
            paste2 = easy_pil.Editor(image2).circle_image()
            paste2.resize((42, 42))
            paste.resize((40, 40))
            back.paste(paste, (279, 35))
            back.paste(paste2, (210, 200))
            await ctx.send(f't xich m lai bh:smiling_imp: :smiling_imp:{arg.mention}', file = discord.File(back.image_bytes, filename='circle.png'))
        except Exception as e:
            print(e)
            await ctx.send('error')
async def setup(bot):
    await bot.add_cog(Tromcho(bot))
