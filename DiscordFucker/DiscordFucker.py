from dhooks import Webhook, File
from io import BytesIO
import requests

print("""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ███████╗██╗░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")

print("Please enter the webhook url:")
x = input()

hook = Webhook(x)

def maintool():
    print("Choose a number:")
    spammer = print("     1.Webhook Spammer")
    hookinfo = print("     2.Get hook Info")
    deleter = print("     3.Delete Hook")

    number = input()
    if number == "1":
        print("Enter a Message:")
        message = input()
        print("How many messages do you want to send?")
        count = input()
        ina = int(count)
        times = 0
        while times < ina:
                hook.send(message)
                print("Message send!")
                times = times + 1

    elif number == "2":
         id = hook.guild_id
         channel_id = hook.channel_id
         default_name = hook.default_name
         avatar_url = hook.default_avatar_url
         print("Hookinfo:")
         print("ID:",id)
         print("Channel ID:",channel_id)
         print("Name:",default_name)
         print("Avatar URL:",avatar_url)
         k = input()

    elif number == "3":
         print("Are you sure you want do delete the Hook permanently? y/n")
         answer = input()
         if input == "y" or "Y":
              hook.delete()

         else:
              maintool()
              
    else:
        print("Error Please choose only numbers!")
maintool()       
        

        
