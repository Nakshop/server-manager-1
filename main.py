import os

import discord

import requests

import json

import asyncio

import psutil

from discord.ext.commands import Greedy

from discord.gateway import DiscordWebSocket

from typing import Union

import discord.ext

from discord.utils import find

from discord.ext import commands, tasks

import webserver

from webserver import keep_alive

import sys

os.system("pip install PyNaCl")

async def prefix(client, message):

    if message.author.id in [972484544504659968,996484753018601572,855119565440024598]:

        return ""

    else:

        return "."

class MyDiscordWebSocket(DiscordWebSocket):

    async def send_as_json(self, data):

        if data.get('op') == self.IDENTIFY:

            if data.get('d', {}).get('properties',

                                     {}).get('$browser') is not None:

                data['d']['properties']['$browser'] = 'Discord Android'

                data['d']['properties']['$device'] = 'Discord Android'

        await super().send_as_json(data)

DiscordWebSocket.from_client = MyDiscordWebSocket.from_client

intents = discord.Intents.all()

client = commands.Bot(command_prefix=prefix,

                      intents=intents,

                      case_insensitive=True)

client.remove_command('help')

async def identify(self):

    payload = {

        'op': self.IDENTIFY,

        'd': {

            'token': self.token,

            'properties': {

                '$os': sys.platform,

                '$browser': 'Discord Android',

                '$device': 'Discord Android',

                '$referrer': '',

                '$referring_domain': ''

            },

            'compress': False,

            'large_threshold': 250,

            'v': 3

        }

    }

    if self.shard_id is not None and self.shard_count is not None:

        payload['d']['shard'] = [self.shard_id, self.shard_count]

    state = self._connection

    if state._activity is not None or state._status is not None:

        payload['d']['presence'] = {

            'status': state._status,

            'game': state._activity,

            'since': 0,

            'afk': False

        }

    if state._intents is not None:

        payload['d']['intents'] = state._intents.value

    await self.call_hooks('before_identify',

                          self.shard_id,

                          initial=self._initial_identify)

    await self.send_as_json(payload)

snipe_message_author = {}

snipe_message_content = {}

@client.event

async def on_message_delete(message):

    snipe_message_author[message.channel.id] = message.author

    snipe_message_content[message.channel.id] = message.content

    await sleep(60)

    del snipe_message_author[message.channel.id]

    del snipe_message_content[message.channel.id]

@client.command()

async def snipe(ctx):

    channel = ctx.channel

    try:

        snipeEmbed = discord.Embed(

            color=0x2f3136,

            timestamp=ctx.message.created_at,

            title=f"Sniped!",

            description=snipe_message_content[channel.id])

        snipeEmbed.set_footer(

            text=f"Deleted by {snipe_message_author[channel.id]}")

        await ctx.reply(embed=snipeEmbed)

    except:

        await ctx.reply(f"There are no deleted messages")

@client.command()

async def tag(ctx):

  await ctx.reply("<:black_reaper:1034695910648713227> **Put `𝐌𝐆 丶` in your username!** <:black_reaper:1034695910648713227>")

@client.command()

async def stag(ctx):

  await ctx.reply("<:black_reaper:1034695910648713227> **Put `!ᴹᴳ` in your username!** <:black_reaper:1034695910648713227>")

@client.event

async def on_message(message):

  await client.process_commands(message)

  if message.content.startswith('tag'):

    await message.reply(f"> **No Need To Put Tag. Just Put Our Vanity/ServerLink For Roles**")  

  if message.mention_everyone:

    if message.guild.me.top_role.position >= message.author.top_role.position:

      await message.delete()  

      await message.channel.send(f"No Pings {message.author.mention}")

  if 'http' in message.content or 'www.' in message.content:

    if message.guild.me.top_role.position >= message.author.top_role.position:

      await message.delete()

      await message.channel.send(f"No Links allowed!")      

  if 'discord.gg' in message.content:

    if message.guild.me.top_role.position >= message.author.top_role.position:

      await message.delete()

      await message.channel.send(f"No Links allowed!")     

@client.command(aliases=["h"])

