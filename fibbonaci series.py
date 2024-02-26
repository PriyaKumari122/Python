n=int(input("Enter the nth term of Fibonacci Sequence :"))

a=0
b=1
i=2
if n>0 :
   print(a,end=',')
if n>1 :
   print(b,end=',')

while i < n :
     c=a+b
     print(c ,end=',')
     i += 1
     a=b
     b=c
print ()
