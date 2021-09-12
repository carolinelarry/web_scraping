# Web Scraping - Mission to Mars

Built a web application that scraped various websites for data related to Mars and displayed the information in a single HTML page.


<img width="1440" alt="Screen Shot 2021-08-30 at 5 25 13 PM" src="https://user-images.githubusercontent.com/79863465/131413830-6bd14c7a-770e-478b-8608-7bf189d190bd.png">
<img width="1440" alt="Screen Shot 2021-08-30 at 5 25 25 PM" src="https://user-images.githubusercontent.com/79863465/131413866-3cadf223-6461-4311-8a9b-09fbfeb3a5d6.png">


## Step 1 - Scraping

Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest news title and paragraph text
### JPL Mars Space Images - Featured Image

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com)

* Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string

### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`

* Appended the dictionary with the image url string and the hemisphere title to a list. This list contained one dictionary for each hemisphere

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of the scraping code from above and returned one Python dictionary containing all of the scraped data

* Next, created a route called `/scrape` that imported your `scrape_mars.py` script and called your `scrape` function

  * Stored the return value in Mongo as a Python dictionary

* Created a root route `/` that queried your Mongo database and passed the mars data into an HTML template to display the data

* Created a template HTML file called `index.html` that took the mars data dictionary and displayed all of the data in the appropriate HTML elements

## Contact
Email: cgrace1011@gmail.com
LinkedIn: https://www.linkedin.com/in/caroline-larry-9112b0187/


© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

