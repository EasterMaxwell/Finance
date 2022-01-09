
from time import *

from datetime import datetime

import random

account_balance = 100000

bank_id = 'Finance Bank'

null = ''

sleep(2)
print('Welcome To My Project')

option_a = 'A. Deposit'
option_b = 'B. Withdraw'
option_c = 'C. Create Account'
option_d = 'D. Borrow cash'
option_e = 'E. Register new account'
option_f = 'F. Transfer Money'

sleep(2)
print('Account Balance :', account_balance)

sleep(2)
print(option_a)
sleep(1)
print(option_b)
sleep(1)
print(option_c)
sleep(1)
print(option_d)
sleep(1)
print(option_e)

sleep(3)
user_input = input('\nWhat Would You Like To Do Today? : ')

if user_input == 'A':
    sleep(2)
    deposit_input = int(input('Enter deposit amount : '))
    sleep(2)
    print('Depositing amount...')
    sleep(6)
    print('Your account has been deposited with the sum of', deposit_input)
    sleep(3)
    print('\npreparing deposit details...')
    sleep(4)
    print('\nCurrent account Balance :', deposit_input + account_balance)
    sleep(2)
    print('Date :', datetime.now())
    sleep(2)
    print('Transaction id :', random.randint(1, 500000))
    sleep(2)

    exit_input = input('\nPress x to exit : ')

    if exit_input == 'x':
        sleep(2)
        print('Thank You For Patronizing us.')
        sleep(2)
        print('exiting...')
        sleep(1)
        exit()

    elif exit_input == null:
        sleep(2)
        print('Error : Input Bar Empty!')
        sleep(2)
        print('Terminating program...')
        sleep(2)
        print('Program terminated by default')

    else:
        sleep(2)
        print('Invalid input')

elif user_input == 'B':
    sleep(2)
    option_input = input('Are you sure, YES or NO? : ')

    if option_input == 'NO':
        sleep(2)
        exit_input = input('okay, press x to exit : ')

        if exit_input == 'x':
            sleep(1)
            print('exiting...')
            sleep(1)
            exit()

        elif exit_input == null:
            sleep(2)
            print('Input Bar empty!')
            sleep(2)
            print('Program terminated')

        else:
            sleep(2)
            print('Invalid input')

    elif option_input == 'YES':
        sleep(2)

        withdraw_input = int(input('Enter amount : '))

        while withdraw_input > account_balance:
            sleep(2)
            print('Detecting error...')
            sleep(4)
            print('Sorry, You cannot withdraw that amount of money')
            sleep(2)
            print('Notice : You can only withdraw less than 100,000')
            sleep(2)
            exit()

        sleep(2)
        print('Withdrawing amount...')
        sleep(6)
        print('Withdraw Successful!')
        sleep(3)
        print('Your Account has been debited with', withdraw_input)
        sleep(2)
        print('\nPreparing withdrawal Details...')
        sleep(5)
        print('\nDate :', datetime.now())
        sleep(2)
        print('Transaction id :', random.randint(1, 6000000))
        sleep(3)
        print('Account Balance :', account_balance - withdraw_input)
        sleep(2)
        print('Thank You for Patronizing us!')

    elif option_input == null:
        sleep(2)
        print('Input Bar empty!')

    else:
        sleep(2)
        print('Invalid Input!')

