from .id_generator import get_next_unique_number
from datetime import datetime

def group_formatter(data, initiated_by):
    """
    Args:
        data (dict): This is where the data collected from the user is sent in the form of a dict.
        initiated_by (str): Full name of the user who entered this information.
    """
    text = ''
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    if data['type']=='Human':
        text+=data['id']
        text+=f"\n{formatted_date}\n"
        text+=f"Initiated by: {initiated_by}\n"
        text+=f"Specie: {data['type']}\n"
        text+=f"Gender: {data['gender']}\n"
        text+=f"Nationality: {data['nationality']}\n"
        text+=f"Education: {data['education']}\n"
        text+=f"Eye Color: {data['eye_color']}\n"
        text+=f"Hair Color: {data['hair_color']}\n"
        text+=f"Height: {data['height']}cm\n"
    elif data['type']=='Animal':
        text+=data['id']
        text+=f"\n{formatted_date}\n"
        text+=f"Initiated by: {initiated_by}\n"
        text+=f"Specie: {data['type']}\n"
        text+=f"Species: {data['species']}\n"
        text+=f"Mammal: {data['mammal']}\n"
        text+=f"Predator: {data['predator']}\n"
        text+=f"Color: {data['color']}\n"
        text+=f"Weight: {data['weight']}kg\n"
        text+=f"Age: {data['age']}\n"
    elif data['type']=='Alien':
        text+=data['id']
        text+=f"\n{formatted_date}\n"
        text+=f"Initiated by: {initiated_by}\n"
        text+=f"Specie: {data['type']}\n"
        text+=f"Race: {data['race']}\n"
        text+=f"Skin Color: {data['skin']}\n"
        text+=f"Dangerous: {data['dangerous']}\n"
        text+=f"Has Reason: {data['reason']}\n"
        text+=f"Weight: {data['weight']}kg\n"
    else:
        text+=f"\n{formatted_date}\n"
        text+=f"Initiated by: {initiated_by}\n"
        text+=f"Specie: {data['type']}\n"
        text+=f"Is Humanoid: {data['humanoid']}\n"
    
    return text
        
        