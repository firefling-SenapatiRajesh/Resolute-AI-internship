import streamlit as st
import pandas as pd
import plotly.express as px
import base64

#defining containers
header=st.container()
pie_chart=st.container()
bar_plot=st.container()

#Import Dataset
df=pd.read_csv('Dataset/Titanic-Dataset.csv',header=0)

with header:
	st.title('Exploring Titanic Dataset')
	st.text('In this projects,I have created a simple view of Embarked titanic passengers')
	st.subheader('1) First 10 Entries of dataset')
	st.markdown('<hr>',unsafe_allow_html=True)
	#creating a button to select the show dataset
	if st.button('Show dataset'):
		st.write(df.head(10))


with pie_chart:
	st.header('Pie chart for Embarked')
	st.markdown("<hr>",unsafe_allow_html=True)
	options=st.multiselect('select features to analyze the data',
		['Ticket class(1st/2nd/3rd)','Sex','No.of Siblings','No.of parents'],default=['Ticket class(1st/2nd/3rd)','Sex'])
	features=[({'Ticket class(1st/2nd/3rd)':'Pclass','Sex':'Sex','No.of Siblings':'SibSp','No.of Parents':'Parch'}).get(x,x) for x in options]
	features.append('Survival')
	features.insert(0,'Source')
	st.write('You have selected:',options)
	df['Survival']=df['Survived'].map({0:'Not survived',1:'Survived'})
	df['Embarked']=df['Embarked'].fillna('N')
	df['Source']=df['Embarked'].map({'S':'Southampton','C': 'Cherbourg','Q': 'Queenstown','N': 'No Record'})
	st.write('Click on slices to explore more through chart')
	fig=px.sunburst(df,path=features)
	fig.update_layout(width=500,height=500)
	st.plotly_chart(fig)






with bar_plot:
	st.header('Bar plot for Sex')
	st.markdown("<hr>",unsafe_allow_html=True)
	df_s = df['Sex'].value_counts().reset_index()
	df_s.columns = ['Gender','Counts']
	df_s['Percentage(%)'] = df_s['Counts']/df_s['Counts'].sum(axis=0) *100
	df_s['Percentage(%)'] = df_s['Percentage(%)'].round(2)
	df_s['Percentage(%)'] = df_s['Percentage(%)'].astype(str)+' %'


	x_axis = df_s['Gender']
	y_axis = df_s['Counts']
	
	fig1 = px.bar(df_s, x=x_axis, y=y_axis, labels={'y':'Counts'},hover_name=df_s['Percentage(%)'])

	st.plotly_chart(fig1)




