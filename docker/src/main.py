import datetime
import os

if __name__ == '__main__':
    print(f"Hello Word!")

    now = datetime.datetime.now()

    import os
    print(os.environ['HOME'])

    for i in range(1, 11):
        print(i)

    print(f"Todays date and time is {now} ")
    