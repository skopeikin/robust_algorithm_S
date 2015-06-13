__author__ = 'serhii'
'''
This function returns mean of sample
'''
def mean(general_sample):
    mean=round(sum(general_sample)/len(general_sample),2)
    return mean
if __name__ == '__main__':
    out = mean([0, 0.28, 0.32, 0.35, 0.4, 0.49, 0.8, 0.95, 1.98])
    print('Mean of the sample = %s' % out)
