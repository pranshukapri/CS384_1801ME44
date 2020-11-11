import csv
import os
import shutil
os.system('cls')

if not os.path.isdir('./grades'):
    os.mkdir('./grades')
else:
    shutil.rmtree('./grades')
    os.mkdir('./grades')
pass

rollnumbers = []

with open('./acad_res_stud_grades.csv', 'r') as csv_file:
    csv_read = csv.DictReader(csv_file, delimiter=',')
    
    for row in csv_read:
        rollno = row["roll"]
        temp = {"Subject" : row["sub_code"], "Credits" : row["total_credits"], "Type" : row["sub_type"], "Grade" : row["credit_obtained"], "Sem" : row["sem"]}
        fieldnames = temp.keys()
        
        if row["credit_obtained"] == 'AA' or row["credit_obtained"] == 'AB' or row["credit_obtained"] == 'BB' or row["credit_obtained"] == 'BC' or row["credit_obtained"] == 'CC' or row["credit_obtained"] == 'CD' or row["credit_obtained"] == 'DD' or row["credit_obtained"] == 'F' or row["credit_obtained"] == 'I':
            if not os.path.isfile("./grades/" + rollno + "_individual.csv"):
                with open("./grades/" + rollno + "_individual.csv", 'a', newline='') as individual_csv:
                    Writer = csv.DictWriter(individual_csv, fieldnames=fieldnames, delimiter=',')
                    Writer.writeheader()
                    Writer.writerow(temp)
                    rollnumbers.append(rollno)
            else:
                with open("./grades/" + rollno + "_individual.csv", 'a', newline='') as individual_csv:
                    Writer = csv.DictWriter(individual_csv, fieldnames=fieldnames, delimiter=',')
                    Writer.writerow(temp)
        
        else:
            if not os.path.isfile("./grades/misc.csv"):
                with open("./grades/misc.csv", 'a', newline='') as misc_csv:
                    Writer = csv.DictWriter(misc_csv, fieldnames=row.keys(), delimiter=',')
                    Writer.writeheader()
                    Writer.writerow(row)
            else:
                with open("./grades/misc.csv", 'a', newline='') as misc_csv:
                    Writer = csv.DictWriter(misc_csv, fieldnames=row.keys(), delimiter=',')
                    Writer.writerow(row)
                
for i in range(len(rollnumbers)):
    with open("./grades/" + rollnumbers[i] + "_individual.csv",'r') as temp_csv_file:
        temp_csv_read = csv.DictReader(temp_csv_file, delimiter=',')
        
        max_sem = 0
        for temp in temp_csv_read:
            max_sem = max(max_sem, int(temp["Sem"]))
    
    with open("./grades/" + rollnumbers[i] + "_individual.csv",'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        list = []    
        for x in range(max_sem):
            list.insert(x,{"Semester" : x+1, "Semester Credits" : 0, "Semester Credits Cleared" : 0, "SPI" : 0, "Total Credits" : 0, "Total Credits Cleared" : 0, "CPI" : 0})
        
        for row in csv_read:
            sem = int(row["Sem"]) - 1
            list[sem]["Semester Credits"] = list[sem]["Semester Credits"] + int(row["Credits"])
            list[sem]["Semester Credits Cleared"] = list[sem]["Semester Credits Cleared"] + int(row["Credits"])
            
            if row["Grade"] == 'AA':
                list[sem]["SPI"] = list[sem]["SPI"] + 10*int(row["Credits"])
            elif row["Grade"] == 'AB':
                list[sem]["SPI"] = list[sem]["SPI"] + 9*int(row["Credits"])
            elif row["Grade"] == 'BB':
                list[sem]["SPI"] = list[sem]["SPI"] + 8*int(row["Credits"])
            elif row["Grade"] == 'BC':
                list[sem]["SPI"] = list[sem]["SPI"] + 7*int(row["Credits"])
            elif row["Grade"] == 'CC':
                list[sem]["SPI"] = list[sem]["SPI"] + 6*int(row["Credits"])
            elif row["Grade"] == 'CD':
                list[sem]["SPI"] = list[sem]["SPI"] + 5*int(row["Credits"])
            elif row["Grade"] == 'DD':
                list[sem]["SPI"] = list[sem]["SPI"] + 4*int(row["Credits"])
            elif row["Grade"] == 'I':
                list[sem]["Semester Credits Cleared"] = list[sem]["Semester Credits Cleared"] - int(row["Credits"])
                
        for j in range(max_sem):
            if list[j]["Semester Credits"] == 0:
                list[j]["SPI"] = 0
                list[j]["Total Credits"] = 0
                list[j]["Total Credits Cleared"] = 0
                list[j]["CPI"] = 0
            elif j == 0:
                list[j]["SPI"] = list[j]["SPI"] / list[j]["Semester Credits"]
                list[j]["Total Credits"] = list[j]["Semester Credits"]
                list[j]["Total Credits Cleared"] = list[j]["Semester Credits Cleared"]
                list[j]["CPI"] = list[j]["SPI"]
            else:
                list[j]["SPI"] = list[j]["SPI"] / list[j]["Semester Credits"]
                list[j]["Total Credits"] = list[j]["Semester Credits"] + list[j-1]["Total Credits"]
                list[j]["Total Credits Cleared"] = list[j]["Semester Credits Cleared"] + list[j-1]["Total Credits Cleared"]
                list[j]["CPI"] = (list[j]["SPI"]*list[j]["Semester Credits"] + list[j-1]["CPI"]*list[j-1]["Total Credits"]) / list[j]["Total Credits"]
                
        with open("./grades/" + rollnumbers[i] + "_overall.csv", 'a', newline='') as overall_csv:
            Writer = csv.DictWriter(overall_csv, fieldnames=list[0].keys(), delimiter=',')
            Writer.writeheader()
            for j in range(max_sem):
                Writer.writerow(list[j])