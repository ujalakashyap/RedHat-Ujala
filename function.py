import os
import io 
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
import urllib.request
from urllib.error import HTTPError
import var

CLIENT_SECRET_FILE = var.CLIENT_SECRET_FILE
API_NAME = var.API_NAME
API_VERSION = var.API_VERSION
SCOPES  = var.SCOPES 


def FileDownload (file_ids, file_names,download_location):
	file_path_res = os.path .exists(download_location.strip())
	if file_path_res == False:
		print ("Download Folder Location is Not Present")
		return False
	if len(file_ids) == 0:	
		return False
	if  len(file_names) == 0:
		return False		
	service = Create_Service (CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
	for file_id, file_name in zip (file_ids, file_names):

		request = service.files().get_media(fileId=file_id)
		fh = io.BytesIO()
		downloader = MediaIoBaseDownload(fh,request)
		done = False

		while not done:
			try:
				status, done = downloader.next_chunk()
				print ("Download Progess {0}". format(status.progress()*100))
				fh.seek(0)	
				with open(os.path.join (download_location, file_name), 'wb') as f:
					f.write(fh.read())
					f.close()
				return True	
			except Exception as e:
				print('File Not Found.')
				print(e)
				return False			
		

			
def test_file_download (test_case_number, test_name,file_ids, file_names,download_location):
	print ('********************************')
	print ("Test Number:", test_case_number, "|","Test Name:", test_name)
	print ('********************************')
	res= FileDownload(file_ids, file_names,download_location)
	if res == True :
		print ("Test Number:", test_case_number, "|","Test Name:", test_name, ": COMPLETED")
		return True
	else:
		print ("Test Number:", test_case_number, "|","Test Name:", test_name, ":  COMPLETED")
		return False

	print ('********************************')
	print ("Test-",test_case_number, 'Test Completed' )
	print ('********************************')	