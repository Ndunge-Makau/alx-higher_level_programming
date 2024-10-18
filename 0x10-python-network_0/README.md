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


### 5. cURL POST parameters

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

* A variable email must be sent with the value test@gmail.com
* A variable subject must be sent with the value I will always be here for PLD
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>5-post_params.sh</b>


### 6. Find a peak

Technical interview preparation:

* You are not allowed to google anything
* Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

* Prototype: def find_peak(list_of_integers):
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
* 6-peak.py must contain the function
* 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
* Note: there may be more than one peak in the list

File: <b>6-peak.py, 6-peak.txt</b>


### 7. Only status code

Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

* You are not allowed to use any pipe, redirection, etc.
* You are not allowed to use ; and &&
* You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>100-status_code.sh</b>


### 8. cURL a JSON file

Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

* Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
* You have to use curl
Please test your scripts in the sandbox provided, using the web server running on port 5000

File: <b>101-post_json.sh</b>


