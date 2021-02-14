# Function to ask a question, user answers, returns answer as a boolean

def yn_to_TF(question):
    yn = input(question)
    while True:
        if yn.lower() in ("yes", "heck yeah!", "yup", "y", "1"):
            TF = True
            break
        elif yn.lower() in ("no", "not on your life!", "nay", "n", "0"):
            TF = False
            break
        else:
            yn = input("\n\nError: invalid response." + question)
    return TF
