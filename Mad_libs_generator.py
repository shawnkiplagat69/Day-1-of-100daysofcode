def doctors_statement():
    print("Let's get to it!")
    verb_1=input("A verb:")
    adjective_1=input("An adjective:")
    verb_2=input("A verb:")
    body_part_1=input("A body part:")
    adverb_1=input("An adverb:")
    body_part_2=input("A body part:")
    noun_1=input("A noun:")
    verb_3=input("A verb:")
    animals_1=input("Animals:")
    noun_2=input("A noun:")
    verb_4=input("A verb:")
    adjective_2=input('An adjective:')
    colour=input("colour:")
    source="""Most doctors agree that bicycle of {} is a/an {} form of exercise.
    {} a bicycle enables you to develop your {} muscles as well as {} increase the rate 
    of a {} beat. More {} around the world would rather {} bicycles than drive {} animals. No matter
    what kind of {} you {}, always be sure to wear a/an {} helmet. Make sure to have {} 
    reflectors too"""
    output=source.format(verb_1, adjective_1, verb_2, body_part_1, adverb_1, body_part_2, noun_1, verb_3, animals_1, noun_2, verb_4, adjective_2, colour)
    print(output)
def missing_case():
    source="""\t THE CASE OF THE MISSING {}\n There once was a detective named {}.
    One day, the detective's neighbour knocked on the door.\n\"I am so {},\" said the neighbour.\n
    \"I can't find my {} anywhere. I saw it before I went to {} club, but later it was gone!\n
    The detective grabbed a pencil and a {} and asked, \"Will you describe it?\"\n\"Certainly,\" said the neighbour.
    \"It is {}, {} and it never {}.\n The detecive searched {} around every {} and behind every {}. 
    \"{}!\" said the detective, \"I found it! It was right here under your {} the whole time!\"\n
    They both had a good {}, and the detective tought, \"Another case {} solved!\""""
    print("This mystery isn't gonna solve iteslef. Let's get to work!")
    title=input("Special noun:").upper()
    name=input("A name:")
    adjective_1=input("Adjective:")
    #noun_1=input("Special noun:")
    verb_1=input("verb inding in 'ing':")
    noun_2=input("noun:")
    colour_1=input("coour:")
    adjective_2=input("adjective:")
    verb_2=input("plural verb:")
    adverb_1=input("adverb:")
    noun_3=input("noun:")
    noun_4=input("noun:")
    exclamation=input("exclamatory clause:")
    noun_5=input("noun:")
    verb_3=input("verb:")
    adverb_2=input("adverb:")
    output=source.format(title, name, adjective_1, title, verb_1, noun_2, colour_1, adjective_2, verb_2, adverb_1, noun_3, noun_4, exclamation, noun_5, verb_3, adverb_2)
    print(output)
print("Welcome to the mad libs generator!")
print("Please make a selection:\n1. Doctor's statement.\n 2. A detective's case.")
choice=int(input())
if choice==1:
    print("Excellent choice!\n How many variations of the story would you like to have?")
    stories=int(input())
    i=1
    while i<=stories:
        doctors_statement()
        i=i+1
else: 
    print("So you'd rather be a sleuth huh! Anyway, how many cases would you like to solve?")
    stories=int(input())
    i=1
    while i<=stories:
        missing_case()
        i=i+1