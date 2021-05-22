### Constant Values for menu items ###

EGG=0.99
BACON=0.49
SAUSAGE=1.49
HASH_BROWN=1.19
TOAST=0.79
COFFEE=1.09
TEA=0.89
SMALL_BREAKFAST=EGG+HASH_BROWN+(2*TOAST)+(2*BACON)+SAUSAGE
REGULAR_BREAKFAST=(2*EGG)+HASH_BROWN+(2*TOAST)+(4*BACON)+(2*SAUSAGE)
BIG_BREAKFAST=(3*EGG)+(2*HASH_BROWN)+(4*TOAST)+(6*BACON)+(3*SAUSAGE)

### Operator/Logical/Processing/Container Variables ###

Quantity=0
Quantity2=0
Number_Error1=0
Number_Error2=0
Order_Error=0
Answer1=0
Order=0
Wordlist=0
Total_Cost=0
Processed_Input=0
Loop_Fix=0
Processed_Input2=0
BREAKFAST_OPTIONS= ["smallbreakfast", "regularbreakfast", "bigbreakfast", "egg", "bacon", "sausage", "hashbrown", "toast", "coffee", "tea"]
EXIT_ENTRY=["q"]

### Sub values ###

Cost=0
Cost1=0
Cost2=0
Cost3=0
Cost4=0
Cost5=0
Cost6=0
Cost7=0
Cost8=0
Cost9=0
Cost10=0
Cost11=0
Cost12=0
Cost13=0
Cost14=0
Cost15=0
Cost16=0
Cost17=0
Cost18=0
Cost19=0
Cost20=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

### String processing block ###

def formatInput(TextLine):
    TextLine=TextLine.lower().strip()
    Wordlist=TextLine.split()
    TextLine="".join(Wordlist)
    return TextLine

###Beginning of my program ###

