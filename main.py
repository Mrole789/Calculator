print("""
 _  __                _        ____      _            _       _             
| |/ /___ _ __  _ __ ( )___   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| ' // _ \ '_ \| '_ \|// __| | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| . \  __/ | | | | | | \__ \ | |__| (_| | | (__| |_| | | (_| | || (_) | |   
|_|\_\___|_| |_|_| |_| |___/  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
""")
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calcus():
    endcalcus = False

    num1 = float(input("What is the first number?\n"))
    for x in operations:
        print(x)

    while not endcalcus:
        ops = input("Pick an operation symbol:\n")
        num2 = float(input("What is the next number?\n"))

        fn = ''
        ans = ''
        fn = operations[ops]
        ans = fn(num1, num2)

        print(f"{num1} {ops} {num2} = {ans}")

        opt = input(f"Type 'y' to continue with {ans} or type 'n' to start a new calculation:\n")
        if opt == "n":
            endcalcus = True
            calcus()
        
        num1 = ans

calcus()