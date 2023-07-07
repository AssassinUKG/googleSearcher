# pip install google-api-python-client


#!/usr/bin/env python3
from googleapiclient.discovery import build
import argparse
import itertools

my_api_key = "Your GOOGLE API KEY"
my_cse_id = "YOUR Custom Search Engine ID" # you can add multiple engines for more results, ie: ["cse1", "cse2", cse3"]

def google_search(search_term, api_key, cse_id, num_results, start_page=1, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, num=num_results, start=start_page, **kwargs).execute()
    if int(res['searchInformation']['totalResults']) > 0:
        return res['items']
    return []

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--searchTerm", help="Enter a search term!")
parser.add_argument("-n", "--numResults", type=int, default=10, help="Enter the number of results to fetch (max 100)")
parser.add_argument("-p", "--page", type=int, default=0, help="Enter the page number (1-10)")
args = parser.parse_args()

if args.searchTerm is None:
    print("Developed by: Richard Jones")
    parser.print_help()
    exit()

searchTerm = args.searchTerm
numResults = min(args.numResults, 100)  # Ensure the number of results is capped at 100

if int(args.page) > 10:
    print("page needs to be between (1-10)")
    exit()


allResults = []
if args.page > 0 :
    page = args.page - 1
    allResults.extend(google_search(
            searchTerm, my_api_key, my_cse_id, num_results=min(numResults, 10), start_page=page * 10 + 1 ))
else:
    # Calculate the number of pages required based on the desired number of results
    num_pages = (numResults - 1) // 10 + 1
    # Find all results from page 1 to the required number of pages
   
    for startPage in range(0, num_pages):
        if startPage >= 1:
            startPage = startPage * 10 + 1
        if startPage >= 100:
            break
        
        allResults.extend(google_search(
            searchTerm, my_api_key, my_cse_id, num_results=min(numResults, 10), start_page=startPage))

if len(allResults) == 0:
    print("No Results found")
else:            
    for result in allResults:
        print(result['link'])
