Firedebug
=========

Tiny python library for remote debugging with firebase


    import firedebug
    
    firedebug.put("https://my-debug.firebaseIO-demo.com/ponies.json", '{"pony": "say hello"}')

    firedebug.log(db, '"Firedebug log() test"')

    obj = {
        "a": 1,
        "b": 2
    }
    firedebug.log_json(db, obj)
