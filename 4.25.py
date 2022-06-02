#function for counting consecutive 1'a at the end
def cons_1(n):

    #getting binary representation of the number
    n=bin(n).replace("0b", "")

    #reversing the string
    n=n[::-1]

    #counter
    cnt=0

    #calc
    for i in n:

        #if 1 increase counter
        if(i=="1"):
            cnt+=1

        #otherwise break
        else:
            break

    #return the counter
    return cnt

#function for printing ruler
def print_ruler(c):

    #printing 0 index for the ruler
    print("-"*c,0)

    #counter variable
    cnt=0

    #variable for the dashes
    num=0

    #printing untile the number dashes are less than c
    while(num<c):

        #adding 1 to the count
        cnt+=1

        #calc number of 1's by calling function
        num=cons_1(cnt)

        #if the 1's are not zero
        if(num!=0):

        #if number is equal to c
            if(num==c):

            #print last index
             print("-"*num,1)
            else:
            #print dashes
             print("-"*num)
        else:
            continue
        #fucntion call for testing the function print_ruler
print_ruler(4)