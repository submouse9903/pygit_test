# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fibona(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fibona(n-1)+fibona(n-2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(fibona(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
