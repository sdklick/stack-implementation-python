# stack implementation in python
# stack oparation push,pop,peek,view,exit

a = []


def datapush(a, b):
    a.append(b)


def datapop(a):
    view = a.pop()
    print('you delete : ', view)


def datapeek(a):
    view1 = a[-1]
    print('your peek element : ', view1)

def datadisplay(a):
    for x in a:
        print(x)


while True:
    userinput = int(input('push=>1 \n pop=>2 \n peek=>3 \n display=>4 \n exit=>5 : '))
    if userinput >= 1 and userinput <= 5:
        if userinput == 1:
            datainput = input("Enter your value : ")
            datapush(a, datainput)
        elif userinput == 2:
            if len(a) == 0:
                print("your Stack is empty")
            else:
                datapop(a)
        elif userinput == 3:
            if len(a) == 0:
                print("your Stack is empty")
            else:
                datapeek(a)
        elif userinput == 4:
            if len(a) == 0:
                print("your Stack is empty")
            else:
                datadisplay(a)
        elif userinput == 5:
            break
    else:
        print('you enter wrong number')
        break