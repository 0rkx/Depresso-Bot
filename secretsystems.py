import discord
from discord.ext import commands
import json
import os
import random
import asyncio
import datetime
import praw
from PIL import Image , ImageFont , ImageDraw
from io import BytesIO
import requests
import asyncpraw
import wikipedia,os
from chatbot import Chat, register_call
import aiohttp
import platform

reddit = praw.Reddit(client_id = "MBHk2bWsfxZppQ" ,
                     client_secret = "rthaxUeYHVlKzgUbLy30_Ui6zl-giw"  , 
                     username = "0rkx_Bot ",
                     password = "owais2006" ,
                     user_agent = "0rxBot" )



intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!" , intents=intents)

client.remove_command('help')




mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"}]



@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms :white_check_mark:')
    

@client.command()
async def link(ctx):
    await ctx.send(
        "https://discord.com/oauth2/authorize?client_id=814488533384429678&permissions=8&scope=bot"
    )
@client.command()
@commands.has_permissions(kick_members = True)
async def poll(ctx,*,message):
    emb=discord.Embed(title="POLL", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    
@client.command()
async def meme(ctx):
	async with ctx.channel.typing():
	    reddit  = asyncpraw.Reddit(client_id = "haeimp-lUnhNcw", client_secret = "nZL64R7MdQg8lc0qa3XFtnsnT7zTpQ", username = "0rkx_Bot", password = "Obaid2020", user_agent = "0rxBot")
	    subreddit = await  reddit.subreddit("memes")

	    all_subs = []
	      
	    async for submission in subreddit.hot(limit=30):
	            all_subs.append(submission)
	            random_sub = random.choice(all_subs)
	            name = random_sub.title
	            url = random_sub.url
	            score = random_sub.score

	          
	    embed = discord.Embed(
	        description =  f"**[{name}]({url})**",

	        color = int("0x{:06x}".format(random.randint(0, 0xFFFFFF)), 16)


	    )

	    
	    embed.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
	    embed.set_image(url=url)
	    embed.set_footer(text=f"👍 {score}")

	    await ctx.send(embed=embed)


#(@client.command()
#async def meme(ctx):
   # await ctx.message.delete()
   # subreddits = await reddit.subreddit("memes")
   # async for submission in subreddits.hot(limit=20):
   #     post_to_pick = random.randint(1, 20)
   # for i in range(0, post_to_pick):
  #      submission = await subreddits.random()
  #  await ctx.send(submission.url)
#)


@client.command(aliases = ["userinfo"])
async def whois(ctx, member:discord.Member =  None):

    if member is None:
        member = ctx.author
        roles = [role for role in ctx.author.roles]

    else:
        roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name="User Info: ")
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="User Name:",value=member.display_name, inline=False)
    embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
    embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
    embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
    embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Top Role:", value=member.top_role, inline=False)
    embed.add_field(name="Bot?:", value=member.bot, inline=False)
    await ctx.send(embed=embed)
    return


@client.command()
async def covid( ctx, *, countryName = None):
    try:
        if countryName is None:
            embed=discord.Embed(title="This command is used like this: ```!covid [country]```", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


        else:
            url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
            stats = requests.get(url)
            json_stats = stats.json()
            country = json_stats["country"]
            totalCases = json_stats["cases"]
            todayCases = json_stats["todayCases"]
            totalDeaths = json_stats["deaths"]
            todayDeaths = json_stats["todayDeaths"]
            recovered = json_stats["recovered"]
            active = json_stats["active"]
            critical = json_stats["critical"]
            casesPerOneMillion = json_stats["casesPerOneMillion"]
            deathsPerOneMillion = json_stats["deathsPerOneMillion"]
            totalTests = json_stats["totalTests"]
            testsPerOneMillion = json_stats["testsPerOneMillion"]

            embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description="This Information Isn't Live Always, Hence It May Not Be Accurate!", colour=0x0000ff, timestamp=ctx.message.created_at)
            embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
            embed2.add_field(name="**Today Cases**", value=todayCases, inline=True)
            embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
            embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
            embed2.add_field(name="**Recovered**", value=recovered, inline=True)
            embed2.add_field(name="**Active**", value=active, inline=True)
            embed2.add_field(name="**Critical**", value=critical, inline=True)
            embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
            embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
            embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
            embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
            await ctx.send(embed=embed2)

    except:
        embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0xff0000, timestamp=ctx.message.created_at)
        embed3.set_author(name="Error!")
        await ctx.send(embed=embed3)

