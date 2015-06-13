__author__ = 'serhii'
from robust_algorithm_s.difference import difference
from robust_algorithm_s.standart_deviation import standard_deviation
from robust_algorithm_s.mediana import mediana
from robust_algorithm_s.first_limit_value import first_limit_value
from robust_algorithm_s.rms_difference import rms_diff
from robust_algorithm_s.algorythm_s import algorythm_s
from robust_algorithm_s.reproducibility_deviation import reproduce_dev
from robust_algorithm_s.iterations_quantity import eval_num
from robust_algorithm_s.pre_selection_rule import selection_rule
from robust_algorithm_s.common_mean import common_mean
from robust_algorithm_s.suitable_algorithm_factors import get_suitable_algorithm_factors
number = int(input('Enter number of samples:'))
volume = int(input('Enter volume of samples:'))
general_sample = []
psi=[]
wi=[]
w=[]
for j in range(0,number):
    general_sample.append([float(input('Enter element %s of sample %s: ' % (i+1,j+1))) for i in range (0,volume)])
if volume == 2:
    for i in range(0,len(general_sample)):general_sample[i] = round(difference(general_sample[i]),2)
elif volume > 2:
    for i in range(0,len(general_sample)):general_sample[i] = round(standard_deviation(general_sample[i]),2)
median = mediana(sorted(general_sample))
psi.append(first_limit_value(median))
wi.append(rms_diff(general_sample))
code_of_selection_rule = selection_rule(general_sample,volume)
if (code_of_selection_rule == [False,False,False]) or (code_of_selection_rule == [False,True,True]) or (code_of_selection_rule == [False,True,False]) or (code_of_selection_rule == [True,True,True]):
    factors = get_suitable_algorithm_factors(general_sample,volume)
    result = algorythm_s(general_sample,psi,wi,eta=factors[0], ksi=factors[1])
    psi=result[0]
    wi=result[1]
    w=result[2]
    sr = reproduce_dev(w)
    iterations = eval_num(w)
    print('List of robust standard deviation by iterations: ', w)
    print('List of standard deviations by iterations: ', wi)
    print('List of limit values by iterations: ', psi)
    print('List of reproducibility deviations by iterations: ', sr)
    print ('Number of iterations to convergence = %s' % (iterations-1))
else:
    RMS_deviation_estimate = common_mean(general_sample,volume)
    print('The most unbiased estimation of RMS deviation is common mean of standard deviation of samples: %s' % RMS_deviation_estimate)
