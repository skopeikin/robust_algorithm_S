__author__ = 'serhii'
'''
This function returns RMS difference for sample of differences
'''
def rms_diff (sample):
    rms_difference = round((sum([i**2 for i in sample])/len(sample))**0.5,2)
    return rms_difference
if __name__ == '__main__':
    out = rms_diff([0,0.28,0.32,0.35,0.40,0.49,0.8,0.95,1.98])
    print('Root mean square difference for differences or standard deviations = %s' % out)