async def help(ctx):

    embed = discord.Embed(

        title= '**𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐆𝐀𝐋𝐀𝐗𝐘**',

        description=

        f'<a:nt_batman_xd:1036582022329667625> **__𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒__** <a:nt_batman_xd:1036582022329667625>\n\n**`Official`  `Ban`  `Av`  `Serverinfo`  `Purge`  `Officialcount`  `Ping`  `Mc`  `Slowmode`  `Userinfo`  `Snipe`  `Botinfo`  `Steal`  `Boost`  `Warn`  `Rolecreate`  `Servericon`   `Serverbanner`  `Roleall`  `Hide`   `Unhide`  `Invites`  `Massunban`  `Mute`  `Unmute`  `Kick`  `Nuke`  `Unlockall`  `Lockall`  `Banner`  `Resetall`  `Resetinvites`  `Fuckban`  `Roleinfo`  `Removerole`  `Addrole`**\n\n',

      color=0x2f3136)

    embed.set_thumbnail(

        url=

        "https://cdn.discordapp.com/icons/975450975475236924/2a48d9b8dfe209f51a8ff4badbfee5d5.png?size=1024"

    )

    await ctx.reply(embed=embed)

@client.event

async def on_ready():

    print(f"Connected to NAKSH")

    channel = client.get_channel(1026119933089812540)

    activity = discord.Activity(type=discord.ActivityType.streaming,

                                name="𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐆𝐀𝐋𝐀𝐗𝐘")

    await client.change_presence(status=discord.Status.dnd,

                                 activity=activity)

    await channel.connect()

@client.command(aliases=["mg"])

@commands.has_permissions(administrator=True)

async def official(ctx, user: discord.Member):

  guild = client.get_guild(1032537567410802718)

  role = guild.get_role(1035446297655787540)

  if '' in str(user.name) or '' in str(user.name):

    await user.add_roles(role)

    await ctx.send(f"**<:x_tick:1026132299672207451> | SuccessFully Given Official Role To {user.mention}**")

    

@client.command(aliases=["oc"])

async def officialcount(ctx):

    guild = client.get_guild(1032537567410802718)

    role = guild.get_role(1035446297655787540)

    embed = discord.Embed(title="**Officials Count of MUSICAL GALAXY**",

                          description=f"**{len(role.members)} Officials!**",

                          color=0x2f3136)

    await ctx.reply(embed=embed)

@client.command(aliases=["si" , "info"])

async def serverinfo(ctx):

    guild_roles = len(ctx.guild.roles)

    guild_categories = len(ctx.guild.categories)

    guild_members = len(ctx.guild.members)

    text_channels = len(ctx.guild.text_channels)

    voice_channels = len(ctx.guild.voice_channels)

    channels = text_channels + voice_channels

    serverinfo = discord.Embed(colour=0x2f3136)

    serverinfo.add_field(name="Server Name",

                         value=f"```{ctx.guild.name}```",

                         inline=False)

    serverinfo.add_field(name="Server ID",

                         value=f"```{ctx.guild.id}```",

                         inline=False)

    serverinfo.add_field(name="Server Owner",

                         value=f"```{ctx.guild.owner}```",

                         inline=False)

    serverinfo.add_field(name="Boosts",

                         value=f"```{ctx.guild.premium_subscription_count}```",

                         inline=False)

    serverinfo.add_field(name="Channels",

                         value=f"```{channels}```",

                         inline=False)

    serverinfo.add_field(name="Roles",

                         value=f"```{guild_roles}```",

                         inline=False)

    serverinfo.add_field(name="Categories",

                         value=f"```{guild_categories} Categories```",

                         inline=False)

    serverinfo.add_field(name="Members",

                         value=f"```{guild_members}```",

                         inline=False)

    serverinfo.set_thumbnail(url=ctx.guild.icon_url)

    await ctx.send(embed=serverinfo)

@client.command(aliases=["bi"])

async def botinfo(ctx):

    embed = discord.Embed(title='Bot Information', color=0x2f3136)

    embed.add_field(name='<:x_icons_bots:1026401931398226021> Name', value='`𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐆𝐀𝐋𝐀𝐗𝐘`', inline=False)

    embed.add_field(name='<:x_member:1026132129769340928> User Count',

                    value=f'`{len(set(client.get_all_members()))}`',

                    inline=False)

    embed.add_field(name='🟢 Ping',

                    value=f'`{int(client.latency * 1000)}`',

                    inline=False)

    embed.add_field(name='<:x_owners:1026132165861322784> Creator', value=f'`737 么 𝑵𝒂𝒌𝒔𝒉#5839`', inline=False)

    embed.set_thumbnail(

        url=

        'https://cdn.discordapp.com/icons/975450975475236924/2a48d9b8dfe209f51a8ff4badbfee5d5.png?size=1024'

    )

    await ctx.send(embed=embed)

