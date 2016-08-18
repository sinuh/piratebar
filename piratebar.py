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


print "Welcome to the Sandy Shorts Pirate Bar! Tell me how ya like yer poison!"
print ""

def preference ():
  global prefs
  prefs = {}
  for key, question in questions.items ():
    my_preference = raw_input ("{} (y/n): ".format (question))
    if my_preference == "y":
      print "So ya like'em", key, "? Great! a pirate after me own heart!"
      prefs[key]=True
    elif my_preference == "n":
      print "So ya don't like'em", key, "? No problem matey!"
      prefs[key]=False
    else:
      print "C'mon, Yes or No ?!?!?"
  return prefs

def drink(preference):
  hooch = []
  for flavor, choice in prefs.items():
      if choice == True:
        hooch.append (random.choice(ingredients[flavor]))
      else:
        continue
  return hooch

def main():
  preference()
  hooch = drink(preference)
  print ""
  print "Alrighty matey, that'll be:"
  for ingredient in hooch:
    print "A {}" .format(ingredient)
  print ""
  print "Enjoy yer poison ya scallywag!"
  
if __name__ == "__main__":
  main()
