import pandas as pd
from sklearn import cross_validation, metrics
from sklearn.neural_network import MLPClassifier

model = [2,4,6,8,9,12,(2,2),(3,3),(4,4),(6,6),(8,8),(9,9),(12,12),(2,2,2),(3,3,3),(4,4,4),(6,6,6),(8,8,8),(9,9,9),(12,12,12)]

train = pd.read_csv('train_10000.csv', index_col = 0)
train_x = pd.DataFrame([train['v'], train['d']]).T
train_y = train['result']

test = pd.read_csv('test_1000.csv', index_col = 0)
test_x = pd.DataFrame([test['v'], test['d']]).T
test_y = test['result']

#train_x, test_x, train_y, test_y = cross_validation.train_test_split(data_set_x, data_set_y, test_size = 20)

for i in range(len(model)):
	clf = MLPClassifier(hidden_layer_sizes = model[i], random_state = 1)
	clf.fit(train_x, train_y)
	print('Model:', model[i], 'Accuracy:', metrics.accuracy_score(test_y, clf.predict(test_x)))