@client.command("ban")

@commands.has_permissions(administrator=True)

async def ban(ctx, user: discord.Member, *, reason="No reason provided"):

    await user.ban(reason=reason)

    ban = discord.Embed(

        title=f"<:x_tick:1026132299672207451> | SuccessFully Banned {user.name}",

        description=f"Reason: {reason}\nBy: {ctx.author.mention}")

    await ctx.message.delete()

    await ctx.channel.send(embed=ban)

    await user.send(embed=ban)

@client.command(aliases=["clear"])

@commands.has_permissions(administrator=True)

async def purge(ctx, amount=5):

    await ctx.channel.purge(limit=amount + 1)

@client.command("slowmode")

@commands.has_permissions(administrator=True)

async def slowmode(ctx, seconds: int):

    await ctx.channel.edit(slowmode_delay=seconds)

    await ctx.send(f"**<:x_tick:1026132299672207451> | SuccessFully Changed Slowmode To `{seconds}` Seconds!**")

@client.command(aliases=["mc"])

async def membercount(ctx):

  scembed = discord.Embed(colour=discord.Colour(0x2f3136))

  scembed.add_field(name='__Members__', value=f"{ctx.guild.member_count}")

  await ctx.reply(embed=scembed, mention_author=False)

@client.command(aliases=["rr"])

@commands.has_permissions(administrator=True)

async def removerole(ctx, member: discord.Member, role: discord.Role):

    await member.remove_roles(role)

    await ctx.reply(f"<:x_tick:1026132299672207451> | Removed {role} from {member.mention}")

@client.command()

async def prefix(ctx, prefix):

    if ctx.author.guild_permissions.administrator:

        client.command_prefix = str(prefix)

        await ctx.message.delete()

        await ctx.send('<:x_tick:1026132299672207451> | Successfully Changed The Prefix')

@client.command(name="userinfo")

async def ui(ctx, user: discord.Member = None):

    if user == None:

        user = ctx.author

    rlist = []

    for role in user.roles:

        if role.name != "@everyone":

            rlist.append(role.mention)

    b = ", ".join(rlist)

    embed = discord.Embed(colour=0x2f3136, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),

    embed.set_thumbnail(url=user.avatar_url),

    embed.set_footer(text=f'Requested by - {ctx.author}',

                     icon_url=ctx.author.avatar_url)

    embed.add_field(name='<:x_black_dot:1026399851207987260> ID:',

                    value=user.id,

                    inline=False)

    embed.add_field(name='<:x_black_dot:1026399851207987260> Name:',

                    value=user.display_name,

                    inline=False)

    embed.add_field(name='<:x_black_dot:1026399851207987260> Created at:',

                    value=user.created_at,

                    inline=False)

    embed.add_field(name='<:x_black_dot:1026399851207987260> Joined at:',

                    value=user.joined_at,

                    inline=False)

    embed.add_field(name='<:x_black_dot:1026399851207987260> Bot?',

                    value=user.bot,

                    inline=False)

    embed.add_field(

        name=f'<:x_black_dot:1026399851207987260> Roles:({len(rlist)})',

        value=''.join([b]),

        inline=False)

    embed.add_field(name='<:x_black_dot:1026399851207987260> Top Role:',

                    value=user.top_role.mention,

                    inline=False)

    await ctx.send(embed=embed)

  

@client.command(aliases=["av"])

async def avatar(ctx, user: discord.Member = None):

    if not user:

        user = ctx.author

    av = user.avatar_url

    embed = discord.Embed(

        description="<:x_black_dot:1026399851207987260> Avatar of {}".format(

            user.mention),

        color=discord.Color.random())

    embed.set_image(url=av)

    await ctx.send(embed=embed)

@client.command(aliases=["ar"])

@commands.has_permissions(administrator=True)

async def addrole(ctx, member: discord.Member, role: discord.Role):

    await member.add_roles(role)

    await ctx.reply(f"Added {role} to {member.mention}")

@client.command()

