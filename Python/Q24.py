# Program to convert decimal -> binary, octal, hexadecimal

n = int(input("Enter the number: "))

print(f"The decimal number of {n} is:")
print(bin(n), "in binary")
print(oct(n), "in octal")
print(hex(n), "in hexadecimal")