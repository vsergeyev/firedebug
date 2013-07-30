"""
Remote debug with firebase.
http://firebase.com

2013, V.Sergeyev <vova.sergeyev@gmail.com>
https://github.com/vsergeyev/firedebug
"""

import urllib2


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