def square(x: int):
    return x**2

print("Squre of 3 is", square(3))

def pow(x,power):
    return x**power

print("3 to the power of 2 is", pow(3,2))

assert pow(3,2) == square(3), "Some mistake in code or assumption"
print("pow(3,2) == square(3) is ", pow(3,2) == square(3))
assert pow(3,3) == square(3), "Some mistake in code or assumption"