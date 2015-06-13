__author__ = 'serhii'
'''This function is used for counting common mean for sample of stabdard deviations.
It takes sample and volume of underlying samples as arguments and returns common mean value'''
from copy import deepcopy
def common_mean(sample,volume):
    nu=volume-1
    local_sample = deepcopy(sample)
    local_sample = [(x**2)*nu for x in local_sample]
    common_mean = (sum(local_sample)/sum([nu+1 for i in range (0,len(local_sample))]))**0.5
    return common_mean
if __name__ == '__main__':
    out = common_mean([0.04,0.29,0.53,1.4,5.58],2)
    print('Common mean as estimate of RMS deviation = %s' % out)