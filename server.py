import socket, json, random, datetime, hashlib, sys

def generate_response(request):
    # Start sample code using hashlib
    m = hashlib.sha256()
    m.update(b"Nobody inspects")
    m.digest()
    # End sample code using hashlib

    # Start code to deal with cookie
    # Extract any existing cookies from the request
    cookies = request.split('\r\n')[-1].split(': ')[-1].split('; ')

    # Check if there's an existing "user_id" cookie
    cookie_userId = [cookie for cookie in cookies if cookie.startswith('user_id=')]

    if cookie_userId:
        # If the "user_id" cookie already exists, retrieve its value
        user_id = cookie_userId[0].split('=')[1]
    else:
        # If the "user_id" cookie doesn't exist, generate a new random value
        user_id = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()[:8]

    # Set the "user_id" cookie in the response
    #response_cookie = f'Set-Cookie: user_id={user_id}; expires={datetime.datetime.now() + datetime.timedelta(days=1)}'
    response_cookie = f'Set-Cookie: user_id={user_id}; expires={datetime.datetime.now() + datetime.timedelta(days=1)}\r\nContent-Type: application/json'
    # End code to deal with cookie
    
    data = {
        "random_number": random.randint(1, 100),
        "current_datetime": str(datetime.datetime.now()),
        "hash value" : m.hexdigest(),
        "user_id": user_id
    }
    #return json.dumps(data)

    # Combine the response data and cookie header
    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(json.dumps(data))}\r\n{response_cookie}\r\n\r\n{json.dumps(data)}"
    
    return response

def handle_request(request):
    # This is a simple example; in a real-world scenario, you'd want to parse the request properly.
    response = generate_response(request)
    #return f"HTTP/1.1 200 OK\r\nContent-Length: {len(response)}\r\n\r\n{response}"
    return response

def start():
    # Create a socket and bind it to the specified port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding the host address and port to the server
    server_socket.bind(("localhost", port))
    # setting the maximum connections to queue before refusing requests
    server_socket.listen(1)

    # output to command line that the server is running
    print(f"Serving on port {port}")

    while True:
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()

        # Receive the client's request
        request = client_socket.recv(1024).decode("utf-8")

        # Handle the request and send the response
        response = handle_request(request)
        client_socket.sendall(response.encode("utf-8"))

        # Close the connection
        client_socket.close()

#take in args
ip = sys.argv[1]
port = int(sys.argv[2])
accFile = sys.argv[3]
sesTimeout = int(sys.argv[4])
rootDir = sys.argv[5]
start()
