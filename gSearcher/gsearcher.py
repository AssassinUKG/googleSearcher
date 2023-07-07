# pip install google-api-python-client


#!/usr/bin/env python3
from googleapiclient.discovery import build
import argparse
import itertools

my_api_key = "Your GOOGLE API KEY"
my_cse_id = ["YOUR Custom Search Engine ID"] # you can add multiple engines for more results, ie: ["cse1", "cse2", cse3"]

def google_search(search_term, api_key, cse_id, num_results, start_page=1, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    try:
        res = service.cse().list(q=search_term, cx=cse_id, num=num_results, start=start_page, **kwargs).execute()
        totalResults = res['searchInformation']['totalResults']
        if totalResults == '0':
            return None
        return res['items']
    except Exception as e:
        print("An error occurred during the search:", str(e))
        return []

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--searchTerm", help="Enter a search term!")
parser.add_argument("-n", "--numResults", type=int, default=10, help="Enter the number of results to fetch (max 100)")
parser.add_argument("-p", "--page", type=int, default=1, help="Enter the page number")
args = parser.parse_args()

if args.searchTerm is None:
    print("Created by: Richard Jones")
    parser.print_help()
    exit()

searchTerm = args.searchTerm
numResults = min(args.numResults, 100)  # Ensure the number of results is capped at 100
page = args.page

rotating_cse_ids = itertools.cycle(my_cse_id)
current_cse_id = next(rotating_cse_ids)

# Find results for the specified page
results = google_search(
    searchTerm, my_api_key, current_cse_id, num_results=min(numResults, 10), start_page=page)
if not results:
    print("No Results found")
    exit()
if len(results) == 0:
    print("No Results found")
else:
    for result in results:
        print(result['link'])
