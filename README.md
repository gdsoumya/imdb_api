![IMDb_API](https://raw.githubusercontent.com/gdsoumya/imdb_api/master/IMDb_API.png)
<br><br>
**IMDb_API** is a custom open-source IMDb search API service, it allows users to make api calls to query the IMDb database. This repo contains all the necessary files required to initialize your own IMDb_API server.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**IMDb_API** requires [ **Python (> Python 3.6)**](https://www.python.org/) .

### Getting the project.

```sh
$ git clone https://github.com/gdsoumya/imdb_api.git
or 
Download and extract the Zip-File
```
### Setting up Virtual Environemt
Setting up a virtual environment would be better for both development and normal execution purposes.
```sh
$ cd imdb_api
$ python -m virtualenv env
$ source env/bin/activate
 or (Windows machine)
$ .\env\Scripts\activate
```
### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ pip install -r dependencies.txt 
```
## Starting the Bot
To start the Flask server run
```sh
$ python api-server.py
```
A Flask development server will be initialized at http://127.0.0.1:5000/ .
The API server is now ready to use, you can send requests to the server and fetch results.

### Warnings 
A possible warning that one might get is :

**WARNING: Do not use the development server in a production environment.**

This warning is displayed because currently a Flask Development Server is running but the default environment of Flask is set to Production, to remove this warning change the FLASK_ENV environment variable.
<br>***Setting environment to development automatically sets the debugger on.**
```sh
$ export FLASK_ENV=development
or (Windows machine)
$ set FLASK_ENV=development
```
## Using IMDb_API to Query Titles

The API server provides 2 endpoints to access the search api :
- **POST** : /imdb-api-post
- **GET** : /imdb-api-get
Both endpoints return the same result.

A complete guide to using the api endpoints can be found at http://127.0.0.1:500/ .

### API Request Parameters
**REQUIRED Parameters**
Atleast one of the following parameters are needed to perform a succesful search.

| Parameter | Description |
| ------ | ------ |
|title |Title/Query to Search|
|keywords |Instead of searching for specific Title, you can search for keywords that are related to the title you want to search <br>.eg. 'detective' or 'jail,escape'|
|plot |**This is a tricky and experimental feature, avoid using it.** <br>Instead of searching for specific Title, you can give the plot of the title you want to search.|

**OPTIONAL Parameters**

| Parameter | Description |
| ------ | ------ |
|title_type |Types of title to search, possible values : <br><ul><li>feature</li><li>tv_movie</li><li>tv_series</li><li>tv_episode</li><li>tv_special</li><li>tv_miniseries</li><li>documentary</li><li>video_game</li><li>short</li><li>video</li><li>tv_short</li></ul><bt>eg. 'feature' or 'feature,tv_series,video' etc..|
|release_date |Two comma separated dates(YYYY-MM-DD) indicating a time range to search for title released in that range of time.<br>eg. '1999-02-20,2018-11-29' or ' ,2000-01-31' or '1999-10-11, ' etc.|
|user_rating |Two comma separated integers(0-10) indicating the range of IMDb rating from which you want to search for the titles.<br>eg. '1,9' or '5.6,9.9' etc.|
|genres |Genre to search titles from, possible values:<br><ul><li>action</li><li>adventure</li><li>animation</li><li>biography</li><li>comedy</li><li>crime</li><li>documentary</li><li>drama</li><li>family</li><li>fantasy</li><li>film-noir</li><li>game-show</li><li>history</li><li>horror</li><li>music</li><li>musical</li><li>mystery</li><li>news</li><li>reality-tv</li><li>romance</li><li>sci-fi</li><li>sport</li><li>talk-show</li><li>thriller</li><li>war</li><li>western</li></ul>eg. 'action,adventure,animation' etc.|
|colors |Color Info to search titles from,possible values:<br><ul><li>color</li><li>black_and_white</li><li>colorized</li><li>aces</li></ul>eg. 'color,colorized,aces' etc.|
|adult |Option to whether include or exclude adult titles, possible values:<br><ul><li>exclude</li><li>include</li></ul>by default it is set to exclude adult content.|
|count |Maximum number of results to fetch.<br>eg. '50','100' etc.<br>Default max count is 50.|

### API CALL
**GET Request**

cURL Example:
```sh
curl -X GET http://127.0.0.1:5000/imdb-api-get?title=game&title_type=feature
```
AJAX Example:
```javascript
$.ajax({
  url:'http://127.0.0.1:5000/imdb-api-get',
  type:'get',
  data:'title=game&title_type=feature',
  success:function(myJson){
     console.log(myJson);
  }
});
```
**POST Request**

cURL Example:
```sh
curl -d '{"title":"Game","title_type":"feature"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/imdb-api-post
```
AJAX Example:
```javascript
$.ajax({
    url:'http://127.0.0.1:5000/imdb-api-post',
    type:'post',
    contentType:'application/json',
    data:JSON.stringify({'title':'game','title_type':'feature'}),
    success:function(myJson){
        console.log(myJson);
    }
 });
```

### API Response 
The Response is a list of dictionaries where each dictionary contains details about one title. The list is ordered in the descending order of Popularity of the titles.

**Success Response** :

  Code: 200
  Response :
```json
[
     {
	"directors": "John Francis Daley, Jonathan Goldstein",
	"genre": "Action, Comedy, Crime",
	"gross": "$69.00M",
	"idm_id": "tt2704998",
	"name": "Game Night (I) (2018)",
	"plot": "A group of friends who meet regularly for game nights find themselves entangled ....",
	"poster": "https://m.media-amazon.com/images/M/MV5BMjI3ODkzNDk5MF5BMl5BanBnX.jpg",
	"rating": "7.0",
	"runtime": "100 min",
	"stars": "Jason Bateman, Rachel McAdams, Kyle Chandler, Sharon Horgan",
	"votes": "155,318",
     },
...
...
...]
```
**Error Response** :

  Code: 400
  Response :
```json
{"error":"Title/Keyword/Plot is required"}
```
**OR**

  Code: 500
  Response :
```json
{"error":"SERVER ERROR"}
```
### API Response Parameters
The parameters returned for each title :

| Parameter | Description |
| ------ | ------ |
|idm_id |IMDb ID of the title.|
|name |Name of the title.|
|plot |Short summary/plot of the story.|
|poster |Poster image urls|
|genre |Genre of the title.|
|runtime |Duration of the movie/title.|
|rating |IMDb Rating of the title.|
|directors |Name of the Directors of the title.|
|stars |Cast of the title.|
|votes |Number of votes recieved by the title on IMDb.|

## Errors and Debugging options
The server by default does not start in debugger mode but to initialize debugger mode change the last line of the '[api-server.py](https://github.com/gdsoumya/imdb_api/blob/master/api-server.py)' file to :
```python
app.run() -> app.run(debug=True)
```
Most errors will be logged to the console and can be referenced later for debugging.
## Packages Used
- **[Requests](http://docs.python-requests.org/en/master/)** : For fetching data from IMDb.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** : For parsing the fetched data.
- **[Flask](http://flask.pocoo.org/)** : For hosting the web interface.
- **[Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)** : For enabling Cross Origin Resource Sharing.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
