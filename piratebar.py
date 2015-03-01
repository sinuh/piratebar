import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def preference ():
  prefs = []
  for key, question in questions.items ():
    print key, "->", question
    my_preference = raw_input ("{} (y/n): ".format (question))
    if my_preference == "y":
      print "I want a drink thats ", key
      prefs.append (key)
    elif my_preference == "n":
      print "I don't want to drink that ", key
    else :
      print "WTF, Yes or No ?!?!?"
  return prefs
  
def drink (prefs):
  a = hash(prefs)
  b = ingredients(a)
  hooch = []
  for pair in b:
    if prefs == pair[0]:
      print "So ya like em", prefs, "? that'll be ", ingredient
      hooch.append (ingredient)
    else:
      continue
  return hooch

preference ()
print drink(preference)







    