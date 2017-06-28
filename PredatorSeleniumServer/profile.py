def returnAdami(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type','text/html')
    requestHandler.end_headers()
    # Send the html message
    requestHandler.wfile.write("Adami")
    return