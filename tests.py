"""
Remote debug with firebase. Tests.
http://firebase.com

2013, V.Sergeyev <vova.sergeyev@gmail.com>
https://github.com/vsergeyev/firedebug
"""

import socket
import datetime

import firedebug


if __name__=="__main__":
	now = datetime.datetime.now().strftime("%m %d %Y %H:%M:%S")
	host = socket.gethostname()

	print firedebug.put(
		"https://my-debug.firebaseIO-demo.com/ponies.json",
		'{"%s": "%s says hello"}' % (now, host)
	)