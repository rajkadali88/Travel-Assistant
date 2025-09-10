from agent_template import Agent
from prompts import flight_system_prompt

def init_flight_agent() -> Agent:
    '''Initialize and return Flight assist agent'''
    return Agent(name="Flight assist",description="Searches for available flights between your origin and destination",system_prompt=flight_system_prompt)

