import requests
from bs4 import BeautifulSoup
youtube_trending_library = 'https://www.youtube.com/feed/trending'
response = requests.get(youtube_trending_library)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
