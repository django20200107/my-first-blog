
import sys
#sys.path.append('/home/user/opt/python')
def application(environ, start_response):
    status = '200 OK'
    #output = b'Hello World! python version : ' + sys.version.encode("utf-8")
    #output = b'Hello World! sys.path : ' + str(sys.path).encode("utf-8")
    #from sqlite3 import dbapi2 as Database
    #output = b'Hello World! db : ' + str(Database.sqlite_version).encode("utf-8")
    output = str(sys.path).encode("utf-8")

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

