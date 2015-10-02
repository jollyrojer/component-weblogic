import os

from qubell.api.testing import *

@environment({
    "default": {}
})
class OracleTestCase(BaseComponentTestCase):
    name = "component-oracle-weblogic"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]
    @classmethod
    def timeout(cls):
        return 60

    @instance(byApplication=name)
    def test_port(self, instance):
        import socket
        host = instance.returnValues['weblogic.wl-host']
        port = instance.returnValues['weblogic.wl-admin-port']
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(host), int(port)))
        assert result == 0
