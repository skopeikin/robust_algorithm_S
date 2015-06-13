__author__ = 'skopeikin'
'''
This function makes replacement of values in sample with limiting value
'''
def replace(sample, psi):
    inner_sample = sample[:]
    for i in range( 0, len(sample)):
        if inner_sample[i] > psi: inner_sample[i] = psi
    return inner_sample
if __name__ == '__main__':
    out = replace([0,0.28,0.32,0.35,0.4,0.49,0.8,0.95,1.98],0.66)
    print('Transformed sample with limit value psi = %s ' % out)
