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
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

course()
country()
email_domain_extract()