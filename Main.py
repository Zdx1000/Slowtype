import sys, time, os
from colorama import Fore, Style
from pystyle import Colors

os.system('Color b')

# Setando cores e Brilho
brilho = Style.BRIGHT
cinza = Colors.gray
branco = Fore.LIGHTWHITE_EX
amarelo = Fore.LIGHTYELLOW_EX
amarelo_claro = Colors.yellow
laranja = Colors.orange
azul = Fore.BLUE
vermelho = Fore.LIGHTRED_EX
verde = Fore.GREEN
azul_claro = Fore.BLUE

os.system('cls' if os.name == 'nt' else 'clear')

def slowtype(text, sec):
    for d in text + "\n":
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(sec / 100)
        #############

slowtype(f'''{cinza}# Importações
{laranja}{brilho}from {branco}discord.ext {laranja}import {branco}commands

{branco}token = {azul}input{branco}({verde}'Digite seu token: '{branco}) {cinza}# Adquirindo um Token
{branco}prefix = {azul}input{branco}({verde}'DIgite seu Prefix: '{branco}) {cinza}# Definindo o Prefixo{branco}

bot = commands.Bot({vermelho}command_prefix{branco}=prefix, {vermelho}self_bot{branco}={laranja}True{branco}) {cinza} # Implementando o Prefixo definido{branco}
bot.remove_command({verde}"help"{branco}){cinza} # Removendo função 'Help'

{cinza}# Ação do bot
{amarelo}@bot.command{branco}()
{laranja}async def {amarelo_claro}clear{branco}(ctx{laranja},{branco} limit: {azul}int{branco}={laranja}None{branco}): {cinza} # Definindo ação a ser efetuada{branco}
    sucedido = {azul}0 {cinza} # Contagem de mensagens apagadas
    {branco}fracassado = {azul}0 {cinza} # Contagem de mensagens não apagadas [Falhas]{branco}
    {laranja}async for {branco}msg {laranja}in {branco}ctx.message.channel.history({vermelho}limit{branco}=limit): {cinza} # Pegando Histórico da conversa
        {laranja}if{branco} msg.author.id == bot.user.id: {cinza} # Definindo o local a ser efetuada a ação
            {laranja}try{branco}:
                {laranja}await{branco} msg.delete() {cinza} # Ação de limpar as mensagens
                {branco}sucedido += {azul}1 {cinza} # [Bem sucedido]
            {laranja}except{branco}:
                fracassado += {azul}1 {cinza}# [Mal sucedido]

{branco}bot.run(token{laranja}, {vermelho}bot{branco}={laranja}False{branco}){cinza} # A função de inicialização em Bot=Human''', 4)
input('')
