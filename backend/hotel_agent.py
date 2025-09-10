from agent_template import Agent
from prompts import hotel_system_prompt


def init_hotel_agent()->Agent:
    return Agent(
        name="Hotel assist",description="Finds suitable accommodations at your destination within budget",system_prompt=hotel_system_prompt
    )