#Program-2.py

#Generate a series of odd number up to the x-th term

n = int(input("Enter the value: "))
print("n = ",n)

#first odd number is 1, next 3, next 5, next 7, etc.,
print("Result: ")

for i in range(n):
    #formula for ith odd number is (2*i+1)
    print(2*i+1,end="," if i!= n-1 else"\n")
