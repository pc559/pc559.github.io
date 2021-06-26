#!/usr/bin/env python

import requests
data = ['','']
data[0] = open('token.txt').read()
data[1] = open('group.txt').read()
results = open('results.txt','w')

class GroupScraper:
	def __init__(self,access_token, group_id):
		self.acc_tk = access_token
		self.grp_id = group_id
		self.url = "https://graph.facebook.com/%s/feed?access_token=%s" %(self.grp_id.strip('\n'),self.acc_tk.strip('\n'))
		self.data = []

	def scrape(self):
		downloaded_data  = requests.get(self.url).json()
		if 'error' in downloaded_data: 
			print downloaded_data['error']['message']
			return
		while True:
			for data in downloaded_data['data']:
				if 'message' in data:
					self.data.append(data['message'])
			if 'paging' in downloaded_data:
				if downloaded_data['paging']['next']:
					print '...downloading...'
					downloaded_data= requests.get(downloaded_data['paging']['next']).json()
			else:break	

thing = GroupScraper(data[0],data[1])
thing.scrape()
for i in thing.data:
	asc = i.encode('ascii','ignore')
	results.write(asc+'\n')

results.close()

