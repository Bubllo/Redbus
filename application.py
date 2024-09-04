import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np

database =  mysql.connector.connect(
    host="localhost",
    user ="root",
    password = "Bubllo@0299"
)

if database.is_connected():
    print("connected")
else:
    print("NA")

cursor = database.cursor()

cursor.execute("USE project1")

cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)

st.markdown("""<style>
            .stApp{
                background-color: #f9d7c4;
            }
            </style>""",unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("Selenium/project/download.png")
with col2:
    st.markdown("""
         <h1 style='color :#ff5733'>REDBUS</h1>
    """,unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("""
            <h4 style="text-align:center; color:#ff5733"><i>The one stop shop for all your bus needs</i></h4>
            """,unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)

tab1,tab2,tab3,tab4 = st.tabs(["Bus Search","Filtering","Bus aggregators","About us"])

with tab1:
    start= st.text_input("Boarding point")
    stop = st.text_input("Deboarding point")
    submit = st.button("submit")
    if submit and start == "bangalore" and stop == "hyderabad":
        st.success("Bus Available!!!")
        cursor.execute("Select * from bus_data")
        a= cursor.fetchall()
        #creating column name
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df = pd.DataFrame(a,columns=col_name)
        st.write(df)
    elif submit and start != "bangalore" and stop != "hyderabad":
        st.markdown("""<p style="font-size: 50px">
                            😢
                        </p>
                    """,unsafe_allow_html=True)
        st.error("enter the board and deboard points correctly")
with tab2:
    a= st.selectbox("select the type of transport",("Choose a option","Goverment Bus","Private Bus"))
    b= st.selectbox("price option",("select price","<2000",">=2000<3000",">=3000"))
    if a == "Choose a option" and b == "select price":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data")
        a = cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df = pd.DataFrame(a,columns=col_name)
        st.table(df)
    elif a == "Goverment Bus" and b == "select price":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname like '%TSRTC%'")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Goverment Bus" and b == "<2000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname like '%TSRTC%' and price < 2000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Goverment Bus" and b == ">=2000<3000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname like '%TSRTC%' and price >=2000 and price < 3000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Goverment Bus" and b == ">=3000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname like '%TSRTC%' and price >= 3000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Private Bus":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname not like '%TSRTC%' ")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Private Bus" and b == "<2000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname not like '%TSRTC%' and price < 2000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Private Bus" and b == ">=2000<3000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname not like '%TSRTC%' and price >=2000 and price < 3000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
    elif a == "Private Bus" and b == ">=3000":
        cursor.execute("select busname,route_name,bustype,duration,price,seats_available from bus_data where busname not like '%TSRTC%' and price >=2000 and price >= 3000")
        b= cursor.fetchall()
        col_name = []
        for i in cursor.description:
            col_name.append(i[0])
        df= pd.DataFrame(b,columns=col_name)
        st.table(df)
with tab3:
    st.write("Travel Aggregators Bus Name")
    st.write("1. Goverment Bus Operation ID's")
    cursor.execute("select busname from bus_data where busname like '%TSRTC%'")
    gov_data = cursor.fetchall()
    gov_df = pd.DataFrame(gov_data,columns=["Bus Name"])
    st.write(gov_df)
    st.write("2. Private Bus Operator ID's")
    cursor.execute("select distinct(busname) from bus_data where busname NOT like '%TSRTC%'")
    pvt_data = cursor.fetchall()
    pvt_df = pd.DataFrame(pvt_data,columns=["Bus Name"])
    st.write(pvt_df)

with tab4:
    st.markdown("""
                <p style = "text-align: Justify;">redBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses. Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. redBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.</p>
                """,unsafe_allow_html=True)


cursor.execute("Select * from bus_data")
bus_data = cursor.fetchall()
bus_data_df = pd.DataFrame(bus_data)
# st.table(bus_data_df)
