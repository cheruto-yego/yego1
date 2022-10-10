from unittest.mock import sentinel
while sentinel != "stop":
 score = float(input(" please Enter Score: "))
if score>=0.9:
      print('you scored A,perfect score')
elif score >=0.8:
      print('you scored B')
elif score >=0.7:
      print('you scored C')
elif score >=0.6:
      print('you scored D ')

      
   

       
else:
    
    print('you scored F')
    sentinel=input("please enter stop to stop the program")