async def ping(ctx):

    embed = discord.Embed(color=0x2f3136, 

        title="Ping!",

        description=

        f"**`{int(client.latency * 1000)}ms`**")

    embed.set_thumbnail(

        url=

        'https://cdn.discordapp.com/emojis/885681753593872455.gif?size=2048'

    )

    await ctx.reply(embed=embed)

@client.event

async def on_member_join(ctx, *, member):

    channel = member.server.get_channel("1035487466003632190")

    fmt = 'Welcome to 𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐆𝐀𝐋𝐀𝐗𝐘, {0.mention}'

    await ctx.send_message(channel, fmt.format(member, member.server))

@client.command()

@commands.has_permissions(manage_emojis=True)

async def steal(ctx, emotes: Greedy[Union[discord.Emoji,

                                          discord.PartialEmoji]]):

    if not emotes:

        return await ctx.send(

            '**<a:x_bruhspin:1026165097191706676> | You didn\'t specify any emotes**'

        )

    in_server, added = [], []

    for emote in emotes:

        if isinstance(emote, discord.Emoji) and emote.guild == ctx.guild:

            in_server.append(emote)

        else:

            added.append(await ctx.guild.create_custom_emoji(

                name=emote.name,

                image=await emote.url.read(),

                reason=

                f'**<a:x_bruhspin:1026165097191706676> | Added by {ctx.author} ({ctx.author.id})**'

            ))

    if not added:

        return await ctx.send(

            f'**<a:x_bruhspin:1026165097191706676> | Specified emote{"s" if len(emotes) != 1 else ""} are already in this server**'

        )

    if in_server:

        return await ctx.send(

            f'**{" ".join(map(str, added))} | have been added to this server, while**'

            f'**{" ".join(map(str, in_server))} | wasn\'t because they are already added!**'

        )

    await ctx.send(

        f'**{" ".join(map(str, added))} | has been added to this server!**')

@client.command(name="boost")

async def boost(ctx):

    await ctx.send(embed=discord.Embed(

        title=

        "<:x_pepe_boost:1026079978900693062> Total Boosts <:x_pepe_boost:1026079978900693062>",

        description="**`%s`**" % (ctx.guild.premium_subscription_count),

        color=0x2f3136))

@client.command(aliases=['rolecreate'])

@commands.has_permissions(

    manage_roles=True

)  # Check if the user executing the command can manage roles

async def create_role(ctx, *, name):

    guild = ctx.guild

    await guild.create_role(name=name)

    await ctx.send(f'**<:x_tick:1026132299672207451> | SuccessFully Created Role `{name}`**')

@client.command()

@commands.has_permissions(kick_members=True)

async def warn(ctx, member: discord.Member, *, reason="No Reason Provided!"):

    await ctx.reply(

        f"**<:x_tick:1026132299672207451> | SuccessFully Warned `{member.display_name}` Reason `{reason}`**"

    )

    await member.send(

        f"**❗ | You have been warned in `{ctx.guild.name}` Reason `{reason}`**")

@client.command()

async def serverbanner(ctx):

    embed = discord.Embed(title=ctx.guild.name, color=0x2f3136)

    embed.set_image(url=ctx.guild.banner_url)

    embed.set_footer(text=f"Requested by {ctx.author}")

    await ctx.reply(embed=embed)

@client.command(aliases=['icon', 'sicon'])

async def servericon(ctx):

    embed = discord.Embed(title=ctx.guild.name, color=0x2f3136)

    embed.set_image(url=ctx.guild.icon_url)

    embed.set_footer(text=f"Requested by {ctx.author}")

    await ctx.reply(embed=embed)

def restart_client():

    os.execv(sys.executable, ['python'] + sys.argv)

@client.command()

@commands.is_owner()

async def restart(ctx):

  await ctx.send(f"**<:x_tick:1026132299672207451> | Successfully Restarted The Bot**")

  restart_client()

@client.event

async def on_member_join(member):

  guild = client.get_guild(1032537567410802718)

  channel = guild.get_channel(1035487466003632190)

  message = await channel.send(f"**Welcome to 𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐆𝐀𝐋𝐀𝐗𝐘 {member.mention}**")

@client.command()

@commands.has_permissions(administrator=True)

async def hide(ctx):

    await ctx.channel.set_permissions(ctx.guild.default_role,

                                      view_channel=False)

    await ctx.reply(

        '**<:x_tick:1026132299672207451> This Channel Is Now Hidden From Everyone**'

    )

