# googleSearcher
A custom Google search (to bypass some limitations on Google with regards to timouts, vpns etc)

The tool has been coded to only return 100 (max) urls from google search. Google only allow 100 results. You can get 100 from page 1-10 or page 11-20 etc, but only ever 100 max results at a time.  
A Limitation imposed by google. 

> WARNING you will qucikly hit the google limit and will need a paid account to get more. 
> Script has been edited to allow number choice 1-100 results

Great for OSINT and Google Dorks!

## Install

```bash
git clone https://github.com/AssassinUKG/googleSearcher.git
cd googleSearcher
pip install -r requirements.txt

cd gSearcher
python3 gsearcher.py
```

## Usage

```bash
python3 gsearcher.py -s "filetype:pdf site:tesla.com"
```

## Screenshots

filetype dork (pdf)
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/e9f3bce8-3481-4a6f-82e6-3401ae72b463)

sqli dork (gallery.php?id=)

** Update: 04/07/2023: Added option for number of results to help free users **
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/76534204-3b00-41f8-8a82-4f864b6d57f8)


---

## Setup (Google stuffs)

You will need a...

* GOOGLE API Key
* GOOGLE CUSTOM SEARCH ENGINE ID

### Google API Key

Link: https://console.cloud.google.com/
To create your application's API key:

Create a new key:

1. Open the Google API Console.
2. Create or select a project.
3. On the Credentials page, get an existing API key or create a new one (Create credentials > API key). You can restrict the key before using it in production by clicking Restrict key.
> Protect your API key by changing the restrictions to only search API or whatever you need.

### Google CSE (Custom Search Engine)

1. Goto https://programmablesearchengine.google.com/controlpanel/all
2. Add a new search engine and hit save after (see image for settings) 
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/86a3dda2-b104-4741-bad3-dc6659084e9a)
3. Get your search engine ID  
![image](https://github.com/AssassinUKG/googleSearcher/assets/5285547/cb664dc2-eb03-417d-8dd3-d3f721f7d9e0)

Now in the gsearcher.py file replace the variables with your key and cse id. 

```python
my_api_key = "Your GOOGLE API KEY"
my_cse_id = "YOU Custom Search Engine ID"
```

Now you're ready to get results! 

