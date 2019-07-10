import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_selinux(host):
    cmd = host.run("getenforce")

    assert 0 == cmd.rc
    assert "Disabled" == cmd.stdout.strip()
