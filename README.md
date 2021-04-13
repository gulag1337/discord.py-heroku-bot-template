# discord.py-heroku-bot-template
## A [discord.py](https://discordpy.readthedocs.io/en/stable/) bot template, ready to host on Heroku.

![Heroku|App](https://imgur.com/hKbTPuz.png)

I'll add more features later on.
You'll see a lot of comments in the code for now; just trying to get the message across as well as possible.
### Coding
- Fork this repo.
- Edit your [main.py](https://github.com/gulag1337/discord.py-heroku-bot-template/blob/main/main.py) file however you like. The basics like ```import discord```, setting the token and ```bot.run(TOKEN)``` should remain untouched.
- Add some of your [cogs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html) to the [cogs folder](https://github.com/gulag1337/discord.py-heroku-bot-template/tree/main/cogs).

### Deployment

- Make a [Heroku](https://signup.heroku.com/) account.
- Click **Create new app** and make your app.
- Go to **Settings** --> **Reveal Config Vars** and write
Under **KEY** :
```Discord Token```
Under **VALUE** :
```insert_your_discord_token``` (follow [this](#your-bot-token) to get your token)
- Click **Add**.
- Click on [Deploy](https://imgur.com/2cgFYja.png).
- Under **Deployment Method**, select **GitHub**.
- Connect your GitHub account.
- Click **Enable Automatic Deploys**.
- Under **Manual Deploy**, click **Deploy Branch** for good measure.
- Click on [Overview](https://imgur.com/2cgFYja.png).
- Under **Dyno formation**, click **Configure Dynos**
- It should look [like this](https://imgur.com/SL8M1bF.png) (give it some time & refresh).
- Click on the ✏️, and [turn it on](https://imgur.com/NfvzOzU.png).
You're all set now! 👏 
Give it some time, and hopefully you'll see your bot online on Discord.

### Debugging
It's crucial that you learn to debug your bot code and fix any runtime errors that might happen on Heroku but not on your PC.

The usual causes are :
- Not adding your external modules/libraries to your ```requirements.txt``` file.
- Moving your files/cogs to another folder. You'd have to update these changes yourself by adding ```directory\file``` in the code or ```Procfile``` yourself.
- Renaming stuff :
     - ```main.py``` file to ```bot.py```. Rename all those previous instances in the code.
     - ```bot``` in the code to ```MyBot```. Same solution as above.
- As always, syntax errors in your code.
- Code that is irrelevant to Ubuntu :

>**What OS does Heroku use?**
Ubuntu
~On Heroku, this is called the "stack"—an operating system image curated and maintained by Heroku. The stack is based on Ubuntu, the open source Linux distribution.

For example, datetime formatting on Windows would be :
```py
fmt = "%#I:%M %p"
```
whilst on Ubuntu, it would be :
```py
fmt = "%-I:%M %p"
```
Always keep a close eye on your application logs. You can access this by selecting **View Logs** under [**More ↕**](https://imgur.com/SJZsduu.png).
### Your bot token
- Go to [your app](https://discord.com/developers/applications).
- Select **Bot**.
- Under **Token**, select **Copy** to get the token.
_Note :  Never reveal your token!_

### Disclaimer
- Unverified Heroku accounts (accounts that do not have valid payment info added) receive 550 free Dyno hours a month. This means that an account without a credit/debit card added can only host a bot for ~22 days every month.
- Verified Heroku accounts (accounts that have valid payment info added) receive 1000 free Dyno hours a month. This is more than enough to host your bot online 24/7.
_Note : you do not need to pay any amount to verify your account or use the free Heroku Dyno. Verification simply increases the number of free Dyno hours. In this case, Dyno hours = bot hosting hours_.
- You CAN take the easy way out :
  - Make two Heroku accounts. Connect your repo to both. Switch the Dyno on in the 1st account.
  - When the 1st one's Dyno hours are all used up, switch off that Dyno.
  - Enable the 2nd account's Dyno's.
  - Switch off the 2nd account's Dyno on the 1st of each month.
  - Repeat this process monthly.

### Learning 
- The best advice I can give is, [read the docs](https://discordpy.readthedocs.io/en/stable/).
- Watch some [YouTube videos](https://www.youtube.com/results?search_query=python+discord+heroku+bot).
- You can **take a look** at [StackOverflow](https://stackoverflow.com/) because usually, someone before you, had your same issue. Never rely on it though, I've lost brain cells reading some people's questions (answers included!). Regardless, it is still a great place to learn from the mistakes of others, provided the *question* is good.
- Try your best NOT to copy-paste code; this helps no one, and if you *have* to, make sure you understand what's happening. This repo is just to get you started and help you learn with examples. Say **NO** to being a skid! 😤

## Happy Coding! 🤠
