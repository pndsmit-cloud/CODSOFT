val1=float(input ("enter your first value"))
val2=float(input("enter your second value"))
op=input("enter your operation  ")

#for addtion of number 
if op == '+':
    result1 = val1+val2
    print("your addition is ",result1)

#for substraction of number 
elif op =='-':
    result2=val1-val2
    print("your substraction  is ",result2)

   #for division of number
elif op=='/':
    if(val2==0):
        print("division by zero is not possible")
    else:
        result3=val1/val2
        print("your divison is ",result3)

#for multiplication of number
elif op =='*':
    result4=val1*val2
    print("your multiplication  is ",result4)

#to get remainder of number 
elif op == '%':
        if(val2==0):
            print("division by zero is not possible")
        else:
            result5=val1%val2
        print("your remainder is ",result5)

    #for invalid expression 
else:
    print("invalidddd o")