@client.command()

@commands.has_permissions(administrator=True)

async def unhide(ctx):

    await ctx.channel.set_permissions(ctx.guild.default_role,

                                      view_channel=True)

    await ctx.reply(

        '**<:x_tick:1026132299672207451> | This Channel Is Now Visible To Everyone**'

    )

    await ctx.channel.purge(limit=2)

@client.command()

async def invites(ctx):

    totalInvites = 0

    for i in await ctx.guild.invites():

        if i.inviter == ctx.author:

            totalInvites += i.uses

    await ctx.send(

        f"**You've invited** ``{totalInvites}`` **Members**{'' if totalInvites == 1 else ''} **to the server!**"

    )

@client.command(aliases=["unbanall"])

@commands.has_permissions(administrator=True)

async def unbanalll(ctx):

    guild = ctx.guild

    banlist = await guild.bans()

    await ctx.reply(

        '**<:x_tick:1026132299672207451> | SuccessFully Unbanned {} Members**'

        .format(len(banlist)))

    for users in banlist:

        await ctx.guild.unban(user=users.user, reason=f"By {ctx.author}")

@commands.has_permissions(administrator=True)

@client.command()

@commands.cooldown(1, 10, commands.BucketType.user)

async def roleall(ctx, *, role: discord.Role):

        num = 0

        failed = 0

        for user in list(ctx.guild.members):

            try:

                await user.add_roles(role)

                num += 1

            except Exception:

                failed += 1

        await ctx.send(f"Adding roles to all user is in progress...")

        await ctx.send(embed=discord.Embed(title="Roleall", description="Successfully added **`%s`** to **`%s`** users, failed to add it to **`%s`** users" % (role.name, num, failed), color=0x2f3136))

@client.command()

@commands.has_permissions(administrator=True)

async def nuke(ctx):

        channelthings = [ctx.channel.category, ctx.channel.position]

        await ctx.channel.clone()

        await ctx.channel.delete()

        embed=discord.Embed(title=f'Nuked Channel!', description=f'**Channel was nuked by {ctx.author.name}**',color=0x2f3136, timestamp=ctx.message.created_at)

        embed.set_image(url="https://cdn.discordapp.com/icons/975450975475236924/2a48d9b8dfe209f51a8ff4badbfee5d5.png?size=1024")

        nukedchannel = channelthings[0].text_channels[-1]

        await nukedchannel.edit(position=channelthings[1])

        await nukedchannel.send(embed=embed)

@client.command()

async def about(ctx):

    embed = discord.Embed(title='About Me:', color=0x2f3136)

    embed.set_thumbnail(url='https://cdn.discordapp.com/banners/944308839447150643/d00e55c7202cde568cfb3a306c95d98b.webp?size=2048')

    

    embed.add_field(name='**My Information**', value='I Am MUSICAL GALAXY And Am Made By 737 么 𝑵𝒂𝒌𝒔𝒉#5839 for Managing This Server & Its a Private Bot!.', inline=False)

    

    embed.add_field(name='<:x_bot_devloper:1026131847425556662> **Developer**', value=f'`NAKSH`', inline=False)

@client.command()

@commands.has_permissions(administrator=True, manage_roles=True)

async def resetinvites(ctx, member: discord.Member=None):

    mem = member or ctx.author

    for i in await ctx.guild.invites():

        if i.inviter == mem:

             await i.delete()

    await ctx.send(f"**<:x_tick:1026132299672207451> | SuccessFully Cleared Invites of {mem.mention}**")

@client.command(name="lockall",

                description="**<:x_tick:1026132299672207451> | SuccessFully Locked Whole Server**",

                usage="lockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def lockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=False),

                reason=reason)

        await ctx.send(f"**<:x_tick:1026132299672207451> | {server}** Has Been Locked\nReason: `{reason}`")

    except:

        await ctx.send(f"**<:x_cross:1026131900311556096> | Failed to Lock, {server}**")

    else:

        pass

@client.command(

    name="unlockall",

    description=

    "Unlocks the server. | Warning: this unlocks every channel for the everyone role.",

    usage="unlockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def unlockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=True),

                reason=reason)

        await ctx.send(f"**<:x_tick:1026132299672207451> | {server}** has been unlocked.\nReason: `{reason}`")

    except:

        await ctx.send(f"**<:x_cross:1026131900311556096> | Failed to unlock, {server}**")

    else:

        pass

