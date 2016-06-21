import os
import shutil
import re

src = 'c:/python/from'
dest = 'c:/python/to'
invoicelist = 'c:/python/invoices.txt'

def invoice_check(inv):
	with open(invoicelist,'r') as file:
		for line in file:
			if inv in line:
				return True

def file_split(name):
	split = re.findall(r'\d{6}',name)
	for a in split:
		if invoice_check(a):
			return True

for root, dirs, files in os.walk(src):
	for names in files:
		filepath = ''.join(root+"/"+names)
		if file_split(names):
			shutil.copy2(filepath,dest)
			print 'Copying:',names