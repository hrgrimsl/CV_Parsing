from sys import argv
import re
import numpy as np

script, first, second = argv

din = open(first, 'r')
dout = open(second, 'w')

seg_arrs = []
ready_list = []

for line in din.readlines():
    line = line.replace(':', '')
    line = line.replace('\n', '')
    if re.search("Segment", line) and line.split()[1] in ready_list:
        seg_arrs.append([])
    elif re.search("Segment", line):
        ready_list.append(line.split()[1])
    elif "Segment" not in line and len(line.split())!=0 and "Potential/V" not in line:
        seg_arrs[-1].append([line.split()[0], line.split()[1]])

maxi = 0
for segment in seg_arrs:
    if len(segment)>maxi:
        maxi = len(segment)

for row in range(0, maxi):
    for col in range(0, len(seg_arrs)):
        try:
            dout.write(seg_arrs[col][row][0]+' '+seg_arrs[col][row][1]+' ')
        except:
            pass
    dout.write('\n')







