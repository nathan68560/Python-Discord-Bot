import discord
from discord.ext import commands
from random import randint

# Create bot and connect to server online
bot = commands.Bot(command_prefix="!", case_insensitive=True)

table = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
play = False
# Command that start the morpion minigame (durée de dev : ~1h10)
@bot.command(name='morpion', description="Joue au morpion contre moi !")
async def morpion(ctx):
    global table, play
    await ctx.message.delete()

    if 'start' in ctx.message.content.lower() and not play:
        table = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
        play = True
        await morpionAI(ctx)
    elif 'stop' in ctx.message.content.lower() and play:
        table = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
        play = False
        await ctx.send(f'{ctx.author.mention} Arrêt de la partie...')
    elif '0' in ctx.message.content.lower() and play:
        if table[0] == ' ':
            table[0] = 'o'
            await morpionAI(ctx)
        elif table[0] == 'x' or table[0] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 0 n\'est pas vide !')
    elif '1' in ctx.message.content.lower() and play:
        if table[1] == ' ':
            table[1] = 'o'
            await morpionAI(ctx)
        elif table[1] == 'x' or table[1] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 1 n\'est pas vide !')
    elif '2' in ctx.message.content.lower() and play:
        if table[2] == ' ':
            table[2] = 'o'
            await morpionAI(ctx)
        elif table[2] == 'x' or table[2] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 2 n\'est pas vide !')
    elif '3' in ctx.message.content.lower() and play:
        if table[3] == ' ':
            table[3] = 'o'
            await morpionAI(ctx)
        elif table[3] == 'x' or table[3] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 3 n\'est pas vide !')
    elif '4' in ctx.message.content.lower() and play:
        if table[4] == ' ':
            table[4] = 'o'
            await morpionAI(ctx)
        elif table[4] == 'x' or table[4] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 4 n\'est pas vide !')
    elif '5' in ctx.message.content.lower() and play:
        if table[5] == ' ':
            table[5] = 'o'
            await morpionAI(ctx)
        elif table[5] == 'x' or table[5] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 5 n\'est pas vide !')
    elif '6' in ctx.message.content.lower() and play:
        if table[6] == ' ':
            table[6] = 'o'
            await morpionAI(ctx)
        elif table[6] == 'x' or table[6] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 6 n\'est pas vide !')
    elif '7' in ctx.message.content.lower() and play:
        if table[7] == ' ':
            table[7] = 'o'
            await morpionAI(ctx)
        elif table[7] == 'x' or table[7] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 7 n\'est pas vide !')
    elif '8' in ctx.message.content.lower() and play:
        if table[8] == ' ':
            table[8] = 'o'
            await morpionAI(ctx)
        elif table[8] == 'x' or table[8] == 'o':
            await ctx.send(f'{ctx.author.mention} La case 8 n\'est pas vide !')
    else:
        await ctx.send(f'{ctx.author.mention}\nPour jouer : !morpion start\nPour arrêter : !morpion stop\nPour placer un cercle : !morpion pos avec pos=0 pour en haut à gauche jusqu\'à pos=8 pour en bas à droite')

# Function that put an X at a random available place
async def morpionAI(ctx):
    global table, play
    
    if not await morpionWin(ctx):
        x = randint(0, 8)
        if table[x] == ' ':
            table[x] = 'x'
            await ctx.send(f'{ctx.author.mention} à joué :\n {table[0]} | {table[1]} | {table[2]} \n {table[3]} | {table[4]} | {table[5]} \n {table[6]} | {table[7]} | {table[8]} ')
            await ctx.send(f'{bot.user.mention} à joué :\n {table[0]} | {table[1]} | {table[2]} \n {table[3]} | {table[4]} | {table[5]} \n {table[6]} | {table[7]} | {table[8]} ')
        elif table[x] == 'x' or table[x] == 'o':
            await morpionAI(ctx)

        if not await morpionWin(ctx):
            i = 0
            for case in table:
                if case == ' ':
                    i+=1

            if i == 0:
                play = False
                await ctx.send(f'{ctx.author.mention} Fin de partie !')

# Check if there's a winner
async def morpionWin(ctx):
    global table

    # Check rows
    if table[0] != ' ' and table[0] == table[1] and table[1] == table[2]:
        if table[0] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada: :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    elif table[3] != ' ' and table[3] == table[4] and table[4] == table[5]:
        if table[3] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    elif table[6] != ' ' and table[6] == table[7] and table[7] == table[8]:
        if table[6] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    # Check diagonals
    elif table[0] != ' ' and table[0] == table[4] and table[4] == table[8]:
        if table[0] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    elif table[2] != ' ' and table[2] == table[4] and table[4] == table[6]:
        if table[2] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    # Check columns
    elif table[0] != ' ' and table[0] == table[3] and table[3] == table[6]:
        if table[0] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    elif table[1] != ' ' and table[1] == table[4] and table[4] == table[7]:
        if table[1] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    elif table[2] != ' ' and table[2] == table[5] and table[5] == table[8]:
        if table[2] == 'o':
            await ctx.send(f'Félicitation, {ctx.author.mention} à gagné ! :trophy::tada:')
        else:
            await ctx.send(f'Dommage, {bot.user.mention} à gagné...')
        return True
    else:
        return False


