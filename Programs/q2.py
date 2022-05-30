import argparse 
def f(x,*y):

    def s1(x):
        s=0
        if x:
            for i in x:
                s+=i
        return s

    def p1(x):
        s =1
        if x:
            for i in x:
                s*=i
        return s

    if y['action']=='sum':
        return s1(*x)
    elif y['action']=='prod':
        return p1(*x)
    elif y['action']=='reciprocal sum': 
        return s1(list(map(lambda k: 1/k , *x)))
    else:
        return f'bad argument :{y}'

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lst',nargs='+',default=['1'],help='List of numbers',type=int)
    parser.add_argument('op',nargs='+',default='sum',help='sum,prod,rec')
    args=parser.parse_args()
    print(f(args.lst,action=args.op))