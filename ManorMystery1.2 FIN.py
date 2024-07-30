### JACOB T LONG ###

import random

#Willie Wonderful Fingers BIO
def willie():
    print ('')
    print ('---Willie Wonderful---')
    print ('Sex: Male ')
    print ('AGE: 43')
    print ('Hair Color: Black')
    print ('Allergies: Peanuts')
    print ('Story: Willie claims to have been stuck on the side of the road with car troubles.')
    print ("Bio: Willie has been Mr Longs buisness rival for 15 years now. There's nothing")
    print ("he'd enjoy seeing more than watching Mr. Longs empire crumble. Willie spends his")
    print ("spare time trading stocks and driving his expensive Rolls Royce down the road")
    print ("with the windows down. His life truly is wonderful.")

#Sammy Sticky Fingers BIO
def sammy():
    print ('')
    print ('---Sammy Sticky Fingers---')
    print ('Sex: Male')
    print ('AGE: 32')
    print ('Hair Color: Blonde')
    print ('Allergies: Strawberries')
    print ('Story: Sammy claim he was wandering the streets last night looking for his dog.')
    print ("Bio: Sammy's lived a life of crime, hes a criminal through and through.")
    print ("He's served 10 years in prison after robbing the local museum and is a")
    print ("master cat burgaler. Sammys claimed to have turned a new leaf spending his")
    print ("afternoons knitting and glueing together collages. He's a simple man now.")
    
#Betty Beautiful BIO
def betty():
    print ('')
    print ('---Betty Beautiful---')
    print ('Sex: Female')
    print ('AGE: 25')
    print ('Hair Color: Red')
    print ('Allergies: Shell Fish')
    print ('Story: Betty told the officers she was spending the night taking selfies with the night sky.')
    print ("Bio: What you havent heard of Betty Beautiful? Not suprising. After a viral")
    print ("video of her furiously demolishing her boyfriends car with a base ball bat Bettys career")
    print ("has gone down the toilet. Betty longs for attention and shiny expensive objects.")
    print ("Betty spends her free times dressing up, partying, and clawing her way to the top.")



#Intro
#Selects a random number to generate a robber
robber=random.randint(1,3)
if robber == 1:
    robber = 'willie'
if robber == 2:
    robber = 'sammy'
if robber == 3:
    robber = 'betty'    

#print (robber) 
print ('Welcome too...')
print ('MANOR MYSTERY!')
print ('What is your first name?')
first_name = input()
print ((first_name),',what is your last name?')
last_name = input()
print ('Nice to meet you DETECTIVE',(last_name)+'.')
print ('Let me brief you on your new assignment.')
print ('')
print ('There has been a robbery at the Long Manor. The robbery happened last night while everyone')
print ('was asleep. The local sherif has gather up 3 potential suspects found soon after the crime was')
print ('committed. Over 3 million dollars worth of possesions were stolen. Find out who done it') 
files = ('')
#While loop that lets the user look through files with suspect discriptions
while files != 'done':
    print ('')
    print ("Here's your suspects detective:")
    print (" 1 [Willie Wonderful]")
    print (" 2 [Sammy Sticky Fingers]")
    print (" 3 [Betty Beautiful]")    
    files = input("here's your potential suspects. [Type (1,2,3,or done)]")
    if files == '1':
        willie()
        files = ('')
    elif files == '2':
        sammy()
        files = ('')
    elif files == '3':
        betty()
        files = ('')
    elif files == ('done'):
        print ('')
    else:
        print('')
        print('INVALID INPUT')
        
        
#ENTER THE HOUSE

