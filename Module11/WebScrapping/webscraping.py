import requests 
import json

def search_jobs(query, location):
    url = "https://api.scrapingdog.com/indeed"
    api_key = "6617bcc273ed7a43ca58445d"
    job_search_url = f"https://www.indeed.com/jobs?q={query}&l={location}"

    params = {"api_key": api_key, "url": job_search_url}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_response = response.json()

        jobs = []
       
        with open('output.json', 'w') as f:
            json.dump(json_response, f, indent=4)
        
        print("JSON response saved to output.json")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    query = input("Enter job title or keyword: ")
    location = input("Enter location: ")
    search_jobs(query, location)