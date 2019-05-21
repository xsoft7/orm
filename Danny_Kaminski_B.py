'''
Question B

The goal of this question is to write a software library that accepts 2 version string as input
and returns whether one is greater than, equal, or less than the other.
As an example: “1.2” is greater than “1.1”.
Please provide all test cases you could think of
'''


def str2float(str1, str2):
    try:
        if r'/' in str1 or r'/' in str2:
            if r'/' in str1:
                num, denom = str1.split('/')
                f1 = float(num) / float(denom)
            else:
                f1 = float(str1)
            if r'/' in str2:
                num, denom = str2.split('/')
                f2 = float(num) / float(denom)
            else:
                f2=float(str2)
        else:
            f1, f2 = float(str1), float(str2)
        if f1 == f2:
            return f'{str1} is Equal to {str2}'
        elif f1 > f2:
            return f'{str1} is bigger then {str2}'
        else:
            return f'{str2} is bigger then {str1}'
    except:

        return Exception('string cannot be converted to a number')

if __name__ == '__main__':
    s1, s2 = '1.2', '1.1'
    print(str2float('1.2', '1.1'))
    print(str2float('-1.2', '1.1'))
    print(str2float('1.2', '-1.1'))
    print(str2float('-1.2', '-1.1'))
    print(str2float('1.1', '1.1'))
    print(str2float('0', '0'))
    print(str2float('-0', '0'))
    print(str2float('asd', '0'))
    print(str2float('0.0000000000000000000', '0'))
    print(str2float('0.0000000000000000001', '0'))
    print(str2float('-0.0000000000000000001', '0'))
    print(str2float('1/2', '0'))
    print(str2float('1/2', '0.5'))
    print(str2float('0.5', '1/2'))