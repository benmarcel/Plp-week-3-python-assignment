def large_power(base, exponent):
    result = base ** exponent;
    # checking if the result is large or not if so returns true else returns false
    if result == 5000: return True;
    else: return False;


base = float(input("Enter the base number:"));
exponent = int(input("Enter the exponent:"))

if large_power(base, exponent) :
    print("The power is large!")
else:
    print("The power is small");



def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0: return True
    else: return False;

number = int(input("Enter number:"))

if divisible_by_ten(number) :
    print(f"{number} is divisible by ten")
else:
    print(f"{number} is not divisible by ten")    
