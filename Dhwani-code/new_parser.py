"""
Function: 
* To take string input fro mstt
* To convert all the compound statements into simple statements.
* For each simple sentences, characterise verb, adjective and noun
* Send the tokenized sentence to the sentiment analyzer
* Pair all the verb and noun as (action, target)

python -m textblob.download_corpora
"""

from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from textblob.sentiments import NaiveBayesAnalyzer
import stt

def parse(string):
	extractor = ConllExtractor()
	#text = "open the browser"
	text = string
	# Commands that Dhwani can handle and their respective targets
	commands = ['open', 'close', 'play', 'start', 'pause', 'stop', 'increase', 'increment', 'decrease', 'decrement', 'set', 'shutdown']
	actions = ['door', 'browser', 'song', 'music', 'player', 'brightness', 'volume']
	attributes = []

	blob = TextBlob(text)
	token_string = blob.words
	mood = blob.sentiment.polarity
	#print(mood)
	found = False

	e = 0.005 # To set range for the neutral mood.

	for index in range(len(token_string)):
		if token_string[index] in str(commands):
			found = True;
			#print(token_string[index])
			#Command found and look for the target
			for ahead in range(index, len(token_string)):
				if token_string[ahead] in str(actions):
					#print(token_string[ahead])
					# Call the execution function for (command, action)
					# Update the index with ahead + 1
					print("Add the execute command function");
					index = ahead + 1
					if token_string[ahead] == 'brightness' or 'volume':
						# If Brightness and volume, look for third attribute
						pass
		elif index == len(token_string) and found == False:
			# Invalid input. Say, "Can you rephrase your words?"
			print("Can you please rephrase your words?")

	if -1 <=  mood <= (0 - e):
		# Bad mood. Call function to cheer him/her up. Songs/jokes
		stt.say("Call the mood, cheer man!")
	if (0 + e) <=  mood <= 1:
		# happy mood. Say, "looks like you are enjoying your day!"
		stt.say("Enjoy the party man!")
	if (0 - e) <=  mood <= (0 + e):
		# Neutral sentiment output. Make a pun joke
		stt.say("Ohh cool")
	

