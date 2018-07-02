import sys
import json
import pandas as pd
# $1: Input data file name, $2: Input settings .json file name

with open(sys.argv[2]) as f:
	settings = json.load(f)
data = pd.read_csv(sys.argv[1])

result = pd.cut(data[settings['target_column']], settings['bins'], labels = settings['group_names'])
data[settings['target_column'] + '_discrete'] = result
data.to_csv(sys.argv[1].split('.')[0] + '_discrete.' + sys.argv[1].split('.')[1], index = False, float_format = '%g')
