import random

import os
import discord
from discord import app_commands
import datetime

token = os.environ.get('DISCORD_BOT_SECRET') #for secrets
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


dj = [ 
  "What does a baby computer call his father? Data.",
  "After an unsuccessful harvest, why did the farmer decide to try a career in music? Because he had a ton of sick beets.",
  "I only seem to get sick on weekdays. I must have a weekend immune system.",
  "My friend was showing me his tool shed and pointed to a ladder. “That's my stepladder",
  "What do you call a Frenchman wearing sandals? Philippe Flop.",
  "Why is it so cheap to throw a party at a haunted house? Because the ghosts bring all the boos.",
  "I don’t get why Marvel doesn’t use the Hulk to advertise more. He’s basically one big Banner.",
  "What brand of underwear do scientists wear? Kelvin Klein.",
  "Which days are the strongest? Saturday and Sunday. The rest are weekdays.",
  "Did you know your pupils are the last part to stop working when you die? They dilate.",
  "My wife asked me the other day where I got so much candy. I said",
  "I always have a few Twix up my sleeve.",
  "How do cows stay up to date? They read the Moo-spaper.",
  "What's the difference between a well-dressed man on a unicycle and a poorly-dressed man on a bicycle? Attire.",
  "I hate my job—all I do is crush cans all day. It’s soda pressing.",
  "Where do pirates get their hooks? Second hand stores.",
  "Of all the inventions of the last 100 years, the dry erase board has to be the most remarkable.",
  "In America, using the metric system can get you in legal trouble.",
  "In fact, if you sneer at any other method of measuring liquids, you may be held in contempt of quart.",
  "Who were the greenest Presidents in US history? The bushes.",
  "My hotel tried to charge me ten dollars extra for air conditioning. That wasn’t cool.",
  "What do you call a beehive without an exit? Unbelievable.",
  "If I ever find the doctor who screwed up my limb replacement surgery…I’ll kill him with my bear hands.",
  "Did you know that the first french fries weren’t cooked in France? They were cooked in Greece.",
  "This morning, Siri said, “Don’t call me Shirley.” I accidentally left my phone in Airplane mode.",
  "It's easy to convince ladies not to eat Tide Pods, but harder to deter gents.",
  "I asked my date to meet me at the gym but she never showed up. I guess the two of us aren't going to work out.",
  "How do you find Will Smith in a snowstorm? You look for fresh prints.",
  "The difference between a numerator and a denominator is a short line. Only a fraction of people will understand this",
  "I found a wooden shoe in my toilet today. It was clogged.",
  "I just broke up with my mathematician girlfriend. She was obsessed with an X.",
  "I can't take my dog to the pond anymore because the ducks keep attacking him. That's what I get for buying a pure bread dog.",
  "To whoever stole my copy of Microsoft Office, I will find you. You have my Word.",
  "What’s Forrest Gump’s password? 1forrest1.",
  "I used to run a dating service for chickens. But I was struggling to make hens meet.",
  "If prisoners could take their own mug shots…They’d be called cellfies.",
  "Have you heard about those new corduroy pillows? They're making headlines.",
  "If a pig loses its voice…does it become disgruntled?",
  "Wanna hear a joke about paper? Never mind. It's tearable.",
  "A panic-stricken man explained to his doctor, “You have to help me, I think I’m shrinking.” “Now settle down,” the doctor calmly told him. “You'll just have to learn to be a little patient.”",
  "What do you call a bundle of hay in a church? Christian Bale.",
  "A ship carrying red paint and a ship carrying blue paint collide in the middle of the ocean. Both crews were marooned.",
  "What is a guitar player's favorite Italian food? Strum-boli.",
  "How does cereal pay its bills? With Chex.",
  "Have you heard about the restaurant on the moon? Great food, no atmosphere.",
  "I don't trust stairs. They're always up to something.",
  "People in Athens rarely get up before sunrise. Dawn is tough on Greece.",
  "Why'd the alternate universe Spider-Man do so well on his driving test? He's an excellent parallel Parker.",
  "Never date a tennis player. Love means nothing to them.",
  "What's a lawyer's favorite drink? Subpoena colada.",
  "What did Yoda say when he saw himself in 4K? HDMI.",
  "What do you call a wizard who's really bad at football? Fumbledore.",
  "How do nonbinary people hurt each other? They slash them. (They/them)",
  "I used to hate facial hair, but then it grew on me.",
  "What's blue and not very heavy? Light blue.",
  "I don't get why bakers aren't wealthier. They make so much dough.",
  "I asked my wife if I was the only one she slept with. She said yes—the others were 7’s and 8’s.",
  "How do you make a tissue dance? You put a little boogie in it.",
  "How do flat-earthers travel? On a plane.",
  "I ordered a chicken and an egg from Amazon. I'll let you know.",
  "Imagine if you walked into a bar and there was a long line of people waiting to take a swing at you. That’s the punch line.",
  "My wife left me because of my obsession with pasta. I'm feeling cannelloni right now.",
  "What’s an astronaut’s favorite part of the computer? The Space Bar.",
  "I was playing chess with my friend and he said, “Let’s make this interesting.” So we stopped playing chess.",
  "I was in a job interview the other day and they asked if I could perform under pressure. I said no, but I could perform Bohemian Rhapsody.",
  "Why didn't the vampire attack Taylor Swift? She had bad blood.",
  "Today I’m attaching a light to the ceiling, but I’m afraid I’ll probably screw it up.",
  "I hate it when people say age is only a number. Age is clearly a word.",
  "I can't take my dog to the pond anymore because the ducks keep attacking him. That's what I get for buying a pure bread dog.",
  "Someone complimented my parking today! They left a sweet note on my windshield that said “parking fine.”",
  "I was excited to hear Apple might start selling its own cars until I learned they wouldn’t support windows.",
  "I just applied for a job down at the diner. I told them I really bring a lot to the table.",
  "Cop: I'm arresting you for downloading the entire Wikipedia. Man: Wait! I can explain everything!",
  "My friend couldn't afford to pay his bill, so I sent him a Get Well Soon card.",
  "I'm Buzz Aldrin, second man to step on the moon. Neil before me.",
  "Why was 2019 afraid of 2020? Because they had a fight and 2021.",
  "Did you hear Bruce Springsteen changed the lyrics to one of his songs? What’s he going to change next—his hair? His clothes? His face?",
  "This year’s Fibonacci convention is going to be really special. Apparently it’s as big as the last two put together.",
  "An apple a day keeps the doctor away. At least it does if you throw it hard enough.",
  "In 2017 I didn't do a marathon. I didn't do one in 2018, 2019, or 2020, either. This is a running joke.",
  "Not to brag but I made six figures last year. I was also named worst employee at the toy factory.",
  "Ever since we started quarantining, I've only been telling inside jokes.",
  "If you're feeling depressed, try drinking a gallon of water before you go to sleep. It'll give you a reason to get out of bed in the morning.",
  "What has five toes and isn't your foot? My foot.",
  "My friend claims he glued himself to his autobiography. I don't believe him, but that's his story and he's sticking to it.",
  "When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.",
  "What's brown and sticky? A stick.",
  "My doctor told me I was going deaf. The news was hard for me to hear.",
  "A century ago, two brothers decided it was possible to fly. And as you can see, they were Wright.",
  "I'm reading a horror story in braille. Something bad is going to happen, I can just feel it.",
  "Anyone looking to buy a Delorean? Good shape, good mileage. Only driven from time to time",
  "During my calculus test, I had to sit between identical twins. It was hard to differentiate between them.",
  "Does anybody know where a guy can find a person to hang out with, talk to, and enjoy spending time with? I'm just asking for a friend.",
  "Why did the Invisible Man turn down a job offer? He couldn’t see himself doing it.",
  "When I die, I want to be cremated. It’s my last chance to have a smokin’ hot body.",
  "Just say NO to drugs!” Well, if I’m talking to drugs, I probably already said yes.",
]
@tree.command(name="dadjoke", description="Get a dadjoke")
async def dadjoke_dadjoke(interaction):
  embed = discord.Embed(title=random.choice(dj), color=0xFF5733)
  embed.set_footer(text='Type: DadJoke')
  embed.set_author(name="Requested By " + str(interaction.user))
  await interaction.response.send_message(embed=embed)





@client.event
async def on_ready():
  await tree.sync()
  print('We have logged in as {0.user}'.format(client))


client.run(token)#if you dont want to store the token as a secret just put the token value here
