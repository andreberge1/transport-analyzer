import requests

def get_stopPlaces():
    url = "https://api.entur.io/journey-planner/v3/graphql"    
    headers = {
        "Content-Type": "application/json",
        "ET-Client-Name": "company-journeyplanner"  # Replace with your app name
    }
    query = """
    {
        stopPlaces {
            id
            name
            latitude
            longitude
            transportMode
        }
    }
    """

    response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Query 'Get stopplaces' failed with status code {response.status_code}")
        print(response.text)

    return data

def get_operators():
    url = "https://api.entur.io/journey-planner/v3/graphql"    
    headers = {
        "Content-Type": "application/json",
        "ET-Client-Name": "company-journeyplanner"  # Replace with your app name
    }
    query = """
    {
    operators {
        id
        name
        url
    }
    }
    """

    response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Query 'Get operators' failed with status code {response.status_code}")
        print(response.text)

    return data