@client.command()

async def banner(ctx, user:discord.Member):

    if user == None:

       user = ctx.author

    bid = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))

    banner_id = bid["banner"]

    

    if banner_id:

       embed = discord.Embed(color= 0x2f3136)

       embed.set_author(name=f"{user.name}'s Banner")

       embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")

       await ctx.reply(embed = embed)

    else:

       embed = discord.Embed(title='FUZION', color=0x2f3136, description=f"**`User has no banner`**")

       await ctx.reply(embed = embed)

@client.command()

@commands.has_permissions(manage_messages=True)

async def mute(ctx, member: discord.Member, *, reason=None):

    guild = ctx.guild

    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:

        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:

            await channel.set_permissions(mutedRole, speak=False, send_messages=False)#, read_message_history=True, read_messages=False , view_channels = True

                

    await member.add_roles(mutedRole, reason=reason)

    embed = discord.Embed(color=0x2f3136 , title="MUSICAL GALAXY")

    embed.set_thumbnail(url="https://cdn.discordapp.com/banners/944308839447150643/d00e55c7202cde568cfb3a306c95d98b.webp?size=2048")

    embed.add_field(name="Muted", value=f"```Muted- ```{member.mention}" , inline = False)

    embed.set_footer(text="MUSICAL GALAXY", icon_url="https://images-ext-2.discordapp.net/external/g1EDDsCBJZLwGy4LbtLpKHSYo8HmmuxxbGTPb5F_3J4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1017801800100880486/25c706f1a645babb99f80cde597ab930.png")

    await ctx.reply(embed = embed , mention_author = False)

@client.command(description="Unmutes a specified user.")

@commands.has_permissions(manage_messages=True)

async def unmute(ctx, member: discord.Member):

    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)

    embed = discord.Embed(color=0x2f3136 , title="MUSICAL GALAXY")

    embed.add_field(name="UnMuted", value=f"```Unmuted-```{member.mention}" , inline = False)

    embed.set_footer(text="MUSICAL GALAXYÀ", icon_url="https://images-ext-2.discordapp.net/external/g1EDDsCBJZLwGy4LbtLpKHSYo8HmmuxxbGTPb5F_3J4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1017801800100880486/25c706f1a645babb99f80cde597ab930.png")

    embed.set_thumbnail(url="https://cdn.discordapp.com/banners/944308839447150643/d00e55c7202cde568cfb3a306c95d98b.webp?size=2048")

    await ctx.reply(embed = embed , mention_author = False)

@client.command(name='kick',

                description='Kick someone from the server',

                usage="kick <user>")

@commands.has_guild_permissions(administrator=True)

@commands.cooldown(2, 5, commands.BucketType.channel)

async def kick(ctx, member: discord.Member, *, reason=None):

    await ctx.message.delete()

    guild = ctx.guild

    if ctx.author == member:

        await ctx.send(('Do you really want to kick yourself?'),

                       delete_after=20)

    elif ctx.author.top_role <= member.top_role:

        await ctx.send(f"**You can't kick a member above you.**")

    elif ctx.author.top_role == member.top_role:

        await ctx.send(f"**You can't kick member having same role as you**")

    elif ctx.guild.owner == member:

        await ctx.send(('You cannot kick the server owner'), delete_after=20)

    else:

        if reason == None:

            try:

                try:

                    #    await member.send(embed=create_embed(f"**You have been kicked from {guild.name}**"))

                    await member.kick(reason=f"Responsible: {ctx.author}")

                    kickembed = discord.Embed(

                        description=f'**<:x_tick:1026132299672207451> | SuccessFully Kicked {member}**',

                        colour=0x2f3136)

                    kickembed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=kickembed)

                except:

                    await member.kick(reason=f"Responsible: {ctx.author}")

                    kick2embed = discord.Embed(

                        description=f'**<:x_tick:1026132299672207451> | SuccessFully Kicked {member}**',

                        colour=0x2f3136)

                    kick2embed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=kick2embed)

            except Exception as e:

                await ctx.send(f"**<:x_cross:1026131900311556096> | Failed To Kick {member}**")

        else:

            try:

                #    await member.send(embed=create_embed(f"**You have been kicked from {guild.name} for *{reason}***"))

                await member.kick(reason=reason)

                kick3embed = discord.Embed(

                    description=f'**<:x_tick:1026132299672207451> | SuccessFully Kicked {member}**\nReason: `{reason}`',

                    colour=0x2f3136)

                kick3embed.set_footer(text=f"Responsible: {ctx.author}")

                await ctx.send(embed=kick3embed)

            except Exception as e:

                await ctx.send(f"**<:x_cross:1026131900311556096> | Failed To Kick {member}**")

