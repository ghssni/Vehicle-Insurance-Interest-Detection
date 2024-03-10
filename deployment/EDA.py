import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ps
from PIL import Image

def run():
# Membuat Title
    st.title('Vehicle Insurance Interest Prediction')

    # Membuat Subheader
    st.subheader('Exploratory Data Analysis')

    # Menambahkan deskripsi
    st.write("This dataset belongs to an insurance company aiming to predict customer interest in purchasing vehicle insurance, alongside existing health insurance coverage")
    st.write('Created by Sani - Data Scientist')

    # Membuat garis lurus
    st.markdown('---')

    # Data Load
    df=pd.read_csv('clean_data.csv')

    # Tampilkan dataframe
    st.dataframe(df)
    # Membuat garis lurus
    st.markdown('---')

    # Load the code
    target = df['response'].value_counts().to_frame(name='count')
    target['percentage'] = df['response'].value_counts(normalize=True)
    target.reset_index(inplace=True)

    # Visualization
    st.write('## Customers Classification')
    fig = plt.figure(figsize=(14, 4))

    # Pie Chart
    plt.subplot(1,2,1)
    plt.title('Customers Classification')
    explode = [0,0.2]
    labels = ['Not Interested','Interested']
    plt.pie(target["percentage"], labels=labels,explode=explode, autopct='%.0f%%')

    # Barplot
    plt.subplot(1,2,2)
    plt.title('Customers Classification')
    ax = sns.countplot(data=df, x='response', hue='response')
    labels = ['Not Interested','Interested']
    for i in ax.containers:
        ax.bar_label(i,)
    ax.set_xticklabels(labels)
    st.pyplot(fig)
    st.write('The response column, which is the target column, has data on customers who are interested 12%\ of the total data with a total of 46710 customers. Customers who are not interested have a percentage of 88%\ of the total data with a total of 334399 customers. This shows that our dataset has an imbalance target data because it has a target data ratio of 1:7')
    st.markdown('---')

    # Visualisasi
    st.write('## Annual Premi Customers Insurance')
    fig = plt.figure(figsize=(10, 4))
    ax = sns.barplot(data=df,x='response', y='annual_premium', hue='response')
    plt.xlabel('response')
    plt.ylabel('annual_premium')
    labels = ['Not Interested','Interested']
    for i in ax.containers:
        ax.bar_label(i,)
    ax.set_xticklabels(labels)
    plt.title('Customers Interest by Annual Premi')
    st.pyplot(fig)
    st.write('It turns out that customers who are interested in insurance have an annual_balance value of 2630 - 540165. The range of annual premium values for customers who are interested and those who are not interested in insurance is the same. But we can see, the difference lies in the average value. Customers who are interested in insurance have a lower average annual premium at 30419.')
    st.markdown('---')

    # Count column vehicle_age
    veh_age = df['vehicle_age'].value_counts().to_frame(name='count')
    veh_age['percentage'] = df['vehicle_age'].value_counts(normalize=True)
    veh_age.reset_index(inplace=True)
    veh_age
    # Visualisasi
    st.write('## Customers Vehicle Age')
    fig = plt.figure(figsize=(10, 4))
    # Visualization
    plt.subplot(1,2,1)
    plt.title('Vehicle Age Customers Insurance')
    plt.pie(veh_age["percentage"], labels=veh_age['index'], autopct='%.01f%%')

    # Barplot
    plt.subplot(1,2,2)
    plt.title('Customers Interested by Vehicle Age')
    ax = sns.countplot(data=df, x='vehicle_age', hue='response')
    for i in ax.containers:
        ax.bar_label(i,)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.write('We can see from the data displayed, the most customers are dominated by 1-2 year old vehicles with a percentage of `52.6%` and customers who are interested in our insurance also have the most vehicles with 1-2 year old vehicles with a total of 34,806 people.')
    st.markdown('---')

    # Count column age_cat
    age_cat = df['age_cat'].value_counts().to_frame(name='count')
    age_cat['percentage'] = df['age_cat'].value_counts(normalize=True)
    age_cat.reset_index(inplace=True)
    age_cat

    # Visualisasi
    st.write('## Customers Age')
    fig = plt.figure(figsize=(10, 4))
    # Visualization
    plt.subplot(1,2,1)
    plt.title('Age Category Customers Insurance')
    plt.pie(age_cat["percentage"], labels=age_cat['index'], autopct='%.01f%%')

    # Barplot
    plt.subplot(1,2,2)
    plt.title('Customers Interested by Age Category')
    ax = sns.countplot(data=df, x='age_cat', hue='response')
    for i in ax.containers:
        ax.bar_label(i,)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.write('If we look at the overall data, our customers are dominated by the adult age category (26-44 years old) with a percentage of 35.3%. If we connect it with the target column, then customers who are interested in our vehicle insurance are also dominated by the adult age category with a total of 21615 people.')
    st.markdown('---')

    # Visualisasi
    st.write('## Customers Vehicle Damage ')
    fig = plt.figure(figsize=(10, 4))
    # Count column vehicle_damage
    vehic_dmg = df['vehicle_damage'].value_counts().to_frame(name='count')
    vehic_dmg['percentage'] = df['vehicle_damage'].value_counts(normalize=True)
    vehic_dmg.reset_index(inplace=True)
    
    # Visualization
    plt.subplot(1,2,1)
    plt.title('Vehicle Damage Customer Insurance')
    labels = ["Yes",'No']
    plt.pie(vehic_dmg["percentage"], labels = labels, autopct='%.01f%%')

    # Barplot
    plt.subplot(1,2,2)
    plt.title('Interest Customers by Vehicle Damage')
    ax = sns.countplot(data=df, x='vehicle_damage', hue='response')
    for i in ax.containers:
        ax.bar_label(i,)
    labels = ["Yes",'No']
    ax.set_xticklabels(labels)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.write('It can be seen that customers are dominated by customers who have vehicles that have been damaged with a percentage of `50.5%`. When viewed from the customer interest, it is also dominated by customers who have vehicles that have been damaged.')
    st.markdown('---')

    st.write('## Conslusion')
    st.write('### Conclusion from Exploratory Data Analysis')
    st.write('The data in the target column or dependent column is not balanced with a percentage split of `88%` and `12%`.')
    st.write('Customers who are interested in insurance have a lower average annual premium with a value of 30419.')
    st.write('Customers who are interested in our insurance are on average 43 years old with an age range of adult (26-44 years).')
    st.write('Customers who are interested in our insurance also have the most vehicles with a vehicle age of 1-2 years.')
    st.write('### Bussiness Insight:')
    st.write('The response column in the Health Insurance Cross-Sell Prediction dataset can be used to get various business insights that can help companies to improve their cross-selling strategy.')
    st.write('- Customers who are interested in vehicle insurance')
    st.write('We can do targeting so that our insurance sales are not misdirected.')
    st.write('- Customers who are not interested in vehicle insurance')
    st.write('We can influence them without making them feel disturbed by the marketing that is being done so that it will increase the chance of customers interest in vehicle insurance.')


if __name__ == '__main__':
  run()