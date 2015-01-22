import os

from qubell.api.testing import *

@environment({
    "default": {},
#    "AmazonEC2_Amazon_Linux": {
#        "policies": [{
#            "action": "provisionVms",
#            "parameter": "imageId",
#            "value": "us-east-1/ami-1ba18d72"
#        }, {
#            "action": "provisionVms",
#            "parameter": "vmIdentity",
#            "value": "ec2-user"
#        }]
#    },
    "AmazonEC2_CentOS_65": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-ee698586"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    }
})
class OracleWeblogicTestCase(BaseComponentTestCase):
    name = "component-oracle-weblogic"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]

    @instance(byApplication=name)
    @values({"output.wl-hosts": "hosts", "output.wl-port": "port"})
    def test_port(self, instance, hosts, port):
        import socket

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hosts, int(port)))

        assert result == 0
