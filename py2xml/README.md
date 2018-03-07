Generate XML of python file. For example:

**scr_pyfile:**

```
# ACSEmulator.py, only find the class as filename.

class ACSEmulator(object):
    '''
    Test class comments.
    '''
    def __init__(self):
        '''
        Comments in the function start with "_" will be ignored.
        '''
        self.host_packet_dict = {}
        self.host_packetthread_dict = {}
        self.host_log_dict = {}
        self.host_acsthread_dict = {}
        self.set_result_path()
        self.interface = Interface()
        self.packet = Packet()
        self.acsstatus = _ACSStatus()
        self.cpeinfo = _CPEInfo()

    def set_result_path(self, path = "Files"):
        '''
        Set path to save result such as logs and packets.
        '''
        self.files_path = path + "/"
        result_path = path + "/TestResult"
        self.packet_path = result_path + "/packet"
        self.log_path = result_path + "/log"

        if os.path.exists(self.packet_path) != True:
            os.makedirs(self.packet_path)

        if os.path.exists(self.log_path) != True:
            os.makedirs(self.log_path)

        return True

    def set_CPE_info(self, ip, username = "RMS", password = "RMS", connection_port = 7547):
        '''
        Set CPE info for connection request.

        : param ip        : IP address of CPE.
        : param username  : Used for CPE authentication.
        : param password  : Used for CPE authentication.
        : param connection_port : CPE connection request port.
        '''
        self.cpeinfo.set_account(ip, username, password)
        self.cpeinfo.set_connection_port(ip, connection_port)
```

**output_xml:**

```
<?xml version='1.0' encoding='UTF-8'?>
<?xml-stylesheet type='text/xsl' href='modules.xsl'?>
<modules>
  <library path="ACSEmulator.py">
    <class name="ACSEmulator">
      <comment><![CDATA[Test class comments.]]></comment>
      <comment><![CDATA[Comments in the function start with "_" will be ignored.]]></comment>
      <def name="set_result_path(path = &quot;Files&quot;)">
        <comment><![CDATA[Set path to save result such as logs and packets.]]></comment>
        <return>True</return>
      </def>
      <def name="set_CPE_info(ip, username = &quot;RMS&quot;, password = &quot;RMS&quot;, connection_port = 7547)">
        <comment><![CDATA[Set CPE info for connection request.<br /><br />: param ip        : IP address of CPE.<br />: param username  : Used for CPE authentication.<br />: param password  : Used for CPE authentication.<br />: param connection_port : CPE connection request port.]]></comment>
      </def>
    </class>
  </library>
</modules>
```

**View by browser:**
![Alt text](https://raw.githubusercontent.com/getpoint/tools/master/py2xml/doc/modules.PNG)
