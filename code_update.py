from fabric.api import env, run, prompt, local, get, sudo, put
from fabric.colors import red, green
from fabric.state import output
from fabric.contrib.files import exists


key_file = '~/.ssh/zocvpc.pem'

def test():
    env.environment = "test"
    env.hosts = ['ip']
    env.user = 'ubuntu'
    env.key_filename = key_file

def onedot():
    env.environment = "onedot"
    env.hosts = ['ip']
    env.user = 'ubuntu'
    env.key_filename = key_file

def live():
    env.environment = "live"
    env.hosts = ['ip', 'ip']
    env.user = 'ubuntu'
    env.key_filename = key_file


def update():
    run('cd /var/www/html && git pull')