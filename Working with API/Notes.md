# Working with API

- A web API is a part of a website to interact with programs. Those programs use very specific URLs to request certain information. This kind of request is called an API call. 
- The requested data will be returned in an easily processed format, such as JSON or CSV.
- Most apps that rely on external data sources, such as apps that integrate with social media sites, rely on API calls.


## Requesting Data Using an API Call

```
https://api.github.com/search/repositories?q=language:python&sort=stars
```

- This call returns the number of Python projects currently hosted on GitHub, as well as information about the most popular python repositories.
- `https://api.github.com/` directs the request to the part of GitHub that responds to API calls.
- `search/repositorie` tells the API to conduct a search through all repositories on GitHub
- `?` signals that we're about to pass an argument.
- the `q` stands for query
- the `=`means that we're assigning a value to the argument
- `language:python` indicates that we want information only on repositories that have Python as the primary language.
- `&sort=stars` sorts the project by the number of stars they've been given.

## Requirements

- Python 3
- requests

### Processing an API Response

```python
import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'applciation/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable and convert it into a python dictionary
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
```

- Simple calls like this should return a complete set of results, so it's safe to ignore the value associated with 'incomplete_results'. But when you're making more complex API calls, your program should check this value.
- Here's some more example:

```python
import requests

# Set-up the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'applciation/vnd.github.v3+json'}

# Request the information
r = requests.get(url, headers=headers)

# Print the status code
print(f"Status code: {r.status_code}")


# Convert the request into a python dictionary and save it to a variable
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

- Many APIs require you to register and obtain an API key to make API calls. As of this writing. GitHub has no such requirements, but if you obtain an API key, your limits will be much higher.


## Visualizing Repositories using Plotly

```python
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
```

## The Hcaker News API

- The Hacker News API is a read-only API that allows you to get information about stories, comments, and users on Hacker News. Here's it's API:

```
https://hacker-news.firebaseio.com/v0/item/19155826.json
```

### Exploring the API


```python
import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
```

## Using the operator library

```python
from operator import itemgetter
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# PRocess information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    i = requests.get(url)
    print(f"id: {submission_id}\tstatus: {i.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```