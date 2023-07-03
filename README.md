# googleSearcher
A custom Google search (to bypass some limitations on google and VPNs)

The tool has been coded to only return 100 (max) urls from google search. Google only allow 100 results. You can get 100 from page 1-10 or page 11-20 etc, but only ever 100 max results at a time.  
A Limitation imposed by google. 

## Setup (google api)

Link: https://console.cloud.google.com/
To create your application's API key:

Create a new key:

1. Open the Google API Console.
2. Create or select a project.
3. On the Credentials page, get an existing API key or create a new one (Create credentials > API key). You can restrict the key before using it in production by clicking Restrict key.
> To prevent quota theft, secure your API key following these best practices.


# Usage

```bash
python3 gsearcher.py -s "filetype:pdf site:tesla.com"
```
