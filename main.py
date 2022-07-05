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
{amarelo}@bot.event{branco}()
{laranja}async def {amarelo_claro}on _ready{branco}():
    {azul}print{branco}({verde}"""{branco}
  {azul}▒{branco}█▀▀█ █{azul}░░ {branco}█▀▀█ {branco}█▀▀ █{azul}░{branco}█ 　 █▀▀ █▀▀█ █{azul}░░{branco}█
  {azul}▒{branco}█▀▀▄ █{azul}░░ {branco}█▄▄█ {branco}█{azul}░░ {branco}█▀{branco}▄ 　 ▀▀█ █{azul}░░{branco}█ █▄▄█
  {azul}▒{branco}█▄▄█ ▀▀▀ {branco}▀{azul}░░{branco}▀ ▀▀▀ ▀{azul}░{branco}▀ 　 ▀▀▀ █▀▀▀ ▄▄▄█ {vermelho}By{branco}: Black spy{cinza}#0001{verde}"""{branco})
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

{branco}bot.run(token{laranja}, {vermelho}bot{branco}={laranja}False{branco}){cinza} # A função de inicialização em Bot=Human''', 0.2)
input('')
os.system('cls' if os.name == 'nt' else 'clear')
slowtype(f'''

  {azul}▒{branco}█▀▀█ █{azul}░░ {branco}█▀▀█ {branco}█▀▀ █{azul}░{branco}█ 　 █▀▀ █▀▀█ █{azul}░░{branco}█
  {azul}▒{branco}█▀▀▄ █{azul}░░ {branco}█▄▄█ {branco}█{azul}░░ {branco}█▀{branco}▄ 　 ▀▀█ █{azul}░░{branco}█ █▄▄█
  {azul}▒{branco}█▄▄█ ▀▀▀ {branco}▀{azul}░░{branco}▀ ▀▀▀ ▀{azul}░{branco}▀ 　 ▀▀▀ █▀▀▀ ▄▄▄█ {vermelho}By{branco}: Black spy{cinza}#0001{verde}"""{branco})

    {cinza}● {vermelho}Logado as{branco}: Black spy{cinza}#0001 {branco}| {roxo}{t}
''', 0.2)
input('')
os.system('cls' if os.name == 'nt' else 'clear')
slowtype(f'''Escola opção Black spy:
   {vermelho}---------------------------------------------------------------------------
   {vermelho}| {roxo}[1] {branco}Nuke   {vermelho}|  {roxo}[4] {branco}Derrubar IPV4   {branco}|  {roxo}[7] {branco}Escolher um novo usúario {vermelho}|
   {vermelho}| {roxo}[2] {branco}Clone  {vermelho}|  {roxo}[5] {branco}DDOS            {branco}|  {roxo}[8] {branco}Sair                     {vermelho}|
   {vermelho}| {roxo}[3] {branco}DIv    {vermelho}|  {roxo}[6] {branco}Consuta         {branco}|                               {vermelho}|
   {vermelho}---------------------------------------------------------------------------
''', 0.2)
input("")
