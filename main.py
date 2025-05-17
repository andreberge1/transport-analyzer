import requests

def fetch_departures(stop_place_id):
    url = "https://api.entur.io/journey-planner/v3/graphql"
    
    headers = {
        "Content-Type": "application/json",
        "ET-Client-Name": "company-journeyplanner"  # Replace with your app name
    }

    query = """
    {
      stopPlace(id: "%s") {
        name
        estimatedCalls(timeRange: 72100, numberOfDepartures: 10) {
          realtime
          aimedDepartureTime
          expectedDepartureTime
          destinationDisplay {
            frontText
          }
          serviceJourney {
            journeyPattern {
              line {
                id
                name
              }
            }
          }
        }
      }
    }
    """ % stop_place_id

    response = requests.post(url, json={"query": query}, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for call in data['data']['stopPlace']['estimatedCalls']:
            print(f"{call['aimedDepartureTime']} to {call['destinationDisplay']['frontText']}")
    else:
        print(f"Query failed with status code {response.status_code}")
        print(response.text)

def get_locations(search_location):
    url = f"https://api.entur.io/geocoder/v1/autocomplete?lang=no&text={search_location}&size=5&boundary.country=NOR"

    r = requests.get(url)

    res = r.json()

    print(res)


# Example usage
# fetch_departures("NSR:StopPlace:58367")  # Oslo S

get_locations("asker")
