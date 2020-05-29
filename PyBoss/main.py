import os
import csv
import re
import datetime

emp_id= []
name= []
dob= []
SSN = []
state= []
header =["EMP ID", "First Name", "Last Name", "DOB", "SSN", "State"]

#opening the file
#Remember to fix the csv path later
#csvpath= os.path.join('Resources','budget_data.csv')
csvpath= (r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBoss\employee_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for rows in csvreader:
        emp_id.append(rows[0] )
        name.append(rows[1] )
        #convert Date of Birth string into DateTime format
        dob.append(datetime.datetime.strptime((rows[2]), '%Y-%m-%d') )
        SSN.append(rows[3] )
        state.append(rows[4] )

#USA abbreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#1 DOB format change
dob1=[]
for x in range(len(dob)):
    #convert DateTime DOB into desired date format
    dob1.append(dob[x].strftime("%Y-%m-%d") )


#2 SSN
SSN_censored=[]
for x in range(len(dob)):
    SSN_censored.append("***-**-"+ (SSN[x][7:]))

#3. Format States
state_translated=[]
for x in state:
    state_translated.append(us_state_abbrev[x])


#4 Splitting Up Name
name2=[]
First_name=[]
Last_name=[]
#splitting from full name
for x in range(len(name)):
    name2.append( name[x].split(" ") )

#assigning to First and Last name
for y in range(len(name2)):
    First_name.append(name2[y][0])
    Last_name.append( name2[y][-1] )


#5 zipping all up
zip_boss=zip(emp_id,First_name , Last_name, dob1,SSN_censored,state_translated)


#6 #print out to csv
csv_output=(r"C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBoss\analysis.csv")
#csv_output=os.path.join("..","analysis","analysis.csv")
with open(csv_output,'w',newline='') as csv_writer:
    csv_writer = csv.writer(csv_writer)
    csv_writer.writerow(["EMP ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    csv_writer.writerows(zip_boss)
    