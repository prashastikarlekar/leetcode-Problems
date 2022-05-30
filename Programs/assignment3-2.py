import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-lst', nargs='+', default = ['1','2','3'], help="List of←↩numbers") # -lst is the name of the argument
parser.add_argument('-op', default ='rec', help = "sum, prod, rec")
# parser.add_argument("-echo", help="echo the string you use here")
parser.add_argument("-square", help="square will be assigned to a number and then calculate its square while calling", type=int)
args = parser.parse_args()
print(args.lst)
print(args.op)
if args.op == "sum":
    s=0
    for i in args.lst:
        s+= int(i)
    print(s)
elif args.op =="prod":
    p=1
    for i in args.lst:
        p *=int(i)
    print(p)
else:
    rec= [i for i in map((lambda i: 1/int(i)), args.lst)]
    print(rec)
# print(args.echo)
# print(args.square**2) 