import random 
saved_headlines = []
templates = [
    "{subject} {action} {person} at {place} — witnesses say 'it was wild!'",
    "BREAKING: {person} caught helping {subject} to {action} the world at {place}!",
    "Shocking: {subject} falls in love with {person} during a chaos at {place}"
]
categories = {
    "conspiracy":{
        "subjects": ["Aliens", "Secret Society", "Flat Earthers", "Time Travelers"],
        "actions": ["expose", "blame", "abduct", "control"],
        "objects": ["the internet", "world leaders", "moon landing", "Wi-Fi signals"]

    },
    "food":{
        "subjects": ["Burger", "Pizza", "Spaghetti", "French Fries"],
        "actions": ["is plotting", "has replaced", "declared war on", "was seen chasing"],
        "objects": ["a salad", "human taste buds", "global diet", "the microwave"]
    },
    "celebrity":{
        "subjects": ["Kanye West", "Taylor Swift", "The Rock", "Mr. Bean"],
        "actions": ["accidentally married", "adopted", "challenged", "fainted after seeing"],
        "objects": ["a clone", "a mirror", "a ghost", "themselves"]
    },
    "animals":{
        "subjects": ["Cat", "Dog", "Parrot", "Llama"],
        "actions": ["sues", "marries", "challenges", "interviews"],
        "objects": ["a lion", "a politician", "a hamster", "a snake"]
    },
    "tech gone wrong":{
        "subjects": ["AI", "Chatbot", "Smart Fridge", "Robot Vacuum"],
        "actions": ["becomes self-aware", "joins a union", "steals electricity", "leaks secrets"],
        "objects": ["your Google searches", "the government", "your dreams", "Elon Musk"]
    },
    "ufo & space":{
        "subjects": ["NASA", "Aliens", "Martians", "Astronauts"],
        "actions": ["discover", "hide", "ban", "mistake"],
        "objects": ["Area 52", "moon cheese", "the sun as a planet", "Earth 2.0"]
    },
    "school & education":{
        "subjects": ["Students", "Teachers", "Principals", "School Cafeteria"],
        "actions": ["ban homework", "start rebellion", "replace exams with memes", "declare summer forever"],
        "objects": ["maths books", "sleep", "TikTok", "online classes"]
    },
    "haunted / supernatural":{
        "subjects": ["Ghosts", "Witches", "Haunted Dolls", "Zombies"],
        "actions": ["attend school", "buy property", "go on vacation", "start a podcast"],
        "objects": ["in Florida", "on Instagram", "with vampires", "in Walmart"]
    },
    "shopping / lifestyle":{
        "subjects": ["Shopaholics", "Influencers", "Grandma", "Black Friday Crowd"],
        "actions": ["fight over", "steal", "break up with", "fall in love with"],
        "objects": ["a toaster", "limited edition socks", "shopping carts", "99% discount"]
    },
    "health & fitness":{
        "subjects": ["Gym Bros", "Yoga Teachers", "Protein Shakes", "Vitamin Gummies"],
        "actions": ["explode", "flex too hard", "start talking", "become sentient"],
        "objects": ["on leg day", "during Zumba", "inside a blender", "at McDonald's"]
    }
}

def generate_fake_news():
    for i, cat in enumerate(categories.keys(), 1):
        print(f"{i}. {cat.title()}")
    category_input= input("Choose a category: ").lower()
    category = next((key for key in categories if key.lower()==category_input), None)
    if category == None:
        print("Invalid category. Please try again.\n")
        return generate_fake_news()
    data = categories.get(category)
    subject = random.choice(data["subjects"])
    action = random.choice(data["actions"])
    obj = random.choice(data["objects"])
    User_choice = input("Do you want to enter a custom name or place? yes/no: ")
    if User_choice.lower()=="yes":
        person_name = input("Enter a person name: ")
        place = input("Enter the name of the place: ")
    else:
        person_name = "a mysterious figure"
        place = "an unknown location"
    template =random.choice(templates)
    headline = template.format(subject=subject, action=action, person=person_name, place=place)
    saved_headlines.append(headline)
    print(f"\n📰 FAKE NEWS HEADLINE:\n{headline}\n")
    save = input(("Do you want to generate another fake news? Yes/No"))
    if save.lower() == "no":
        with open("fake_news_headlines.txt", "w") as file:
            for line in saved_headlines:
                file.write(line + "\n")
        print("Headlines saved to 'fake_news_headlines.txt'!")
        print("\nThanks for using the Fake News Generator! 😂")
        exit()
    else:
        generate_fake_news()
    

generate_fake_news()
    



