import sys, os
class PersistDict(dict):
  def __init__(self,filename):
    dict.__init__(self):
    self.filename = os.path.abspath(filename)
    if 
  
