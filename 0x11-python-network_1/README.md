# 0x11. Python - Network #1

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service


## Tasks

### 0. What's my status? #0

Write a Python script that fetches https://alx-intranet.hbtn.io/status

* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed like the following example (tabulation before -)
* You must use a with statement

File: <b>0-hbtn_status.py</b>


### 1. Response header value #0

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a with statement

File: <b>1-hbtn_header.py</b>


### 2. POST an email #0

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

* The email must be sent in the email variable
* You must use the packages urllib and sys
* You are not allowed to import packages other than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>2-post_email.py</b>


### 3. Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

* You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
* You must use the packages urllib and sys
* You are not allowed to import other packages than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>3-error_code.py</b>

