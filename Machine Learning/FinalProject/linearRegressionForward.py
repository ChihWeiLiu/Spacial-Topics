import sys
import json
import math
import numpy as np
import pandas as pd
from sklearn import linear_model, cross_validation, metrics
from sklearn.utils import shuffle
# $1: Input train data file name, $2: Input test data file name, $3: Input settings .json file name

train = pd.read_csv(sys.argv[1])
#train = shuffle(train)
test = pd.read_csv(sys.argv[2])
with open(sys.argv[3]) as f:
	settings = json.load(f)

train_attributes = list()
test_attributes = list()
for attribute in settings['attributes']:
	train_attributes.append(train[attribute])
	test_attributes.append(test[attribute])
train_x = pd.DataFrame(train_attributes).T
train_y = train[settings['class']]
test_x = pd.DataFrame(test_attributes).T
test_y = test[settings['class']][1]

'''regr.fit(train_x, train_y)
predict_y = regr.predict(test_x)
print('Test root mean square error: ', math.sqrt(metrics.mean_squared_error(test_y, predict_y)))

result = pd.DataFrame({settings['class'] + '_predict' : predict_y})
(pd.concat([test, result], axis = 1)).to_csv(sys.argv[2].split('/input/')[0] + '/output/LR_' + sys.argv[3].split('/input/')[1].split('.')[0] + '.csv', index = False, float_format = '%g')'''
