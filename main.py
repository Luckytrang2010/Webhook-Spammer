from discord_webhook import DiscordWebhook, DiscordEmbed
check = open("webhook.txt","r")
if check.read() != "":
    #check.read() is the webhook if the text's not blank
    intro = input("Webhook Spammer\n----------------------------------------------------------------------\nMade by 4Bytes#9688\nRead webhook file? [Y/N]: ")
    if intro.lower() == "y":
        question = input("Limited spam amount? [Y/N]: ")
        if question.lower() == "y":
            times = input("How many times do you want the bot to spam?: ")
            message = input("Enter message here to spam: ")
            try:
                for i in range(0,(int(times)-1)):
                    webhook = check.read()
                    spam = DiscordWebhook(url=webhook,content=str(message))
                    done = spam.execute()
            except Exception as error:
                print(f"Error occured, try again.\nMore about error: {error}")
        elif question.lower() == "n":
            activate = False
            message = input("Enter message here to spam: ")
            try:
                activate = True
                while activate == True:
                    webhook = check.read()
                    spam = DiscordWebhook(url=webhook,content=(str(message)))
                    done = spam.execute()
            except Exception as error:
                print(f"Error occured, try again.\nMore about error: {error}")
    elif intro.lower() == "n":
        webhook = input("Enter webhook here: ")
        question = input("Limited spam amount? [Y/N]: ")
        if question.lower() == "y":
            times = input("How many times do you want the bot to spam?: ")
            message = input("Enter message here to spam: ")
            try:
                for i in range(0,(int(times)-1)):
                    spam = DiscordWebhook(url=webhook,content=str(message))
                    done = spam.execute()
            except Exception as error:
                print(f"Error occured, try again.\nMore about error: {error}")
        elif question.lower() == "n":
            activate = False
            message = input("Enter message here to spam: ")
            try:
                activate = True
                while activate == True:
                    spam = DiscordWebhook(url=webhook,content=(str(message)))
                    done = spam.execute()
            except Exception as error:
                print(f"Error occured, try again.\nMore about error: {error}")
else:
    webhook = input("Enter webhook here: ")
    question = input("Limited spam amount? [Y/N]: ")
    if question.lower() == "y":
        times = input("How many times do you want the bot to spam?: ")
        message = input("Enter message here to spam: ")
        try:
            for i in range(0,(int(times)-1)):
                spam = DiscordWebhook(url=webhook,content=str(message))
                done = spam.execute()
        except Exception as error:
            print(f"Error occured, try again.\nMore about error: {error}")
    elif question.lower() == "n":
        activate = False
        message = input("Enter message here to spam: ")
        try:
            activate = True
            while activate == True:
                spam = DiscordWebhook(url=webhook,content=(str(message)))
                done = spam.execute()
        except Exception as error:
            print(f"Error occured, try again.\nMore about error: {error}")