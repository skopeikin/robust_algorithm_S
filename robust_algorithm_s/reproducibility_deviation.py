__author__ = 'serhii'
'''
This function returns reproducibility deviation of sample
'''
def reproduce_dev(robust_stdev):
    sr = []
    for i in range(0,len(robust_stdev)):
        sr.append(round(robust_stdev[i]/pow(2,0.5),2))
    return sr
if __name__ == '__main__':
    out = reproduce_dev([0.52, 0.61, 0.66, 0.68])
    print('Reproducibility deviation of samples = %s' % out)
