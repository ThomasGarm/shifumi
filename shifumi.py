#SHIFUMI:
#-------
#1=Stone    2=Scissor    3=Paper

name=input("Hello, first enter your name: ")


import random
liste = [ 1, 2, 3]
scoreU=0
scoreC=0





try:
   while scoreU or scoreC != 3:
         print(name,",tap:\n 1 to play Stone,\n 2 to play Scissor,\n 3 to play Paper")  
         user=int(input("Choose!"))
         comp= random.choice(liste)
         

         if user==3 and comp==1:
            print("Paper beat Stone!")
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
         if user==2 and comp==3:
            print("Scissor beat Paper!")
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
         if user==1 and comp==2:
            print("Stone beat Scissor")
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
         if user==comp:
            print("DRAW!")
            print ( "Your score:", scoreU,"-Computer: ",scoreC)
except ValueError:
       pass
       print("Invalid command.")
