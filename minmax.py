import numpy
from scipy import stats
arr = [1,22,3,4,2,5,2,6,7,8,2]
x = numpy.mean(arr)
print("Mean",x)
x = numpy.median(arr)
print("Median",x)
#x = stats.mode(arr)
modevalue,modecount=stats.mode(arr)
print("Mode Value",modevalue[0],"Mode count",modecount[0])