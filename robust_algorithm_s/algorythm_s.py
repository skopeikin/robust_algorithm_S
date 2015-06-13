__author__ = 'skopeikin'
'''
This function executes robust algorythm S and returns robust standard deviation of sample
'''
from robust_algorithm_s.sample_transformation import replace
from robust_algorithm_s.rms_difference import rms_diff
def algorythm_s(sample, psi, wi, w = [], eta = 1.645, ksi = 1.097):
    i=0
    main_result=[]
    while 1:
        inner_sample = replace(sample,psi[i])
        inner_rms = rms_diff(inner_sample)
        wi.append(inner_rms)
        inner_robust_value = round(inner_rms * ksi, 2)
        w.append(inner_robust_value)
        psi.append(round(inner_robust_value * eta,2))
        if abs(psi[i+1] - psi[i]) < 0.00001: break
        else:i+=1
        main_result.append(psi)
        main_result.append(wi)
        main_result.append(w)
    return main_result
if __name__ == '__main__':
    out = algorythm_s([0,0.28,0.32,0.35,0.4,0.49,0.8,0.95,1.98],[0.4*1.645],[0.83])
    print('List of robust standard deviations by iterations: %s' % out[2] + '\n'+ 'List of standard deviations by iterations: %s' % out[1] +  '\n' + 'List of limit values by iterations: %s' % out[0])
