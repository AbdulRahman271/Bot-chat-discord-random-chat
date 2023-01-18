import discord
import random
import string
import asyncio
import datetime
import requests
import time
import os
import json
import pyfiglet
from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")
        
def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()


chat_list = ['Just let him that has been released go crashing Never again chase him because he is not a kite that can still be chased as long as you still tie it with the rope','hello siir','Good Project','Some people are just like friends no matter how comfortable they are Missing bothers you so much ','When someone asks about my weakness ityou Because you make me weak because of this longing and waiting Even in every minute of my life it ','good morning','The Super Amazing Project is a comedy-sketch YouTube show created by Dan Howell and Phil Lester. It contains many fun segments. The show is no longer continued, but Lester and Howell promised to return for seasonal specials due to popular demand.','Some say love is a tribulation but for me it is a strength Strength to be better and to give everything to those who are loved Strength to be able to survive in any situation','Along with this opportunity  Ive taken part in this airdrop Im so enthusiastic because this will be an excellent project lets take it to the moon','This project is looks so innovative and impactful, happy to take participate in such huge project','When you want to love someone, dont ever look at the looks of them Because kindness and sincerity dont exist in looks','Never regret a love that doesnt end according to your own desires Because from it you learn about the meaning of a sacrifice of waiting and sincerity']

os.system('cls')
result = pyfiglet.figlet_format("""Discord Auto Random Chat""", font = "graceful"  )
print (colored(result, 'blue'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now()
print (colored('''Created by: MITYO''', 'cyan', attrs=['bold'])) 
print (colored('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••', 'green', attrs=['bold']))
print (colored(f"Ξ Follow myGithub : https://github.com/mityoe860 \nΞ START           : {x} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• \n', 'green', attrs=['bold']))
print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
while True:
        try:
            setdelay = int(input("Please input delay time chat in seconds = "))
            break
        except:
            print("ONLY USE NUMBER!")
print (colored('\nWrite on discord chat: \n!ikuzo <number of messages>', 'cyan', attrs=['bold']))



@client.command()
async def ikuzo(ctx,amount: int):
    await ctx.message.delete()
    msgsend = amount
    sec = setdelay * msgsend
    convert = str(datetime.timedelta(seconds = sec))
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}messages\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{convert}\n")
    while msgsend > 0:
        try:    
            msgsend -= 1  
            output = random.choice(chat_list)
            await ctx.send(output)  
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Message success sent = {Fore.WHITE}#{msgsend + 1} {output}{Fore.LIGHTBLACK_EX} | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}")                 
        except:
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot send message {Fore.WHITE}#{msgsend + 1}")
            pass
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Success delete message = {Fore.WHITE}#{msgsend + 1} {output}")
            except:
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot delete message {Fore.WHITE}#{msgsend + 1} {output}")
                pass
        if msgsend == 0:
            print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All messages was sent")
        await asyncio.sleep(setdelay)
    
    return


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)


Init()
