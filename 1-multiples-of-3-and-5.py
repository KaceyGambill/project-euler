###
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###
arrayOfMultiples =[]

def sumMultiples3and5(num):
    totalSum = 0
    for x in range(1, num):
        if (x % 3 == 0 or x % 5 == 0):
            print ("%d is divisible by 3 or 5" % x)
            arrayOfMultiples.append(x)
            

        print("in loop number: %d" % x)
    print ("end")
    print(arrayOfMultiples)
    for i in arrayOfMultiples:
        totalSum += i
    print ("total sum: %d" % totalSum)

sumMultiples3and5(1000)