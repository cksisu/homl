"""
Code for chapter 2 exercises 
"""
import pandas as pd
import sklearn as skl

from utils.paths import Paths

paths = Paths()

# 1) Try a Support Vector Machine regressor (sklearn.svm.SVR), with various
#    hyperparameters such as kernel="linear" (with various values for the C
#    hyperparameter) or kernel="rbf" (with various values for the C and gamma
#    hyperparameters). Don’t worry about what these hyperparameters mean for now.
#    How does the best SVR predictor perform?

housing = pd.read_csv(paths.data.joinpath("housing", "housing.csv"))
housing.head().T
