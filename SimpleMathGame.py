import random
import operator

def randomProblems():
    operat = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    op = random.choice(list(operat.keys()))
    answer = operat[op](n1, n2)
    print("age gofti "f'({n1} {op} {n2})'" chand mishe?")
    return answer

def getUserInput():
    answer = randomProblems()
    Canswer = int(input("inja benevis : "))
    if Canswer == answer:
        return True
    else:
        return False

emtiaz = 0       
while True:
    if  getUserInput() == True:
        emtiaz += 1
        print("afariiiiiiiiiiin")
    else:
        print("Ridi !!!")
        print(f"emtiaz shoma : {emtiaz}")
        break
     
    

