# Importing the necessary class libraries for discord bot.

import discord 
import os 
import random 
from ec2_metadata import ec2_metadata 
# Importing the dotenv class library so that we can securly acces our discord bot token.
from dotenv import load_dotenv 

# Printing out the necessary ec2_metadata.
print(ec2_metadata.public_ipv4)
print(ec2_metadata.region)
print(ec2_metadata.instance_id)
print(ec2_metadata.availability_zone)

load_dotenv() 

# Creating the discord client.
client = discord.Client() 
# Getting the bot token from the env file.
token = os.getenv('TOKEN')

# Indicating that the bot is ready and successfully logged in.
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))


@client.event 
# Extracting relavent information from the message.
async def on_message(message): 
	# Extracting the username from the message author's string.
	username = str(message.author).split("#")[0] 
	# Getting the name of the channel where the message was sent.
	channel = str(message.channel.name) 
	# Extracting the content of the message.
	user_message = str(message.content) 

	# Printing information about the message to the console.
	print(f'Message {user_message} by {username} on {channel}') 



	# Makes sure the bot only responds to users and not itself.
	if message.author == client.user: 
		return
	
	# Checks if the message is sent in the random channel and initiates if statements.
	if channel == "random": 
		# Makes all user input lowercase.
		if user_message.lower() == "hello" or user_message.lower() == "hi" or user_message.lower() == "hello world": 
			await message.channel.send(f'Hello what can I do for you? {username}') 
			return
		
		elif user_message.lower() == "whats going on":            						   #user input messages  
			await message.channel.send(f'Nothing much just waiting around {username}')      #bot responses 

		elif user_message.lower() == "Who created you": 
			await message.channel.send(f'Bezza {username}')

		elif user_message.lower() == "tell me about my server": 
			await message.channel.send(f'Here is your IP Address: {ec2_metadata.public_ipv4}, your EC2 Region: {ec2_metadata.region}, and your Availability Zone: {ec2_metadata.availability_zone}  {username}')

		elif user_message.lower() == "bye": 
			await message.channel.send(f'Bye {username}')
		# If the message is "tell me a joke" a random selection will be chosen from the jokes list.
		elif user_message.lower() == "tell me a joke": 
			jokes = [" RIP boiling water\ you will be mist", 
					"Which Bear is the most condescending\ A pan-duh.", 
					"What do you call it when Batman skips church \ Christian Bale.",
					"I know a ton of dad jokes...\ I keep them all in my dad-abase."] 
			await message.channel.send(random.choice(jokes)) 
		# Last else statement notifying the user of an incorrect input 
		else:
			await message.channel.send("I don't understand, Please provide a correct prompt.") 


# Run the bot with the token.
client.run(token)