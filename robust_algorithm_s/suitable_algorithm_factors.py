__author__ = 'serhii'
'''This function is used to get the factors of algorithm S which produces the most unbiased robust estimate.
 It takes sample of standard deviations and volume of underlying samples and returns eta and ksi'''
from robust_algorithm_s.factors_finder import factor_finder
def get_suitable_algorithm_factors(sample, volume):
    nu = volume-1
    interval_mapping = {1:[0.8414, 0.8614, 0.88, 0.9305],2:[0.6838, 0.7115, 0.7339, 0.7563],3:[0.5981, 0.6276, 0.6547, 0.6744],4:[0.5441, 0.6066, 0.6334, 0.6755], 5:[0.5061, 0.5771, 0.6336, 0.7002], 6:[0.4783, 0.5838, 0.6336, 0.6806], 8:[0.4387, 0.5562, 0.5888, 0.6329]}
    g_cochren = (((max(sample))**2)/sum(x**2 for x in sample))
    interval = interval_mapping[nu]
    interval_code = []
    for i in interval:
        if g_cochren > i:
            interval_code.append(1)
        else:
            interval_code.append(0)
    key = sum(interval_code)
    probabilities_mapping = {1:[0.935, 0.945, 0.95, 0.995],2:[0.93, 0.955, 0.955, 0.995],3:[0.875, 0.935, 0.955, 0.995],4:[0.81, 0.93, 0.96, 0.995], 5:[0.8, 0.93, 0.98, 0.995], 6:[0.815, 0.955, 0.985, 0.995], 8:[0.825, 0.945, 0.98, 0.995]}
    probability_list = probabilities_mapping[nu]
    the_best_probability = probability_list[key-1]
    factors = factor_finder(the_best_probability,nu)
    return factors
if __name__ == '__main__':
    out = get_suitable_algorithm_factors([0.108,0.174,0.575,0.988,4.533],2)
    print('the best factors for sample = %s' % out)
