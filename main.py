#best practice to import libraries at the beggining of the script
from time import sleep
from datetime import datetime  # To receive live time to be as accurate as possible.



def main():
    try:
        while True:
            question()
    except KeyboardInterrupt:
        print("\n[*] Exiting \n")


def question():
    #cleaner way to print multiple lines back to back
    print ("""It is now time to get the money you deserve
Keep tract of the money you lend with You Owe Me
Below ths line you need to just put the PERSON, AMOUNT given, and the DATE you gave it to that person.
""")
    print('-' * 150)
    print('\n')
    while True:
        a = str(input('Person- '))
        if  isinstance(a, str) == True:
            break
        else:
            print("[*] please input a string")
    while True:
        try:
            b = int(input('Amount Due- '))
            break
        except ValueError:
            print("\n[*] Please Input a Number")

    while True:
        try:
           c1 = int(input("year- "))
           c2 = int(input("month- "))
           c3 = int(input("day- "))
           real_date = datetime.date(c1, c2, c3)
           break
        except ValueError:
           print("\n[*] Please Input Number")
    print ("\n- Person: {}".format(a))
    print ("- Money They Owe You: ${}".format(b))
    print ("- Date: {}/{}/{}".format(c2, c3, c1))
    print (real_date)
    #Now it's time to set the reminder when to collect your funds.

    I1 = input('Set A Time To Remind Yourself When To Get Your Money! (Make sure to take up four digts. Ex: 0328 = 3:28)--------->')
      # Makes it easy to set the alarm.
    if len(I1) > 3:  # The time needs to be 4 numbers long with no semicolon e.g. 0730\
        hour1 = I1[0:2]  # seperrates the hour from the minutes
        minute1 = I1[2:]  # seperrates the minutes from the hours
        print('Alarm set for: %s:%s' % (hour1,minute1))  # confirms the set time

    while True:  # constantly updates the current time and variables\
        now = datetime.now()
        hournow = now.hour
        minnow = now.minute
        if int(hournow) == int (hour1) and int(minnow) == int(minute1):\
            print('GET YOUR MONEY FROM ') + a  # this is a substitute for a buzzer or a beeper
        sleep (1)

if __name__ == '__main__': main()
