__author__ = 'serhii'
'''
This function returns median of sample
'''
def mediana(List):
    if len(List)/2-len(List)//2==0:
        mediana=(List[len(List)//2-1]+List[len(List)//2])/2
    else:
        mediana=List[(len(List)-len(List)//2)-1]
    return mediana
if __name__ == '__main__':
    out = mediana([0, 0.28, 0.32, 0.35, 0.4, 0.49, 0.8, 0.95, 1.98])
    print('Median of the sample = %s' % out)
