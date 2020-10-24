# pythontwitchbot
 A simple twitch Bot for Twitchplays

Most of the Code in twitchPlaysBot.py is ispired by a tutorial found on:
https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8

simulateInput.py is taken from:
https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events-in-python

You Have to create a .env-File for this bot to work look at:
https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
when you want to know how its done. It should look like this:

TMI_TOKEN=[YourOauthToken]
CLIENT_ID=[YourClientId from TwitchDev for your Project]
BOT_NICK=[Nickname of your Bot]
BOT_PREFIX=[Your Command prefix (!..)]
CHANNEL=[The name of the Channel where the bot should connect]



To start the Bot create a enviroment:

1.  Install pipenv:
    pip install pipenv

2.  Create an enviroment in the folder where the .env file is stored:  
    pipenv --python [Path to your Pythonversion or just use a Path-Variable]
    e.g.: pipenv --python python

3.  Install twitchio in your enviroment:
    pipenv install twitchio

4.  Start the Bot:
    pipenv run python twitchPlaysBot.py
