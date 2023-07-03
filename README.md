# googleSearcher
A custom Google search (to bypass some limitations on Google with regards to timouts, vpns etc)

The tool has been coded to only return 100 (max) urls from google search. Google only allow 100 results. You can get 100 from page 1-10 or page 11-20 etc, but only ever 100 max results at a time.  
A Limitation imposed by google. 

## Setup

You will need a...

GOOGLE API Key
GOOGLE CUSTOM SEARCH ENGINE ID

### Google API Key

Link: https://console.cloud.google.com/
To create your application's API key:

Create a new key:

1. Open the Google API Console.
2. Create or select a project.
3. On the Credentials page, get an existing API key or create a new one (Create credentials > API key). You can restrict the key before using it in production by clicking Restrict key.
> To prevent quota theft, secure your API key following these best practices.

### Google CSE (Custom Search Engine)

1. Goto https://programmablesearchengine.google.com/controlpanel/all
2. Add a new search engine and hit save after (see image for settings) 
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/86a3dda2-b104-4741-bad3-dc6659084e9a)
3. Get your search engine ID  
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/cb664dc2-eb03-417d-8dd3-d3f721f7d9e0)

## Install

```
git clone
cd
pip install -r requirements.txt
```


## Usage

```bash
python3 gsearcher.py -s "filetype:pdf site:tesla.com"
```
