import os

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import environment, instance, workflow, values

@environment({
    "default": {},
    "AmazonEC2_Amazon_Linux": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-1ba18d72"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ec2-user"
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
    def test_port(self, instance):
        import socket
        host = instance.returnValues['weblogic.wl-hosts']
        port = instance.returnValues['weblogic.wl-admin-port']       
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, int(port)))

        assert result == 0
