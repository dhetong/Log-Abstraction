from random import randint
import time

"""
This is use for create 30 file one by one in each 5 seconds interval. 
These files will store content dynamically from 'lorem.txt' using below code
"""


def main():
    a = 1
    with open('Zookeeper.txt', 'r') as file:  # reading content from 'lorem.txt' file
        lines = file.readlines()
        while a <= 30:
            totalline = len(lines)
            linenumber = randint(0, totalline - 10)
            with open('C://Users//skyba//Documents//GitHub//Log//log{}.txt'.format(a), 'w') as writefile:
                writefile.writelines(' '.join(line for line in lines[linenumber:totalline]))
            print('creating file log.txt'.format(a))
            a += 1
            time.sleep(5)


if __name__ == '__main__':
    main()