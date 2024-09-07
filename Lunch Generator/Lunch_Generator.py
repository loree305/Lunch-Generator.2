
#Menu
def displayMenu():
    print ("The Restaurtant program")
    print ("\nChoose an option")
    print ("healthy - Show all American restaurants that are healthy-ish")
    print ("fast - Show American fast food places")
    print ("asian - Show all Asian restaurants")
    print ("spanish -Show all hispanic food places")
    print ("vegan - Show all vegan restaurants")
    print ("indian - Show all Indian restaurants")
    print ("edit - Edit an item")
    print ("exit - exit program")
    print()



#Options
American = ["bolay" ,"newks","just salads"]
AmericanFast = ["ihop","waffle house","panda express",]
Asian = ["bento"]
Spanish =["mi apa","taco bell"]
Vegan =["mint"]
Indian =["mint"]

#Showing what's in *food list*
def healthy(American):
    y = 0
    for x in American:
        y = y +1
        print (str(y) + "." , x)

#Showing what's in *show what's in food list*
def fast(AmericanFast):
    y = 0
    for x in AmericanFast:
        y = y +1
        print (str(y) + "." , x)

#Showing what's in *show what's in food list*
def asianfood(Asian):
    y = 0
    for x in Asian:
        y = y +1
        print (str(y) + "." , x)

#Showing what's in *show what's in food list*
def spanishfood(Spanish):
    y = 0
    for x in Spanish:
        y = y +1
        print (str(y) + "." , x)

#Showing what's in *show what's in food list*
def veganfood(Vegan):
    y = 0
    for x in Vegan:
        y = y +1
        print (str(y) + "." , x)

#Showing what's in *show what's in food list*
def indianfood(Indian):
    y = 0
    for x in Indian:
        y = y +1
        print (str(y) + "." , x)

    


        
#Main/Makes the magic happen
#Display~
def main():
    print ("The Restaurtant program")
    print ("\nChoose an option")
    print ("healthy - Show all American restaurants that are healthy-ish")
    print ("fast - Show American fast food places")
    print ("asian - Show all Asian restaurants")
    print ("spanish -Show all hispanic food places")
    print ("vegan -Show all vegan restaurants")
    print ("indian - Show all Indian restaurants")
    print ("exit - exit program")
    print()
    
#While a command = whatever is typed it carries out the command
    option = ""
    while option != "exit":
        if option.lower() == "healthy":
            healthy(American)
        elif option.lower() == "fast":
            fast(AmericanFast)
        elif option.lower() == "asian":
            asianfood(Asian)
        elif option.lower() == "spanish":
            spanishfood(Spanish)
        elif option.lower() == "vegan":
            veganfood(Vegan)
        elif option.lower() == "indian":
            indianfood(Indian)
        option = str(input ("\nWhat are you in the mood to eat?: "))
    print ("Bye!")




if __name__ == "__main__":
    main()
