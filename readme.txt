# mycontacts
Python program (mac OS) to add contact details, show contact details to/from a YAML file and display complete contact list

setup:
python setup.py install

goto: (from installed path)
cd build/lib/mycontacts
ls -ltr mycontacts.py

USAGE :

Help :
python mycontacts.py -h
python mycontacts.py --help

Version :
python mycontacts.py --version

Add Contact Details :
python mycontacts.py -N <enter name> -E <enter email id> -M <enter mobile number>
e.g.:
mycontacts.py -N Sambit -E sambit@gmail.com -M 9988765342

Show Contact Details :
python mycontacts.py -S <enter name>
e.g.:
python mycontacts.py -S Sambit

Display complete contact list :
python mycontacts.py -L all