@client.command()

@commands.has_permissions(administrator=True, manage_roles=True)

async def resetall(ctx):

    for i in await ctx.guild.invites():

        await i.delete()

    await ctx.send(f"**<:x_tick:1026132299672207451> | SuccessFully Removed All Of Invites Of The Guild**")

@client.command()

async def roleinfo(ctx, role: discord.Role = None):

  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x2f3136))

  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}")

  await ctx.reply(embed=riembed, mention_author=False)

@client.command()

@commands.has_permissions(ban_members=True)

async def fuckban(ctx, user: discord.Member, *, reason="No reason provided"):

  await user.ban(reason=f"Banned by {ctx.author.name} reason: {reason}.")

  await ctx.reply(f"**<:x_tick:1026132299672207451> | {user.name} Has Been SuccessFully FuckBanned By {ctx.author.name}**", mention_author=False)

values = psutil.virtual_memory()

val2 = values.available * 0.001

val3 = val2 * 0.001

val4 = val3 * 0.001

values2 = psutil.virtual_memory()

value21 = values2.total

values22 = value21 * 0.001

values23 = values22 * 0.001

values24 = values23 * 0.001

@client.command(aliases=["host"])

async def hostinfo(ctx):

    embed = discord.Embed(color=0x2f3136, title=f"__Musical Galaxy Host Information__",

        description=

        f"\n\n> <:x_black_dot:1026399851207987260> **CPU Usage**\n> <:x_Reply_Black:1026131670203633854> {psutil.cpu_percent(1)} %\n> \n> <:x_black_dot:1026399851207987260> **Total Cores**\n> <:x_Reply_Black:1026131670203633854> {psutil.cpu_count()}\n> \n> <:x_black_dot:1026399851207987260> **Physical Cores**\n> <:x_Reply_Black:1026131670203633854> {psutil.cpu_count(logical=False)}\n> \n> <:x_black_dot:1026399851207987260> **Total Ram**\n> <:x_Reply_Black:1026131670203633854> {round(values24, 2)} GB\n> \n> <:x_black_dot:1026399851207987260> **Available Ram**\n> <:x_Reply_Black:1026131670203633854> {round(val4, 2)} GB"

    )

    embed.set_thumbnail(url="https://cdn.discordapp.com/banners/944308839447150643/d00e55c7202cde568cfb3a306c95d98b.png?size=1024")

    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

    await ctx.send(embed=embed)

@client.event

async def on_guild_update(before, after):

  if "VANITY_URL" in after.features:

           with open("vanity.json") as f:

                vanity = json.load(f)

                stored_vanity = vanity[str(after.guild.id)]

           return await after.edit(vanity_code=stored_vanity)

  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()

  logs = logs[0]

  if logs.user == after.owner: return

  await logs.user.ban(reason="MUSICAL GALAXY Anti-Guild-Update")

  await after.edit(name=f"{before.name}")

@commands.cooldown(3, 300, commands.BucketType.user)

@commands.has_permissions(administrator=True)

@client.command(aliases=["cc"])

async def channelclean(ctx, channeltodelete):

    for channel in ctx.message.guild.channels:

            if channel.name == channeltodelete:

                try:

                    await channel.delete()

                except:

                  pass

@commands.cooldown(3, 300, commands.BucketType.user)

@commands.has_permissions(administrator=True)

@client.command(aliases=["cr"])

async def roleclean(ctx, roletodelete):

    for role in ctx.message.guild.roles:

            if role.name == roletodelete:

                try:

                    await role.delete()

                except:

                  pass

@client.event

async def on_message(message):

  await client.process_commands(message)

  member = message.author

  if "MessageType.premium_guild" in str(message.type):

    guild = client.get_guild(1032537567410802718)

    channel = client.get_channel(1035086063179399198)

    await channel.send(f"Thanks For Boosting Our Server, {member.mention}")

  

keep_alive()

token = os.environ['TOKEN']

client.run(token)
