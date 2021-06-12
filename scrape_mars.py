from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Scraping websites
def scrape_info():
    #Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_collection = {}

    #-----NASA URL--------

    #Setting our url
    nasa_url = 'https://redplanetscience.com/'

    #Visiting our url on separate browser
    browser.visit(nasa_url)

    time.sleep(2)

    #NASA website: scrape page into soup
    nasa_html = browser.html
    nasa_soup = bs(nasa_html, 'html.parser')

    #Finding the news title name
    nasa_results = nasa_soup.find('div', class_='list_text')
    news_title = nasa_results.find('div', class_='content_title').text

    #Findind the news paragraph
    news_p = nasa_results.find('div', class_='article_teaser_body').text

    mars_collection["NASA_News_Title"] = news_title
    mars_collection["NASA_Paragraph"] = news_p

    

    #-----JPL URL--------
    #Setting url variable
    jpl_url = 'https://spaceimages-mars.com/'

    #Visiting our url on separate browser
    browser.visit(jpl_url)

    #JPL website HTML file
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, 'html.parser')

    #Getting featured image url
    jpl_results = jpl_soup.find('div', class_='floating_text_area')

    #Finding link for image
    image_link = jpl_results.a['href']

    #Adding image link to main url to create complete url
    complete_image_link = jpl_url + image_link

    #Adding link to dictionary
    mars_collection["JPL_Mars_Spaces_Images_Featured_Image"] = complete_image_link


    #-----MARS FACTS URL--------
    #Setting url to variable
    facts_url = 'https://galaxyfacts-mars.com/'

    #Reading table from website into table in pandas
    mars_table = pd.read_html(facts_url)

    #Creating a datafrace from the table
    mars_facts_df = mars_table[1]

    mars_facts_df.columns=["Name of Measurements", "Measurements"]

    #To html table
    html_table = mars_facts_df.to_html()

    mars_collection["table"] = html_table

    


    #-----MARS HEMS URL--------
    #Setting url variable
    hemisphere_images_url = 'https://marshemispheres.com/'

    #Visiting our url on separate browser
    browser.visit(hemisphere_images_url)

    #Mars Hemispheres website HTML file
    mars_hems_html = browser.html
    mars_hems_soup = bs(mars_hems_html, 'html.parser')

    #Getting all results for class=item
    mars_hems_results = mars_hems_soup.find_all('div', class_='item')

    #Looping through to get all image urls

    hemisphere_image_urls = []

    for result in range(len(mars_hems_results)):
        browser.find_by_css("a.product-item img")[result].click()
        img_link = browser.find_by_text("Sample").first["href"]
        img_title = browser.find_by_css("h2.title").text
        hemisphere_image_urls.append({"img_title": img_title, "img_link": img_link})
        browser.back()
    
    mars_collection["Hemisphere_Title_Link"] = hemisphere_image_urls
    

    browser.quit()

    return mars_collection

