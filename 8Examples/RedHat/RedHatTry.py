import pandas as pd
import numpy as np
from sklearn.cross_validation import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def leaveOneOut(data1, data2, columnName, useLOO=False):
    grpOutcomes = data1.groupby(columnName).mean().reset_index()
    outcomes = data2['outcome'].values
    x = pd.merge(data2[[columnName, 'outcome']], grpOutcomes,
                 suffixes=('x_', ''),
                 how='left',
                 on=columnName,
                 left_index=True)['outcome']
    if(useLOO):
        x = ((x*x.shape[0])-outcomes)/(x.shape[0]-1)
    return x.fillna(x.mean())

def preprocessing(act_train_data, act_test_data, people_data):
    # Join people data set with activity data sets
    print "Joining data sets..."
    train_data = act_train_data.merge(people_data, on="people_id", how="left")
    test_data = act_test_data.merge(people_data, on="people_id", how="left")

    # Prepare data
    print "Preparing data..."
    # Fill NA
    train_data.fillna("-999", inplace=True)
    test_data.fillna("-999", inplace=True)

    # Extract new features from dates
    train_data["dif_date"] = train_data.date_x - train_data.date_y
    test_data["dif_date"] = test_data.date_x - test_data.date_y

    train_data["year"] = train_data.date_x.apply(lambda x: x.year)
    test_data["year"] = test_data.date_x.apply(lambda x: x.year)

    train_data["month"] = train_data.date_x.apply(lambda x: x.month)
    test_data["month"] = test_data.date_x.apply(lambda x: x.month)

    # Scale data
    train_pred = pd.DataFrame()
    for col in train_data:
        if (col != "activity_id" and col != "outcome" and col != "people_id"):
            train_pred[col] = LeaveOneOut(train_data, train_data, col, True).values

    test_data["outcome"] = 0

    test_pred = pd.DataFrame()
    for col in train_data.columns:
        if (col != "outcome" and col != "activity_id" and col != "people_id"):
            test_pred[col] = LeaveOneOut(train_data, test_data, col, False).values

    train_pred.to_csv("train_pred.csv")
    test_pred.to_csv("test_pred.csv")

def featureImportance(alg, predictors):
    importances = alg.feature_importances_
    indices = np.argsort(importances)[::-1]

    print("Feature importances:")
    for f, idx in enumerate(indices):
        print("{:2d}. feature '{:5s}' ({:.4f})".format(f + 1, predictors[idx], importances[idx]))

def main():
    # Load data
    print "Loading data..."
    path = "D:/DataScience0/Kaggle/PredictingRedHatBusinessValue/"
    train_data = pd.read_csv(path + "act_train.csv", parse_dates=["date"])
    test_data = pd.read_csv(path + "act_test.csv", parse_dates=["date"])

    train_pred = pd.read_csv(path + "train_pred.csv")
    test_pred = pd.read_csv(path + "test_pred.csv")

    activity_id = test_data.activity_id.values

    # Select features
    selector = SelectKBest(f_classif, k=5)
    selector.fit(train_pred, train_data.outcome)
    predictors = list()
    sup = list(selector.get_support())
    for i in xrange(0, len(train_pred.columns.values)):
        if sup[i]:
            predictors.append(train_pred.columns.values[i])

    #predictors = ['date_x', 'activity_category', 'char_1_y', 'group_1',
    #              'char_2_y', 'date_y', 'char_3_y', 'char_4_y', 'char_5_y',
    #              'char_6_y', 'char_7_y', 'char_8_y', 'char_9_y', 'char_10_y',
    #              'char_11', 'char_12', 'char_13', 'char_14', 'char_15', 'char_16',
    #              'char_17', 'char_18', 'char_19', 'char_20', 'char_21', 'char_22',
    #              'char_23', 'char_24', 'char_25', 'char_26', 'char_27', 'char_28',
    #              'char_29', 'char_30', 'char_31', 'char_32', 'char_33', 'char_34',
    #              'char_35', 'char_36', 'char_37', 'char_38', 'dif_date']

    # Cross validation
    cv = StratifiedKFold(train_data.outcome, n_folds=5, shuffle=True, random_state=1)

    # Select model
    print "Training model..."

    # Logistic regression
    #alg_log = LogisticRegression(C=100000.0)
    #scores = cross_val_score(alg_log, train_pred[predictors], train_data.outcome, cv=cv, n_jobs=-1)
    #print("Accuracy (logistic regression): {}/{}".format(scores.mean(), scores.std()))

    # Random forest classifier
    alg_frst_model = RandomForestClassifier(n_jobs=-1, max_features="sqrt")
    alg_frst_params = [{
        "n_estimators": [350, 400, 450],
        "min_samples_split": [6, 8, 10],
        "min_samples_leaf": [1, 2, 4]
    }]
    alg_frst_grid = GridSearchCV(alg_frst_model, alg_frst_params, cv=cv, refit=True, verbose=1, n_jobs=-1)
    alg_frst_grid.fit(train_pred[predictors], train_data.outcome)
    alg_frst_best = alg_frst_grid.best_estimator_
    print("Accuracy (random forest auto): {} with params {}"
          .format(alg_frst_grid.best_score_, alg_frst_grid.best_params_))

    # Submission
    print "Creating a submission file..."
    alg_test = alg_frst_best
    predictions = alg_frst_best.predict_proba(test_pred[predictors])
    submission = pd.DataFrame({
        "activity_id": activity_id,
        "outcome": predictions
    })
    submission.to_csv("NewTry.csv", index=False, float_format='%.3f')

if __name__ == '__main__':
    print "Started"
    main()
    print "Finished!"

