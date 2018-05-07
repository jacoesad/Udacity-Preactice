import time
import csv
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


"""
the class of movie infomation
"""
class Movie:
	"""docstring for Movie"""
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link
	
	"""
	def print(self):
		print('name = {}'.format(name))
		print('rate = {}'.format(rate))
		print('location = {}'.format(location))
		print('category = {}'.format(category))
		print('info_link = {}'.format(info_link))
		print('cover_link = {}'.format(cover_link))
	"""

	def list(self):
		return "{},{},{},{},{},{}".format(self.name, self.rate, self.location,
			                              self.category, self.info_link, self.cover_link)


"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
""" 
def getHtml(url, loadmore = False, waittime = 2):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html


"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}"\
	      .format(category,location)
	return url


"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):


	movie_url = getMovieUrl(category, location)
	movie_html = getHtml(movie_url, True)
	soup = BeautifulSoup(movie_html, "html.parser")
	content_div = soup.find(id="content").find(class_="list-wp")

	movies_list = []

	for element in content_div.find_all("a", recursive=False):
		m = Movie(element.find(class_ = "title").text,
                  element.find(class_ = "rate").text,
                  location,
                  category,
                  element.get('href'),
                  element.find(class_ = "cover-wp").find('img').get('src'))
		movies_list.append(m.list())

	return movies_list


"""
write file feom input list
"""
def write_file(list):
	
	with open('movies.csv','w') as f:
		for element in list:
			f.write(element + '\n')


"""
get all info of movies
"""
def get_all_movies(categories_list):
	

	html = getHtml('https://movie.douban.com/tag/#/')
	soup = BeautifulSoup(html, "html.parser")
	locations_list = [i.get_text() for i in soup.find_all(class_ = 'category')[2].find_all(class_ = 'tag')[1:]]


	total_list = []

	for category in categories_list:
		for location in locations_list:
			total_list += getMovies(category, location)
			time.sleep(1)

	write_file(total_list)

	return 0
"""
generate output.txt from movies.csv
"""
def generate_output(categories_list):

    output_txt =[]
    df = pd.read_csv('movies.csv','rd',header = None,engine='python')
    df['name'],df['score'],df['location'],df['type'],df['url_1'],df['url_2'] = zip(*df[0].map(lambda x:x.split(',')))
    df.drop([0], axis = 1, inplace=True)
    for category in categories_list:
        output_txt.append(category+':')
        for i in range(3):
            output_txt.append('第{}名：{}，{:.2%}'.format(i+1, df[df['type'] == category]['location'].value_counts().index[i],
                                                      df[df['type'] == '剧情']['location'].value_counts().values[i]/len(df[df['type'] == '剧情'])))

           
    with open('output.txt','w') as f:
        for element in output_txt:
            f.write(element + '\n')
        
    
    return 0
	










get_all_movies(['剧情','爱情','科幻'])
generate_output(['剧情','爱情','科幻'])

