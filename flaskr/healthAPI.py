import json
from flaskr import app 
from flask import request

@app.route('/api/v1/health/checkStatus/', methods=['GET'])
def check_status():
	"""
	Returns a 200 if SDDCAPI is running and 400 if stopped.

	"""
	if request.method == 'GET':
		return json.dumps({"Status": "Running"}), 200,  {'Etag': ''}