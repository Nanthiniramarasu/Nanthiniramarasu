#Program-3.py

#Generate series of odd number based on a given input with even/odd rules.
#Odd number = n
#Even number = n-1

n = int(input("Enter the value: "))
print("n = ",n)

if n%2 == 0:
    count = n-1
else:
    count = n
print("Result: ")

for i in range(count):
    print(2*i+1, end ="," if i!=count-1 else "\n")
