import sys
import json
import pandas as pd
# $1: Input data file name, $2: settings .json file name, $3: Output data file name

with open(sys.argv[2]) as f:
	settings = json.load(f)
data = pd.read_csv(sys.argv[1])

result = pd.cut(data[settings['target_column']], settings['bins'], labels = settings['group_names'])
#print(result)
data[settings['target_column'] + '_discrete'] = result
data.to_csv(sys.argv[3], index = False, float_format = '%g')
