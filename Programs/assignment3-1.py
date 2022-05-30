def f(*x,**y):
    def s1(x):
        s = 0
        if x:
            for i in x:
                s += i
        return s
    def p1(x):
        s = 1
        if x:
            for i in x:
                s*= i
        return s
    def sumOfReciprocals(x):
        reciprocals = list(map(lambda i: 1/i, x))
        return s1((reciprocals))



    if y["action"] == "sum":
        return s1(*x)
    elif y["action"] == "prod":
        return p1(*x)
    elif y["action"] == "reciprocal sum":
        return sumOfReciprocals(*x)
    else:
        return f"bad argument: {y}"

if __name__  =='__main__':
    xlst = [1,2]
    print(f(xlst, action = "sum"))
    print(f(xlst, action = "prod"))
    print(f(xlst, action = "reciprocal sum"))




# ls = [1,2,3,4,5,6]
# def s1(*li):
#         s = 0
#         if li:
#             for i in li:
#                 s += i
#         return s

# reciprocals = list(map(lambda x: 1/x, ls))
# print(reciprocals)


