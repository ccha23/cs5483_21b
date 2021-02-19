# first line: 1
@memory.cache
def bagging(n_estimators, max_depth):
    BAG = ensemble.BaggingClassifier(
        base_estimator=tree.DecisionTreeClassifier(max_depth=max_depth),
        n_estimators=n_estimators,
        random_state=0)
    BAG.fit(X_train, Y_train)
    return BAG.score(X_test, Y_test)
