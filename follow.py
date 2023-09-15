from instabot import Bot
import time
import random


user="username"#input("Enter your username:")
passw="password"#input("Enter your password:")
bot = Bot()
bot.login(username=user,
          password=passw)



# Follow

base="cassowear"#input("Enter a username to examine and follow appropriate followers (Example: gymshark):")
minFollowers=0#input("Enter a minimum following you would like the people you follow to have:")
maxFollowers=99999999#input("Enter a maximum following you would like the people you follow to have:")
lkeyword="fit gym Gym Fit page"#input("Enter desired keywords seperated by spaces: ")

keywords=lkeyword.split()




followers = bot.get_user_followers(base)
print(f'Followers of {base} acquired')
print(followers)

following=bot.get_user_following(user)
print(f'Following of {user} acquired')

for follower in followers:
    if follower in following:
        continue




    username = bot.get_username_from_user_id(follower)
    user_info = bot.get_user_info(follower)
    bio = user_info['biography']
    name = user_info['full_name']
    
    #filter
    for keyword in keywords:
        if keyword in username or keyword in user_info or keyword in bio or keyword in username:


            print("Match found")
            bot.follow(follower)
            with open("Followed.txt","a") as file:
                file.write(username+" ")
                
            print(f'Followed {username}')
            #this is to make it seem organic
            random_delay = random.uniform(28, 38)
                
            time.sleep(random_delay)






print("No more matching accounts with these constraints")
time.sleep(10)

