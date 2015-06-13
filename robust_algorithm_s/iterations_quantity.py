__author__ = 'serhii'
'''
This function returns number of iterations of algorythm S
'''
def eval_num(w):
    iterations = len(w)
    return iterations
if __name__ == '__main__':
    out = eval_num([0.4, 0.52, 0.61, 0.66, 0.68])
    print ("Number of iterations = %s" % out)