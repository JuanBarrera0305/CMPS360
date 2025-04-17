import requests
import json

def search_jobs(query, location, geo_id):
    
    url = "https://api.scrapingdog.com/linkedinjobs"
    api_key = "67ff29c97097704407ca8245"
    
    
    params = {
        "api_key": api_key,
        "field": query,  
        "geoid": 90000070,  
        "page": 2,  
        "sortBy": "day",  
        "jobType": "part_time",  
        "expLevel": "entry_level",  
        "workType": "at_work",  
        "filterByCompany": ""  
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_response = response.json()
        
        with open('output.json', 'w') as f:
            json.dump(json_response, f, indent=4)
        
        print("LinkedIn Job search results saved to output.json")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    query = input("Enter job title or keyword: ")
    location = input("Enter location: ")

    geo_id = "1012481"  

    search_jobs(query, location, geo_id)
