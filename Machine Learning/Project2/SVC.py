import sys
import json
import numpy as np
import pandas as pd
from sklearn import cross_validation, metrics
from sklearn.svm import SVC
# $1: Input train data file name, $2: Input test data file name, $3: settings .json file name, $4: Output data file name

train = pd.read_csv(sys.argv[1])
test = pd.read_csv(sys.argv[2])
with open(sys.argv[3]) as f:
	settings = json.load(f)

attributes = list()
for attribute in settings['attributes']:
	#print(attribute)
	attributes.append(train[attribute])
#print(attributes)
train_x = pd.DataFrame(attributes).T
train_y = train[settings['class']]

attributes = list()
for attribute in settings['attributes']:
	attributes.append(test[attribute])
test_x = pd.DataFrame(attributes).T
test_y = test[settings['class']]

train_vx, test_vx, train_vy, test_vy = cross_validation.train_test_split(train_x, train_y, test_size = 0.5)
#print(train_x)

clf = SVC(kernel = 'rbf', C = 1.0, gamma = 0.7)
clf.fit(train_vx, train_vy)
predict_vy = clf.predict(test_vx)
print('Validation accuracy: ', metrics.accuracy_score(test_vy, predict_vy))
print(metrics.classification_report(test_vy, predict_vy))

clf.fit(train_x, train_y)
predict_y = clf.predict(test_x)
print('Test mean square error: ', metrics.mean_squared_error(test_y, predict_y))

result = pd.DataFrame({settings['class'] + '_predict' : predict_y})
(pd.concat([test, result], axis = 1)).to_csv(sys.argv[4], index = False, float_format = '%g')
