denary = 0
valid_binary = False
while not valid_binary:
    binary = input('Enter a binary number: ')
    valid_binary = True # let's assume it's OK
    # then we check if any bit is not 0 or 1
    for bit in binary:
        if bit != '0' and bit != '1':
            valid_binary = False
            break
            # no point checking anymore if one digit isn't binary
    for bit in binary:
        denary = denary + int(bit)
        denary = 2 * denary
    denary = denary / 2 # because we multiply by 2 one time too many
    print(f'Binary {binary} = Denary {denary}')
    