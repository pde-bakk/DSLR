from pkgs.parsing import check_input
import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle


def print_result(y_test, y_pred):
	correct = 0
	for test, pred in zip(y_test, y_pred):
		if test == pred:
			correct += 1
	print(f'Got {correct}/{len(y_test)} correct!')


def save_weights(logreg):
	pickle.dump(logreg, open('datasets/weights', 'wb'))


def main():
	check_input(sys.argv)

	df = pd.read_csv(sys.argv[1], index_col=0)
	df.fillna(0, inplace=True)  # Fill all NaN's with 0's

	x = np.array(df.values[:, np.arange(7, 11)], dtype=float)  # Course score to train the model on
	y = df.values[:, 0]   # Hogwarts House

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=4)

	log_reg = LogisticRegression(max_iter=1000)
	log_reg.fit(x_train, y_train)

	y_pred = log_reg.predict(x_test)

	print_result(y_test, y_pred)
	save_weights(log_reg)


if __name__ == '__main__':
	main()