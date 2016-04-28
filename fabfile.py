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

# check the environment and running the corresponding deploy function
def deploy():
    """ deploy function """
    if env.environment not in ("local", "test"):
        print( red('Please specify a correct environment from ("local", "test") and running command such as `fab local deploy`.') )
    else:
        # exec the specify environment install function 
        globals()["deploy_{0}_environment".format(env.environment)]()


def deploy_local_environment():
    run('ls -al')

def deploy_test_environment():
    print('local install')


def sync_code():
    """ sync your code """
    if env.environment not in ("local", "test"):
        print( red('Please specify a correct environment from ("local", "test") and running command such as `fab local sync_code`.') )
    else:
        # exec the specify environment install function 
        globals()["sync_{0}_code".format(env.environment)]()


def sync_local_code():
    print('sync local code')