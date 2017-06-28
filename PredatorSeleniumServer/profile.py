from urlparse import urlparse, parse_qs
import json
import hack

def getFriends(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type','text/html')
    requestHandler.end_headers()
    # Send the html message
    query_components = parse_qs(urlparse(requestHandler.path).query)
    userId = query_components["userid"][0]
    requestHandler.wfile.write(json.dumps(hack.getFriends(userId)))
    return