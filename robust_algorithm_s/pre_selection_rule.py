__author__ = 'serhii'
''' This function is used to decide whether or not sample is applicable for robust algorithm.
 It takes sample of standard deviations and volume of each underneath sample and returns list of booleans,
  which is used as code for further actions'''
from robust_algorithm_s import mediana
from statistics import stdev
def selection_rule(sample,volume):
    code_of_rule = []
    nu = volume - 1
    g_cochren = (((max(sample))**2)/sum(x**2 for x in sample))
    is_small = False
    if (volume < 5):
        is_small=True
    is_wide = False
    if max(sample) - mediana.mediana(sample) < 2 * stdev(sample):
        is_wide = False
    else:
        is_wide = True
    interval_mapping = {1:[0.8414, 0.8614, 0.88, 0.9305],2:[0.6838, 0.7115, 0.7339, 0.7563],3:[0.5981, 0.6276, 0.6547, 0.6744],4:[0.5441, 0.6066, 0.6334, 0.6755], 5:[0.5061, 0.5771, 0.6336, 0.7002], 6:[0.4783, 0.5838, 0.6336, 0.6806], 8:[0.4387, 0.5562, 0.5888, 0.6329]}
    interval = interval_mapping[nu]
    interval_code = []
    for i in interval:
        if g_cochren > i:
            interval_code.append(1)
        else:
            interval_code.append(0)
    is_outlier = False
    if sum(interval_code) > 2:
        is_outlier=True
    else:
        is_outlier=False
    code_of_rule.append(is_outlier)
    code_of_rule.append(is_wide)
    code_of_rule.append(is_small)
    return code_of_rule
if __name__ == '__main__':
    out = selection_rule([0.04,0.29,0.53,1.4,5.58],2)
    print('Code of selection rule = %s' % out)
