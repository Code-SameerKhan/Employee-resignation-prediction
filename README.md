# Employee resignation prediction
# Summary

![](visuals/dist_feature.png)

* Created a tool that predicts when an employee is going to resign in order to help perfect employee management and improve working space environment.
* Based on the public release data available on Kaggle, the features are employed.
* Engineered features to calculate dependencies of the target variable on the independent variables.
* Optimized Logistic, Random Forest, Decision Tree and Naive Bayes classifier using GridSearchCV to reach best model.
* Achieved an accuracy of 90.62% in correctly predicting the outcome.

Getting to understand employees is a major task in any successful organization. Various factors combine enough to create a snowball effect in the minds of employee on whether he/she sees the future of oneself in their current working environment.

Some of the major factors include Salary, Satisfaction level, promotion, average working hours, etc… By correlating the different features we can arrive on a decision based on the prediction. Since the output here is whether the employee leaves or not therefore it is termed as a classification problem.

![](visuals/feature-impact.png)

A classification model attempts to draw some conclusion from observed values. Given one or more inputs a classification model will try to predict the value of one or more outcomes.

![](visuals/dynamic-relationship.png)

Popular algorithms that can be used for binary classification include:

1. Logistic Regression
2. k-Nearest Neighbors
3. Decision Trees
4. Support Vector Machine
5. Naive Bayes

By employing the GridSearchCV on the above classifying algorithms we conclude-

Decision Tree classifier to be optimum with 90.62% accuracy

![Demo](visuals/employee-demo.gif)

# Built with
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="30" src="https://matplotlib.org/_static/logo2.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>
