# Program to show Constant Time Complexity
def OnTime(n):
    iterations = 0
    for i in range(1,n+1):
        iterations += 1
    print("When n is ",n," Iterationa ",iterations)

OnTime(10)
OnTime(20)
OnTime(47)

print("\nWith every 'n' the time taken and iterations will increase")