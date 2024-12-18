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


### 4. What's my status? #1

Write a Python script that fetches https://alx-intranet.hbtn.io/status

* You must use the package requests
* You are not allow to import packages other than requests
* The body of the response must be display like the following example (tabulation before -)

File: <b>4-hbtn_status.py</b>


### 5. Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)

File: <b>5-hbtn_header.py</b>

                                                                                                                   
### 6. POST an email #1

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

* The email must be sent in the variable email
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to error check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>6-post_email.py</b>


### 7. Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

* If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000

File: <b>7-error_code.py


### 8. Search API

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

* The letter must be sent in the variable q
* If no argument is given, set q=""
* If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
* Otherwise:
	* Display Not a valid JSON if the JSON is invalid
	* Display No result if the JSON is empty
* You must use the package requests and sys
* You are not allowed to import packages other than requests and sys
Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

File: <b>8-json_api.py</b>


### 9. My GitHub!

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

* You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a personal access token as password)
* You must use the package requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)

File: <b>10-my_github.py</b>


### 10. Time for an interview!

The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.

* The first argument will be the repository name
* The second argument will be the owner name
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)
* Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.

File: <b>100-github_commits.py</b>
