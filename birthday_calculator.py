# Datetime mod
import time, datetime as dt

# Make a function
def birthday_calc(YY, MON, DD, HH, MIN):
    # Estblish dates
    birthtime = dt.datetime(YY, MON, DD, HH, MIN)
    now = dt.datetime.now()
    birthday = dt.datetime(now.year, MON, DD, HH, MIN)

    # Function to convert timedelta days into years, months, and days
    def daychop(days):
        chopped = {
            'years' : (int(days//365.2422)),
            'months' : (int((days%365.2422)//30.43685)),
            'days' : (int((days%365.2422)%30.43685))
        }
        return chopped

    # Function to convert timedelta seconds into hours, and minutes
    def secondchop(seconds):
        chopped = {
            'hours' : str(int(seconds//3600)).zfill(2),
            'minutes' : str(int((seconds%3600)//60)).zfill(2)
            }
        return chopped

    # Calculate age
    age = now - birthtime
    age_dict = daychop(age.days)
    age_dict.update(secondchop(age.seconds))
    full_age = '{years} years, {months} months, {days} days, and {hours}:{minutes}'.format(**age_dict)

    # Calculate countdown
    countdown = birthday - now
    countdown_dict = daychop(countdown.days)
    countdown_dict.update(secondchop(countdown.seconds))
    full_countdown = '{months} months, {days} days, and {hours}:{minutes}'.format(**countdown_dict)

    # Display
    print(f'\n\nI am {full_age} old.')
    print(f'{full_countdown} until my next birthday.')

# Run the birthday_calc() function for your birthday
birthday_calc(2001, 1, 1, 1, 1)
