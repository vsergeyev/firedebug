"""
Remote debug with firebase.
http://firebase.com

2013, V.Sergeyev <vova.sergeyev@gmail.com>
https://github.com/vsergeyev/firedebug
"""

import urllib2
import datetime
import json


def log_json(api_endpoint, obj):
	"""
	Serialize object and then call log()
	"""
	return log(
		api_endpoint,
		json.dumps(obj)
	)


def log(api_endpoint, data):
	"""
	Put entry with timestamp
	"""
	now = datetime.datetime.now().strftime("%m %d %Y %H:%M:%S")

	return put(
		api_endpoint,
		'{"%s": %s}' % (now, data)
	)


def put(api_endpoint, data):
	"""
	Sample:
	api_endpoint: https://my-debug.firebaseIO-demo.com/debug.json
	data: '{"test": "true"}'
	"""

	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(api_endpoint, data=data)
	request.get_method = lambda: 'PATCH'
	
	res = opener.open(request)
	
	return res.read()