#!/usr/local/bin/python

import os
import sys
import shutil
import re
import glob

currentDir = os.getcwd()
#prompt - what do you want to do?  (Delete site (incl db), delete db)

target = {}

#get info from settings
f = open(currentDir + "/settings.php","r")
settingsAsString = f.read()

#slog through the settings.php file line by line
for line in settingsAsString.split("\n"):
  #find db info in settings file
  #db user
  u = re.compile("(\s*['\"]username['\"]\s=>\s['\"])(\w*)")
  m = u.match(line)
  if m:
    target['dbUser'] = m.group(2)

  #db pass
  p = re.compile("(\s*['\"]password['\"]\s=>\s['\"])(\w*)")
  m = p.match(line)
  if m:
    target['dbPass'] = m.group(2)

  #db host
  h = re.compile("(\s*['\"]host['\"]\s=>\s['\"])(\S*)(['\"])")
  m = h.match(line)
  if m:
    target['dbHost'] = m.group(2)

  #db name
  db = re.compile("(\s*['\"]database['\"]\s=>\s['\"])(\w*)")
  m = db.match(line)
  if m:
    target['dbName'] = m.group(2)

  # does this have a solr instance?
  #s = re.compile("([\S\s]*['solr']['url']\s=\s')(\S*)(')")
  #m = s.match(line)
  #if m:
  #  print m.group(2)
  #  target['host'] = m.group(2)

#get apache conf using the current dir
confFiles = glob.glob("/etc/httpd/sites/*.conf")
for name in confFiles:
  f = open(name,"r")
  confAsString = f.read()
  for line in confAsString.split("\n"):
    a = re.compile("(\s*DocumentRoot\s)([\s\S]*)")
    m = a.match(line)
    if m:
      if m.group(2) == currentDir + "/drupal-webroot":
        target['apache'] = name

print target

gogogo = raw_input("This is not the site you're looking for. *waves hand*  (Do you REALLY want to get rid of " + currentDir + " [y/n]?)\n")
if gogogo not in ["y","n"]:
  gogogo = raw_input("Try again (y/n)")
  if gogogo not in ["y","n"]:
    print "Alright, you had your chance."
    sys.exit()
if gogogo == "n":
  sys.exit()
elif gogogo == "y":
  # Now go and thrash the site
  print "This isn't the site you're looking for."


#log in to appropriate mysql box and drop the database
#print "Getting rid of " + target['dbName'] + ".  Who needs it anyway?"
os.system("mysql -u" + target['dbUser'] + " -p" + target['dbPass'] + " --host=" + target['dbHost'] + " -e \"DROP DATABASE IF EXISTS " + target['dbName'] + "\"")

#delete apache conf
try:
  if os.path.isfile(target['apache']):
    #print "Getting rid of " + target['apache'] + ".  Who needs it anyway?"
    os.remove(target['apache'])
    #restart apache
    os.system("/etc/init.d/httpd restart")
except KeyError:
  print "We don't need to see his apache conf."


#delete the solr instance

#remove the site directory
shutil.rmtree(currentDir)
os.chdir("../")

print "This isn't the site we're looking for. Move along.  Move along."
