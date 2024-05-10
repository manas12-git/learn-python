

def find_armstrom(num):
    sum=0
    temp=num
    while num>0:
        arm=num%10
        sum=(arm*arm*arm)+sum
        num=num//10
    #  if sum==temp:
    #     print(f"{temp} number is armstrom") 
    # else:
    #     print(f"{temp} number is not armstrom")
    return sum==temp






num=int(input("enter your number"))

res=find_armstrom(num)

if res:
    print(f"{num} number is armstrom")
else:
    print(f"{num} number is not armstrom")

