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
    stats = json.dumps(hack.getFriendsStatistics(userId))
    requestHandler.wfile.write(stats)
    return

def getPersonal(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type','text/html')
    requestHandler.end_headers()
    # Send the html message
    query_components = parse_qs(urlparse(requestHandler.path).query)
    userId = query_components["userid"][0]
    stats = json.dumps(hack.getPersonalData(userId))
    requestHandler.wfile.write(stats)
    return

def getImageData(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type','text/html')
    requestHandler.end_headers()
    # Send the html message
    query_components = parse_qs(urlparse(requestHandler.path).query)
    userId = query_components["userid"][0]
    stats = json.dumps({"netDuplicates": hack.getProfilePicSites(userId)})
    requestHandler.wfile.write(stats)
    return