def odd_even(num):
    if num % 2 == 0:
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"


print(odd_even(7))
print(odd_even(10))