elif user_input == 'C':
    sleep(2)
    choice_input = input('Are you sure to create an account, YES or NO : ')

    if choice_input == 'NO':
        sleep(2)
        terminate_input = input('Alright, press x to exit : ')
        if terminate_input == 'x':
            sleep(2)
            print('exiting...')
            sleep(2)
            exit()

        elif terminate_input == null:
            sleep(2)
            print('Input Bar Empty!')

        else:
            print('Invalid input')


    elif choice_input == 'YES':
        sleep(2)
        name_input = input('Enter Your name : ')
        sleep(2)
        pin_input = int(input('Enter pin number : '))
        sleep(2)
        age_input = int(input('Enter your age : '))

        while age_input < 18:
            sleep(2)
            print('Detecting error...')
            sleep(3)
            print('Your age is not eligible')
            exit()

        while age_input > 120:
            sleep(2)
            print('Detecting error...')
            sleep(3)
            print('Invalid age')
            exit()

        phone_input = int(input('Enter your mobile phone number : '))
        sleep(2)
        print('Creating account...')
        sleep(6)
        print('Account creation successful!')
        sleep(3)
        print('Here are your account details : ')
        sleep(3)
        print('Name :', name_input)
        sleep(2)
        print('Age :', age_input)
        sleep(2)
        print('Pin :', pin_input)
        sleep(2)
        print('Phone number :', phone_input)
        sleep(3)
        print('Your account was created :', datetime.now())
        sleep(2)

        id_num_input = input('press O to get id number : ')

        if id_num_input == '0':
            sleep(3)
            print('Your id number is : ', random.randint(1, 9000000))
            sleep(2)
            print('You are now a verified user!')
            sleep(2)
            print('Thank You for Patronizing us.')

        elif id_num_input == null:
            sleep(2)
            print('Input Bar Empty')

        else:
            sleep(2)
            print('Invalid input')

        sleep(2)
        delete_account_input = input('\nPress d if you want to delete account : ')

        if delete_account_input == 'd':
            sleep(2)
            print('Notice : account is not retrievable after deletion')
            sleep(2)
            print('Deleting account information...')
            sleep(4)
            print('\033[1;36m Account deleted!')

            print('\nDetails : ')
            print('\033[1;08m Name : ', name_input)
            sleep(1)
            print('\033[1;08m Age : ', age_input)
            sleep(1)
            print('\033[1;08m Pin : ', age_input)
            sleep(1)
            print('\033[1;08m Age : ', age_input)
            sleep(2)
            exit()

        elif delete_account_input == null:
            sleep(2)
            print('Input bar empty!')
            sleep(1)
            print('exiting...')
            sleep(3)
            print('program terminated!')
            exit()

        else:
            sleep(2)
            print('Invalid input!')
            sleep(2)
            print('Program terminating by default...')
            sleep(3)
            print('Program terminated!')
            exit()

    elif choice_input == null:
        sleep(2)
        print('Program terminated!')
        sleep(2)
        exit()

elif user_input == 'D':
    sleep(2)
    borrow_input = int(input('Enter the amount : '))
    sleep(2)
    due_input = input('Enter pay back period : ')
    sleep(2)
    n_input = input('Enter your name : ')
    sleep(2)
    p_input = int(input('Enter your pin : '))
    sleep(3)
    print('Borrowing amount...')
    sleep(7)
    print('Borrow successful!')
    sleep(4)
    print('Current Account Balance :', borrow_input + account_balance)
    sleep(3)

    borrow_details_input = input('Do you want to view borrow details, YES or NO : ')

    if borrow_details_input == 'YES':
        sleep(2)
        print('Amount Borrowed :', borrow_input)
        sleep(2)
        print('Date :', datetime.now())
        sleep(2)
        print('Bank Transaction id :', random.randint(1, 9000000))
        sleep(2)
        print('Amount due in :', due_input)
        sleep(2)
        print('Recipient :', n_input)
        sleep(2)
        print('pin info :', p_input)
        sleep(3)
        print('Thank You for Patronizing us!')

    if borrow_details_input == 'NO':
        sleep(3)
        print('Thank you for using our service!')
        sleep(2)
        print('Have a good day!')

    elif borrow_details_input == null:
        sleep(2)
        print('Input bar empty')
        sleep(2)
        print('exiting...')
        sleep(2)
        exit()

