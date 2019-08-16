import subprocess

import pytest


@pytest.mark.run(order=1)
def test_can_install():
    subprocess.run('jupyter nbextension install --py jupytemplate --sys-prefix').check_returncode()


@pytest.mark.run(order=2)
def test_can_enable():
    subprocess.run('jupyter nbextension enable jupytemplate/main --sys-prefix').check_returncode()


@pytest.mark.run(order=3)
def test_can_disable():
    subprocess.run('jupyter nbextension disable jupytemplate/main --sys-prefix').check_returncode()


@pytest.mark.run(order=4)
def test_can_uninstall():
    subprocess.run('jupyter nbextension uninstall --py jupytemplate --sys-prefix').check_returncode()
