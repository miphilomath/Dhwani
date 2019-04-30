"""
Function: 
* To take string input fro mstt
* To convert all the compound statements into simple statements.
* For each simple sentences, characterise verb, adjective and noun
* Send the tokenized sentence to the sentiment analyzer
* Pair all the verb and noun as (action, target)

python -m textblob.download_corpora


References: (https://www.clips.uantwerpen.be/pages/MBSP-tags)
NN: Noun
NP: Noun Phrase
JJ: Adjective
RB: Adverb
IN: Preposition
VB: Verb
VP: Verb Phrase
NP-SUBJ: Subject
NP-OBJ: object
DT: Determiners
WDT: wh-Determiners
MD: Modal Auxillary
"""

from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()
#text = "open the browser"
text = str(input())

blob = TextBlob(text.lower(), np_extractor=extractor)
print (blob.pos_tags)

verb = []
noun = []

for _tuple in blob.pos_tags:
	if _tuple[1] in ("VBZ", "VB", "RB"):
		# Add the action to the action dictionary key
		verb.append(_tuple[0])
		#print(verb)
	elif _tuple[1] in ("NN", "NP", "NNP"):
		# Add the target to the action dictory value
		noun.append(_tuple[0])
		#print(noun)

my_dict = {}
for index in range(len(verb)):
	my_dict[verb[index]] = noun[index]

print(my_dict)
