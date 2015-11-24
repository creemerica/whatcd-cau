import os
import sys
import json
import requests
from subprocess import call

class Whatcd():
	def __init__(self, username, password, tracker='http://tracker.what.cd:34000/'):
		'''
		Create and upload torrents to What.cd

		username 	- your username for What.cd
		password 	- your password for What.cd
		tracker		- the What.cd tracker/announce URL incase it changes in the future
		'''

		self.username 	= username
		self.password 	= password
		self.tracker	= tracker
		self.session 	= requests.session()

		try:
			self.login()
		except ValueError as err:
			print err

	def login(self):
		'''
		Login the user using the provided username and password.

		Saves information for use later such as auth and passkeys for creating/uploading torrents.
		'''

		data = {
			'username'	: self.username,
			'password'	: self.password,
			'login'		: 'Login',
			'keeplogged': '1'
		}

		login 	= self.session.post('https://what.cd/login.php', data=data)
		index 	= self.session.get('https://what.cd/ajax.php?action=index')
		content = json.loads(index.content)
		check 	= content["status"]
		authkey = content["response"]["authkey"]
		passkey = content["response"]["passkey"]

		if check != 'success':
			raise ValueError('Error - An error occured while logging in')

		self.authkey 	= authkey
		self.passkey 	= passkey
		self.announce	= self.tracker + self.passkey + '/announce'

	def create(self, path, torrent_name, piece_size="18"):
		'''
		Creates a torrent file for use with What.cd and their private tracker. It requires you have mktorrent installed on your system.

		path 			- the path to the file/directory you are creating a torrent of
		torrent_name 	- the name of the torrent file you are creating
		piece_size 		- piece size should be between 18 and 24; defaults to 18.
		'''

		make = call(["mktorrent", "-p", "-l", piece_size, "-a", self.announce, "-o", torrent_name, path])

		if make != 0:
			raise ValueError('Error - An error occured while creating the torrent')

	def upload(self, title, tags, description, torrent, file_type=1):
		'''
		Uploads a torrent to What.cd.

		title 		- The title of your upload as it will appear in seach results on What.cd
		tags  		- Various tags you would like the torrent searchable by
		description - A description of the torrent
		torrent 	- Path to your torrent file you would like to upload.
		file_type 	- Sets the type of torrent you are uploading; defaults to 1 (application)

		Available file_types:

		0 - Music
		1 - Applications
		2 - E-Books
		3 - Audiobooks
		4 - E-Learning Videos
		5 - Comedy
		6 - Comics

		Not all file_types will work. For example, Music requires more fields to be submitted.
		Currently Applications (1), E-Books (2), E-Learning Videos (4), and Comics (6) will work.
		'''

		self.session.get('https://ssl.what.cd/upload.php')

		files = {
			'file_input': (torrent, open(torrent, 'rb'))
		}

		data = {
			'submit': 'true',
			'type'	: file_type,
			'title'	: title,
			'tags'	: tags,
			'desc'	: description,
			'auth'	: self.authkey
		}

		response = self.session.post('https://what.cd/upload.php', data=data, files=files)

		if 'torrents.php' not in response.url:
			raise ValueError('Error - Torrent not uploaded')

