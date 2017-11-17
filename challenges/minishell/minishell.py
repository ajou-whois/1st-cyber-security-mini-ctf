#!/usr/bin/python

import sys,os,md5

def md5_enc(data):
	return md5.md5(data).hexdigest()

def main():

	os.chdir("/home/minishell/account")

	account_dir = os.listdir(".")
	names = []

	for i in account_dir:
		if len(i)!=32:
			account_dir.remove(i)

	for i in account_dir:
		path = i + "/name"
		f = open(path,"rb")
		names.append(f.read())
		f.close()

	sys.stdout.write("name : ")
	sys.stdout.flush()
	name = raw_input()


	for i in range(len(names)):
		if names[i] == name:
			print "already exist"
			sys.stdout.flush()
			return


	p = md5_enc(name)
	try:
		os.mkdir(p)
		os.chdir(p)
	except:
		print "error occurred"
		sys.stdout.flush()

	f2 = open("./name","wb")
	f2.write(name)
	f2.close()

	c = ""
	while c!="exit":
		sys.stdout.write("$ ")
		sys.stdout.flush()
		c = raw_input()
		if c == "ls":
			os.system("ls")
			sys.stdout.flush()
		elif c.find("cat ")>-1:
			n = c.split(" ")
			try:
				filename = n[1].replace('.','')
				sys.stdout.write(open(filename,"rb").read())
			except:
				print "error occurred"
			sys.stdout.flush()
		elif c == "id":
			os.system("id")
			sys.stdout.flush()
		elif c == "?":
			print "You have to find the FLAG that somewhere to be"
			sys.stdout.flush()


main()
