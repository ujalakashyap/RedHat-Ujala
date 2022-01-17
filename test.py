import unittest
import os
import var
from function import test_file_download

class TestFileDownload(unittest.TestCase):

	def test_single_file_download(self):
		res = test_file_download(1, 'Validate Single File Download from google drive at given location', var.single_file_id, var.single_file_name, var.download_location)
		path = os.path.join (var.download_location, var.single_file_name[0])
		if res == True:
			result = os.path.isfile(path)
		else:
			result = False	
		self.assertTrue(result, True) 

	def test_multiple_file_download(self):
		res = test_file_download(2, 'Validate Multiple Files Download from google drive at given location', var.file_ids, var.file_names, var.download_location)
		path = os.path.join (var.download_location, var.file_names[0])
		if res == True:
			result = os.path.isfile(path)
		else:
			result = False	
		self.assertTrue(result, True) 

	def test_multiple_file_types_download(self):
		res = test_file_download(3, 'Validate Different Type of files download from google drive at given location', var.differnt_file_type_ids, var.differnt_file_type_names, var.download_location)
		path = os.path.join (var.download_location, var.differnt_file_type_names[0])
		if res == True:
			result = os.path.isfile(path)
		else:
			result = False	
		self.assertTrue(result, True) 

	def test_download_location_not_provided(self):
		result = test_file_download(4, 'Validate if given location is not given', var.file_ids, var.file_names, '')
		self.assertFalse(result, True)	

	def test_file_ids_not_provided(self):
		file_id = []
		result = test_file_download(5, 'Validate if file id to download file is not given', file_id, var.file_names, var.download_location)
		self.assertFalse(result, True)    

	def test_file_names_not_provided(self):
		file_name = []
		result= test_file_download(6, 'Validate if file name is not provided', var.file_ids, file_name, var.download_location)
		self.assertFalse(result, True)   

	def test_invalid_file_id(self):
		result = test_file_download (7, 'Validate if file id is invalid','abcccc','abc.txt',var.download_location)
		self.assertFalse(result, False)

	def test_download_non_binary_file(self):
		result = test_file_download(8, 'Validate downloading of non binary file',var.not_binary_content_file_id,'abc.txt',var.download_location)
		self.assertFalse(result, False)	

	def test_large_file_size_download(self):
		result = test_file_download(9, 'Validate large file download',var.large_file_size_id,var.large_file_name,var.download_location)
		self.assertTrue(result, True)

	def test_large_file_id_from_other_google_account(self):
		result = test_file_download(10, 'Validate file id is from another google account',var.other_google_account_file_id,var.other_google_account_file_name,var.download_location)
		print (result)
		self.assertFalse(result, False)	

	def  test_folder_download(self):
		result = test_file_download (11, 'Validate folder download', var.folder_file_id,var.folder_name,var.download_location)
		self.assertFalse(result, False)

	def test_file_id_from_another_google_account(self):
		result = test_file_download(12,'Validate file id from another google account',var.test_id,var.test_name, var.download_location)
		self.assertTrue(result, True)

	def test_file_is_downloaded_with_given_extension(self):
		res = test_file_download(13,'Validate file is downloaded has extension which was given',var.file_id_another_extension,var.file_name_another_extension, var.download_location)
		path = os.path.join (var.download_location, var.file_name_another_extension[0])
		if res == True:
			result = os.path.isfile(path)
		else:
			result = False	
		self.assertTrue(result, True)	

if __name__ == '__main__':
    unittest.main()