# Import(s)
from sys import exit

# Variable(s)
COUNT = 0
USER_FIRST_NAME = ''
USER_LAST_NAME = ''
AGE_CHECK = 0
CITIZEN_CHECK = ''
USER_STATE_CHECK = ''
USER_ZIP_CHECK = 0

# Initial 'Welcome' message
print("\n" + "Welcome to the Python Voter Registration Application" + "\n")


def mk_line(length, is_first=False):
    ''' Fills the beginning and last line of printing output '''
    line = ''
    if is_first:
        line += '+'
    return line + '-' * length + '+'


def first_name():
    ''' User first name setting function '''
    global USER_FIRST_NAME
    USER_FIRST_NAME = input("What is your first name?\n> ").capitalize()
    if USER_FIRST_NAME.isalpha():
        return voter_reg_checks()
    else:
        print("Please enter a valid first name, using only letters.")
        return voter_reg_checks()


def last_name():
    '''' User last name setting function '''
    global USER_LAST_NAME
    USER_LAST_NAME = input("What is your last name?\n> ").capitalize()
    if USER_LAST_NAME.isalpha():
        return voter_reg_checks()
    else:
        print("Please enter a valid last name, using only letters.")
        return voter_reg_checks()


def user_age():
    ''' User age checking function '''
    global AGE_CHECK
    AGE_CHECK = int(input("What is your age? (Between 1 and 119)\n> "))
    if 18 < AGE_CHECK < 120:
        return voter_reg_checks()
    elif 1 <= AGE_CHECK <= 17:
        print("\nYou must be at least 18 to vote. Please try again later.")
        exit()
    else:
        print("\n" + "Please enter an age between 1 and 119." + "\n")
        return user_age()


def user_citizen():
    ''' User Citizenship checking function '''
    global CITIZEN_CHECK
    CITIZEN_CHECK = input("Are you a US citizen?\n> ").capitalize()
    if CITIZEN_CHECK == 'Yes':
        return voter_reg_checks()
    if CITIZEN_CHECK == 'No':
        print("\n" + "We're sorry, you may not vote at this time. Please" +
              " ensure that you are a U.S. citizen and above 18 years old.")
        exit()
    else:
        print("Please enter 'yes' or 'no'.")
        return voter_reg_checks()


def user_state():
    ''' User state checking function '''
    global USER_STATE_CHECK
    us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
                 'FL', 'GA', 'HI', 'IA', 'IL', 'IN', 'IA', 'KS', 'KY',
                 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
                 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
                 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX',
                 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    USER_STATE_CHECK = input("What state do you live in? " +
                             "(TX, MD, etc.)\n> ").upper()

    if USER_STATE_CHECK in us_states:
        return voter_reg_checks()
    else:
        print("Please enter a valid state. (ex. VA, PA, AK, CA, etc)")
        return user_state()


def user_zip():
    ''' User zip code checking function '''
    global USER_ZIP_CHECK
    USER_ZIP_CHECK = input("What is your zip code? (Needs 5 digits)\n> ")

    if len(USER_ZIP_CHECK) == 5:
        return registered_voter()
    else:
        print("Please enter a valid zip code. (ex. 79118, 15222, etc)")
        return user_zip()


def registered_voter():
    ''' Final return statements '''
    line_len = 11
    mk_line.line = mk_line(line_len, True) + (mk_line(line_len, True) +
                                              mk_line(line_len) * 2) * 3
    print(mk_line.line)
    print("\n" + "Thank you for registering to vote. Here is the" +
          " information we've been given:\n")
    print(f'Name (first, last): {USER_FIRST_NAME} {USER_LAST_NAME}')
    print(f'Age: {AGE_CHECK}')
    print(f'U.S. Citizen: {CITIZEN_CHECK}')
    print(f'State: {USER_STATE_CHECK}')
    print(f'Zip Code: {USER_ZIP_CHECK}')
    print("\n" + "Thank you for trying the voter registration application." +
          " Your voter registration card should be shipped within 3 weeks." +
          "\n")
    print(mk_line.line)
    exit()



def voter_reg_checks():
    ''' Main program function '''
    global COUNT
    user_selection = None

    user_selection = input("Do you want to continue with Voter Registration?" +
                           "\n> ").lower().strip()
    if user_selection == 'yes':
        if COUNT == 0:
            user_selection = None
            COUNT = COUNT + 1
            first_name()
        elif COUNT == 1:
            user_selection = None
            COUNT = COUNT + 1
            last_name()
        elif COUNT == 2:
            user_selection = None
            COUNT = COUNT + 1
            user_age()
        elif COUNT == 3:
            user_selection = None
            COUNT = COUNT + 1
            user_citizen()
        elif COUNT == 4:
            user_selection = None
            COUNT = COUNT + 1
            user_state()
        elif COUNT == 5:
            user_selection = None
            COUNT = COUNT + 1
            user_zip()
    if user_selection == 'no':
        print("\n" + "Thank you for trying the Voter Registration" +
              " application. We hope to see you again!" + "\n")
        exit()
    else:
        print("Please enter 'yes' or 'no'.")
        return voter_reg_checks()

voter_reg_checks()
