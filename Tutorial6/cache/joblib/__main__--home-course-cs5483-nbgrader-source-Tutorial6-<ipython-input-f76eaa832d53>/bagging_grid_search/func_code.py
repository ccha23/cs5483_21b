# first line: 1
@memory.cache
def bagging_grid_search():
    param_grid=[{'n_estimators': n_estimators_list}]
    
    grid_search = GridSearchCV(
        ensemble.BaggingClassifier(
            base_estimator=tree.DecisionTreeClassifier(max_depth=10),
            random_state=0), 
        param_grid, verbose=1, n_jobs=4)

    grid_search.fit(X_train, Y_train)
    return grid_search.score(X_test, Y_test)