field = "a1 | a2 | a3 | a4 | a5 | a6 | a7 | a8 | a9 |\nb1 |     |     |     |     |     |     |     |     |\nc1 |     |     |     |     |     |     |     |     |\nd1 |     |      |     |     |     |     |    |     |"
places = [
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'
]
pField = []
botField = []
gameState = 0
# Command that start the bataille navalle minigame (durée de dev : ~1h30)
@bot.command(name='bataille', description="Joue à une partie de bataille navalle contre moi !")
async def bataille(ctx):
    global field, places, pField, botField, gameState

    # Delete command message for UX
    await ctx.message.delete()

    # If add navire, check if navire isn't already listed and add it, else throw an error message
    if " add " in ctx.message.content.lower():
        if len(pField) >= 6:
            await ctx.send(f'{ctx.author.mention} Vous avez déjà positionné 6 navires')
        else:
            for p in places:
                if len(pField) < 6:
                    if p in ctx.message.content.lower() and p not in pField:
                        pField.append(p)
                        await ctx.send(f'{ctx.author.mention} Un navire à été positionné en {p}')
                    elif p in ctx.message.content.lower() and p in pField:
                        await ctx.send(f'{ctx.author.mention} Un navire est déjà positionné en {p}')
    # If try attack, check if there's a navire there
    elif " try " in ctx.message.content.lower():
        for p in places:
            if p in ctx.message.content.lower() and p in botField:
                botField.remove(p)
                await ctx.send(f'{ctx.author.mention} Un navire adverse à été détruit en {p} ! {6-len(botField)}/6 de détruit ! ')
                if not await batailleWin(ctx):
                    await batailleBot(ctx)
                return True
            elif p in ctx.message.content.lower():
                await ctx.send(f'{ctx.author.mention} Aucun navire adverse en {p}... {6-len(botField)}/6 de détruit !')
                await batailleBot(ctx)
                return True
        await ctx.send(f'{ctx.author.mention} Mauvaise commande, cette case n\'existe pas !')
    elif " stop" in ctx.message.content.lower():
        pField = []
        botField = []
        gameState = 0
        await ctx.send(f'{ctx.author.mention} Arrêt de la partie...')
    elif gameState == 0:
        await ctx.send(f"{ctx.author.mention} Prêt pour une partie de bataille navale ?!\n Voici la carte avec le nom des case :\n{field}")
        await ctx.send(f"{ctx.author.mention} Commence par positioner 6 navires avec la commande !bataille add (position)")
    
    # If there's 6 navire and still in the first gamestate, active the second one and let the bot make his field
    if len(pField) == 6 and gameState == 0:
        gameState = 1
        while len(botField)<6:
            b = places[randint(0, 35)]
            if b not in botField:
                botField.append(b)
        await ctx.send(f'{ctx.author.mention} Phase de préparation fini, vous allez maintenant pouvoir attaquer grâce à la commande : !bataille try (position)')

# Function for the bot to try and hit us
async def batailleBot(ctx):
    global field, places, pField, botField, gameState

    c = places[randint(0, 35)]
    if c in pField:
        pField.remove(c)
        await ctx.send(f'{ctx.author.mention} Notre navire en {c} à été détruit ! Il nous reste {len(pField)} navires...')
    else:
        await ctx.send(f'{ctx.author.mention} Un missile à été tiré en {c}, aucun de nos navires touchés... Il nous reste {len(pField)} navires...')
    
    await batailleWin(ctx)

# Function check if bataille win
async def batailleWin(ctx):
    if len(pField) == 0:
        await ctx.send(f'{ctx.author.mention} à perdu, ça flotte à été détruite !')
        return True
    elif len(botField) == 0:
        await ctx.send(f'{ctx.author.mention} à gagné, il à détruit la flotte adverse ! :trophy::tada:')
        return True
    
    return False

# Event when a message is send on discord
@bot.event
async def on_message(message):
    if message.author == bot.user: # Ignor message from self
        return
    elif " ping " in message.content.lower(): # If 'hey', respond
        await message.channel.send(f"{message.content.lower().replace('ping', 'pong')} {message.author.mention}")
    elif bot.user.name.lower() in message.content.lower() or bot.user.mention.lower() in message.content.lower():
        await message.channel.send(f"{message.author.mention}\n{bot.user.name} à votre service ! Liste de mes commandes :\n-!morpion pour faire une partie de morpion contre moi !\n-Pierre, feuille, ciseau pour faire un tour contre moi\n-!bataille pour faire une partie de bataille navalle contre moi !")
    # Pierre feuille ciseau (durée de dev : <10min)
    elif message.content.lower() == 'pierre' or message.content.lower() == 'feuille' or message.content.lower() == 'ciseau':
        choice = [ 'Pierre', 'Feuille', 'Ciseau' ]
        c = choice[randint(0, 2)]
        if message.content.lower() == 'pierre' and c.lower() == 'ciseau' or message.content.lower() == 'ciseau' and c.lower() == 'feuille' or message.content.lower() == 'feuille' and c.lower() == 'pierre':
            await message.channel.send(f'{c} ! Félicitation, {message.author.mention} à gagné ! :trophy::tada:')
        elif message.content.lower() == 'pierre' and c.lower() == 'feuille' or message.content.lower() == 'ciseau' and c.lower() == 'pierre' or message.content.lower() == 'feuille' and c.lower() == 'ciseau':
            await message.channel.send(f'{c} ! Dommage, {message.author.mention} à perdu...')
        else:
            await message.channel.send(f'{c} ! Oh, ex-equo ! {message.author.mention}')
    else:
        await bot.process_commands(message)

# Run bot
bot.run("Bot_Access_Token")
