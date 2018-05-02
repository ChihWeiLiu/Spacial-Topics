import sys
import pandas as pd
# $1: Input data 1 file name, $2: Input data 2 file name, $3: Merging target column name, $4 Output data file name

data_1 = pd.read_csv(sys.argv[1])
data_2 = pd.read_csv(sys.argv[2])
result = pd.merge(data_1, data_2, on = sys.argv[3])
result.to_csv(sys.argv[4], index = False, float_format = '%g')
