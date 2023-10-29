import time, threading, os, discord, requests, json
from os import system 
from discord.ext import commands
from colorama import Fore
from time import sleep
print(f"\033[0;34m")
print("""
███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

░██████╗██╗░░██╗░█████╗░██████╗░
██╔════╝██║░░██║██╔══██╗██╔══██╗
╚█████╗░███████║██║░░██║██████╔╝
░╚═══██╗██╔══██║██║░░██║██╔═══╝░
██████╔╝██║░░██║╚█████╔╝██║░░░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░
""")

token = input(f"\033[0m TOKEN BOT : ")
guildid = input (f"ไอดีเซิฟ : ")

header = {"Authorization": "Bot "            + token}
intents = discord.Intents.all()
client = commands.Bot(command_prefix="s!", intents=intents)
client.remove_command("help")

class stuff:
    def __init__(self, method, jsons, message, present):
        self.method = method
        self.jsons = jsons
        self.message = message
        self.present = present
    def dostuff(self, url):
        while True:
            if self.method == "delete":
                r = requests.delete(url, headers=header, json=self.jsons)
            elif self.method == "put":
                r = requests.put(url, headers=header, json=self.jsons)
            elif self.method == "post":
                r = requests.post(url, headers=header, json=self.jsons)

            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                print(f"    [+]{self.message}")
                break
            elif r.status_code == 429:
                print(f"    Rate limited")
                sleep_time = r.json()["retry_after"]
                sleep_time = int(sleep_time)/1000
                time.sleep(sleep_time)
                self.dostuff(url)
                break
            else:
                print(f"    [+] Could not {self.present}")
                break


ban = stuff("put", None, "banned user", "ban user")
kick = stuff("delete", None, "kicked user", "kick user")

wbhook_status = False
def main():
    system("cls & mode 70, 20 & title " + f"selfbot-golang x songkran discord id > {guildid}")
    print(f"""

    [+] 1.Ban All
    [+] 2.Kick All 
    [+] 0.exit
    [+] by night shop
    [+] dc : https://discord.gg/fRHNaAm53t

 """)

    try:
        choice = input(f"    [+] Number: ")
        choice = int(choice)
    except:
        print(f"    Enter valid information")
        time.sleep(3)
        main()
    if choice == 1:
        try:
            size = os.path.getsize("users.txt")
            if size > 0:
                pass
            else:
                print(f"    s!play")
                time.sleep(3)
                main()
        except:
            print(f"    s!play")
            time.sleep(3)
            main()
        f = open("users.txt","r")
        for id in f:
            thread = threading.Thread(target=ban.dostuff, args=[f"https://discord.com/api/guilds/{guildid}/bans/{id}"])
            thread.start()
        f.close()
        time.sleep(3)
        main()
        
    elif choice == 2:
        try:
            size = os.path.getsize("users.txt")
            if size > 0:
                pass
            else:
                print(f"    s!play")
                time.sleep(3)
                main()
        except:
            print(f"    s!play")
            time.sleep(3)
            main()
        f = open("users.txt","r")
        for id in f:
            thread = threading.Thread(target=kick.dostuff, args=[f"https://discord.com/api/guilds/{guildid}/members/{id}"])
            thread.start()
        f.close()
        time.sleep(3)
        main()

    elif choice == 0:
     os._exit(0)

    else:
        print(f"    Enter a valid option")
        time.sleep(3)
        main()

@client.command()
async def play(ctx):
    await ctx.message.delete()
    try:
        os.remove("users.txt")
    except:
        pass
    members = 0
    with open('users.txt', 'w') as f: 
        for member in ctx.guild.members:
            f.write(str(member.id)+"\n") 
            members = members+1
    f.close()

@client.event
async def on_ready():
    main_thread = threading.Thread(target=main)
    main_thread.start()
try:
    client.run(token)
except:
    print(f"    Check  Token ")
    time.sleep(0.1)