__author__ = 'serhii'
'''
This function returns standard deviation of sample
'''
from robust_algorithm_s.mean import mean
import statistics
def standard_deviation(general_sample):
    for i in range(0,len(general_sample)):
        buffer_list = []
        buffer_list.append((general_sample[i] - mean(general_sample))**2)
        standard_deviation = statistics.stdev(general_sample)
    return standard_deviation
if __name__ == '__main__':
    out = round(standard_deviation([0, 0.28, 0.32, 0.35, 0.4, 0.49, 0.8, 0.95, 1.98]),2)
    print('Standard deviation of the sample = %s' % statistics.stdev([0, 0.28, 0.32, 0.35, 0.4, 0.49, 0.8, 0.95, 1.98]))




