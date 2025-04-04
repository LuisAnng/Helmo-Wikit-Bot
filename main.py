import discord
from math import floor
from discord.ext import commands
from dotenv import load_dotenv
import os
import logs


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# Isso sincroniza os comandos
# Caso você tenha adicionado um novo comando, reinicie o bot e o discord para adicioná-lo ao aplicativo
# (não sei como isso realmente funciona, mas funcionou para mim kkkk).
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot {bot.user.name} ha iniciado sesión y comandos sincronizados.")


# isso exclui um comando que você mesmo adicionou.
#   bot.tree.remove_command("helpp")
#   Sincronize novamente para aplicar a alteração.
#   await bot.tree.sync()

##############################################################################################
# Se você quiser adicionar um novo comando, é fácil
# @bot.tree.command("nome de seu comando", description="uma descrição do que ele faz")
# async def test(interaction: discord.Interaction):
#   a lógica de seu comando
#
#
#    await interaction.response.send_message("o resultado do comando que você deseja enviar")
##############################################################################################


##############################################################################################
# Se quiser investigar mais, basta pesquisar discord.py (o que quer que você queira fazer)
# e você obterá algumas informações
##############################################################################################


@bot.tree.command(name="helpp", description="Mostrar todos os comandos do bot")
async def help_panel(interaction: discord.Interaction):
    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Comandos do bot")

    embed.add_field(name="/xp", value="Ex:/xp 578", inline=False)
    embed.add_field(
        name="/quest", value="Mostra as quests mais importantes do jogo", inline=False
    )
    embed.add_field(
        name="/boss", value="Mostra os avisos do bosses no jogo", inline=False
    )
    embed.add_field(
        name="/cgame", value="Mostra todos os comandos no jogo", inline=False
    )
    embed.add_field(
        name="/benefits",
        value="Mostra os benefícios do premmy e do patreon",
        inline=False,
    )
    embed.add_field(
        name="/inf",
        value="Mostra informações sobre o criador do bot e o repositório do bot no github",
    )

    img = discord.File("./assets/helmo.png", filename="helmo.png")
    embed.set_thumbnail(url="attachment://helmo.png")
    await interaction.response.send_message(file=img, embed=embed)


@bot.tree.command(name="inf", description="Informação sobre o criador do bot")
async def info_creator(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.dark_red(), title="Informações sobre o bot e o criador"
    )

    embed.add_field(name="Criador", value="Luis AV", inline=False)

    embed.add_field(
        name="Meu discord",
        value="""sleepingg01\n**Se você tiver alguma sugestão para adicionar ao bot ou se tiver encontrado algum erro envie-me uma mensagem**""",
        inline=False,
    )

    embed.add_field(
        name="Repositório do Github.",
        value="**com uma guia sobre como implantar o bot em seus próprios servidores\nhttps://github.com/LuisAnng/Helmo-Wikit-Bot**",
        inline=False,
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="xp",
    description="Veja o nível mínimo e máximo com o qual você divide a experiência",
)
async def share_experience(interaction: discord.Interaction, arg: int = None):
    embed = discord.Embed(
        colour=discord.Colour.dark_red(), title="**você pode compartilhar o xp com**"
    )

    try:
        if not arg or int(arg) == 0 or arg is None:
            await interaction.response.send_message(
                "Entrada incorreta, tente novamente"
            )
        else:
            lv_min = floor((int(arg) * 0.7))
            lv_max = floor(int(arg) / 0.7)
            embed.add_field(name="**lv mínimo.**", value=f"{lv_min}", inline=False)
            embed.add_field(name="**lv max.**", value=f"{lv_max}", inline=False)
            img = discord.File("./assets/xp_boost.png", filename="xp_boost.png")
            embed.set_thumbnail(url="attachment://xp_boost.png")
            await interaction.response.send_message(file=img, embed=embed)

    except ValueError:
        await interaction.response.send_message(
            ":x: Entrada incorreta, tente novamente :x:"
        )
    except commands.errors.MissingRequiredArgument:
        await interaction.response.send_message(":x: Digite seu nível :x:")


@bot.tree.command(name="boss", description="Todos os avisos de bosses no jogo")
async def boss_announcement(interaction: discord.Interaction):
    boss_announcement = logs.announcements
    emojis = logs.emojis
    fulldialog = ""
    for i, (boss, dialog) in enumerate(boss_announcement.items()):
        for line in dialog:
            e = emojis[i]
            fulldialog += f"{boss}{e}\n"
            fulldialog += f"{line}\n\n"
            alert = "\n:warning:Essa mensagem será deletada em 35 segundos para evitar spam:warning:\n "

    full_dialog_with_alert = f"{alert}{fulldialog.strip()}\n{alert}"
    await interaction.response.send_message(full_dialog_with_alert, delete_after=35)


