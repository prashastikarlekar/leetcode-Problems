def power(x,n):
    if (n==0): return 1
    if n>0:
        if n%2==0: return power(x, n/2) * power(x,n/2)
        else : return x * power(x,(n-1)/2) * power(x, (n-1)/2)
    # else:

# def power(x,n):
#     if(n==0): return 1
#     if(n==1): return x
    
#     if(n%2==0):
#         return power(x,n/2)**2
#     else:
#         m = (n-1)/2
#         return x*power(x,m)**2

print(power(9,0))
