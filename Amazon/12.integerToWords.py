n = 121
number = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen",
"sixteen","seventeen","eighteen","nineteen"]
numberMoreThan19 = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","thousand","lacs","crore"]

res =''
if n<=19:
    print(number[19])
if n>19:
    res = numberMoreThan19[n//100] + " "
    res+= numberMoreThan19[n//10] + " "+ number[n%10]
    print(res)