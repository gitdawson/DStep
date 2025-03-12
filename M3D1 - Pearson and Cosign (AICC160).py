import math


y = 1
x = 2
 
def pearson(x,y):
    if len(x) != len(y):
        return "Error: Lists are not the same length"
    else:
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum([i**2 for i in x])
        sum_y2 = sum([i**2 for i in y])
        psum = sum([x[i]*y[i] for i in range(n)])
        num = psum - (sum_x * sum_y/n)
        den = ((sum_x2 - pow(sum_x,2)/n) * (sum_y2 - pow(sum_y,2)/n))**.5
        if den == 0:
            return "Error: Denominator is zero"
        else:
            return num/den
        

def cosinesimilarity(x,y):
    if len(x) != len(y):
        return "Error: Lists are not the same length"
    else:
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum([i**2 for i in x])
        sum_y2 = sum([i**2 for i in y])
        psum = sum([x[i]*y[i] for i in range(n)])
        num = psum - (sum_x * sum_y/n)
        den = ((sum_x2 - pow(sum_x,2)/n) * (sum_y2 - pow(sum_y,2)/n))**.5
        if den == 0:
            return "Error: Denominator is zero"
        else:
            return num/den





