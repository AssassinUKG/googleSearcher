# pip install google-api-python-client

from googleapiclient.discovery import build
import argparse

my_api_key = "Your GOOGLE API KEY"
my_cse_id = "YOU Custom Search Engine ID"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--searchTerm", help="Enter a searchterm!")
args = parser.parse_args()


if args.searchTerm is None:
    print("Enter a search term, exiting")
    exit()

searchTerm = args.searchTerm

results = google_search(
    searchTerm, my_api_key, my_cse_id, num=10)

#print(results)
# find all 100 results from page 1 to page 10
allResults = []
for startPage in range(1, 10):
    allResults.append(google_search(
        searchTerm, my_api_key, my_cse_id, num=10, start=startPage))

if len(allResults) == 0:
    print("No Results found")
else:
    print("Results found")        
    for result in allResults:
        for r in result:
            print(r['link'])
            #pprint.pprint(result)
