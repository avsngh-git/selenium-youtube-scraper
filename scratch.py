from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
youtube_trending_library = 'https://www.youtube.com/feed/trending'
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver =webdriver.Chrome(options=chrome_options )
  return driver

def get_videos(driver):
  driver.get(youtube_trending_library)
  video_div_tag = 'ytd-video-renderer'
  video_divs = driver.find_elements(By.TAG_NAME, video_div_tag)
  return video_divs
  
def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src') 

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text

  return {
    'Title': title,
    'URL': url,
    'Thumbnail URL': thumbnail_url,
    'Channel Name': channel_name,
    'Video Description': description
  }
  
if __name__ == '__main__':
  driver = get_driver()

  videos = get_videos(driver)

  print(f'Found {len(videos)} Videos')
  
  top_10_videos = [parse_video(video) for video in videos[:10]]

  #Create a Pandas Dataframe using Parsed data and Write to CSV
  print('saving data to CSV')
  videos_df = pd.DataFrame(top_10_videos)
  videos_df.to_csv('trending.csv', index=None)
  