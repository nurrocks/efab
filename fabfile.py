from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists

# global variable
env.environment = ''

# local server informations
def local():
    """ choose local environment """
    env.hosts = ['127.0.0.1:2200']
    env.user = 'vagrant'
    env.password = 'vagrant'
    env.environment = 'local'

    # server config
    env.remote_web_folder = '/usr/share/nginx/html'
    env.remote_web_conf_available_folder = '/etc/nginx/sites-available'
    env.remote_web_conf_enable_folder = '/etc/nginx/sites-enabled'
    env.local_web_folder = '/var/www/html/efab'

# check the environment and running the corresponding deploy function
def setup():
    """ deploy function """
    if env.environment not in ("local", "test"):
        print( red('Please specify a correct environment from ("local", "test") and running command such as `fab local deploy`.') )
    else:
        # exec the specify environment install function 
        globals()["setup_{0}".format(env.environment)]()


def setup_local():
    # install github code
    if prompt( red('* Sync github repository.(y/n)?'), default='y' ) ==  'y':
        sync_github_code()
    print(green('* Done sync github repository. \n'))

    # install web server
    if prompt( red('* Deploy nginx web server.(y/n)?'), default='y' ) ==  'y':
        deploy_web_server()
    print(green('* Done deploy nginx web server. \n'))

def sync_github_code():
    # install git
    sudo('apt-get update -y')
    sudo('apt-get install git -y')

    # get github link
    github_link = prompt(green('Paste your github repository link: \n'))

    # create web folder
    if not exists('{0}'.format(env.remote_web_folder), use_sudo=True):
        sudo('mkdir -p {0}'.format(env.remote_web_folder))    
        
    # change folder permission and git clone code
    sudo('chmod -R 777 {0}'.format(env.remote_web_folder))
    run('cd {0} && git clone {1}'.format(env.remote_web_folder, github_link))

def deploy_web_server():
    sudo("apt-get update -y")

    # install mysql
    sudo('apt-get install mysql-server php5-mysql -y')
    sudo('mysql_install_db')
    sudo('/usr/bin/mysql_secure_installation')

    # install nginx
    sudo('apt-get install nginx -y')

    # move config 
    put('{0}/server.conf'.format(env.local_web_folder), '{0}'.format(env.remote_web_conf_available_folder),  use_sudo=True)
    sudo('rm -rf {0}/default'.format(env.remote_web_conf_enable_folder))
    sudo('ln -s {0}/server.conf {1}'.format(env.remote_web_conf_available_folder, env.remote_web_conf_enable_folder))

    # restart server
    sudo('service nginx stop')
    sudo('service nginx start')

    # install php
    sudo('apt-get install php5-fpm')

