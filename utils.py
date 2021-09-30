# Mason Manca
# CPSC 222
# Dr.Sprint
# 9/27/21
import math

def read_data(filename):
   data = []
   headers = []
   infile = open(filename, "r")
   headers = infile.readline()
   lines = infile.readlines() 
   infile.close()
   cleaned_lines = clean_Lines(lines)

   for line in cleaned_lines:
       vals = line.split(",")
       data.append(vals)
   data = remove_whitespace(data)
  
   return(headers,data)

def display_table(headers,data):
    print(headers)
    for values in data:
       print(values,end= '\t'*2)
    print()

def clean_Lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines

def remove_whitespace(data):
    for row in data:
        for i in range(len(row)):
            row[i] = row[i].strip() #clean up lines
    return data

def get_column(headers, col_name, data):
    userData = []
    idx = 0
    idx = headers.index(col_name) # returns index of col_name
    for row in data:
        userData.append(row[idx])
    return(userData)

def convert_column_to_numeric(data):
    int_map = map(int,data)

    integer_list = list(int_map)
    return integer_list

def findStandardDeviation(n):
    mean = findMean(n)
    j = 0
    newLst = []
    newLst[:] = n
    for i in newLst:
        newLst[j] = ((newLst[j]) - mean) #subtract mean from each element
        newLst[j] = newLst[j] ** 2
        j += 1
    mean = findMean(newLst) # find mean of the list

    return(math.sqrt(mean)) #return sqrt

def findMedian(n):
    sortedLst = sorted(n) # needs to be sorted for median
    index = ((len(n)-1) // 2)
    
    if(len(sortedLst) % 2):
        return(sortedLst[index])
    else:
        return((sortedLst[index] + sortedLst[index + 1]) / 2.0)

def findMean(n):
    mean = (sum(n)/len(n))
    return(mean)
    def findMin(n):
        tempMin = n[0]
    for i in n:
        if i < tempMin: # if smaller 
            tempMin = i

    return tempMin

def findMax(n):
    tempMax = n[0]
    for i in n:
        if i > tempMax:
            tempMax = i
    return tempMax

def findMin(n):
    tempMin = n[0]
    for i in n:
        if i < tempMin: # if smaller 
            tempMin = i

    return tempMin

def main():
    col_name = input("Enter a column to compute data for: ") 
    return col_name

