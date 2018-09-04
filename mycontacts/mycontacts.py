import argparse
import yaml
import re


def yaml_loader(filepath):
	with open(filepath, "r") as file_descriptor:
		data = yaml.load(file_descriptor)
	return data

def yaml_dump(filepath, data):
	with open(filepath, 'r') as file_descriptor:
		 dt=yaml.safe_load(file_descriptor)
	if dt:
	    with open(filepath, "w") as write:
		      z=dt.copy()
		      z.update(data)
		      yaml.safe_dump(z, write)


def Main():
	parser = argparse.ArgumentParser(description="Contact Details")
	parser.add_argument("-E", "--email", type=str, metavar='', help='Add email along with Name')
	parser.add_argument("-M", "--mobile", type=int, metavar='', help='Add Mobile Number along with Name')
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-N', '--name', help='Add Name in Contact List')
	group.add_argument('-S', '--show', help='Show Contact Details of a Single Person')
	group.add_argument('-L', '--list', help='Show the Entire List of Contacts')
	group.add_argument('-V','--version', action='version', version='%(prog)s 1.0')

	args = parser.parse_args()

	filepath = "./data/test.yaml"
	data = yaml_loader(filepath)

	entry = data.get(args.show)
#Code to Search details of a particular contact
	if (args.show):
		for item_name, item_value in entry.iteritems():
			print item_name, item_value

#Code to Display the Contact List
	if args.list=="all":
		print yaml.safe_dump(data)


#Code to Add Name, Email and Mobile#
	if args.name:
		print "Name is : %s\nEmail is : %s\nMobile Number is : %s" % (args.name, args.email, args.mobile)
		if (len(str(args.mobile))!=10):
			print "Enter a valid 10 digit mobile number"
			exit(1)
		elif (not args.name.isalpha()):
			print "Enter a valid name"
			exit(1)
		elif (not re.search(r'[\w\.-]+@[\w\.-]+', args.email)):
			print "Enter a valid email id"
			exit(1)
		else:
			print"** Contact List Updated **"
			data={
			"%s"%(args.name):{
                  "Name":"%s"%(args.name),
                  "Email":"%s"%(args.email),
                  "Mobile_Number":"%s"%(args.mobile)
	        }
	}
	yaml_dump(filepath,data)


if __name__ == "__main__":
	Main()
