from instabot import Bot
import time
import random

filePath="Followed,txt"

user="username"#input("Enter your username:")
passw="password"#input("Enter your password:")
bot = Bot()
bot.login(username=user,
          password=passw)



while True:
    with open(filePath, 'r') as inputFile:
    
        accounts = inputFile.read().split()

        bot.unfollow(accounts[0])
        accounts.remove(accounts[0])

        #break when there is no one else to unfollow
        if accounts==None:
            break

 
        modifiedContent = ' '.join(accounts)

        #The reason I read and write for every account rather than once is because the program might end abruptly at any time for whatever external reason.
        with open(filePath, 'w') as outputFile:

            outputFile.write(modifiedContent)
    #to make it seem organic
    random_delay = random.uniform(28, 38)
                
    time.sleep(random_delay)


print("No more accounts to unfollow. You have unfollowed all accounts followed using the follow.py script")