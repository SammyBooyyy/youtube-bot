#dar import as modules
from discord.ext import commands
import discord, time, os, json

#dar load token
with open('config.json') as c:
    config = json.load(c)
    token = config['TOKEN']


def main():
    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix="!", intents=intents)

    #diz quando o bot está totalmente pronto
    @client.event
    async def on_ready():
        os.system('cls')
        print('Bot iniciado com sucesso!!!')

    #comando ping
    @client.command()
    async def ping(ctx):
        embed = discord.Embed(title='Comando PING', description='Da return a Pong', color=discord.Color.dark_purple())
        embed.add_field(name='Ping', value='Pong')
        await ctx.send(embed=embed)

    #entradas
    @client.event
    async def on_member_join(member):
        canal_entradas = client.get_channel(869401787583586385)
        embed = discord.Embed(title='Bem vindo!', description=f'Espero que te divirtas no servidor {member.name}', color=discord.Color.dark_gold())
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_image(url='https://media.tenor.com/images/45d415851009f2150902f525d58f166f/tenor.gif')
        embed.add_field(name='Não te esqueças de ler as regras', value='Vai a sala <#869407266938441788> para ler as regras', inline=False)
        embed.add_field(name='Não te esqueças de te verificares', value='Vai a sala <#869407287469559838> para te verificares', inline=False)
        embed.set_footer(text='Coded by Fukk!!CodeREd', icon_url=' https://cdn.discordapp.com/avatars/270241940681785344/a_230db72df85974a7871224bb2bbbdab8.png?size=128')
        await canal_entradas.send(embed=embed)

    client.run(token)

if __name__ == '__main__':
    main()

