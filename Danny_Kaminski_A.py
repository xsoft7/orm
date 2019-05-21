'''
Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on
the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
'''


def overlap(line1, line2):
    # first check, if they are the same, they are crossing.. except if it's a single dot. e.g: (1,1),(2,2)..
    if line1 == line2 and line1[0] != line1[1]:
        return line1,line2,'overlapping'
    # needed for incorrect input,  it fixes it
    if line1[0] > line1[1]:
        line1 = tuple(reversed(line1))

    if line2[0] > line2[1]:
        line2 = tuple(reversed(line2))

    # checks if first coordiante is within the limits of the other line
    if line2[0] < line1[0] < line2[1] or line1[0] < line2[0] < line1[1]:
        return line1,line2,'overlapping'
    # checks if second coordiante is within the limits of the other line
    elif line2[0] < line1[1] < line2[1] or line1[0] < line2[1] < line1[1]:
        return line1,line2,'overlapping'

    else:
        return line1,line2,'Not overlapping'

if __name__ == '__main__':
    #different use cases

    l1 = (1, 5)
    l2 = (2, 6)
    l3 = (6, 8)

    l4 = (1.0, 5.0)
    l5 = (2.0, 6.0)
    l6 = (6.0, 8.0)

    l7 = (-1, -5)
    l8 = (-2, -6)
    l9 = (-6, -8)

    l10 = (-5, -1)
    l11 = (-6, -2)
    l12 = (-8, -6)

    l13 = (0, 5)
    l14 = (2, 5)
    l15 = (-1, 1)
    l16 = (0, 0)
    l17 = (0, 0.1)
    l18 = (-0, 0)
    '''
    just switch the lines you want to check/compare with
    '''
    print(f'The lines are: {overlap(l1, l2)}')
    print(f'The lines are: {overlap(l2, l3)}')
    print(f'The lines are: {overlap(l1, l3)}')



