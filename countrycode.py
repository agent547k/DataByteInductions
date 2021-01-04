import csv
# Opening File
handle = open('data_csv.csv', mode='r')
dic = dict()
for word in handle:
    # Going over each row, split based on ','
    row = word.strip().split(',')
    # add key val pair to dict
    dic[row[1]] = row[0]
# Checks can be included here, c1 and c2 store the country names
c1 = dic[input("Code 1 - ")]
c2 = dic[input("Code 2 - ")]

# c1 is lower limit and c2 is upper limit
if c2 < c1:
    temp = c2
    c2 = c1
    c1 = temp
# iterate over values and check if in range and then print
for val in dic.values():
    if val > c1 and val < c2:
        print(val)
