# Mason Manca
# CPSC 222
# Dr.Sprint
# 9/27/21

import utils

col_name = utils.main()

headers,data = utils.read_data("fitbit_data_3-8_9-16.csv")

headers = headers.split(',')
#
column = utils.get_column(headers,col_name, data)

column = utils.convert_column_to_numeric(column)

utils.display_table(headers,column)

Average = utils.findMean(column)

print("The mean of the data is: " + "{:.2f}".format(Average))

standardDeviation = utils.findStandardDeviation(column) # changes lst here


print("The standard deviation of the data is: " + "{:.2f}".format(standardDeviation))
#
median = utils.findMedian(column)
#
print("The median of the data is: " + "{:.2f}".format(median))
#
minimum = utils.findMin(column)
#
print("The minimum value of the data is: " + "{:.2f}".format(minimum))
#
maximum = utils.findMax(column)
#
print('The maximum value of the data is: ' + "{:.2f}".format(maximum))

