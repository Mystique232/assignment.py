
import numpy as np

file = open("Loan_prediction_dataset.csv", "r")

data = np.genfromtxt(file, delimiter=",", skip_header=1, dtype=str, encoding="utf-8")

file.close()

loan_amounts = np.array([float(x) if x else np.nan for x in data[:, 8]])

mean = np.nanmean(loan_amounts)
median = np.nanmedian(loan_amounts)
std = np.nanstd(loan_amounts)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
