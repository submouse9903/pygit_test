print("helloword")

def selecNum(n):
    for i in range(2, n):
        if(n%i == 0):
            return "소수가아님"
        return "소수"

print(selecNum(8))

