import random
num=[]
for i in range(1,101):
    num.append(i)

gus=random.choice(num)
gg=input("Hard or easy?")

if(gg=="easy"):
    tr=10
    
elif(gg=="hard"):
    tr=5
print("The number from 1 to 100")
while(tr>0):
    n=int(input("number is :"))
    if(n>gus):
        print("Too high")
        tr=tr-1
        print(f"tries left {tr}")
        
    elif(n<gus):
        print("Too low")
        tr=tr-1
        print(f"tries left {tr}")
        
    elif(n==gus):
        print("You win")
        break

if(tr==0):
    print(f"You lose the number is {gus}")
