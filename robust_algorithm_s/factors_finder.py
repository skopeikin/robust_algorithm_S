__author__ = 'serhii'
'''This function returns eta and ksi - the factors for robust algorithm S.
 It takes probabilities and nu'''
from scipy import stats
def factor_finder(probability,nu=1):
    factors=[]
    eta = (stats.chi2.ppf(probability,nu)/nu)**0.5
    probabilities=[x*0.01 for x in range(1,100)]
    z=0
    for x in probabilities:
        prob = (stats.chi2.ppf(1-x,nu+2))
        if prob < nu*(eta**2):
            z=1-x
            break
    ksi = 1/((z+((1-probability)*(eta**2)))**0.5)
    factors.append(eta)
    factors.append(ksi)
    return factors
if __name__ == '__main__':
    out = factor_finder(0.935,1)
    print('Factors for interval A and nu=1 = %s' % out)

