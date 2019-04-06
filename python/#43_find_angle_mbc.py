'''
Find Angle MBC
'''

import math

if __name__ == '__main__':
    ab = float(input())
    bc = float(input())

    angle = int(round(math.degrees(math.atan2(ab,bc))))
    print(str(angle) + '°')

