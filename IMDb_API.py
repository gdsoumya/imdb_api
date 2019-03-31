'''
	This is the main script that :

		1. Parses the client API request.

		2. Queries and Fetches the data from IMDb.

		3. Extracts and Parses the response into JSON format which is then relayed back to the client.
'''

import requests
from bs4 import BeautifulSoup
import re

def SearchApi(title,title_type,release_date,user_rating,genres,colors,keywords,plot,adult,count):

	# Building the query
	query='title='+title+'&title_type='+title_type+'&release_date='+release_date+'&user_rating='+user_rating+'&genres='+genres+'&colors='+colors+'&keywords='+keywords+'&plot='+plot+'&adult='+adult+'&count='+count
	
	# Requesting the search result
	try:
		resp = requests.get('https://www.imdb.com/search/title?'+query)
		soup = BeautifulSoup(resp.text,"html.parser")
		response=[]

		# Extracting Data and Parsing the response into JSON Format
		for movie in soup.find_all('div',class_='lister-item'):
			header = movie.find('h3',class_='lister-item-header')
			name = ' '.join(header.text.split('\n')[2:-1]).strip()
			id = header.find('a')['href'].split('/')[2]
			try:
				details = movie.find_all('p',class_='text-muted')
				try:
					runtime = details[0].find('span',class_='runtime').text.strip()
				except:
					runtime=None
				try:
					genre = details[0].find('span',class_='genre').text.strip()
				except:
					genre=None
				desc = details[1].text.strip() if details[1].text.strip()!='Add a Plot' else None
				if desc is not None:
					desc=desc.split('...')[0]+'...'
			except:
				runtime = None
				genre	= None
				desc = None
			try:
				rating = movie.find('div',class_='ratings-imdb-rating').text.strip()
			except:
				rating=None

			cast = movie.find_all('p')
			try:
				vg = movie.find('p',class_='sort-num_votes-visible').text
				t=re.split('Votes:|Gross:|Vote:|\|',vg)
				t = [ i.replace('\n','') for i in t if i.strip()!='']
				# print('hello',t,'\n')
				if 'Vote' in vg and 'Gross' not in vg:
					vote = t[0]
					gross = None
				elif 'Vote' not in vg and 'Gross' in vg:
					vote = None
					gross = t[0]
				elif 'Vote' not in vg and 'Gross' not in vg:
					vote = None
					gross = None
				else:
					vote=t[0]
					gross=t[1]
				cast=cast[-2]
			except:
				cast=cast[-1]
				vote=None
				gross=None
			try:
				x= cast.find_all('a')
				if x == []:
					raise Exception('Not Right Block')
				cast=cast.text
				t=re.split('Directors:|Stars:|Star:|Director:|\|',cast)
				t = [ i.replace('\n','') for i in t if i.strip()!='']
				if 'Director' in cast and 'Star' not in cast:
					director = t[0]
					star = None
				elif 'Director' not in cast and 'Star' in cast:
					director = None
					star = t[0]
				elif 'Director' not in cast and 'Star' not in cast:
					director = None
					star = None
				else:
					director=t[0]
					star=t[1]
			except:
				director = None
				star = None
			img = movie.find('img',class_='loadlate')['loadlate']
			if 'nopicture' not in img:
			 	img = img.split('._V1_')[0]+'._V1_UX300_CR0,0,,300_AL_.jpg'
			response.append({'idm_id':id,
			'name':name,
			'poster':img,
			'plot':desc,
			'runtime':runtime,
			'genre':genre,
			'rating':rating,
			'directors':director,
			'stars':star,
			'votes':vote,
			'gross':gross})

		# A list of Dictionaries is returned to the client
		return response
	except	Exception as e:
		print('SERVER ERROR :',e)
		return "ERROR"