@client.command()
async def members(ctx):

    embed = discord.Embed(title=f"There are {len(ctx.guild.members)} members in {ctx.guild.name}!", colour=0xffff00, timestamp=ctx.message.created_at)
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)


@client.event
async def on_ready():
    print ("Ready")
    await client.change_presence(activity=discord.Game(f"!help | In {len(client.guilds)} servers"))


    
@client.command(name="help" )
async def help(ctx ): 
     embed=discord.Embed(title="Help", color=0x691b1b)
     embed.set_author(name="0.rkx Bot")
     embed.add_field(name="General Commands", value=""" 
ping                (Used To See The Ping)
help                (Shows This Message)""", inline=False)
     embed.add_field(name="Useful Commands", value="""
whois               (More info About User)
serverinfo          (More info in Sevrer)
covid               (Corona Sats OF THe Country)
avatar              (Used To See The User's Avatar)""", inline=False)
     embed.add_field(name="Fun Commands", value="""
Spank               (Used To Spank Someone)
Wanted              (i cant think of what to put here)
Beat                (Well Try It...)""", inline=True)
     embed.add_field(name="Economy Commands", value=""" 
beg                 (2 Mins Cooldown)
shop                (Shows The Shop)
withdraw            (Used To Withdraw Money From The Bank)
balance             (Shows The Balance Left)
deposit             (Used To Deposit Money in The Bank) 
rob                 (Used To Rob Someone)
slots               (A Mini Game That Helps You Earn Cash)
leaderBoard         (Used To View The Leaderboard)
buy                 (Used To Buy Something From The Shop)
sell                (Used To Sell Something From Bag)
bag                 (Used You See Your Inventory)""", inline=True)
     embed.set_footer(text="Thank You For Using My Bot | More Commands Will Be Added Soon Thank You Stay Tuned")
     await ctx.send(embed=embed)
    


@client.command(name="balance", aliases=["bal"])
async def balance(ctx , user : discord.Member = None):
    await open_account(ctx.author)
    if user is None :
        user = ctx.author
        return
    
    
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"] 
    em = discord.Embed(title = f"{user.name}'s Balance" , color = discord.Color(15105570))
    em.set_footer(text=f"Requested by: {ctx.author}", )
    em.add_field(name = "Wallet Bal", value = wallet_amt , inline=False )
    em.add_field(name = "Bank Bal", value = bank_amt , inline=False )
    em.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed = em)


@commands.cooldown(1, 120, commands.BucketType.user)    
@client.command()
async def beg(ctx) :
    await open_account(ctx.author)
    
    users = await get_bank_data()
    
    user = ctx.author
    
    earnings = random.randrange(501)
    
    await ctx.send(f"Someone Gave You {earnings} coins!!")
    
    
   
    
    users[str(user.id)]["wallet"] += earnings
    
    with open("yes.json" , "w" ) as f:
        json.dump(users,f)
        
@beg.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is In CoolDown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error
        
@client.command(name="withdraw", aliases=["with"])
async def withdraw(ctx, amount = None) :
    await open_account(ctx.author)
    
    
    if amount == None:
        await ctx.send("Please Enter The Amount")
        return
    
    bal = await update_bank(ctx.author)
    
    
    amount = int(amount)
    
    if amount>bal[1]:
        await ctx.send("You Dont Have That Much Money!")
        return
    if amount<0:
        await ctx.send("Amount Must Be Positive")
        return
    
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount , "bank")
    
    await ctx.send(f"You Withdrew {amount} coins")
    
    

    
@client.command(name="deposit", aliases=["dep"])
async def deposit(ctx, amount = None) :
    await open_account(ctx.author)
    
    
    if amount == None:
        await ctx.send("Please Enter The Amount")
        return
    
    bal = await update_bank(ctx.author)
    
    
    amount = int(amount)
    
    if amount>bal[0]:
        await ctx.send("You Dont Have That Much Money!")
        return
    if amount<0:
        await ctx.send("Amount Must Be Positive")
        return
    
    await update_bank(ctx.author,-1* amount)
    await update_bank(ctx.author, amount , "bank")
    
    await ctx.send(f"You Deposited  {amount} coins")
    
    
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed) 

    
@client.command()
async def send(ctx, member:discord.Member ,  amount = None) :
    await open_account(ctx.author)
    await open_account(member)
    
    if amount == None:
        await ctx.send("Please Enter The Amount")
        return
    if amount == "all":
        amount = bal[0]
    
    bal = await update_bank(ctx.author)
    
    
    amount = int(amount)
    
    if amount>bal[0]:
        await ctx.send("You Dont Have That Much Money!")
        return
    if amount<0:
        await ctx.send("Amount Must Be Positive")
        return
    
    await update_bank(ctx.author,-1* amount , "bank")
    await update_bank(member, amount , "bank")
    
    await ctx.send(f"You gave  {amount} coins")
    
    
