#!/usr/bin/python
#########################################################
# A simple Birthday reminder script that mails reminders.
#########################################################
"""
cat > CALENDAR.txt
Description,Event Type,Date,Month,Year
Simba & Dimba,wedding aniversary,3,January,
clarence smith,Birthday,4,January,
rajesh nayak,Birthday,11,January,
ram's dinner party,Feast,25,January,
Republic day, national holiday, 26, January, 1947
"""
# to execute, use:
# 
import csv
import sys
import datetime
import commands
mailto = "trohit+date@gmail.com"

# temporary file to be mailed 
body_file = "body.txt"
def get_today_date():
        mydate = datetime.datetime.now()
        mmdd = mydate.strftime("%d%B").lstrip("0").replace(" 0", " ")
        #print str(mmdd)
        return mmdd

f = open(sys.argv[1],'rb')
reader = csv.reader(f)
for row in reader:
        print row
        rawlist = [desc, evtype, dd,mm,yyyy] = row[0], row[1], row[-3], row[-2], row[-1]
        # strip any leading spaces from all elms of the list
        rawlist = map(str.lstrip, rawlist)
        [desc, evtype, dd,mm,yyyy] = rawlist
        print("this:" + str(rawlist))

        #print( str(dd) + ":" + str(mm) + ":" + str(yyyy))
        today = dd + mm;
        today_date = get_today_date()
        today = str(today).lower()
        today_date = str(today_date).lower()
        print("Comparing " + str(today_date) + " with " + str(today))

        if today.lower() == today_date.lower():
                print ("yes, it matches")
                print(today)
                print("Description:" + str(desc))
                print("Event Type:" + str(evtype))
                print("On:" + str(dd) + str(mm) + str(yyyy))
                body = str(desc) + " " + str(evtype) +  "On:" + str(dd) + str(mm) + str(yyyy)

                # write the body to a file
                f = open(body_file, 'w')
                f.write(body)  # python will convert \n to os.linesep
                f.close()  # you can omit in most cases as the destructor will call it

                cmd = "./sendgmail " + mailto + " '" + desc + "' '" + body_file + "'"
                print(cmd)
                res = commands.getstatusoutput(cmd)
                print(res)
                print ("-----")
