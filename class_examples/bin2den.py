denary:int = 0
valid_binary:bool = False # so that we go into the loop at least once!
while not valid_binary:
    # we use a string for binary so we can use the for loop later
    # to go through each bit
    binary = input('Enter a binary number: ')
    valid_binary = True # let's assume it's OK
    # then we check if any bit is not 0 or 1 otherwise
    # this is a format check-all characters in binary string
    # must be 0 or 1, it's not a binary number
    for bit in binary:
        if bit != '0' and bit != '1' and bit != ' ':
            valid_binary = False
            print('Error - input is not a binary number! Please input again.')
            break
            # no point checking anymore if one digit isn't binary
        #end if
#end while
for bit in binary:
    if bit != ' ':
        denary = denary + int(bit)
        denary = 2 * denary
    #end if
denary = int(denary / 2) # because we multiply by 2 one time too many
print(f'Binary {binary} = Denary {denary}')
