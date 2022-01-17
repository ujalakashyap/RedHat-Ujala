Objective: Download files from Google Drive

Used google API to download the file

Authentication:
Every request your application sends to the Drive API must include an authorization token. The token also identifies your application to Google.

Your application must use OAuth 2.0 to authorize requests. No other authorization protocols are supported.

Step 1. Enable Google Drive API service
	-Log in to your Google Cloud Platform,
	-Select your project
	-Enable Google Drive API service

Step 2. Install Python Library
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Step 3: Setup OAuth Client Account and download client_secret.json. Refer the link to create and download
https://developers.google.com/adwords/api/docs/guides/authentication

File Explantion:
Google.py---> Validates the client-secert.json file and generated the .pickle file
which will be used for Authentication purspose

This .pickle file created when we run code for the first time and ask for Project Authenication

function.py----> 1) consit of function that will download the file from google drive
				 2) cosnsit of fucntion for testing the file download code

				
test.py---->1) uses unitclass library
			2) consist of the all automated test cases in the mentioned in the file TestCaseDocument.xlsx
			3) To run the test simply go to cmd and location and type py test.py and enter

var.py-----> Consist of all the variables used in the project

TestCaseDocument.xlsx ---> Collection of test cases

RandomFile---> folder where file will be downloaded

