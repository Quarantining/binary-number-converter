# very simple decimal to binary number converter using the subtraction method.
# had some help with chatgpt but I figured it out
decimal_num = int(input("> ")) # asks user for a decimal num
binary = [] # creates an empty list to store the binary nums

# can convert numbers from 1-256
powers_of_2 = [256, 128, 64, 32, 16, 8, 4, 2, 1]

# for loop to iterate through list
for i in powers_of_2: # i = current list index
    if decimal_num < i: # checks if decimal is less than i
        binary.append(0) # if so, adds 0 to binary
    else: # otherwise (it must be greater)
        binary.append(1) # it adds 1
        decimal_num -= i # and subtracts i

p1 = binary.index(1) # checks for first occurrence of 1 (p1 means position 1 in index)
binary = binary[p1:] # removes everything before p1
binary = ''.join(str(i) for i in binary) # changes to more readable string
print(binary) # prints to screen