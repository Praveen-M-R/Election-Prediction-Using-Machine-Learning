import os
#os.chdir("C:/Users/prave/Desktop/Project/Code")
import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from collections import Counter
import matplotlib.pyplot as plt

# Define main page
def main_page():
    st.header("Analysing and Predicting Election Outcomes")
    st.markdown("""
    ### Introduction 
Elections serve as the cornerstone of democratic societies, shaping governance and reflecting the collective will of citizens. In the context of Kolar district, Karnataka, assembly elections are fiercely contested, with multiple political parties vying for supremacy. As data enthusiasts, our objective is to leverage machine learning techniques to predict which party is likely to emerge victorious in this electoral battleground.
### Problem Statement
Given historical election data, candidate profiles, and key issues, our task is to build predictive models that estimate the probability of each political party’s victory in Kolar district. By doing so, we aim to provide valuable insights for voters, analysts, and policymakers.
Key Challenges:
1.	Feature Selection: Choosing relevant features that significantly influence electoral outcomes.
2.	Model Selection: Identifying the most suitable machine learning algorithms for this task.
3.	Data Preprocessing: Cleaning, transforming, and preparing the dataset for modeling.

### Hypothesis
1.  Voters choose the congress party due to the guaranteed benefits provided by the congress government.
2.  The failure of the Modi government in controlling essential commodity(LPG gas, milk, mustard oil, petrol, diesel) will effect the voting behavior of low-income and middle-class households.
3.  Youth voters are inclined to support the BJP due to its positions on foreign policy decisions and international relations
4.  Female voters prefer the congress party due to its focus on women-centric schemes like shakti and Gruha Lakshm
5.  The Karnataka BJP’s decision to rejig the EWS(economically weaker section) quota and allocate part of it to Vokkaligas and Lingayats may impact voting preferences.
6.  poor and middle-class families like Gruha Jyoti and Gruha Lakshmi scheme and influence their voting decisions
7.  Hindu voters tend to vote for the BJP due to its stance on the construction of Ram Mandir in Ayodhya
8.  Congress partie attract Muslim voters due to concerns related to the hijab and the concept of a Hindu Rashtra
9.  Unemployment is a critical concern for the youth population and influence their voting decisions.
""")

