#!/usr/bin/python
# -*- utf-8


import sys
import signal
import random


def main():
    print 'You are TA(Teaching Assistant) of Ajou University Calculation Training Course.'
    print 'Grade all students\' answers to get the master\'s degree.'
    print 'Each students solved 128 problems and all of the problems are 1 point.'
    print 'You have 64 seconds to do this task.'
    print 'If you understand, type "YES" to start'
    print '= Did you understand? : '
    sys.stdout.flush()

    input_str = sys.stdin.readline().strip('\n')

    if(input_str != 'YES'):
        print 'You need to understand this instruction first.'
        sys.stdout.flush()
        return

    for i in range(0, 64):
        p_error = random.random()
        print 'Student %d out of 64' % (i+1)
        sys.stdout.flush()
        correct = 0

        for j in range(0, 128):
            terms = random.randint(1, 15)
            s = ''

            s += str(random.randint(1, 128))
            for k in range(0, terms):
                op = random.randint(0, 2)
                if op == 0:
                    s += '+'
                elif op == 1:
                    s += '-'
                else:
                    s += '*'
                s += str(random.randint(1, 128))

            if random.random() < p_error:  # correct
                s += '=' + str(eval(s))
                correct += 1
            else:
                s += '=' + str(random.randint(-1048576, 1048576))

            print(s)
            sys.stdout.flush()
            #sys.stdout.write(s)

        print '= Score of this student : '
        sys.stdout.flush()

        score = int(sys.stdin.readline().strip('\n'))

        if score == correct:
            print 'Correct!'
            sys.stdout.flush()
        else:
            print 'Incorrect!'
            sys.stdout.flush()
            return

    print 'Success! You can get a master\'s degree!'
    print 'Flag is "M4S73R_0F_C4LCUL4710N_D3GR33"'
    sys.stdout.flush()


def timeout(signum, frame):
    print '\n\nFailed! Too slow.'
    sys.stdout.flush()
    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(64)
    main()
