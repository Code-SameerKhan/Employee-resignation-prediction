# Employee resignation prediction
# Summary

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

![Demo](employeeresignation/data/employee_demo.webm)
