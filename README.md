# YRESL Tournament Bot

Used for custom features required to run YRESL events.

Based on the [Vaughan Esports Tournament Bot](https://github.com/Vaughan-Esports/VE-Tourney-Bot).

## How to Use
Prefix: `yr!`

Command: `team {game} {teamamtes}`
- game is either `val` or `lol`
- teammates are their discord username (no #) with a space apart 
    - if there's a space in the persons name surround it in quotes .e.g. `"brandon ly"`


Example: `yr!team val ayu "brandon ly" pranav REALLY!? larry`

Makes a role called `VAL TEAM: ayu-brandon ly-pranav-really!?-larry`

Makes a channel called: `team-ayu-brandon ly-pranav-really!?-larry` in the valorant category

Once done with tourney you can do `yr!purge` and it'll delete everything, no warning so only do it when ur actually done xd

## How to setup
Just clone this repo and make sure to have the LTS node.js installed on your PC (Windows, MacOS, or Linux its up to you) and add your bot's token to the client.login()
and run "node ." this will connect to discord using the bot's token and will start your bot