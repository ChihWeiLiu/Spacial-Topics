import sys
import pandas as pd
# $1: Input file name, $2: Shifted column name, $3: Numder of shifted rows

data = pd.read_csv(sys.argv[1])
for i in range(0, int(sys.argv[3])):
	data[sys.argv[2] + '_shifted_' + str(i + 1)] = data[sys.argv[2]].shift(i + 1, axis = 0)
data.dropna().to_csv(sys.argv[1].split('.')[0] + '_shifted.' + sys.argv[1].split('.')[1], index = False, float_format = '%g')
