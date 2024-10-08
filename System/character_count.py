# This program Counts all the characters in a file



input = input("enter a file name:")


file = open(input,"r")


for line in file.readlines():
  char = 0
  s = line
  char += len(s)

  for c in s:
    n = 0
    if(c[n] =='\n'):
      char -=1
       

    n += 1

print (char,":characters")
