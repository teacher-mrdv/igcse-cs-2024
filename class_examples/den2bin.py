# denary to binary
# we need to use a string '' or "" so that we can prepend
# the binary digit (aka read the modulos backwards)
binary = ''			# '' is an empty string
denary = int( input('Enter an integer >= 0: ') )
# validation: range
while denary < 0:
    denary = int( input('Error. Enter an integer >= 0: ') )

number = denary		# make a copy of the input for processing
while number > 0:
    bit = number % 2
    binary = str(bit) + binary	# convert the bit to a string
    number = number // 2			# floor division

print(f'{denary} in denary = {binary} in binary')