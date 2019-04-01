''' 
	Server Script to initialize personal IMDb_API .
	
	The API can be accessed using GET or POST methods :

		1. For POST Method use endpoint /imdb-api-post
	
		2. For GET Method use endpoint /imdb-api-get

'''

from IMDb_API import SearchApi 
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS

# CONFIG
app = Flask(__name__)
CORS(app)

# ROUTES

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/test-api')
def api_test():
	return render_template('api_test.html')

# GET METHOD ENDPOINT
@app.route('/imdb-api-get',methods = ['GET'])
def imdb_api_get():

	# Building API Params
	try:
		title=request.args.get('title','')
		title_type=request.args.get('title_type','')
		release_date=request.args.get('release_date','')
		user_rating=request.args.get('user_rating','')
		genres=request.args.get('genres','')
		colors=request.args.get('colors','')
		keywords=request.args.get('keywords','')
		plot=request.args.get('plot','')
		adult=request.args.get('adult','')
		count=request.args.get('count','')
		if title=='' and keywords=='' and plot=='':
			return jsonify({"error":"Title/Keyword/Plot is required"}),400
		# Generating Response
		response = jsonify(SearchApi(title,title_type,release_date,user_rating,genres,colors,keywords,plot,adult,count))
		if response != 'ERROR':
				return response
		return	jsonify({"error":"SERVER ERROR"}),500

	except Exception as e:
		print("GET-ERROR:",e)
		return jsonify({"error":"Malformed Request"}),400


# POST METHOD ENDPOINT
@app.route('/imdb-api-post',methods = ['POST'])
def imdb_api_post():

	# Building API Params
	try:
		title=request.get_json().get('title','')
		title_type=request.get_json().get('title_type','')
		release_date=request.get_json().get('release_date','')
		user_rating=request.get_json().get('user_rating','')
		genres=request.get_json().get('genres','')
		colors=request.get_json().get('colors','')
		keywords=request.get_json().get('keywords','')
		plot=request.get_json().get('plot','')
		adult=request.get_json().get('adult','')
		count=request.get_json().get('count','')
		if title=='' and keywords=='' and plot=='':
			return jsonify({"error":"Title/Keyword/Plot is required"}),400
		# Generating Response
		response = jsonify(SearchApi(title,title_type,release_date,user_rating,genres,colors,keywords,plot,adult,count))
		if response != 'ERROR':
				return response
		return	jsonify({"error":"SERVER ERROR"}),500

	except Exception as e:
		print("POST-ERROR:",e)
		return jsonify({"error":"Malformed Request"}),400


if __name__ == '__main__':
	app.run()
