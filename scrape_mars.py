#!/usr/bin/env python
# coding: utf-8

# In[46]:


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import pymongo


# In[47]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


db = client.mars_db
collection = db.articles

# In[2]:

def scrape():

    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    # In[5]:


    news = soup.find_all('div', class_="bottom_gradient", limit=1)
    news_title=news[0].text


    # In[6]:


    para = soup.find_all('div', class_="article_teaser_body", limit=1)
    news_p=para[0].text


    # In[7]:


    url_img = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url_img)


    # In[8]:


    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    # In[9]:


    photo = soup.find_all('', class_="showimg fancybox-thumbs")


    # In[10]:


    for i in photo:    
        pic = i['href']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + pic
    featured_image_url


    # In[11]:


    table_url = "https://space-facts.com/mars/"


    # In[12]:


    tables = pd.read_html(table_url)
    tables


    # In[13]:


    df = tables[0]
    df.columns = ["Info", "Mars"]
    mars_facts = df.to_html()
    mars_facts


    # In[24]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[36]:


    Hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Hemispheres_url)


    # In[38]:


    browser.click_link_by_partial_text('Cerberus')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[39]:


    photos = soup.find_all("a", target="_blank")

    all_img_url = []

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url


    # In[40]:


    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[41]:


    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url


    # In[42]:


    browser.click_link_by_partial_text('Major Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[43]:


    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url


    # In[44]:


    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[45]:


    photos = soup.find_all("a", target="_blank")

    for photo in photos:
        if photo.text.strip() == "Sample":
            image_url = photo["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    all_img_url.append(a)

    all_img_url
    
if __name__ == "__main__":
    scrape_info()
