from OSC import OSCClient, OSCMessage
import sys
import plistlib

channel = sys.argv[1]
channel = '%02d' % (int(channel))
name_string = sys.argv[2]

path_l = len(sys.argv[0])-11
path = sys.argv[0][:path_l] + 'br-x32.plist'

pl = plistlib.readPlist(path)
ip = pl['IP address']

address = '/ch/' + channel + '/config/name'

client = OSCClient()
client.connect( (ip, 10023) )

oscmsg = OSCMessage()
oscmsg.setAddress(address)
oscmsg.append(name_string)

client.send(oscmsg)