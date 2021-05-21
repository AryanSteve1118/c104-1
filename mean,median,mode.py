import csv
from collections import Counter

def mean(new_data):

    n = len(new_data)
    total =0
    for x in new_data:
        total += float(x)

    mean = total / n
    print("Mean / Average is: " + str(mean))
def median(new_data):

    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2 - 1])
        median = (median1 + median2)/2
    else:
        median = float(new_data[n//2])
    print("Median is: " + str(median))
def mode(new_data):
    
    data  = Counter(new_data)

    mode_data_for_range = {
        "110-120":0,
        "120-130":0,
        "130-140":0,
        "140-150":0
    }
    for weight, occurence in data.items():
        if 110 < float(weight) < 120:
            mode_data_for_range["110-120"] += occurence
        elif 120 < float(weight) < 130:
            mode_data_for_range["120-130"] += occurence
        elif 130 < float(weight) < 140:
            mode_data_for_range["130-140"] += occurence
        elif 140 < float(weight) < 150:
            mode_data_for_range["140-150"] += occurence


        # if 75 < float(weight) < 85:
        #     mode_data_for_range["75-85"] += occurence
        # elif 85 < float(weight) < 95:
        #     mode_data_for_range["85-95"] += occurence
        # elif 95 < float(weight) < 105:
        #     mode_data_for_range["95-105"] += occurence
        # elif 105 < float(weight) < 115:
        #     mode_data_for_range["105-115"] += occurence
        # elif 115 < float(weight) < 125:
        #     mode_data_for_range["115-125"] += occurence
        # elif 125 < float(weight) < 135:
        #     mode_data_for_range["125-135"] += occurence
        # elif 135 < float(weight) < 145:
        #     mode_data_for_range["135-145"] += occurence
        # elif 145 < float(weight) < 155:
        #     mode_data_for_range["145-155"] += occurence
        # elif 155 < float(weight) < 165:
        #     mode_data_for_range["155-165"] += occurence
        # elif 165 < float(weight) < 175:
        #     mode_data_for_range["165-175"] += occurence

    mode_range,mode_occurence = 0,0
    for range,occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")

def litten():
    with open('data.csv',newline='') as h:
        reader = csv.reader(h)
        file_data = list(reader)
    
    file_data.pop(0) 

    new_data=[]
    
    for i in range(len(file_data)):
        n_num = file_data[i][2]
        new_data.append(n_num)

    mean(new_data)
    median(new_data)
    mode(new_data)

litten()

