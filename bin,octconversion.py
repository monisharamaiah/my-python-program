def binary_to_decimal(binary):
  decimal=0
  for digit in binary:
    decimal=decimal*2+int(digit)
  return decimal
def octal_to_hexadecimal(octal):
  decimal=0
  for digit in octal:
    decimal=decimal*8+int(digit)
  hexadecimal=hex(decimal).strip("0x").upper()
  return hexadecimal
binary=input("Enter a binary number: ")
octal=input("Enter an octal number: ")
decimal=binary_to_decimal(binary)
print("The decimal equvalent of",binary,"is",decimal)
hexadecimal=octal_to_hexadecimal(octal)
print("The hexadecimal equvalent of",octal,"is",hexadecimal)
