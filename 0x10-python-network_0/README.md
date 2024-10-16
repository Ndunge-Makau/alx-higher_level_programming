# 0x10. Python - Network #0

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)


## Tasks

### 0. cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

* The size must be displayed in bytes
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>0-body_size.sh</b>


### 1. cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>1-body.sh</b>


### 2. cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>2-delete.sh</b>


### 3. cURL only methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>3-methods.sh</b>


### 4. cURL headers

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

* A header variable X-School-User-Id must be sent with the value 98
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>4-header.sh</b>




