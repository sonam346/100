#Assignment B1:program on regular expression

import re
print("----------MENU-------------")
print("1.use of ^ caret")
print("2.use of $ dollar")
print("3.use of [] range")
print("4.use of * asterik")
print("5.use of \ backslash")
print("6.exit")
while (True):
    i=int(input("enter your choice"))
    if(i==1):
            s=input("enter a string")
            x=re.findall("^the",s)
            if(x):
                  print("yes,the string",s,"starts with the")
            else:
                    print("no,the string",s," doesnt starts with the")
    elif(i==2):
            s=input("enter a string")
            x=re.findall("spain$",s)
            if(x):
                    print("yes,the string",s,"starts with spain")
            else:
                    print("no,the string",s," doesnt starts with spain")
    elif(i==3):
            s=input("enter a string")
            x=re.findall("[m-z]",s)
            print(x)
    elif(i==4):
            s=input("enter a string")
            x=re.findall("yt*",s)
            print(x)
    elif(i==5):
            s=input("enter a string")
            x=re.findall("\d",s)
            print(x)
    elif(i==6):
            break
    else:
            print("invalid choice")
            
        
            
                             
                   
               
            
           
              
          

