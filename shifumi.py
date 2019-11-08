#SHIFUMI:
#-------
#1=Stone    2=Scissor    3=Paper
print("=====================================")
name=input("Hello, first enter your name: ")
print("=====================================")

import random
liste = [ 1, 2, 3] #Computer choices
scoreU=0 #User score
scoreC=0 #Computer score



try:
   while scoreU or scoreC != 3:
         print(name,",tap:\n 1 to play Stone,          2 to play Scissor,            3 to play Paper")  
         user=int(input("Choose!"))
         comp= random.choice(liste)
         

         if user==3 and comp==1:
            print("Paper beat Stone!")
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")
            
         if user==2 and comp==3:               
            print("Scissor beat Paper!")
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")

         if user==1 and comp==2:
            print("Stone beat Scissor")               
            scoreU += 1
            print ("Bravo! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")

         if user==comp:
            print("DRAW!")
            print ( "Your score:", scoreU,"-Computer: ",scoreC)              
            print ("------------------------------------------------")

         if user==1 and comp==3:
            print("Paper beat Stone!")
            scoreC += 1
            print ("Too Bad! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")

         if user==3 and comp==2:
            print("Scissor beat Paper!")
            scoreC += 1
            print ("Too Bad! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")

         if user==2 and comp==1:
            print("Stone beat Scissor")
            scoreC += 1
            print ("Too Bad! Your score:", scoreU,"-Computer: ",scoreC)
            print ("------------------------------------------------")

         if scoreU == 3 or scoreC == 3:
            print("============================================")
            text = input("Continue ? Y/N :")
            if text== "Y":
               scoreU=0
               scoreC=0
            if text == "N":
               print:("=========")
               print("Game Over")
               print("==========")
               break
            print("invalid command")
      
except ValueError:
       print("Invalid command")
      


          