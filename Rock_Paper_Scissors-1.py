import random

while True:
  print("enter choice \n1. Rock \n2. Paper\n 3. scissor\n")
  choice=int(input("user's turn ..."))
  while choice>3 or choice<1:
    choice=int(input("enter valid input"))
    if choice==1:
      choice_name="Rock"
    elif choice==2:
      choice_name="Paper"
    else:
      choice_name="scissor"
  print("user choice is:", choice_name)
  print("now computer's turn...")
  comp_choice=random.randint(1,3)
  if comp_choice==1:
     comp_choice_name="rock"
  elif comp_choice==2:
        comp_choice_name="paper"
  else:
      comp_choice_name="scissor"

  print("computer chocie is.."+ comp_choice_name)

  print(choice_name+"V/S"+comp_choice_name)

  if((choice==1 and comp_choice_name==2) or (choice==2 and comp_choice_name==1)):
   print("paper wins ..")
   result="paper"
  elif  ((choice==1 and comp_choice_name==3) or (choice==3 and comp_choice_name==1)):
   print("Rock wins ..")
   result="Rock"

  else:
    print("scissor Wins")
    result="scissor"

  if result==choice_name:
     print("user is winner")
  else:
     print("computer wins")
     print("do you want to play again? (Y/N")
ans=input()

if ans=='n' or ans=='N':
    Break

print("thanks for playing")
