__author__ = 'serhii'
'''
This function returns difference of values if volume of sample is 2
'''
def difference(sample):
    diff = round (abs (sample[0] - sample[1]),2)
    return diff
if __name__ == '__main__':
    out = difference([24.28, 24.00])
    print ('Difference between results = %s' % out)