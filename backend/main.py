from flight_agent import init_flight_agent
from hotel_agent import init_hotel_agent
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class query(BaseModel):
    origin:str
    destination:str
    start_date:str
    budget:str
    travelers:int
    
class hotel_query(BaseModel):
    destination:str
    budget:str 

app = FastAPI(debug=True,description="Trip Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_origins=['*']
)

flight_agent = init_flight_agent()
hotel_agent = init_hotel_agent() 
        
def create_base_prompt(trip_details:query)->str:
    '''This is the standard template for prompt'''
    return f"""
    Plan a trip with the following details:
    - Origin: {trip_details.origin}
    - Destination: {trip_details.destination}
    - Departure Date: {trip_details.start_date}
    - Budget Level: {trip_details.budget}
    - Number of travelers: {trip_details.travelers}
    """
        
@app.post('/flight')        
def run_flight_agent(trip_details:query):
    base_prompt = create_base_prompt(trip_details)
    return {'result':flight_agent.run(user_prompt=base_prompt+"Find flight options for this trip between the origin and destination.")}
    
@app.post('/hotel')
def run_hotel_agent(details:hotel_query):
    '''this is the api for hotel agent'''
    return {'result':hotel_agent.run(user_prompt="Find the hotel options in {details.destination} that fit in the budget level of {details.budget}")}
    
    
    
    
        
        