while Order not in EXIT_ENTRY:
    Order=input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    Processed_Input=formatInput(Order)
    if Processed_Input in BREAKFAST_OPTIONS:
        Quantity=input("Enter quantity: ")
        if Quantity.isnumeric():
            Quantity=float(Quantity)
            if Processed_Input in BREAKFAST_OPTIONS[0]:                         ### Loop #1 with no input errors ###
                Cost1=Quantity*SMALL_BREAKFAST
                a=a+1
            elif Processed_Input in BREAKFAST_OPTIONS[1]:
                Cost2=Quantity*REGULAR_BREAKFAST
                b=b+1
            elif Processed_Input in BREAKFAST_OPTIONS[2]:
                Cost3=Quantity*BIG_BREAKFAST
                c=c+1
            elif Processed_Input in BREAKFAST_OPTIONS[3]:
                Cost4=Quantity*EGG
                d=d+1
            elif Processed_Input in BREAKFAST_OPTIONS[4]:
                Cost5=Quantity*BACON
                e=e+1
            elif Processed_Input in BREAKFAST_OPTIONS[5]:
                Cost6=Quantity*SAUSAGE
                f=f+1
            elif Processed_Input in BREAKFAST_OPTIONS[6]:
                Cost7=Quantity*HASH_BROWN
                g=g+1
            elif Processed_Input in BREAKFAST_OPTIONS[7]:
                Cost8=Quantity*TOAST
                h=h+1
            elif Processed_Input in BREAKFAST_OPTIONS[8]:
                Cost9=Quantity*COFFEE
                i=i+1
            elif Processed_Input in BREAKFAST_OPTIONS[9]:
                Cost10=Quantity*TEA
                j=j+1
        else:
            while Number_Error1.isalnum():
                Number_Error1=input("Please input a quantity: ")
    else:
        if Order in EXIT_ENTRY:
            print("")                                                               ### Terminating Code ###
            print("This is your bill")
            print("")
        else:
            while Order_Error not in BREAKFAST_OPTIONS:
                Order_Error=input("Sorry that is not a menu item, please choose again: ")    ### Menu Item Error ###
                Processed_Input2=formatInput(Order_Error)

            if Processed_Input2 in BREAKFAST_OPTIONS:
                Quantity2=input("Enter quantity: ")
                if Quantity2.isnumeric():
                    Quantity2=float(Quantity2)
                    if Processed_Input2 in BREAKFAST_OPTIONS[0]:
                        Cost11=Quantity2*SMALL_BREAKFAST
                    elif Processed_Input2 in BREAKFAST_OPTIONS[1]:
                        Cost12=Quantity2*REGULAR_BREAKFAST
                    elif Processed_Input2 in BREAKFAST_OPTIONS[2]:
                        Cost13=Quantity2*BIG_BREAKFAST
                    elif Processed_Input2 in BREAKFAST_OPTIONS[3]:
                        Cost14=Quantity2*EGG
                    elif Processed_Input2 in BREAKFAST_OPTIONS[4]:
                        Cost15=Quantity2*BACON
                    elif Processed_Input2 in BREAKFAST_OPTIONS[5]:
                        Cost16=Quantity2*SAUSAGE
                    elif Processed_Input2 in BREAKFAST_OPTIONS[6]:
                        Cost17=Quantity2*HASH_BROWN
                    elif Processed_Input2 in BREAKFAST_OPTIONS[7]:
                        Cost18=Quantity2*TOAST
                    elif Processed_Input2 in BREAKFAST_OPTIONS[8]:
                        Cost19=Quantity2*COFFEE
                    elif Processed_Input2 in BREAKFAST_OPTIONS[9]:
                        Cost20=Quantity2*TEA
                        Loop_Fix= Order_Error not in BREAKFAST_OPTIONS
                        Order=EXIT_ENTRY
                else:
                    while Answer1 is not True:
                        Number_Error2=input("Please input a quantity: ")
                        if Number_Error2.isnumeric():                                   ### Quantity input error ###
                            Number_Error2=float(Number_Error2)
                            if Processed_Input2 in BREAKFAST_OPTIONS[0]:
                                Cost11=Number_Error2*SMALL_BREAKFAST
                            elif Processed_Input2 in BREAKFAST_OPTIONS[1]:
                                Cost12=Number_Error2*REGULAR_BREAKFAST
                            elif Processed_Input2 in BREAKFAST_OPTIONS[2]:
                                Cost13=Number_Error2*BIG_BREAKFAST
                            elif Processed_Input2 in BREAKFAST_OPTIONS[3]:
                                Cost14=Number_Error2*EGG
                            elif Processed_Input2 in BREAKFAST_OPTIONS[4]:
                                Cost15=Number_Error2*BACON
                            elif Processed_Input2 in BREAKFAST_OPTIONS[5]:
                                Cost16=Number_Error2*SAUSAGE
                            elif Processed_Input2 in BREAKFAST_OPTIONS[6]:
                                Cost17=Number_Error2*HASH_BROWN
                            elif Processed_Input2 in BREAKFAST_OPTIONS[7]:
                                Cost18=Number_Error2*TOAST
                            elif Processed_Input2 in BREAKFAST_OPTIONS[8]:
                                Cost19=Number_Error2*COFFEE
                            elif Processed_Input2 in BREAKFAST_OPTIONS[9]:
                                Cost20=Number_Error2*TEA
                                Loop_Fix= Order_Error not in BREAKFAST_OPTIONS
                                Order=EXIT_ENTRY
                                Answer1=True
                        else:
                            Answer1=False

### Final calculation of totals ###

Total_Cost=Cost1+(Cost2*b)+(Cost3*c)+(Cost4*d)+(Cost5*e)+(Cost6*f)+(Cost7*g)+(Cost8*h)+(Cost9*i)+(Cost10*j)+Cost11+Cost12+Cost13+Cost14+Cost15+Cost16+Cost17+Cost18+Cost19+Cost20
Total_Cost2=Total_Cost*0.13
Total_Cost3=Total_Cost*1.13
print("Cost: ""$ %.2f"% Total_Cost)
print("Tax: ""$ %.2f"% Total_Cost2)
print("Total: ""$ %.2f"% Total_Cost3)
