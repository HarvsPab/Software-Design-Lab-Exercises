def power(n, exp):
    if(exp == 0):
#if exp is 0 then it will return 1 and the back recursive returning to function call begin if it triggers this base condition.
        return 1
    else:
        return n * power(n , exp - 1)
#this is the recursive condition to calculate the power , this runs untill the epx valu becomes zero and returns from there.
print(power(2,5))