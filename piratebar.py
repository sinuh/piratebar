import random

def Preference():
	"""Makes up a list of drink preferences"""

	questions = {
    	"strong": "Do ye like yer drinks strong?",
    	"salty": "Do ye like it with a salty tang?",
    	"bitter": "Are ye a lubber who likes it bitter?",
    	"sweet": "Would ye like a bit of sweetness with yer poison?",
    	"fruity": "Are ye one for a fruity finish?"
	}

	prefs = {}

	for key, question in questions.items ():
		my_preference = ""
		while my_preference != "y" and my_preference != "n":
			my_preference = raw_input("{} (y/n): ".format (question))
			if my_preference == "y":
				print "So ya like'em", key, "? Great! a pirate after me own heart!"
				prefs[key]=True
				break
			elif my_preference == "n":
				print "So ya don't like'em", key, "? No problem matey!"
				prefs[key]=False
				break
			else:
				print "\nC'mon, Yes or No ?!?!?"

	return prefs

def drink(chosen_prefs):
	"""Gets a list of drink preferences and makes a list of flavours"""

	ingredients = {
    	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
    	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    	"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
	}

  	hooch = []
  	for flavor, choice in chosen_prefs.items():
		if choice == True:
			hooch.append (random.choice(ingredients[flavor]))
      	else:
			pass

  	return hooch

def main():
    """Starts everything"""

	print "\nWelcome to the Sandy Shorts Pirate Bar! Tell me how ya like yer poison!\n"

	chosen_hooch = drink(Preference())

	if len(chosen_hooch) != 0:
		print "\nAlrighty matey, that'll be:"
		for ingredient in chosen_hooch:
			print "A {}" .format(ingredient)
		print "\nEnjoy yer poison ya scallywag!\n"
	else:
		print"\nAlright matey, nothing to drink tonight\n"
  
if __name__ == "__main__":
	main()
