KasiChat
========

Dropbox chat app example.


Requirements:
-------------

You will need the following things properly installed on your computer.

- [python3](https://www.python.org/downloads/>)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/>)

Getting Started
---------------

1. Clone the repo:

	```
	$ git clone https://github.com/Ntu2koTrevor/kasichat.git
	$ cd kasichat
	```

2. Setup the VirtualEnv
	```
	$ virtualenv ve
	$ source ve/bin/activate
	```

3. Install requirements
	```
	$ pip install dropbox
	```

Setup the Dropbox App
----------------------

- To create a Dropbox App, Login to your Dropbox account and follow this [steps](https://www.dropbox.com/developers/apps/create).
- Go to https://www.dropbox.com/h
- Create a folder called KasiChat and a file called chat.txt inside the KasiChat folder

Execution
---------

	```
	$ python chat.py register <username>
	$ python chat.py start <username>
	```
