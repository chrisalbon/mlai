Title: Store API Credentials For Open Source Projects   
Slug: store_api_credentials_for_open_source_projects   
Summary: Store API Credentials For Open Source Projects   
Date: 2016-11-01 12:00  
Category: Python  
Tags: Basic  
Authors: Chris Albon  

One issue which repeated comes up is how to manage private API credentials when the project is available on GitHub. This is the method I use for my own projects. I store all credentials in a JSON file and tell [gitignore](https://git-scm.com/docs/gitignore) to not upload that file. Then when I am running that code locally, load the API credentials from the JSON file.

## Preliminaries


```python
import json
```

## Step 1: Create a JSON with the API credentials


```python
credentials = {'access_secret': '392n39d93',
               'access_token': 'sdf424f',
               'consumer_key': 'sdf3223',
               'consumer_secret': 'dsf2344'}
```


```python
with open('credentials.json', 'w') as f:
    json.dump(credentials, f, ensure_ascii=False)
```

## Step 2: Add File To gitignore

Follow the [instructions here](https://help.github.com/articles/ignoring-files/).

Here is an [example of a good gitignore](https://gist.github.com/octocat/9257657) file.

## Step 3: Retrieve The Credentials From The JSON File

This step should be the one done inside your project or script.

### Load JSON File


```python
# Import API Keys
with open('credentials.json') as creds:    
    credentials = json.load(creds)
```

### Retrieve The Credentials


```python
credentials['consumer_key']
```




    'sdf3223'


