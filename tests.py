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

    db = "https://my-debug.firebaseIO-demo.com/ponies.json"

    print firedebug.put(db,
        '{"%s": "%s says hello"}' % (now, host)
    )

    print firedebug.log(db, '"Firedebug log() test"')

    obj = {
        "a": 1,
        "b": 2
    }
    print firedebug.log_json(db, obj)