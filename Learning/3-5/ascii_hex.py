# ascii_hex.py , Python 3.5
# Show an uppercase character ASCII codes in decimal and hex

foo = None

while(foo != 48): # Loop until the user enters a '0'
	foo = ord(input('Letter: ').upper()) # capitalize and convert to ASCII code
	print(foo) # print the code in decimal
	print(hex(foo)) # in hex
