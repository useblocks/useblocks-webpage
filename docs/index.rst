Welcome to useblocks webpage
============================

Welcome to the documentation of **useblocks webpage**.

Author is **team useblocks**, who can easily be contacted by writing an email
to info@useblocks.com.

To start the app, simply open a command line interface and type::

    useblocks_webpage

This will give you an overview about available commands.

Installation
------------

On the deployment Ubuntu server, run the following commands::

    cd  # go to home directory
    sudo apt install virtualenv  # python3.6 -m venv lacks activate_this.py for wsgi
    virtualenv -p python3.6 py36_venv_ub_webpage
    . /home/<user>/py36_venv_ub_webpage/bin/activate

    git clone https://github.com/useblocks/useblocks-webpage.git
    cd useblocks-webpage

Edit the file in location /home/<user>/useblocks_webpage/applications/configuration.py::

    FLASK_SERVER_NAME = os.getenv("FLASK_SERVER_NAME", "<server IP address>")  # productive

Edit the file in location /home/<user>/useblocks-webpage/useblocks_webpage/applications/useblocks_webpage_app.wsgi and
adapt the path of the file 'activate_this.py' to your venv::

    activate_this = '/home/<user>/py36_venv_ub_webpage/bin/activate_this.py'

Run the command::

    pip install -e .  # install the package to the venv

Prepare apache2::

    sudo apt install apache2
    sudo apt install libapache2-mod-wsgi-py3
    sudo a2enmod wsgi

Create a file in location /etc/apache2/sites-available/useblocks-webpage.conf with content::

    <VirtualHost *:80>
        ServerName <server IP address>

        WSGIDaemonProcess useblocks-webpage user=<user> group=<user> threads=5
        WSGIScriptAlias / /home/<user>/useblocks-webpage/useblocks_webpage/applications/useblocks_webpage_app.wsgi

        <Directory <checkout-location of the repo>>
            WSGIProcessGroup useblocks-webpage
            WSGIApplicationGroup %{GLOBAL}
            Require all granted
        </Directory>
    </VirtualHost>

Run::

    sudo a2ensite useblocks-webpage.conf
    sudo systemctl start apache2
    sudo systemctl reload apache2  # needed if you do any changes
