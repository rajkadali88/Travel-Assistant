import streamlit as st 
import datetime
import requests
import json 

st.set_page_config(
    page_title="Trip Planning Assist",
    layout="wide",
)

st.title("AI-Travel Planner")

st.markdown("Let the AI agent help you to plan your trip!")


def render_trip_form():
    with st.form("trip_details_form"):
        st.header("Enter your trip details")
        col1, col2 = st.columns(2)
        
        with col1:
            origin = st.text_input("Origin City","New York")
            destination = st.text_input("Destination City","Tokyo")
            
        with col2:
            today = datetime.date.today()
            start_date = st.date_input("Departure Date",today+ datetime.timedelta(days=30))
            
        col1,col2 = st.columns(2)
        with col1:
            budget=st.selectbox(
                "Budget Level",
                options = ["Budget","Moderate","Luxury"],
                index=1
            )
        with col2:
            travelers = st.number_input("Number of Travelers",min_value=1,max_value=10, value=2)
            
            
        submitted = st.form_submit_button("Start Planning")
        
        if submitted:
            return {
                "origin":origin,
                "destination":destination,
                "start_date":json.dumps(start_date,default=str),
                'budget':budget,
                'travelers':travelers,
                'submitted':True 
            }
        else:
            return {
                'submitted':False
            }
            
def main():
    trip_details = render_trip_form()
    
    if trip_details['submitted']:
        try:
            response = requests.post("http://backend:8000/flight",json={
                "origin":trip_details['origin'],
                "destination":trip_details['destination'],
                "start_date":trip_details['start_date'],
                'budget':trip_details['budget'],
                'travelers':trip_details['travelers'],
            })
            flight_response = response.json().get('result','no result from flight api')
            
            response = requests.post("http://backend:8000/hotel",json={
                'destination':trip_details['destination'],
                'budget':trip_details['budget']
            })
            hotel_response = response.json().get('result','no result from hotel api')
            
            tabs = st.tabs(['Flight','Hotel'])
            with tabs[0]:
                st.markdown(flight_response['content'])
            with tabs[1]:
                st.markdown(hotel_response['content'])
        except Exception as e:
            st.error(str(e))
            
            
if __name__=='__main__':
    main()