if user_input == 'E':
    sleep(2)
    register_input = input('Are you sure about your option, YES or NO : ')

    if register_input == 'YES':
        sleep(2)
        r_name_input = input('Enter Your name : ')
        sleep(2)
        r_age_input = int(input('Enter Your age : '))
        sleep(2)

        while r_age_input < 18:
            sleep(2)
            print('Detecting error...')
            sleep(2)
            print('Your age is not eligible!')
            exit()

        while r_age_input > 120:
            sleep(2)
            print('Detecting Error...')
            sleep(2)
            print('Invalid age!')
            exit()

        r_pin_input = int(input('Enter Your pin (Notice, Ensure not to forget pin) : '))
        sleep(2)
        r_phone_input = int(input('Enter Your mobile phone number : '))
        sleep(3)
        print('Completing Registration...')
        sleep(6)
        print('Registration Successful!')
        sleep(3)
        print('Your account has been registered!')
        sleep(2)

        details_input = input('Would you like to view your details, YES or NO : ')

        if details_input == 'YES':
            sleep(2)
            print('Preparing details...')
            sleep(4)
            print('DETAILS : ')
            sleep(1)
            print('Name of recipient : ', r_name_input)
            sleep(2)
            print('Age : ', r_age_input)
            sleep(2)
            print('Pin number :', r_pin_input)
            sleep(2)
            print('Phone number :', r_phone_input)
            sleep(2)
            print('Registration date : ', datetime.now())
            sleep(2)
            print('Bank id : ', bank_id)
            sleep(2)

            e_input = input('Press x to exit : ')

            if e_input == 'x':
                sleep(2)
                exit()

            elif e_input == null:
                sleep(2)
                print('Input bar empty')
                sleep(2)
                print('Program terminated!')

            else:
                sleep(2)
                print('Invalid input')
                sleep(2)
                print('program exited')

        elif details_input == 'NO':
            sleep(2)
            print('Alright,')
            sleep(2)
            print('\nHey, Thank you for choosing us as your bank!')
            sleep(2)
            print('Good day!')

        elif details_input == null:
            sleep(2)
            print('input bar empty')
            sleep(2)
            print('Program terminated')

    elif register_input == 'NO':
        sleep(2)
        print('Program terminated!')
        sleep(2)
        exit()

    elif register_input == null:
        sleep(2)
        print('Input Bar empty!')
        sleep(2)
        print('exiting...')
        sleep(2)
        exit()

elif user_input == 'F':
    sleep(2)
    transfer_input = int(input('Enter amount : '))
    sleep(2)

    while transfer_input > account_balance:
        sleep(2)
        print('detecting error...')
        sleep(3)
        print('Sorry, you cannot transfer that amount of money')
        sleep(2)
        print('Your account balance is just 100,000')
        exit()

    receiver_input = input('Enter name of receiver : ')
    sleep(2)
    t_pin_input = int(input('Enter your pin : '))
    sleep(2)
    receivers_bank_name = input('Enter bank of receiver : ')
    sleep(2)
    receiver_acc_number = int(input('Enter receivers account number : '))
    sleep(2)

    print('\nProcessing Transaction...')
    sleep(7)
    print('Transfer successful!')
    sleep(2)
    print('Preparing transfer details...')
    sleep(4)

    print('Amount transferred :', transfer_input)
    sleep(2)
    print('Amount transferred to : ')
    sleep(2)
    print('Pin : ', t_pin_input)
    sleep(2)
    print('Bank of receiver : ', receivers_bank_name)
    sleep(2)
    print('Receivers account number : ', receiver_acc_number)
    sleep(2)
    print('Date :', datetime.now())
    sleep(2)
    print('Current Account Balance :', account_balance - transfer_input)
    sleep(3)

    print('\nThank you for Choosing us as Your Bank!')

elif user_input == null:
    sleep(2)
    print('Error : Input Bar Empty!')
    sleep(2)
    print('Program terminated!')
    sleep(2)
    print('Tip : restart program!')






















