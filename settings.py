import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("DISCORD_TOKEN")

tourney_name = "YRESL April Break 2021 Tournaments"
footer_note = "Ping Brandon for help."
footer_icon = "https://image.brandonly.me/yresllogo.png"
rulebook_url = "http://bit.ly/YRESLRulebook"  # url to rulebook
newline = "_ _\n"  # dont touch me

# bot settings
prefix = "yr!"
description = "Tournament Bot for YRESL"

# tourney categories
val_category_id = 829931140574871573
lol_category_id = 829931170233712690
guild_id = 762532363695292455
exec_role_id = 829931042386739271

# channel where matches can be started
match_creation_channel_id = 828867315256000513

# timeout settings (in seconds)
veto_timeout = 1800

# message to send when making the channel - CAN NOT BE BLANK
init_message = "Welcome to your team channel! this is another spot for you " \
               "to communicate with your team before games. make sure your " \
               "whole team is signed up on avgl if you want to play! "
