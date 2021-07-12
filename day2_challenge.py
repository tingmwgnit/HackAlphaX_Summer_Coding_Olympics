# prompt a character from the user: y for continue, n for quit
def IfContinue():
    n = input('Would you like to do some calculations? (y/n):')
    while n != 'y' and n != 'n':
        print('Please enter a valid value.')
        n = input('Would you like to do some calclations? (y/n):')
    return n

# prompt for numbers and operations, then return the answer
def Prompt():
    x = float(input('Please enter your first number:'))  
    oper = input('Please select an operation(+,-,*,/,^,!,sqrt):')
    
    if oper == '!':
        if x == int(x):
            return [x,0,oper]
        else:
            print('*You have entered a non-integer number to apply factorial')
            print('*we have rounded it down to the nearest interger for you')
            return [int(x),0,oper]
    elif oper == 'sqrt':
        if x < 0:
            print('*You have entered a negative number to apply squareroot')
            print('*we have transformed it positive for you')
            return [-x, 0, oper]
        else:
            return [x,0,oper]
    
    y = float(input('Please enter your second number:'))
    return [x,y,oper]

def Factorial(x):
    if x<0:
        print("*Negative Numbers don't have Factorials")
        return 'error'
    elif x==0 or x==1:
        return 1
    else:
        return x*Factorial(x-1)

def Calculate(l):
    x = l[0]
    y = l[1]
    oper = l[2]
    
    # deal with 3 special cases
    if y == 0 and oper == '/':
        print()
        print('*Calculation failed: You cannot divide by 0.')
        print()
        return 'error'
    elif oper == '^':
        oper = '**'
    elif oper == '!':
        return Factorial(x)
    elif oper == 'sqrt':
        return x**(1/2)
        
    return eval(str(x)+oper+str(y))


def PrintAnswer_1(result,l):
    x = l[0]
    y = l[1]
    o = l[2]
    width=20
    print(' '+'✽'*(width-9))
    print('✽'+' '*18+'✽')
    print('✽'+(str(x)+' '+str(o)+' '+str(y)+' is :').center(18,' ')+'✽')
    print('✽'+' '*18+'✽')
    print('✽'+(str(result)).center(18,' ')+'✽')
    print('✽'+' '*18+'✽')
    print(' '+'✽'*(width-9))
    
def PrintAnswer_2(result,l):
    x = l[0]
    y = l[1]
    o = l[2]
    width=20
    print(' '+'✽'*(width-9))
    print('✽'+' '*18+'✽')
    print('✽'+(str(x)+' '+str(o)+' is :').center(18,' ')+'✽')
    print('✽'+' '*18+'✽')
    print('✽'+(str(result)).center(18,' ')+'✽')
    print('✽'+' '*18+'✽')
    print(' '+'✽'*(width-9))

# formatting the title
print('')
print('')
text='HAXCodingOlympics'
width2=((len(text))*2)+7
lis=[range(7),range(13),range(17)]
temp=0
for i in lis:
    for j in i:
        if j%2==0:
            print('-',end='')
        else:
            print('+',end='')
    print(' '*2,end='')
print('')
for i in text:
    temp+=2
    print('|'+i,end='')
    if temp in [6,15,18,34]:
        print('|',' ',end='')
print('')
for i in lis:
    for j in i:
        if j%2==0:
            print('-',end='')
        else:
            print('+',end='')
    print(' '*2,end='')
print('')
print('')
print('')

width=20
# formatting the welcome message
print('','✽'*(width-1))
print('✽',' '*31,'✽')
print('✽',"Welcome to Team 37's Calculator".center(29,' '),'✽')
print('✽',' '*31,'✽')
print('','✽'*(width-1))

print('')
print('')

# take the order from the user
order = IfContinue()
    
# if 'y', then move on to prompt for numbers
while order == 'y':
    l = Prompt()
    answer = Calculate(l)
    
    if l[2] in ['!','sqrt']:
        PrintAnswer_2(answer,l)
    else:
        PrintAnswer_1(answer,l)
        
    order = IfContinue() #ask if the user wants more calculations
    
# the user wishes to stop, say good bye
print('','✽'*(width+1))
print('✽',' '*34,'✽')
print('✽','Thank You for Using Our Calculator'.center(34,' '),'✽')
print('✽',' '*34,'✽')
print('','✽'*(width+1))

    








