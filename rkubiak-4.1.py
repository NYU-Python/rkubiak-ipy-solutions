Import datetime
Import sys
Import os

class Logger(object):
	Def __init__(self, filename, priority='DEBUG',datetime=True, scriptname=True)
	  priorities = {
	  'DEBUG': 1,
	  'INFO': 2,
	  'WARNING': 3,
	  'ERROR': 4,
	  'CRITICAL': 5
	  }

#open file, raise error if any
  try: 
  		Fh = open(filename, ‘a’)
  		Self.fh = fh
  except IOError, e:
  		Raise IOError(“config file cant be opened: {}”.format(e))

#adjust priority based on integer assigned by dictionary, raise error if priority is missing
  try: 
  		Priority_adj = int(priorities(priority))
  		Self.priority_adj = priority_adj
  except KeyError:
  		Raise KeyError(“{} is not a valid priority”)
#Prepend datetime if needed, raise error if date not a bool
  try: 
  		If datetime:
  			Self.datetime_adj = time.ctime()
  		else:
  			Self.datetime_adj = ‘’
  except NameError:
  		Raise NameError(“{} datetime is not bool. Insert bool flag”.format(datetime))



#provide scriptname if needed: raise error if flag not a bool
  try: 
  		If scriptname:
  			Self. scriptname_adj = filename
  		Else:
  			Self. scriptname _adj = ‘’
  except NameError:
  		Raise NameError(“{} scriptname is not bool. Insert bool flag”.format(scriptname))

# provide methods for all log scenatios
  Def debug(self, msg):
  	Self.write_log(msg, 1)
  Def info(self, msg):
  	Self.write_log(msg, 2)
  Def warning(self, msg):
  	Self.write_log(msg, 3)
  Def error(self, msg):
  	Self.write_log(msg, 4)
  Def critical(self, msg):
  	Self.write_log(msg, 5)

#log entry
  def write_log(self, mesg, level):
# change datetime and scriptname to string
	head = ‘’
	if  self.priority_adj >= level:
		self.handle.write(‘{0} {1} \n’.format(self.prepend_func(), msg)) 
## prepend datetime and scriptname
  def prepend_func(self):
  	self.prepend = ‘’
  	if self.datetime:
  		self.prepend = time .ctime() + ‘ ‘
  	if self.scriptname:
  		self.prepend = self.prepend + os.path.basename(sys.argv(o))
  	return self.prepend
#4.1a  	
class Config():
	def __init__(self, filename, overwrite_keys = True):
		try:
			fh = open(filenmae)
		except IOError:
			print 'IOError, file cant be opened'
		self.overwrite = overwrite_keys
		self.fh = fh
		list_fh = self.fh.read().splitlines()
		mylist = []
		self.dict = {}
		for i in list_fh:
			i = i.split('=', 1)
			mylist.append(i)
		self.fh = open(filename, 'w')
	def get(self, field):
		try:
			myfield = self.dict[field]
		except KeyError:
			print 'KeyError. There is no data for this entry'
		return myfield
	def set (self, mykey, myval):
		if mykey in self.dict.keys() and not self.overwrite:
			print 'ValueError. data alreasy in file'
		else:
			
			
		
