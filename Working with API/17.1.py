import requests
import json
import matplotlib.pyplot as plt

url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# Convert the response to a Python dictionary
data = r.json()

data_items = data['items']

# Save the data into a json
with open("github-data.json", 'w') as f:
    json.dump(data, f, indent=4)


owner, stars = [], []
for item in data_items:
    owner.append(item['owner']['login'])
    stars.append(item['stargazers_count'])

## Just for fun
fig, ax = plt.subplots()

ax.bar(owner, stars)
plt.tick_params(axis='both', labelsize=5)
plt.show()