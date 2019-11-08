import json
import sys
import os
import getpass

dirname = os.path.dirname(os.path.realpath(__file__))

with open(dirname + '/projects.json') as f:
	data = json.load(f)
	os.system('git config --global credential.helper cache')

	for project in data['projects']:
		project_path = dirname + '/' + project['folder'] + '/' + project['name']
		if not os.path.exists(project_path):
			os.makedirs(project_path)
			os.system('git clone https://' + data['host'] + '/' + data['username'] + '/' + project['name'] + '.git' + ' ' + project['folder'] + '/' + project['name'])
			print()