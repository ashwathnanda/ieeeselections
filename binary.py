def binarySearch(a,item):
    first = 0
    last = len(a)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if a[midpoint] == item:
            found = True
        else:
            if item < a[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if found==True:
        print "element found and is in",midpoint+1,"th Position"
    else:
        print "Element not found"
	
a=input("Enter the list :")
n=input("Enter the Number to be found :")
binarySearch(a,n)

