import random

subjects=["You","I","Someone", "Nobody","No one","The girl",
"The boy", "The woman","The man"]
verbs=["will", "took","stood", "reached for", "escaped to", "ran", "sang", "drowned",
"spoke","died", "wrote","left","cried","rejoiced","loved","feared","followed",
"hated","flew"]
adjectives=["greatly","slowly","beautifully","languidly", "quietly","softly","loudly","angrily"]
objects=["hope","love","the past","peace","fear","a path", "freedom", "circumstance", "confusion",
"dreams", "hate","despair","passion","intelligence","yearning"]
adverbial_phrases=["to find","to love","to the shore","to live","to fight","to wonder",
"to discover", "to learn","to sleep"]



#makes lines
def generate_lines():
    chosen_subject=random.choice(subjects)
    chosen_verb=random.choice(verbs)
    chosen_object=random.choice(objects)
    chosen_adjective=random.choice(adjectives)
    chosen_adverbial_phrase=random.choice(adverbial_phrases)
    sentence_structures=[(chosen_object.capitalize()),(chosen_subject.capitalize()),(chosen_verb.capitalize()),
     (chosen_adverbial_phrase.capitalize()),
    (chosen_subject.capitalize()+" "+chosen_verb+" "+chosen_adjective+", "+chosen_object),
    (chosen_subject.capitalize()+" "+chosen_verb+" "+chosen_adjective+", "+chosen_object+" "+chosen_adverbial_phrase),
    (chosen_subject.capitalize()+" "+chosen_adjective+" "+chosen_verb+" " +chosen_object),
    (chosen_subject.capitalize()+" "+chosen_verb+" "+chosen_object+" "+chosen_adverbial_phrase),
    (chosen_subject.capitalize()+" "+chosen_verb),(chosen_subject+" "+chosen_verb+" "+chosen_object)]
    title=random.choice(subjects)
    poem=random.choice(sentence_structures)
    print poem

#puts lines together
def make_poem(number_of_lines):
    title=random.choice(objects)
    print "Title: "+title.capitalize()

    for i in range(number_of_lines):
        generate_lines()

line_number=input("How many lines should the poem have? ")
make_poem(line_number)
