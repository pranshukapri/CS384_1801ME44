import csv
import os
import shutil
os.system('cls')

if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics"):
    os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics")
else:
    shutil.rmtree("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics")
    os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics")

def course():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course")
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
                    if not os.path.isfile('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv'):
                        with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv', 'a', newline='') as misc_file:
                            Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                            Writer_misc.writeheader()
                            Writer_misc.writerow(row)
                    else:
                        with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv', 'a', newline='') as misc_file:
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
                if not os.path.isfile('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv'):
                    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv', 'a', newline='') as misc_file:
                        Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer_misc.writeheader()
                        Writer_misc.writerow(row)
                else:
                    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Course/misc.csv', 'a', newline='') as misc_file:
                        Writer_misc = csv.DictWriter(misc_file, fieldnames=fieldnames, delimiter=',')
                        Writer_misc.writerow(row)
    pass


def country():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Country"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Country")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Country")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Country")
            
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
    pass


def email_domain_extract():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Email"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Email")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Email")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Email")
            
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
    pass


def gender():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Gender"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Gender")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Gender")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Gender")
            
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
    pass


def dob():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Dob"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Dob")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Dob")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Dob")
            
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
    pass


def state():
    # Read csv and process
    
    pass


def blood_group():
    # Read csv and process
    with open('g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/studentinfo_cs384.csv', 'r') as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=',')
        
        if not os.path.isdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Blood_Group"):
            os.mkdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Blood_Group")
        os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Blood_Group")
        
        for row in csv_read:
            os.chdir("g:/Study Materials/5th Sem/CS384/CS384_1801ME44/Assignment3/Analytics/Blood_Group")
            
            
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
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

course()
country()
email_domain_extract()
gender()
dob()
blood_group()