import random, yes_no

# Declare some important variables
chars = ""
code = ""
i = 0
repeat = True
plan_break = False
partition = "\n___________________________________________________________________________________"

print(partition)

# Function determine whether to allow repeating charachters 
def repeat_setter(possible_char_num):
    global repeat
    if possible_char_num >= char_amount:
        repeat = yes_no.yn_to_TF(partition + "\n\nAllow repeating charachters?")
    else:
        repeat = True

print(partition)

# Determine which charachters to include
while True:
    char_type = input("\n\nEnter all that apply:\n1)Capital Alphabet\n2)Lowercase Alphabet\n3)Numbers\n4)Symbols\n(1/3/1,4/etc)\n")

    if "1" in char_type:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        plan_break = True
    if "2" in char_type:
        chars += "abcdefghijklmnopqrstuvwxyz"
        plan_break = True
    if "3" in char_type:
        allow_zero = yes_no.yn_to_TF(partition + "\n\nAllow the number 0?")
        if allow_zero:
            chars += "1234567890"
        else:
            chars += "123456789"
        plan_break = True
    if "4" in char_type:
        chars += "!@#$%&*?~+=_-"
        plan_break = True
    if plan_break == True:
        break
    else:
        print(partition + "Invalid input")

# Scramble possible charachters for added randomness
char_list = [chars]
random.shuffle(char_list)
chars = char_list[0]

# Prompmt for how many charachters the password should be
char_amount = int(input(partition + "\n\nHow many charachters should the password be? "))

repeat_setter(len(chars))

# Generate password
while i < char_amount:
    char = random.choice(chars)
    if repeat == False and char in code:
        continue
    else:
        code += char
        i += 1

# Print password
print(partition + "\n\nYour password is:  " + code)
