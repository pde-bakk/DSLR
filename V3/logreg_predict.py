import pandas as pd
import numpy as np
import sys
import os
import pickle

if len(sys.argv) != 3 or 'dataset_test.csv' not in sys.argv[1]:
	print('It takes as a parameter dataset_test.csv and a file containing the weights trained by previous program.')
	quit()

filename, extension = os.path.splitext(sys.argv[1])
if extension != '.csv' or not os.path.exists(sys.argv[1]):
	print(f'Please provide a valid .csv file.')
	quit()

df = pd.read_csv(sys.argv[1], index_col=0)

df.fillna(method='ffill', inplace=True)
X = np.array(df.values[:, np.arange(7, 11)], dtype=float)  # Hogwarts course score to predict Hogwarts house
y = df.values[:, 0]  # Hogwarts House

LogReg = pickle.load(open('datasets/weights', 'rb'))

y_pred = LogReg.predict(X)

with open('datasets/houses.csv', 'w+') as f:
	f.write('Index,Hogwarts House\n')
	for i in range(len(y_pred)):
		f.write(f'{i}, {y_pred[i]}\n')