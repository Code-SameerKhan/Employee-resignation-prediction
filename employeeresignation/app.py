import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler


st.write("""
# Employee Resignation Prediction Application

This app predicts whether an **Employee** will **Resign** or **not**.
""")

st.sidebar.header('User Input Features')

# Function to make a dataframe out of user input features


def user_input_features():
    satisfaction_level = st.sidebar.slider('Satisfaction Level', 1, 10, 5)
    last_evaluation = st.sidebar.slider('Last Evaluation Score', 1, 10, 5)
    number_project = st.sidebar.slider('Number of Projects', 1, 10, 5)
    average_montly_hours = st.sidebar.slider('Average Monthly Hours', 90,
                                             320, 170)
    time_spend_company = st.sidebar.slider('Time at the company (in yrs)',
                                           2, 10, 4)
    Work_accident = st.sidebar.slider(
        'Work Related Accident (0 for No, 1 for Yes)', 0, 1, 0)
    promotion_last_5years = st.sidebar.slider(
        'Promotion in Last 5 Years(0 for No, 1 for Yes)', 0, 1, 1)
    Department = st.sidebar.selectbox('Department of Working',
                                      ('IT', 'RandD', 'accounting', 'hr',
                                       'management', 'marketing',
                                       'product_mng', 'sales', 'support',
                                       'technical'))
    salary = st.sidebar.selectbox('Salary Range',
                                  ('high', 'medium', 'low'))
    data = {'satisfaction_level': satisfaction_level/10,
            'last_evaluation': last_evaluation/10,
            'number_project': number_project,
            'average_montly_hours': average_montly_hours,
            'time_spend_company': time_spend_company,
            'Work_accident': Work_accident,
            'promotion_last_5years': promotion_last_5years,
            'Department': Department,
            'salary': salary}
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()

emp_raw = pd.read_csv('./data/hrdata.csv')
emp = emp_raw.drop(columns=['left'])
df = pd.concat([input_df, emp], axis=0)

new_df = pd.get_dummies(df, prefix=None, drop_first=True)

scale = StandardScaler()
scale_df = scale.fit_transform(new_df)

user_df = new_df[:1]  # The user input data, concatenated row wise


st.subheader('User Input Features')

st.write(df.head(1))

# Loading the model
load_clf = pickle.load(open('employee_resignation_prediction.pickle', 'rb'))

# Applying model for prediction
prediction = load_clf.predict(scale_df)
# prediction_probs = load_clf.prediction_proba(df)

st.subheader('**PREDICTION**')
if prediction[0] == 1:
    st.write('*Employee will resign*')
else:

    st.write('*Employee will not resign*')

# Feature importance from random forest model in jupyter notebook
y = [0.3250634787813269,
     0.2476071601447333,
     0.14868223221435112,
     0.14181207451276234,
     0.10831226255263442]

x = ['Satisfaction Level', 'No. of Projects', 'Time Spent in Company',
     'Avg Monthly Salary', 'Last Evaluation']
dataframe = pd.DataFrame(y, index=x)

agree = st.button('''Click here to see the features
influencing the most in this WebApp!''')
if agree:
    st.bar_chart(dataframe, width=400, height=400)
