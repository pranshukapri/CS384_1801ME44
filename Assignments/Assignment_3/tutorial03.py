### IMP: All the files and folders are created in the working directory of the file and not where the .py file is saved!!

import csv
import os
import shutil
os.system('cls')

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if not os.path.isdir('./Analytics'):
        os.mkdir('./Analytics')
    else:
        shutil.rmtree('./Analytics')
        os.mkdir('./Analytics')
    pass

def course():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Course"):
            os.mkdir("./Analytics/Course")
        os.chdir("./Analytics/Course")
        
        for row in csv_read:
            os.chdir(cwd + "/Analytics/Course")
            if row["id"][0].isdigit() and row["id"][1].isdigit() and row["id"][2].isdigit() and row["id"][3].isdigit() and row["id"][4].isalpha() and row["id"][5].isalpha() and row["id"][6].isdigit() and row["id"][7].isdigit():
                
                course = row["id"][4] + row["id"][5]
                temp = row["id"][2] + row["id"][3]
                
                if temp == '01':
                    degree = 'Btech'
                elif temp == '11':
                    degree = 'Mtech'
                elif temp == '12':
                    degree = 'MSc'
                elif temp == '21':
                    degree = 'Phd'
                else:
                    fieldnames = row.keys()
                    if not os.path.isfile('./misc.csv'):
                        with open('./misc.csv', 'a', newline='') as misc_file:
                            Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                            Writer_misc.writeheader()
                            Writer_misc.writerow(row)
                    else:
                        with open('./misc.csv', 'a', newline='') as misc_file:
                            Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                            Writer_misc.writerow(row)
                        
                if not os.path.isdir("./" + course):
                    os.mkdir("./" + course)
                os.chdir("./" + course)
                
                if not os.path.isdir("./" + degree):
                    os.mkdir("./" + degree)
                os.chdir("./" + degree)         
                
                fieldnames = row.keys()
                if not os.path.isfile('./' + row["id"][0] + row["id"][1] + '_' + course + '_' + degree + '.csv'):
                    with open('./' + row["id"][0] + row["id"][1] + '_' + course + '_' + degree + '.csv', 'a', newline='') as misc_file:
                        Writer = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer.writeheader()
                        Writer.writerow(row)
                else:
                    with open('./' + row["id"][0] + row["id"][1] + '_' + course + '_' + degree + '.csv', 'a', newline='') as misc_file:
                        Writer = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer.writerow(row)
                
            else:
                fieldnames = row.keys()
                if not os.path.isfile('./misc.csv'):
                    with open('./misc.csv', 'a', newline='') as misc_file:
                        Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer_misc.writeheader()
                        Writer_misc.writerow(row)
                else:
                    with open('./misc.csv', 'a', newline='') as misc_file:
                        Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def country():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Country"):
            os.mkdir("./Analytics/Country")
        os.chdir("./Analytics/Country")
        
        for row in csv_read:
            
            country = row["country"]
            
            fieldnames = row.keys()
            if not os.path.isfile('./' + country + '.csv'):
                with open('./' + country + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + country + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def email_domain_extract():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Email"):
            os.mkdir("./Analytics/Email")
        os.chdir("./Analytics/Email")
        
        for row in csv_read:
            
            temp = row["email"]
            domain = ''
            flag = 0
            
            for i in temp:
                if i == '@':
                    flag = 1
                    continue
                if i == '.':
                    break
                if flag == 1:
                    domain = domain + i
            
            fieldnames = row.keys()
            if not os.path.isfile('./' + domain + '.csv'):
                with open('./' + domain + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + domain + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def gender():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Gender"):
            os.mkdir("./Analytics/Gender")
        os.chdir("./Analytics/Gender")
        
        for row in csv_read:
            
            gender = row["gender"]
            
            fieldnames = row.keys()
            if not os.path.isfile('./' + gender + '.csv'):
                with open('./' + gender + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + gender + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def dob():
    # Read csv and process
    cwd = os.getcwd()
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Dob"):
            os.mkdir("./Analytics/Dob")
        os.chdir("./Analytics/Dob")
        
        for row in csv_read:
            
            temp = row["dob"][6] + row["dob"][7] + row["dob"][8] + row["dob"][9]
            
            if temp>='1995' and temp<='1999':
                dob = 'bday_1995_1999'
            elif temp<='2004':
                dob = 'bday_2000_2004'
            elif temp<='2009':
                dob = 'bday_2005_2009'
            elif temp<='2014':
                dob = 'bday_2010_2014'
            elif temp<='2019':
                dob = 'bday_2015_2020'
            else:
                dob = 'misc'
            
            fieldnames = row.keys()
            if not os.path.isfile('./' + dob + '.csv'):
                with open('./' + dob + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + dob + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def state():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/State"):
            os.mkdir("./Analytics/State")
        os.chdir("./Analytics/State")
        
        for row in csv_read:
            
            state = row["state"]
            
            fieldnames = row.keys()
            if not os.path.isfile('./' + state + '.csv'):
                with open('./' + state + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + state + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


def blood_group():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("./Analytics/Blood_Group"):
            os.mkdir("./Analytics/Blood_Group")
        os.chdir("./Analytics/Blood_Group")
        
        for row in csv_read:            
            
            if row["blood_group"] == 'a+' or row["blood_group"] == 'A+':
                blood_group = 'A+'
            elif row["blood_group"] == 'a-' or row["blood_group"] == 'A-':
                blood_group = 'A-'
            elif row["blood_group"] == 'b+' or row["blood_group"] == 'B+':
                blood_group = 'B+'
            elif row["blood_group"] == 'b-' or row["blood_group"] == 'B-':
                blood_group = 'B-'
            elif row["blood_group"] == 'o+' or row["blood_group"] == 'O+':
                blood_group = 'O+'
            elif row["blood_group"] == 'o-' or row["blood_group"] == 'O-':
                blood_group = 'O-'
            elif row["blood_group"] == 'ab+' or row["blood_group"] == 'AB+' or row["blood_group"] == 'Ab+' or row["blood_group"] == 'aB+':
                blood_group = 'AB+'
            elif row["blood_group"] == 'ab-' or row["blood_group"] == 'AB-' or row["blood_group"] == 'Ab-' or row["blood_group"] == 'aB-':
                blood_group = 'AB-'
            else:
                blood_group = 'misc'
                
            fieldnames = row.keys()
            if not os.path.isfile('./' + blood_group + '.csv'):
                with open('./' + blood_group + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row)
            else:
                with open('./' + blood_group + '.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row)
    os.chdir(cwd)
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    cwd = os.getcwd()
    os.chdir(cwd)
    with open('./studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        for row in csv_read:
            
            full_name = row["full_name"]
            first_name = ''
            last_name = ''
            
            flag = 0
            for i in full_name:
                if i == ' ':
                    flag = 1
                    continue
                if flag == 0:
                    first_name = first_name + i
                else:
                    last_name = last_name + i
                    
                row2 = {"id": row["id"], "first_name": first_name, "last_name": last_name, "country": row["country"], "email": row["email"], "gender": row["gender"], "dob": row["dob"], "blood_group": row["blood_group"], "state": row["state"]}
            
            fieldnames = row2.keys()
            if not os.path.isfile('./Analytics/studentinfo_cs384_names_split.csv'):
                with open('./Analytics/studentinfo_cs384_names_split.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(row2)
            else:
                with open('./Analytics/studentinfo_cs384_names_split.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(row2)
                    
    with open('./Analytics/studentinfo_cs384_names_split.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        temp = list(csv_read)
        
        length = len(temp)
        
        for i in range(length):
            for j in range(length-1):
                    if temp[j+1]["first_name"] < temp[j]["first_name"]:
                        temp[j], temp[j+1] = temp[j+1], temp[j]
        
        for rows in temp:
            fieldnames = rows.keys()
            if not os.path.isfile('./Analytics/studentinfo_cs384_names_split_sorted_first_name.csv'):
                with open('./Analytics/studentinfo_cs384_names_split_sorted_first_name.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writeheader()
                    Writer_misc.writerow(rows)
            else:
                with open('./Analytics/studentinfo_cs384_names_split_sorted_first_name.csv', 'a', newline='') as misc_file:
                    Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                    Writer_misc.writerow(rows)
                             
    os.chdir(cwd)
    pass
