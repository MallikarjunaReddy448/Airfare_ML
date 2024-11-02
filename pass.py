import pandas as pd 
import datetime
import streamlit as st 
import pickle
from pickle import load
import datetime
import plotly.express as px


df = pd.read_csv("International_Airlines_Passengers_cleaned.csv",index_col="Month")
df.index.freq="MS"

model = load(open("Airline_Passengers.sav",'rb'))


def main(): 

    st.set_page_config(
        page_title= "Forecasting Web Application",
        layout= "wide"
    )

    st.title("International Airlines Passengers Number Forecasting")
    
    Menu = ["About","Forecast","Contact"]
    
    load= st.button("Go to Menu")
    
    if "load_state" not in st.session_state :
        st.session_state.load_state = False
        st.warning('Click on Go to Menu button to choose different options')

        st.warning("""Welcome to International Airlines Passengers Data Forecasting web application which is running based on 
        pre-trained 'Machine Learning Model/Algorithm'. And try to explore this application based on the instructions.""")
       



    if load or st.session_state.load_state:
        st.session_state.load_state= True

        choice = st.sidebar.selectbox("Keep Exploring this Web Application", Menu)
        st.sidebar.warning('''Please close the side bar to get better view after choosing any one option
                            you can access side bar by clicking on ">" icon on top left corner''')

        if choice=='About':

    
            col1,col2 = st.columns(2)
            with col1:
                st.write("Original Historical Data")
                st.write(df)
            with col2:
                fig = px.line(df,x=df.index,y=df["Thousands of Passengers"],title="Line plot of Original Data")
                st.plotly_chart(fig)

            st.subheader("Details:")
            st.write('''The data is monthly data collected on every month starting and it contains the records from 1949-01-01 to 1960-12-01.
            And the data was analysed and noticed that the data is having multiplicative seasonality and trend. We can say that the data is 
            following the Seasonal Pattern plus Linear Growth.
            \n The model I have trained on this data was HoltWinters's Triple Exponential Smoothing aka Winter’s Exponential Smoothing (WES).
            This model is capable of reading both trend and seasonality.
            \n Here are some graphical representations of the data are provided where we can clearly check the trend and seasonality"
            ''')

            col3,col4 = st.columns(2)
            with col3:
                fig = px.histogram(df, x=df.index, y=df["Thousands of Passengers"],
                                title = "Histogram of International Airlines Passengers")
                st.plotly_chart(fig)

        elif choice == 'Forecast':
            st.warning("Starting Year is Default please choose ending Year")    

            # This is to forecast till today  
            end = st.date_input("End",min_value= pd.to_datetime('1964-01-01'),
                                        max_value = None )

            # end = st.date_input("End", min_value=pd.to_datetime('1961-01-01'),
            #         max_value=pd.to_datetime('1964-01-01'),
            #         value=pd.to_datetime('1961-12-01'))

            pred = model.predict(start = df.index[-1],end = end)         
            forecast = []
            for i in pred:
                forecast.append(i)
            forecasted = pd.DataFrame(forecast)
            forecasted['Month'] = pred.index
            forecasted = forecasted.set_index("Month")
            forecasted.index = forecasted.index.date
            forecasted['Forecasted No. of Passengers'] = forecast
            forecasted.drop(columns=0,inplace=True)
            col5,col6 = st.columns(2)
            with col5:
                st.write(forecasted)

            with col6:
                new_df = pd.concat([df,forecasted])
                fig =  px.line(new_df,title="Line plot of Original Data with Forecasted Data")
                fig.update_layout(yaxis_title="Thousands of Passengers",xaxis_title ="Month")
                st.plotly_chart(fig)

if __name__=='__main__':
    main()