@client.command()
async def slots(ctx , amount = None):
    await open_account(ctx.author)
    
    
    if amount == None:
        await ctx.send("Please Enter The Amount")
        return
    
    
    bal = await update_bank(ctx.author)
    
    
    amount = int(amount)
    
    if amount>bal[0]:
        await ctx.send("You Dont Have That Much Money!")
        return
    if amount<0:
        await ctx.send("Amount Must Be Positive")
        return
    final = []
    emoji_1 = random.choice(["😊" , "😛" , "🙃"])
    emoji_2 = random.choice(["😊" , "😛" , "🙃"])
    emoji_3 = random.choice(["😊" , "😛" , "🙃"])
        
    await ctx.send(f"{emoji_1} , {emoji_2} , {emoji_3}")
    
    if  emoji_1 == emoji_2 and emoji_2 == emoji_3 : 
        await update_bank(ctx.author,3* amount)
        await ctx.send("You Won")
    if emoji_1 == emoji_3:
        await update_bank(ctx.author , 1.5*amount)
        await ctx.send("You Win Half The Prize")
    else:
        await update_bank(ctx.author,-1* amount)
        await ctx.send("You Lost")
    
    
    
@client.command()
async def rob(ctx, member:discord.Member ) :
    await open_account(ctx.author)
    await open_account(member)
    
    
    bal = await update_bank(member)
    
    
    if bal[0]<100:
        await ctx.send("Its Not Worth It")
        return
    
    earnings = random.randrange(0 , bal[0])

    
    await update_bank(ctx.author,earnings)
    await update_bank(member, -1*earnings )
    
    await ctx.send(f"You robbed and got  {earnings} coins")
    
@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

@client.command(aliases = ["lb"])
async def leaderboard(ctx,x = 3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)
    
@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)



@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)    
    
    


        
    

#helper functions

async def open_account(user):
    
    users = await get_bank_data()
        
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        
    with open("yes.json" , "w" ) as f:
        json.dump(users,f)
    return True
    

async def get_bank_data():
    with open("yes.json" , "r" ) as f:
        users = json.load(f)
    return users
    
async def update_bank(user , change = 0, mode = "wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    
    with open("yes.json" , "w" ) as f:
        json.dump(users,f)
        
    bal = [users[str(user.id)]["wallet"] , users[str(user.id)]["bank"]]
    return bal

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("yes.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("yes.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

@client.command()
async def wanted(ctx, user: discord.Member = None):
     if user == None:
         user = ctx.author

    
     wanted = Image.open("wanted.png")

     asset = user.avatar_url_as(size = 128)

     data = BytesIO(await asset.read())
     pfp = Image.open(data)
     pfp = pfp.resize((161,161))

     wanted.paste(pfp , (102,168))

     wanted.save("profile.png")

     await ctx.send(file = discord.File("profile.png"))


@client.command()
async def spank(ctx , user : discord.Member = None):
    if user == None:
        await ctx.send("Please Specify A Member to Spank")
        return
    if user == ctx.author:
        await ctx.send("You Cant Spank Yoursef")
        return

    spank = Image.open("spank.jpg")


    asset = user.avatar_url_as(size = 128)
    asset1 = ctx.author.avatar_url_as(size = 128)

    data =  BytesIO(await asset.read())

    data1 = BytesIO(await asset1.read())

    pfp = Image.open(data)
    pfp = pfp.resize((190 , 190))
    userpfp = Image.open(data1)
    userpfp = userpfp.resize((213,213))
     
    spank.paste(pfp , (422,551))
    spank.paste(userpfp , (463,203))

    spank.save("spanked.jpg")

    await ctx.send(file = discord.File("spanked.jpg"))


@client.command()
async def beat(ctx , user : discord.Member = None):
    if user == None:
        await ctx.send("Please Specify A Member to Beat")
        return
    if user == ctx.author:
        await ctx.send("You Cant Beat Yoursef")
        return

    beat = Image.open("beat.png")


    asset = user.avatar_url_as(size = 128)
    asset1 = ctx.author.avatar_url_as(size = 128)

    data =  BytesIO(await asset.read())

    data1 = BytesIO(await asset1.read())

    pfp = Image.open(data)
    pfp = pfp.resize((158 , 158))
    userpfp = Image.open(data1)
    userpfp = userpfp.resize((127,127))
     
    beat.paste(pfp , (201,75))
    beat.paste(userpfp , (690,14))

    beat.save("beaten.png")

    await ctx.send(file = discord.File("beaten.png"))


@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    if avamember == None :
        avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



@client.command(aliases=["cs","ci","channelinfo"])
async def channelstats(ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel

        embed = discord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=discord.Colour.random())
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=True)
        embed.add_field(name="Channel Id", value=channel.id, inline=True)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=True)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=True)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=True)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=True)
        embed.add_field(name="Channel Permissions Synced",value=channel.permissions_synced,inline=True)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)

        await ctx.send(embed=embed)



