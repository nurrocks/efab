from fabric.api import env, run, prompt, local, get, sudo, put
from fabric.colors import red, green
from fabric.state import output
from fabric.contrib.files import exists


key_file = '~/.ssh/zocvpc.pem'

def test():
    env.environment = "test"
    env.hosts = ['52.5.144.54']
    env.user = 'ubuntu'
    env.key_filename = key_file

def onedot():
    env.environment = "onedot"
    env.hosts = ['ec2-52-20-210-122.compute-1.amazonaws.com']
    env.user = 'ubuntu'
    env.key_filename = key_file

def live():
    env.environment = "live"
    env.hosts = ['54.208.83.166', '52.90.50.45']
    env.user = 'ubuntu'
    env.key_filename = key_file


def update():
    run('cd /var/www/html && git pull')