def Guarantee():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    features_test=data_test[['Gruha lakshmi0','Gruha Lakshmi1','Shakthi0','Shakti1','Gruha jyothi0','Gruha jyothi1','Annabhagya0','Annabhagya1','Yuva nidhi0','Yuva nidhi1','Vote based on Guarantee1','Last Vote1']]
    target_test=data_test['Vote']
    # Load models from file
    with open('all_guarantee.pkl', 'rb') as file1, open('all_guarantee_tree.pkl', 'rb') as file2, open('all_guarantee_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### Voters choose the congress party due to the guaranteed benefits provided by the congress government.

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def essential_commodity():
    values=('Less than ₹20,000','₹20,000 - ₹99,999')
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test = data_test[data_test['Monthly Income'].isin(values)]
    features_test = data_test[['Monthly Income1','LPG/Milk1','Petrol/diesel1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('commodity_Ran.pkl', 'rb') as file1, open('commodity_tree.pkl', 'rb') as file2, open('commodity_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### The failure of the Modi government in controlling essential commodity(LPG gas, milk, mustard oil, petrol, diesel) will effect the voting behavior of low-income and middle-class households.

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def EWS():
   values=('Brahmin','Reddy+Vokkaliga+Gowda')
   data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
   data_test=data_test[data_test['Caste'].isin(values)]
   features_test = data_test[['Education1','Occupation1','EWS1','Last Vote1']]
   target_test = data_test['Vote']
    # Load models from file
   with open('ews_ran.pkl', 'rb') as file1, open('ews_tree.pkl', 'rb') as file2, open('ews_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
   st.markdown("""
    ### The Karnataka BJP’s decision to rejig the EWS(economically weaker section) quota and allocate part of it to Vokkaligas and Lingayats may impact voting preferences.

""")
     # Model selection list below the heading
   selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
   prediction = None

   if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
   elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
   elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
   result_counts = Counter(prediction)

    # Compute total count
   total_count = sum(result_counts.values())

    # Calculate percentages
   result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
   for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
   accuracy = accuracy_score(target_test, prediction)
   st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
   result_labels = list(result_percentages.keys())
   result_percentages = list(result_percentages.values())

    # Create the pie chart
   fig1, ax1 = plt.subplots()
   ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
   ax1.axis('equal')
   st.pyplot(fig1)

def Fe_Guarantee():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test=data_test[data_test['Gender']=="Female"]
    features_test=data_test[['Gruha lakshmi0','Gruha Lakshmi1','Shakthi0', 'Shakti1','Vote based on Guarantee1','Last Vote1']]
    target_test=data_test['Vote']
    # Load models from file
    with open('fe_gurantee_ran.pkl', 'rb') as file1, open('fe_gurantee_tree.pkl', 'rb') as file2, open('fe_gurantee_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### Female voters prefer the congress party due to its focus on women-centric schemes like shakti and Gruha Lakshm

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def Foreign():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test=data_test[(data_test['Age'] >= 18) & (data_test['Age'] <= 35)]
    features_test = data_test[['Age','Foreign Policy1','Education1','Occupation1','Narendra Modi1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('Foreign_ran.pkl', 'rb') as file1, open('Foreign_tree.pkl', 'rb') as file2, open('Foreign_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### Youth voters are inclined to support the BJP due to its positions on foreign policy decisions and international relations

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def MP_Guarantee():
    values=('Less than ₹20,000','₹20,000 - ₹99,999')
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test = data_test[data_test['Monthly Income'].isin(values)]
    features_test = data_test[['Monthly Income1','Gruha lakshmi0','Gruha Lakshmi1','Gruha jyothi0','Gruha jyothi1','Vote based on Guarantee1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('MP_Guarantee_ran.pkl', 'rb') as file1, open('MP_Guarantee_tree.pkl', 'rb') as file2, open('MP_Guarantee_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### poor and middle-class families like Gruha Jyoti and Gruha Lakshmi scheme and influence their voting decisions

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def Ram():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    features_test = data_test[['Hindu','Happy with Ram Mandir1','HINDU RASHTRA1','Vote based on Ram Mandir1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('Ram_Ran.pkl', 'rb') as file1, open('Ram_tree.pkl', 'rb') as file2, open('Ram_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### Hindu voters tend to vote for the BJP due to its stance on the construction of Ram Mandir in Ayodhya

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def Muslim():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test = data_test[data_test['Caste']=='Muslim']
    features_test = data_test[['HINDU RASHTRA1','Hijab1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('Muslim_Ran.pkl', 'rb') as file1, open('Muslim_tree.pkl', 'rb') as file2, open('Muslim_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### 	Congress partie attract Muslim voters due to concerns related to the hijab and the concept of a Hindu Rashtra

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

def Unemployment():
    data_test=pd.read_excel("EP_data.xlsx", sheet_name="Test_data1")
    data_test=data_test[(data_test['Age'] >= 18) & (data_test['Age'] <= 35)]
    features_test = data_test[['unemployment1','Occupation1','Monthly Income1','Last Vote1']]
    target_test = data_test['Vote']
    # Load models from file
    with open('Unemployment_ran.pkl', 'rb') as file1, open('Unemployment_tree.pkl', 'rb') as file2, open('Unemployment_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ### 	Unemployment is a critical concern for the youth population and influence their voting decisions.

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

# Define final page
def final_page():
    data_test=pd.read_excel("EP_data1.xlsx", sheet_name="Test_data")
    features_test=data_test[['Age','Gender1','Education1','Monthly Income1','Occupation1','Caste1','Caste in election1','Effect of tax on election1','Vote based on Guarantee1','Vote based on Ram Mandir1','Last Vote1']]
    target_test=data_test['Vote']
    # Load models from file
    with open('Final_Ran.pkl', 'rb') as file1, open('Final_tree.pkl', 'rb') as file2, open('Final_LR.pkl', 'rb') as file3:
        model1 = pickle.load(file1)
        model2 = pickle.load(file2)
        model3 = pickle.load(file3)
    st.markdown("""
    ## 	Final Result

""")
     # Model selection list below the heading
    selected_model = st.selectbox(
        'Choose a model for prediction',
        ['RandomForest', 'DecisionTree', 'Logistic Regression']
    )
    prediction = None

    if selected_model == 'RandomForest':
        prediction = model1.predict(features_test)
    elif selected_model == 'DecisionTree':
        prediction = model2.predict(features_test)
    elif selected_model == 'Logistic Regression':
        prediction = model3.predict(features_test)
        
        
   

    # Calculate counts
    result_counts = Counter(prediction)

    # Compute total count
    total_count = sum(result_counts.values())

    # Calculate percentages
    result_percentages = {result: (count / total_count) * 100 for result, count in result_counts.items()}
    # Display percentages
    for result, percentage in result_percentages.items():
            st.write(f"{result}: {percentage:.2f}%")
            
    accuracy = accuracy_score(target_test, prediction)
    st.write(f"--->Accuracy is {accuracy * 100}%.")
    # Assuming 'result_percentages' is a dictionary with result names as keys and percentages as values
    result_labels = list(result_percentages.keys())
    result_percentages = list(result_percentages.values())

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(result_percentages, labels=result_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)


# Sidebar navigation
st.sidebar.title("Hypothesis Analysis")
page = st.sidebar.radio("Go to", ["Introduction","Hypothesis 1","Hypothesis 2","Hypothesis 3" ,"Hypothesis 4","Hypothesis 5","Hypothesis 6","Hypothesis 7","Hypothesis 8","Hypothesis 9","Final Result"])

if page == "Introduction":
    main_page()
elif page=="Hypothesis 1":
    Guarantee()
elif page=="Hypothesis 2":
     essential_commodity()   
elif page=="Hypothesis 3":
     EWS()  
elif page=="Hypothesis 4":
     Fe_Guarantee() 
elif page=="Hypothesis 5":
     Foreign() 
elif page=="Hypothesis 6":
     MP_Guarantee()   
elif page=="Hypothesis 7":
     Ram() 
elif page=="Hypothesis 8":
     Muslim() 
elif page=="Hypothesis 9":
     Unemployment() 
else:
    final_page()