#CLUES
clues = {
    'willie':{'Parlor':'The window in the parlor has been smashed by a brick. Seems like a sloppy entry point.',
              'Foyer':'Nothing Here... Probably should check some of the other rooms.',
              'Dinning Room':'Theres a hair on the ground. Its Black. Is there a cat around here?.',
              'Study':'The filing cabinets have been ransacked.',
              'Living Room':'After careful examination you find that theres a boot print on the floor.',
              'Kitchen':'Stealing sure does work up an appetite. Looks like there is remnants of a Shrimp Cocktail.',
              'Laundry Room':'There is just a pile of stinky socks.',
              'Bedroom':'The maid is sitting on the bed scared. she claims that she heard the loud comotion but was too afraid to investigate.'
              },
    'sammy':{'Parlor':'The window in the parlor has been left open. This was most likely the entry point.',
              'Foyer':'Nothing Here... Probably should check some of the other rooms.',
              'Dinning Room':'There is a piece of blue string and a thimble underneath the dinning table.',
              'Study':'There is a bare space on the wall labeled "Stary Night". The Theif must have taken the painting.',
              'Living Room':'After careful examination you find that theres a sneaker print on the floor.',
              'Kitchen':'Stealing sure does work up an appetite. Looks like there is remnants of a PBJ sandwich.',
              'Laundry Room':'There is just a pile of stinky socks.',
              'Bedroom':'The maid is sitting on the bed scared. she claims that she never heard a thing and slept through the whole night soundly.'
             },
    'betty':{'Parlor':'The window in the parlor has been smashed by a brick. Seems like a sloppy entry point.',
              'Foyer':'Nothing Here... Probably should check some of the other rooms.',
              'Dinning Room':'A Red piece of thread sticks out on the green carpet.',
              'Study':'The desk in the middle of the room appears to be missing a few fancy watches.',
              'Living Room':'After careful examination you find that there is a sneaker print on the floor.',
              'Kitchen':'Stealing sure does work up an appetite. Looks like there is remnants of a slice of Strawberry Pie.',
              'Laundry Room':'There is just a pile of stinky socks.',
              'Bedroom':'The maid is sitting on the bed scared. she claims that she heard someone humming "Party Rock Anthem" but was too afraid to investigate.'
             }
         }

#ROOMS    
rooms ={
    'Foyer': {'north':'Living Room','east':'Dinning Room','west':'Parlor','south':'Outside'},
    'Parlor': {'north' : 'x','east':'Foyer','south' : 'x','west' : 'x',},
    'Dinning Room': {'north':'Kitchen','east':'x','south' : 'x','west':'Foyer'},
    'Living Room': {'north':'Bedroom','east':'Kitchen','west':'Study','south':'Foyer'},
    'Study': {'north' : 'x','east':'Living Room','south' : 'x','west' : 'x'},
    'Kitchen': {'north':'Laundry Room','east':'x','west':'Living Room','south':'Dinning Room'},
    'Laundry Room': {'north' : 'x','east':'x','south':'Kitchen','west' : 'x'},
    'Bedroom' : {'north' : 'x','east':'x','south' : 'Living Room','west' : 'x'},
    }

notebook = []

print ("You ready to look for clues Detective",(last_name)+"? I'll walk you inside.")
print ("Once you've gatherd all the evidence meet me outside[South of Foyer]")
room = 'Foyer'

#MAIN ROOM NAV

while room != ('Outside'):
    direction = ' '
    print ('_____________________________________')
    print('You are in the', room+'.')
    direction = input('What would you like to do? ')
    if direction in ( 'north' ,'east', 'south', 'west'):
        outroom = rooms[room][direction]
        if outroom != 'x':
            room = outroom
        if outroom == 'x':
            print ('[There is no room',direction+'!]')
    elif direction == ('search'):
        print (clues[robber][room])
        if room in ( 'Parlor','Dinning Room','Study','Living Room','Kitchen','Bedroom'):
            if clues[robber][room] not in notebook:
                notebook.append(clues[robber][room])
                #print (len(notebook))
        room=room
    else:
        print ('INVALID INPUT [Try "north","east","south","west" or "search"]')
        room=room


#END GAME
       
print ('_____________________________________')
guess = 0
if len(notebook) >= 6:
    print("Well Detective",(last_name),"Who do you think robbed the house?")
    while guess == 0:
        print (' "willie" [Willie Wonderful]')
        print (' "sammy" [Sammy Sticky Fingers]')
        print (' "betty" [Betty Beautiful]')
        print (' "notebook" [Look over clues]')
        guess = input()
        if guess in ( 'willie' ,'sammy', 'betty', 'notebook'):
            if guess == 'notebook':
                for hint in notebook:
                    print ('-',hint)
                guess = 0
                print ('')
            elif guess == robber:
                    print (robber+": Oh fine I admit it! It was me! I would have gotten away with it if it wasn't for you detective", last_name)
                    print ('The robber was,',robber, ',You WIN')
                    print ('GOOD WORK DETECTIVE!')
            else:
                    print (guess+": YOU THINK ITS ME!?! I swear it wasn't!")
                    print ('The robber was,',robber, ',You LOSE')

        else:
            print ('INVALID INPUT [Try "willie","sammy","betty" or "notebook"]')
            guess = 0
else:
    print(first_name,"you FOOL! You barley have any evidence! I don't allow rookies on my task force! YOUR FIRED!" )
    print('You LOSE! Try searching all rooms next time before you leave the manor') 
