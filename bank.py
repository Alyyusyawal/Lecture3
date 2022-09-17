#Lecture 3

answer = input("greeting : ").strip().lower()
if answer != 'h':
  print ("$100")
elif answer == ("hello"):
  print ("$0")
elif answer.startswith ("h"):
  print ("$20")

  
  answer = input("greeting : ").strip().lower()
if answer == "hello" :
    print("$0")
elif answer == "how you doing"or answer.startswith ("h"):
    print("$20")
else:
    print("$100")
