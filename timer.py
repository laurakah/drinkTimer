import time
import sys
import sound

def main():
    print(' ')
    print(' ')
    print('Instructions: Input drinking schedule.')
    print(' ')

    c = ':'

    hourz = input('Hours: ')
    minz = input('Minutes: ')
    secz = input('Seconds: ')

    while True:
            print(' ')

            hour = int(hourz)
            min = int(minz)
            sec = int(secz)

            while hour > -1:
                while min > -1:
                    while sec > 0:
                        sec=sec-1
                        time.sleep(1)
                        sec1 = ('%02.f' % sec)
                        min1 = ('%02.f' % min)
                        hour1 = ('%02.f' % hour)
                        sys.stdout.write('\n' + str(hour1) + c + str(min1) + c + str(sec1))

                    min = min-1
                    sec = 60
                hour = hour-1
                min = 59

            print(' Drink!')

            sound.play()

            time.sleep(1)

if __name__ == '__main__':
    main()
