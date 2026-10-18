def play_mad_libs():
    print("welcome to the python mad libs generator!")
    print("------------------------------------\n")
    adjective1=input("enter an adjective (describing  a word)")
    noun1=input("enter a noun (place,thing,name) ")
    verb_past=input("enter a pastence word(action word)")
    adverb=input("enter an adverb (ends in -ly )")
    adjective2=input("enter another adjective")
    noun2=input("enter another noun")
    name3=input("enter a name(place)")
    name4=input("enter a name(wife)")
    name5=input("enter a name(daughter)")
    name6=input("enter a name(son)")
    adjective3=input("enter an adjective")
    emotion=input("enter an emotion(happinesss,sadness)")
    story=f"\n today i went to the zoo. i saw a very{adjective1} {noun1} outside."\
        f" it unexpectedly {verb_past}right towards me! i turned and ran away"\
        f" {adverb}.luckily, i bumbed into a{adjective2}security guard who"\
        f"scare it off with a gaint {noun2}.what a wild day!"\
        f"and later i go to {name3} that is my village."\
        f"my wife name is{name4},she is very {adjective3},i have two children a daughter and a son.daughter name is{name5}"\
        f"my son name is{name6},i love my family."\
        f"i am the more{emotion} person."

    print("\n here is yur finished mad libs story")
    print(story)
if __name__=="__main__":
    play_mad_libs()