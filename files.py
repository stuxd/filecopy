import os
import shutil
import re

src = 'c:/python/from'
dest = 'c:/python/to'
invoicelist = 'c:/python/invoices.txt'

def invoice_check(b):
	with open(invoicelist,'r') as file:
		for line in file:
			if b in line:
				return True

def name_check(name):
	na = re.findall(r'\d{6}',name)
	for b in na:
		if invoice_check(b):
			return True

for root, dirs, files in os.walk(src):
	for names in files:
		n = ''.join(root+"/"+names)
		if name_check(names):
			shutil.copy2(n,dest)
			print 'Copying:',names