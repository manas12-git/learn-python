# def sum(n):
#     if n==1:
#         return n
#     return n+sum(n-1)

# # sum(50)
# print(sum(50))


def fact(num):
    if num==1:
        return num
    return num*fact(num-1)
n=int(input("enter your number"))
print(fact(n))