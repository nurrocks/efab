from fabric.colors import red, green
from fabric.api import env, prompt, run, hosts

# global variable
env.environment = ''

# local server informations
def local():
    """ choose local environment """
    env.hosts = ['127.0.0.1:2222']
    env.user = 'vagrant'
    env.password = 'vagrant'
    env.environment = 'local'

# check the environment and running the corresponding function
def deploy():
    """ deploy function """
    if env.environment not in ("local", "test"):
        print( red('Please specify a correct environment from ("local", "test").') )
    else:
        # exec the specify environment install function 
        globals()["install_{0}_environment".format(env.environment)]()


def install_local_environment():
    run('ls -al')

def install_test_environment():
    print('local install')