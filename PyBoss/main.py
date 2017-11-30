import pandas as pd

df1 = pd.read_csv("employee_data1.csv")
df2 = pd.read_csv("employee_data2.csv")

frame = [df1, df2]

employees_info = pd.concat(frame)

names = employees_info['Name'].str.split(' ', expand=True)

employees_info['First Name'] = names[0]
employees_info['Last Name'] = names[1]

del employees_info['Name']

employees_info['DOB'] = pd.to_datetime(employees_info.DOB)

employees_info['DOB'] = employees_info['DOB'].dt.strftime("%m/%d/%Y")

employees_info['SSN'] = "***-**-" + employees_info['SSN'].str[7:11]

state_abbreviated = {
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

state_abbreviated = [state_abbreviated[i] for i in employees_info['State']]

state_abbreviated = pd.Series(state_abbreviated)

employees_info['State'] = state_abbreviated

reorder = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

employees_info = employees_info.reindex(columns = reorder)

employees_info.to_csv("PyBossOutput.csv", index = False, header = True)