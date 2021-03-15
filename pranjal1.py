#write a program to identify the character with upp lower digit special character
a=input()
if(a>='A' and a<='Z'):
    print("upper")
elif(a>='a' and a<='z'):
    print("lower")
elif a>='0' and a<='9':
    print("digit")
else:
    print("special character")
