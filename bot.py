import discord.ext.commands.errors
from discord.ext import commands
from discord.ext.commands import MissingPermissions

from settings import prefix, description, BOT_TOKEN, tourney_name
from settings import match_creation_channel_id, guild_id, exec_role_id
from settings import val_category_id, lol_category_id
from settings import init_message

import embeds

intents = discord.Intents.default()
intents.members = True
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=True)
bot = discord.ext.commands.Bot(command_prefix=prefix,
                               intents=intents,
                               description=description,
                               case_insensitive=True,
                               allowed_mentions=allowed_mentions)


@bot.command()
async def team(ctx, game, *args):
    """
    Creates a private text channel between you and your opponent(s)
    """
    # guild and category objects
    guild = bot.get_guild(guild_id)
    category = None
    if game == 'val':
        category = guild.get_channel(val_category_id)
    elif game == 'lol':
        category = guild.get_channel(lol_category_id)
    else:
        await ctx.send("Not a valid game! `val` or `lol`")
        return

    # game coordinator role
    exec_role = guild.get_role(exec_role_id)

    print(args)

    # create the role
    name = f"{game.upper()} TEAM: {'-'.join(args)}"
    team_role = await guild.create_role(name=name)

    print(f"XD: {guild.members}")

    for team_member in args:
        print(f"Args: {team_member.lower()}")
        for member in guild.members:
            print(f"Member: {member.name.lower()}")
            if team_member.lower() == member.name.lower():
                print("true")
                await member.add_roles(team_role)

    # overwrites for the match channel
    overwrites = {
        team_role: discord.PermissionOverwrite(add_reactions=True,
                                               read_messages=True,
                                               send_messages=True,
                                               external_emojis=True,
                                               attach_files=True,
                                               embed_links=True),

        exec_role: discord.PermissionOverwrite(add_reactions=True,
                                               read_messages=True,
                                               send_messages=True,
                                               external_emojis=True,
                                               attach_files=True,
                                               embed_links=True),
        guild.default_role: discord.PermissionOverwrite(read_messages=False)
    }

    # create channel
    name = team_role.name[4:]
    topic = team_role.name
    team_channel = await guild.create_text_channel(name=name,
                                                    category=category,
                                                    topic=topic,
                                                    overwrites=overwrites)

    # send message linking to channel
    await ctx.send(embed=await embeds.match_started(team_channel))

    # send instructions into the channel
    await team_channel.send(f"{team_role.mention}\n\n{init_message}")


@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx):
    """
    Purges all channels in the inactive category
    """

    # guild
    guild = bot.get_guild(guild_id)
    # purge roles
    for role in guild.roles:
        if 'TEAM' in role.name:
            await role.delete()

    # purge valorant
    val_category = guild.get_channel(val_category_id)
    for channel in val_category.text_channels:
        await channel.delete()

    # purge league
    lol_category = guild.get_channel(lol_category_id)
    for channel in lol_category.text_channels:
        await channel.delete()

    await ctx.send(embed=await embeds.purged())


@purge.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "You don't have permission to purge tournament channels!"
        await ctx.send(embed=await embeds.missing_permission_error(text))


bot.run(BOT_TOKEN)
