import sys
import pandas as pd
import numpy as np

def GetReynoldsNumber(v, d, nu):
	return v * d / nu

def GetType(Re):
	if Re < 2000:
		return 'Laminar'
	elif Re >= 2000 and Re <= 4000:
		return 'Transition'
	elif Re > 4000:
		return 'Turbulent'
	else:
		return 'Error'

v = np.random.uniform(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[6]))
d = np.random.uniform(float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[6]))
nu = float(sys.argv[5])
result = list()

for i in range(len(v)):
	Re = GetReynoldsNumber(v[i], d[i], nu)
	result.append(GetType(Re))

df = pd.DataFrame(np.transpose([v, d, result]), columns = ['v', 'd', 'result'])
df.to_csv(sys.argv[7])

print('Laminar:{0}, Transition:{1}, Turbulent:{2}, Error:{3}', result.count('Laminar'), result.count('Transition'), result.count('Turbulent'), result.count('Error'))
print('All done.')
