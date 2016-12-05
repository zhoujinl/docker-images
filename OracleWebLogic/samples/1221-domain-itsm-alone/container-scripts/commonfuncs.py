import os
import socket
import random
import string

# Variables
# =========
# Environment Vars
hostname       = socket.gethostname()
# Admin Vars
admin_username = os.environ.get('ADMIN_USERNAME', 'weblogic')
admin_password = os.environ.get('ADMIN_PASSWORD') # this is read only once when creating domain (during docker image build)
admin_host     = os.environ.get('ADMIN_HOST', 'wlsadmin')
admin_port     = os.environ.get('ADMIN_PORT', '8001')
# Node Manager Vars
#nmname         = os.environ.get('NM_NAME', 'Machine-' + hostname)

# Functions
def editMode():
    edit()
    startEdit(waitTimeInMillis=-1, exclusive="true")

def saveActivate():
    save()
    activate(block="true")

def connectToAdmin():
    connect(url='t3://' + admin_host + ':' + admin_port, adminServerName='AdminServer')
    
def get_new_nmname():
  hostname       = socket.gethostname()
  if os.path.exists('/tmp/wls-machine-name.txt'):
    f = open('/tmp/wls-machine-name.txt')
    nmname = f.readline().strip('\n')
    if nmname:
      print nmname,
    f.close()
    return nmname
  else:
    random_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
    nmname = 'Machine-%s-%s' % (random_name, hostname)
    f=open('/tmp/wls-machine-name.txt','w')
    print >>f,nmname
    f.close()
    return nmname

nmname = get_new_nmname()
print 'get nmname :[%s]' % nmname