import sys
import pandas as pd
# $1: Complete data file name, $2: Missing data file name, $3: Missing column name in missing data (align column is default to first column), $4 Output data file name

data_1 = pd.read_csv(sys.argv[1])
data_2 = pd.read_csv(sys.argv[2])

pointer = 0;
value = 0;


for i in range(0, len(completeData)):
	#print(missingData.iloc[pointer, 0])
	if completeData.iloc[i, 0] == missingData.iloc[pointer, 0]:
		#print(missingData[sys.argv[3]][pointer])
		value = missingData[sys.argv[3]][pointer]
		pointer += 1;
	newColumn.append(value)

completeData[sys.argv[3]] = newColumn;
#print(completeData)

completeData.to_csv(sys.argv[4], index = False)


import sys
from datetime import datetime
import numpy as np
import pandas as pd
# $1: Complete data file name, $2: Missing data file name, $3: Missing column name in missing data (align column is default to first column), $4 Output data file name

data_1 = pd.read_csv(sys.argv[1])
data_2 = pd.read_csv(sys.argv[2])
pointer_1 = 0;
pointer_2 = 0;
timestampFormat = '%Y/%m/%d %H:%M'
columnNames = np.array(sys.argv[3])
for e in data_1.columns.values:
	if e != sys.argv[3]:
		columnNames = np.append(columnNames, e)
for e in data_2.columns.values:
	if e != sys.argv[3]:
		columnNames = np.append(columnNames, e)
#print(columnNames)

print(pd.merge(data_1, data_2, on=sys.argv[3]))
'''
result = pd.DataFrame(columns = columnNames)
result = result.append(pd.DataFrame([1,2,3,4], columns = columnNames))
print(result)

while timestamp_1 and timestamp_2:
	timestamp_1 = datetime.strptime(data_1[sys.argv[3]][pointer_1], timestampFormat)
	timestamp_2 = datetime.strptime(data_2[sys.argv[3]][pointer_2], timestampFormat)
	if timestamp_1 > timestamp_2:
		pointer_2 += 1
	elif timestamp_1 < timestamp_2:
		pointer_1 += 1
	else:
		timestamp_1.strftime(timestampFormat)

completeData[sys.argv[3]] = newColumn;
completeData.to_csv(sys.argv[4], index = False)
'''
