import string
import re
import codecs
import csv
import time
import datetime
# all global variable
nameFile = "sample-data-test - Email Collection Report.csv"
numberOfOlder = 0
numberOfPeopleInHCM = 0
hcmarray = ['hcm','ho chi minh']
hnarray  = ['hn','ha noi']
# bo dau tieng viet
INTAB = u"ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"

r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))
listOfrecruitedPerson = []
listOfrecruitedPersonWeekend = []
def khongdau(utf8_str):
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
# check int of a string
def isInt(value):
    try:
        int(value)
        return True
    except:
        return False
# check date at weekend and from 6PM to 10PM
def checkinweekendAndrange18to22(dateString):
    dateString = dateString.strip()
    try:
        date = datetime.datetime.strptime(dateString, '%Y-%m-%d %H:%M')
        if date.isoweekday() == 6 or date.isoweekday() == 7:
            second = date.hour * 3600 + date.minute * 60 + date.second
            if second >= 64800 and second <= 79200:
                return True
    except:
        return False
    return False

with open(nameFile, newline = '', encoding = 'utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        if isInt(row[2]) and int(row[2]) > 32:
        	numberOfOlder = numberOfOlder + 1
        u = row[3].lower()
        u = khongdau(u)
        if (hcmarray[0] in u) or (hcmarray[1] in u):
            numberOfPeopleInHCM = numberOfPeopleInHCM + 1
            if isInt(row[2]) and (int(row[2]) < 20) and (row[1] == 'Female'):
                listOfrecruitedPerson.append(row)
            if checkinweekendAndrange18to22(row[0]):
                listOfrecruitedPersonWeekend.append(row)
        elif (hnarray[0] in u) or (hnarray[1] in u):
            if checkinweekendAndrange18to22(row[0]):
                listOfrecruitedPersonWeekend.append(row)
print('****** number of people who are older than Mark *******')
print(numberOfOlder)
print('****** number of people living at HCM *******')
print(numberOfPeopleInHCM)
print('****** The list of people who live in Ho Chi Minh City, age less than 20 and gender is “Female” *****')
print(len(listOfrecruitedPerson))
for element in listOfrecruitedPerson:
    print(element)
print('****** The list of people who recruited on weekend from 6 PM to 10 PM, live in Ho Chi Minh City or Ha Noi City *******')
print(len(listOfrecruitedPersonWeekend))
for element in listOfrecruitedPersonWeekend:
    print(element)