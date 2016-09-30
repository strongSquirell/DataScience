
import pandas as pd
import numpy as np
import xgboost as xgb
import re
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

class DataDigest:

    def __init__(self):
        self.ages = None
        self.fares = None
        self.titles = None
        self.cabins = None
        self.families = None
        self.tickets = None

def get_title(name):
    if pd.isnull(name):
        return "Null"

    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1).lower()
    else:
        return "None"


def get_family(row):
    last_name = row["Name"].split(",")[0]
    if last_name:
        family_size = 1 + row["Parch"] + row["SibSp"]
        if family_size > 3:
            return "{0}_{1}".format(last_name.lower(), family_size)
        else:
            return "nofamily"
    else:
        return "unknown"

# Validation function
def errFun(act, pred):
    s = 0
    for i in xrange(len(act)):
      if act[i] == pred[i]:
          s +=1;
    return float(s)/len(act)

# Data Exploration
def dataExpl(data):

    # Statistical description of the data
    data.describe()

    sns.barplot(x='Sex', y='Survived', data=data)
    age_df = data[['Age','Survived', 'Sex']].copy()
    age_df.loc[age_df.Age<15,'AgeGroup'] = 'Children'
    age_df.loc[age_df.Age>=15,'AgeGroup'] = 'Adult'
    sns.barplot(x='AgeGroup', y='Survived', hue='Sex', data=age_df)
    sns.swarmplot(x='Age',y='Sex',hue='Survived',data=data)

def get_index(item, index):
    if pd.isnull(item):
        return -1
    try:
        return index.get_loc(item)
    except KeyError:
        return -1

# Data Preparation
def dataPrep(data, digest):

    # Age - replace NA to median regarding Gender
    data["AgeF"] = data.apply(lambda r: digest.ages[r["Sex"]] if pd.isnull(r["Age"]) else r["Age"], axis=1)

    # Fare - replace NA to median regarding Class
    data["FareF"] = data.apply(lambda r: digest.fares[r["Pclass"]] if pd.isnull(r["Fare"]) else r["Fare"], axis=1)

    # female = 0, Male = 1
    data['Gender'] = data['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
    # or genders = {'male': 1, 'female': 0}
    #data['Gender'] = data['Sex'].apply(lambda s: genders.get(s))

    # Gender - extending
    gender_dummies = pd.get_dummies(data["Sex"], prefix="SexD", dummy_na=False)
    data = pd.concat([data, gender_dummies], axis=1)

    # Embarkment - replacement
    embarkments = {"U": 0, "S": 1, "C": 2, "Q": 3}
    data["EmbarkedF"] = data["Embarked"].fillna("U").apply(lambda e: embarkments.get(e))

    # Embarkment - extending
    embarkment_dummies = pd.get_dummies(data["Embarked"], prefix="EmbarkedD", dummy_na=False)
    data = pd.concat([data, embarkment_dummies], axis=1)

    # Number of relatives on board
    data["RelativesF"] = data["Parch"] + data["SibSp"]

    # Single persom
    data["SingleF"] = data["RelativesF"].apply(lambda r: 1 if r == 0 else 0)

    # Deck - replacement
    decks = {"U": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "T": 8}
    data["DeckF"] = data["Cabin"].fillna("U").apply(lambda c: decks.get(c[0], -1))

    # Deck - extending
    deck_dummies = pd.get_dummies(data["Cabin"].fillna("U").apply(lambda c: c[0]), prefix="DeckD", dummy_na=False)
    data = pd.concat([data, deck_dummies], axis=1)

    # Titles - extending
    title_dummies = pd.get_dummies(data["Name"].apply(lambda n: get_title(n)), prefix="TitleD", dummy_na=False)
    data = pd.concat([data, title_dummies], axis=1)

    # Replacement from Data Digest
    data["CabinF"] = data["Cabin"].fillna("unknown").apply(lambda c: get_index(c, digest.cabins))
    data["TitleF"] = data["Name"].apply(lambda n: get_index(get_title(n), digest.titles))
    data["TicketF"] = data["Ticket"].apply(lambda t: get_index(t, digest.tickets))
    data["FamilyF"] = data.apply(lambda r: get_index(get_family(r), digest.families), axis=1)

    age_bins = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90]
    data["AgeR"] = pd.cut(data["Age"].fillna(-1), bins=age_bins).astype(object)

    return data

def main():
    # Load data
<<<<<<< HEAD
    train_data = pd.read_csv('../input/train.csv', header=0)
    test_data = pd.read_csv('../input/test.csv', header=0)
=======
    train_data = pd.read_csv('D:/DataScience0/titanic/RawData/input/train.csv', header=0)
    test_data = pd.read_csv('D:/DataScience0/titanic/RawData/input/test.csv', header=0)
