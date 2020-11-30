import csv
import math
import os
import shutil

if not os.path.isdir('./Groups'):
    os.mkdir('./Groups')
else:
    shutil.rmtree('./Groups')
    os.mkdir('./Groups')
pass

def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    data = {}
    total_stud = 0
    left = []
    list_sorted = []
    stats = []
    
    with open("./" + filename, 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        branch_code = []
        
        for row in csv_read:
            temp = row['Roll'][4] + row['Roll'][5]
            flag = 0
            for code in branch_code:
                if temp == code:
                    flag = 1
                    break
            if flag == 0:
                branch_code.append(temp)
                list_temp = []
                list_temp.append(row)
                data[temp] = list_temp
            else:
                list_temp = data[code]
                list_temp.append(row)
                data[temp] = list_temp
    
    with open("./Groups/Branch_Strength.csv", 'w', newline='') as branch_strength:
        Writer = csv.DictWriter(branch_strength, fieldnames=["Branch_Code", "Strength"], delimiter=',')
        Writer.writeheader()
                    
        list_temp = []
        for branch in data.keys():
            dict_temp = {"Branch_Code" : branch, "Strength" : len(data[branch])}
            list_temp.append(dict_temp)
            total_stud = total_stud + len(data[branch])
        list_sorted = sorted(list_sorted, key=lambda i: i["Branch_Code"])
        list_sorted = sorted(list_temp, key=lambda i: i["Strength"], reverse=True)
        
        for i in list_sorted:
            Writer.writerow(i)
    
    for branch_code in data.keys():
        with open("./Groups/" + branch_code + ".csv", 'w', newline='') as indi_branch:
            Writer = csv.DictWriter(indi_branch, fieldnames=data[branch_code][0].keys(), delimiter=',')
            Writer.writeheader()
            data[branch_code] = sorted(data[branch_code], key=lambda i: i["Roll"])
            Writer.writerows(data[branch_code])
    
    for i in range(number_of_groups):
        I = i + 1
        if I<10:
            I = '0' + str(I)
        else:
            I = str(I)
        with open("./Groups/Group_G" + I + ".csv", 'w', newline='') as groups:
            Writer = csv.DictWriter(groups, fieldnames=data[branch_code][0].keys(), delimiter=',')
            Writer.writeheader()
            for k in list_sorted:
                num = int(k["Strength"] / number_of_groups)
                for j in range(num):
                    Writer.writerow(data[k["Branch_Code"]][0])
                    del data[k["Branch_Code"]][0]
    
    for k in list_sorted:
        for i in data[k["Branch_Code"]]:
            left.append(i)
        
    for i in range(len(left)):
        I = i%number_of_groups + 1
        if I<10:
            I = '0' + str(I)
        with open("./Groups/Group_G" + str(I) + ".csv", 'a', newline='') as group:
            Writer = csv.DictWriter(group, fieldnames=left[i].keys(), delimiter=',')
            Writer.writerow(left[i])

    for i in range(number_of_groups):
        I = i + 1
        if I<10:
            I = '0' + str(I)
        dict_temp = {}
        with open("./Groups/Group_G" + str(I) + ".csv", 'r') as group:
            csv_read = csv.DictReader(group, delimiter=',')
            dict_temp = {"Group" : "Group_G" + str(I) + ".csv", "Total" : 0}
            for row in csv_read:
                dict_temp["Total"] = dict_temp["Total"] + 1
                branch_code = row['Roll'][4] + row['Roll'][5]
                if branch_code in dict_temp.keys():
                    dict_temp[branch_code] = dict_temp[branch_code] + 1
                else:
                    dict_temp[branch_code] = 1
                    
        stats.append(dict_temp)
    
    with open("./Groups/Stats_Grouping.csv", 'w', newline='') as stats_group:
        Writer = csv.DictWriter(stats_group, fieldnames=stats[0].keys(), delimiter=',')
        Writer.writeheader()
        Writer.writerows(stats)

filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)