import random

# Subjects 
subjects = [
    "Shahrukh Khan",
    "Amitabh Bachchan",
    "Deepika Padukone",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from Delhi"
]

# Actions
actions = [
    "cancels",
    "launches",
    "dances with",
    "eats",
    "orders",
    "celebrates"
]

# Phrases
places_or_things = [
    "at Red Fort",
    "at Mumbai Local Train Station",
    "inside Parliament",
    "at Ganga Ghat",
    "During IPL match",
    "at Taj Mahal"
]

# Headline Genrator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        break

print("\nThanks for using our headline generator!")    