@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        embed = discord.Embed(title="8-ball",description=f"{random.choice(responses)}",color=discord.Colour.green())
        await ctx.send(embed=embed)

@client.command(aliases=['sslowmode','slowmode'])
async def setslowmode(ctx,tm):
    t = convert_time_to_seconds(tm)
    await ctx.channel.edit(slowmode_delay=t)

    if tm.find('h')!=-1 or tm.find('s')!=-1 or tm.find('m')!=-1:
        await ctx.send(f"⌚ Set the slowmode delay in this channel to {tm}!",delete_after=10.5)
        return False
    else:
        await ctx.send(f"⌚ Set the slowmode delay in this channel to {tm}s!",delete_after=10.5)



def convert_time_to_seconds(time):
    time_convert = {"s": 1, "m": 60, "h": 3600}

    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = '' , description = f' Locked the Channel {channel.mention}' , color = discord.Color.green())
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = '' , description = f' Unlocked the Channel {channel.mention}' , color = discord.Color.green())
    await ctx.send(embed=embed)





@client.event

async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    argerroremb = discord.Embed(title=":7037_MonkaGun: | Missing Arguements !", description="Hey! You haven't given me all required arguments! How do you expect me to execute the command?")
    await ctx.send(embed=argerroremb)
  if isinstance(error, commands.MissingPermissions):
    permerroremb = discord.Embed(title=":7037_MonkaGun: | Missing Perms!", description="Hey! You don't have the permissions to use this command!")
    await ctx.send(embed=permerroremb)
  if isinstance(error, commands.MemberNotFound):
      memberroremb = discord.Embed(title=":7037_MonkaGun: | Member not found!", description="There ain't no member like that :|")
      await ctx.send(embed=memberroremb)
  if isinstance(error, commands.BotMissingPermissions):
      botpermerror = discord.Embed(title=":7037_MonkaGun: | Bot Missing Perms!", description="Hey I don't have the permssions to do that :v.")
      await ctx.send(embed=botpermerror)
  else :
       raise error

@client.command()
async def fraudcheck(ctx, member: discord.Member = None):
    member = member or ctx.author
    tod = datetime.datetime.now()
    today = datetime.date(tod.year, tod.month, tod.day)
    user = datetime.date(member.created_at.year, member.created_at.month, member.created_at.day)
    days = int(str(today-user).split()[0])
    if days <= 10:
        return await ctx.send('Fraudulent account located...')
    if days <= 60:
        return await ctx.send('Seems abit dodgy...')
    if days <= 120:
        return await ctx.send('Doesnt seem that bad...')
    else :
        await ctx.send('He\'s good to go...')

@client.command()
async def cat(ctx):
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('http://aws.random.cat/meow') as r:
                        data = await r.json()

                        em = discord.Embed(title='Cat',timestamp=ctx.message.created_at)
                        em.set_image(url = data['file'])
                        em.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")
                        await ctx.send(embed=em)




@client.command(aliases=["pepe"])
async def pp(ctx, *, user: discord.Member = None) :
    if user == None:
        user = ctx.author
    dong = "=" * random.randint(1, 15)
    embed= discord.Embed(title=f"{user.display_name}'s pepe size", description=f"8{dong}D", color=0xfff)
    await ctx.send(embed = embed)

@client.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    client.version = '0.4'
    embed = discord.Embed(title=f'{client.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value=client.version)
    embed.add_field(name='Python Version:', value=pythonVersion)
    embed.add_field(name='Discord.Py Version', value=dpyVersion)
    embed.add_field(name='Total Guilds:', value=serverCount)
    embed.add_field(name='Total Users:', value=memberCount)
    embed.add_field(name='Bot Developers:', value="<@691278451738411148>")

    embed.set_footer(text=f"Requested By {ctx.author} ")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

client.run("ODE0NDg4NTMzMzg0NDI5Njc4.YDeljg.MSmOXHLymyhuAhPhvVnKlDj1J2Q")