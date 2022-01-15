
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#import requests
#from bs4 import BeautifulSoup



def get_driver():
  chrome_options=Options()
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage-")
  driver=webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
    video_div_tag="ytd-video-renderer"
    Youtube_Trending_url="https://www.youtube.com/feed/trending"
    driver.get(Youtube_Trending_url)
    videos=driver.find_elements(By.TAG_NAME,video_div_tag)
    return videos


    #print(f"found {len(videos)} videos")
    
    
def parse_video(video):
    title_tag=video.find_element(By.ID,"video-title")
    title=title_tag.text
    url=title_tag.get_attribute("href")
   
    thumbnail_url=video.find_element(By.TAG_NAME,"img").get_attribute("src")

    channel_name=video.find_element(By.CLASS_NAME,"ytd-channel-name").text
    description=video.find_element(By.ID,"description-text").text
    other_info=video.find_element(By.CLASS_NAME,"ytd-video-meta-block").text

    return{
        "title": title,
        "url":url,
        "thumbnail_url":thumbnail_url,
        "description":description,
        "channel_name":channel_name,
        "others":other_info
      }






    
 
    #video_url=video_tag.get_attribute("href")
if( __name__=="__main__"):
    print("creating driver")
    driver=get_driver()
    videos=get_videos(driver)
    print("parsing first 10 videos info")
    videos_data=[parse_video(video) for video in videos[:10]]
    
    videos_data_df=pd.DataFrame(videos_data)
    videos_data_df.to_csv("youtube_top_trending.csv",index=None)



    



#check the reponse from url
#print(response.status_code)
#

# with open("trending.html","w") as f:
  # f.write(response.text)

#doc=BeautifulSoup(response.text,"html.parser")
#print("title",doc.title.text)