>>>>>>> a57fd894ad474cbd981cb9a46e8ca6b4372c75a9
    all_data = pd.concat([train_data, test_data]).reset_index(drop=True)

    # First exploration
    print(train_data.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True))

    # Compare test and train sets
    describe_fields = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
    print(train_data[train_data["Sex"] == "male"][describe_fields].describe())
    print(test_data[test_data["Sex"] == "male"][describe_fields].describe())
    print(train_data[train_data["Sex"] == "female"][describe_fields].describe())
    print(test_data[test_data["Sex"] == "female"][describe_fields].describe())

    # Create Data Digest
    data_digest = DataDigest()
    data_digest.ages = all_data.groupby("Sex")["Age"].median()
    data_digest.fares = all_data.groupby("Pclass")["Fare"].median()
    data_digest.titles = pd.Index(test_data["Name"].apply(get_title).unique())
    data_digest.families = pd.Index(test_data.apply(get_family, axis=1).unique())
    data_digest.cabins = pd.Index(test_data["Cabin"].fillna("unknown").unique())
    data_digest.tickets = pd.Index(test_data["Ticket"].fillna("unknown").unique())

    # Prepare data for analysis
    train_data_prep = dataPrep(train_data, data_digest)
    test_data_prep = dataPrep(test_data, data_digest)
    all_data_prep = pd.concat([train_data_prep, test_data_prep])

    # Choose predictors
    predictors = ["Pclass",
                  "AgeF",
                  "TitleF",
                  "TitleD_mr", "TitleD_mrs", "TitleD_miss", "TitleD_master", "TitleD_ms",
                  "TitleD_col", "TitleD_rev", "TitleD_dr",
                  "CabinF",
                  "DeckF",
                  "DeckD_U", "DeckD_A", "DeckD_B", "DeckD_C", "DeckD_D", "DeckD_E", "DeckD_F", "DeckD_G",
                  "FamilyF",
                  "TicketF",
                  "SexF",
                  "SexD_male", "SexD_female",
                  "EmbarkedF",
                  "EmbarkedD_S", "EmbarkedD_C", "EmbarkedD_Q",
                  "FareF",
                  "SibSp", "Parch",
                  "RelativesF",
                  "SingleF"]

    selector = SelectKBest(f_classif, k=5)
    selector.fit(train_data_prep[predictors], train_data_prep["Survived"])

    # Scale predictors
    scaler = StandardScaler()
    scaler.fit(all_data_prep[predictors])

    train_data_scaled = scaler.transform(train_data_prep[predictors])
    test_data_scaled = scaler.transform(test_data_prep[predictors])

    # Plot
    sns.pairplot(train_data_prep, vars=["AgeF", "Pclass", "SexF"], hue="Survived", dropna=True)
    sns.plt.show()

    # Cross validation
    cv = StratifiedKFold(train_data["Survived"], n_folds=3, shuffle=True, random_state=1)

    # Modeling
    # k-neighbours classifier
    alg_ngbh = KNeighborsClassifier(n_neighbors=3)
    scores = cross_val_score(alg_ngbh, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1)
    print("Accuracy (k-neighbors): {}/{}".format(scores.mean(), scores.std()))

    # SGD classifier
    alg_sgd = SGDClassifier(random_state=1)
    scores = cross_val_score(alg_sgd, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1)
    print("Accuracy (sgd): {}/{}".format(scores.mean(), scores.std()))

    # SVC
    alg_svm = SVC(C=1.0)
    scores = cross_val_score(alg_svm, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1)
    print("Accuracy (svm): {}/{}".format(scores.mean(), scores.std()))

    # Caussian NB
    alg_nbs = GaussianNB()
    scores = cross_val_score(alg_nbs, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1)
    print("Accuracy (naive bayes): {}/{}".format(scores.mean(), scores.std()))

   # Linear regression
    def linear_scorer(estimator, x, y):
        scorer_predictions = estimator.predict(x)

        scorer_predictions[scorer_predictions > 0.5] = 1
        scorer_predictions[scorer_predictions <= 0.5] = 0

        return metrics.accuracy_score(y, scorer_predictions)

    alg_lnr = LinearRegression()
    scores = cross_val_score(alg_lnr, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1,
                             scoring=linear_scorer)
    print("Accuracy (linear regression): {}/{}".format(scores.mean(), scores.std()))

    # Logistic regression
    alg_log = LogisticRegression(random_state=1)
    scores = cross_val_score(alg_log, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1,
                             scoring=linear_scorer)
    print("Accuracy (logistic regression): {}/{}".format(scores.mean(), scores.std()))

    # Random forest classifier
    alg_frst = RandomForestClassifier(random_state=1, n_estimators=500, min_samples_split=8, min_samples_leaf=2)
    scores = cross_val_score(alg_frst, train_data_scaled, train_data_prep["Survived"], cv=cv, n_jobs=-1)
    print("Accuracy (random forest): {}/{}".format(scores.mean(), scores.std()))

    # Improved random forest
    alg_frst_model = RandomForestClassifier(random_state=1)
    alg_frst_params = [{
        "n_estimators": [350, 400, 450],
        "min_samples_split": [6, 8, 10],
        "min_samples_leaf": [1, 2, 4]
    }]
    alg_frst_grid = GridSearchCV(alg_frst_model, alg_frst_params, cv=cv, refit=True, verbose=1, n_jobs=-1)
    alg_frst_grid.fit(train_data_scaled, train_data_prep["Survived"])
    alg_frst_best = alg_frst_grid.best_estimator_
    print("Accuracy (random forest auto): {} with params {}"
          .format(alg_frst_grid.best_score_, alg_frst_grid.best_params_))

    # xgboost
    ald_xgb_model = xgb.XGBClassifier()
    ald_xgb_params = [
        {"n_estimators": [230, 250, 270],
         "max_depth": [1, 2, 4],
         "learning_rate": [0.01, 0.02, 0.05]}
    ]
    alg_xgb_grid = GridSearchCV(ald_xgb_model, ald_xgb_params, cv=cv, refit=True, verbose=1, n_jobs=1)
    alg_xgb_grid.fit(train_data_scaled, train_data_prep["Survived"])
    alg_xgb_best = alg_xgb_grid.best_estimator_
    print("Accuracy (xgboost auto): {} with params {}"
          .format(alg_xgb_grid.best_score_, alg_xgb_grid.best_params_))

    # Prediction
    alg_test = alg_frst_best
    alg_test.fit(train_data_scaled, train_data_prep["Survived"])
    predictions = alg_test.predict(test_data_scaled)
    submission = pd.DataFrame({
        "PassengerId": test_data["PassengerId"],
        "Survived": predictions
    })
    submission.to_csv("titanic-submission.csv", index=False)

if __name__ == "__main__":
    main()