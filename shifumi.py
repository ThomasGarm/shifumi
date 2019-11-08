#SHIFUMI:
#-------
#1=Stone    2=Scissor    3=Paper


   
      

print("=====================================")
name=input("Hello, first enter your name: ")
print("=====================================")

scoreU=0 #User score
scoreC=0 #Computer score
from functionshifumi import * 



try: #let's introduce all cases.
   while scoreU != 3 and scoreC != 3:#loop condition
         print(name,",tap:\n 1 to play Stone,   2 to play Scissor,    3 to play Paper") # short tuto 
         user=int(input("Choose!"))
         comp = computer_random()
            
         

         if user==3 and comp==1:#user win
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
            print("DRAW!") #egality
            print ( "Your score:", scoreU,"-Computer: ",scoreC)              
            print ("------------------------------------------------")

         if user==1 and comp==3: #computer win
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



         if scoreU == 3 or scoreC == 3: #condition that engage end game
               print("============================================")
               text = input("Continue ? Y/N :") #avoid breaking if user input too fast
         
               if text== "Y":#score réinitialisation
                  scoreU=0
                  scoreC=0
               if text == "N":#end game
                  print:("=========")
                  print("Game Over")
                  print("==========")
                  break
               if text not in ("Y","N"):
                  print("invalid command")
                  

except: 
  pass
      
               
      

      


          