__author__ = 'serhii'
'''
This function returns first limiting value for Algorythm S
'''
def first_limit_value(median, eta = 1.645):
    return (round(median * eta,2))
if __name__ == '__main__':
    out = first_limit_value(0.4,1.96)
    print('First limit value for Algorythm S = %s' % out)