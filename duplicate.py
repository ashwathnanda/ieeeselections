def count(a,n):
    x=a[0]
    for i in range (1,n):

        x=x^a[i]
    return x
a=input('Enter list of values')
print count(a,len(a))
#https://wiki.python.org/moin/BitwiseOperatorss
