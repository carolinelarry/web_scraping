from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    #Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data = {}

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

    mars_data["NASA News Title"] = news_title
    mars_data["NASA Paragraph"] = news_p

    #return(mars_data)

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
    mars_data["JPL Mars Spaces Images: Featured Image"] = complete_image_link

    #-----MARS FACTS URL--------
    #Setting url to variable
    facts_url = 'https://galaxyfacts-mars.com/'
    #FIGURE OUT WHAT NEEDS TO GO HERE

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

    #hemisphere_image_urls = []: from jupyter notebook

    for result in mars_hems_results:
    
        image_link = result.img['src']
        image_title = result.h3.text
    
        complete_image_link = hemisphere_images_url + image_link
    
        #hemisphere_image_urls.append({image_title: complete_image_link})
       
        mars_data[image_title] = complete_image_link

    browser.quit()

    return mars_data

