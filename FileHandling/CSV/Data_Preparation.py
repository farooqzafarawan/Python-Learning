import re
import csv
import os

def format_phone(phoneNum):
    phone = re.sub(r'\D', '', phoneNum)   # strip non-numeric characters
    phone = phone.lstrip('1')             # remove leading 1 (area codes never start with 1)

    return f'({phone[0:3]}) {phone[3:6]} {phone[6:]}'

def spaces_two(namestr):
    twospaces = '  '
    finalStr = twospaces + namestr

    return finalStr

def remove_Chars(inputstr):
    cleanString = re.sub('[^A-Za-z0-9\s]+','', inputstr )
    
    return cleanString


dirpath = r'C:\CODE'
# Existing csv file containing data
csvfile = os.path.join(dirpath,'cust_5.csv')

# csv file for writing new records
csvwritef = os.path.join(dirpath,'newfile.csv') 

with open(csvwritef, mode='w') as csvwrite, open(csvfile) as csvf:
    writer = csv.writer(csvwrite)

    linecount = 0
    for row in csvf: 
        rec = list(row.split(','))
        fname = rec[3]
        lname = rec[4]
        email = rec[5]
        phone = rec[6]

        cleanPhone = format_phone(phone)
        cleanFName = spaces_two(fname)
        cleanLName  = remove_Chars(lname)
        print(cleanPhone,cleanFName,cleanLName)
        
        #writer.writerow([rec[2], rec[3]])
