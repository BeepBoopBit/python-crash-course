from operator import itemgetter
import requests
from plotly import offline
from plotly.graph_objs import Bar, Layout


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

# 'score'
# 'title'
# 'type'

score, title_link = [], []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    
    score.append(response_dict['score'])
    if(response_dict.get('url')):
        title_link.append(f"<a href={response_dict['url']}>{response_dict['title']}</a>")
    else:
        title_link.append(response_dict['title'])
    
data = [{
    'type': 'bar',
    'x': title_link,
    'y': score,
}]
my_layout = Layout(title='Hacker News Top 30 Stories', xaxis={'title': 'Title'}, yaxis={'title': 'Score'})
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')