@bot.tree.command(name="cgame", description="Mostrar comandos do jogo")
async def game_command(interaction: discord.Interaction):
    game_c = logs.c_house

    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Comandos no jogo")

    embed.add_field(
        name=f"{game_c[0]}", value="mostra todos os comandos da casa", inline=False
    )
    embed.add_field(
        name=f"{game_c[1]}",
        value="mostra todos os jogadores conectados no servidor",
        inline=False,
    )
    embed.add_field(
        name=f"{game_c[2]}", value="mostra todos os comandos da guild", inline=False
    )
    embed.add_field(
        name=f"{game_c[3]}",
        value="mostra o tempo restante para perder pk",
        inline=False,
    )
    embed.add_field(
        name=f"{game_c[4]}",
        value="mostra o número de jogadores que você matou e quando o frag expira.",
        inline=False,
    )

    img = discord.File("./assets/helmo.png", filename="helmo.png")
    embed.set_thumbnail(url="attachment://helmo.png")
    await interaction.response.send_message(file=img, embed=embed)


@bot.tree.command(
    name="quest",
    description="mostra links do Youtube com tutoriais para fazer as quests importantes no jogo",
)
async def quest(interaction: discord.Interaction):
    quests = logs.quests

    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Comandos no jogo")

    embed.add_field(
        name=f"{quests[0]}",
        value="https://youtu.be/qu6alt3wcQU?si=lkRli8QxBVFJ7s6I",
        inline=False,
    )
    embed.add_field(
        name=f"{quests[1]} + {quests[2]}",
        value="https://youtu.be/9DV3V-yvXlk?si=-9Qt3_3I7LNdQpQj&t=56",
        inline=False,
    )
    embed.add_field(
        name=f"{quests[3]}",
        value="https://youtu.be/DHiZHm8UKvk?si=KMAQDlv7MJPuseDu",
        inline=False,
    )
    embed.add_field(
        name=f"{quests[4]}",
        value="https://www.youtube.com/watch?v=YytYPDfBNuA",
        inline=False,
    )
    embed.add_field(
        name=f"{quests[5]}",
        value="**PARTE 1** https://youtu.be/Zmzi49bitVk?si=j9xIyz86n95wNhFf\n**PARTE 2** https://youtu.be/Y8zMRVEnJ0k?si=GWgdxm8SNnuB2_fu",
        inline=False,
    )
    embed.add_field(
        name=f"{quests[6]}",
        value="https://youtu.be/g3kwF-cRZvk?si=vwzyfOaS5qhPsqUd",
        inline=False,
    )
    img = discord.File("./assets/helmo.png", filename="helmo.png")
    embed.set_thumbnail(url="attachment://helmo.png")

    await interaction.response.send_message(file=img, embed=embed)


@bot.tree.command(
    name="benefits", description="Mostrar benefícios do premmy e do patreon"
)
async def benefits(interaction: discord.Interaction):
    embed = discord.Embed(
        colour=discord.Colour.dark_red(), title="Benefícios do Premmy e do Patreon"
    )

    embed.add_field(
        name="Premmy<:premmy:1357527016307429457>",
        value="""- 50% mais exp nas primeiras 3 horas de stamina preço\n - 40 slots na bag loot (grátis só tem 15)
        \n- perde menos experiência quando morre\n - preço 100 hc<:hc:1357529625026236578> ou 12$ Reais no site do helmo https://www.helmorpg.com/site/store.php""",
        inline=False,
    )

    embed.add_field(
        name="Patreon<:bronze:1357527038898081954>",
        value="""- Nome roxo e acesso ao assistente (premmy necessário para usá-lo) preço 250 hc<:hc:1357529625026236578>
        \n- ou 20$ Reais no site do helmo https://www.helmorpg.com/site/store.php""",
        inline=False,
    )
    img = discord.File("./assets/hc.png", filename="hc.png")
    embed.set_thumbnail(url="attachment://hc.png")
    await interaction.response.send_message(file=img, embed=embed)


# Aqui você passa seu token de bot que deve ser colocado no arquivo .env que está no mesmo diretório do script.
bot.run(TOKEN)
