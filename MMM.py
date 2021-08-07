import csv
from collections import Counter

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
newData = []
for i in range (len(data)):
    Weight=data[i][2]
    newData.append(float(Weight))
length = len(newData)
newData.sort()

sum = 0
for i in newData:
    sum += i
mean = sum/len(newData)

if length%2==0:
    median1 = newData[length//2]
    median2 = newData[length//2-1]
    median = (median1+median2)/2
else:
    median = newData[length//2]

frequency = Counter(newData)
range = {
    "75-85":0, "85-95":0, '95-105':0, '105-115':0,'115-125':0,'125-135':0,'135-145':0,'145-155':0,'155-165':0,'165-175':0}
for Weight,occurance in frequency.items():
    if (Weight<85 and Weight>75):
        range["75-85"] += occurance
    elif (Weight<95 and Weight>85):
        range["85-95"] += occurance
    elif (Weight<105 and Weight>95):
        range["95-105"] += occurance
    elif (Weight<115 and Weight>105):
        range["105-115"] += occurance
    elif (Weight<125 and Weight>115):
        range["115-125"] += occurance
    elif (Weight<135 and Weight>125):
        range["125-135"] += occurance
    elif (Weight<145 and Weight>135):
        range["135-145"] += occurance
    elif (Weight<155 and Weight>145):
        range["145-155"] += occurance
    elif (Weight<165 and Weight>155):
        range["155-165"] += occurance
    elif (Weight<175 and Weight>165):
        range["165-175"] += occurance
modeRange = 0
modeOccurance = 0
for r,occurance in range.items():
    if(occurance>modeOccurance):
        modeRange,modeOccurance = [int(r.split("-")[0]),int(r.split("-")[1])],occurance
mode = (modeRange[0]+modeRange[1])/2

print(mode)
print(median)
print(mean)