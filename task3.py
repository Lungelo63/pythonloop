num = 20            #assigning 20 to variable num
while num >= 0:     #initiating while loop num is bigger than or equal 0

    print(num)      #printing num
    num = num - 1   #minus 1 for every cir  cirlation until True



numb = 2                #assigning 2 to variable numb
while numb <= 20:       #initiating while loop num is smaller than or equal 20

    print(numb)         #printing numb
    numb = numb + 2     #adding 2 to numb for every circulation




for i in range(5):      #for i in range of 5
    print("*")          #print *
    i * 2               #times i by two for every circulation until True





first = float(input("Enter the first number: "))        #taking in user input
second = float(input("Enter the second number: "))

cf = min(first, second)                                 #first and seconds minimum
while first % cf != 0 or second % cf != 0:              #while first or second modulus cf is not equal to 0
    cf -= 1

print("The Highest Common Factor is " + str(round(cf)))  #printing HCF


