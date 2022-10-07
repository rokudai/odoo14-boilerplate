# Quick install - Odoo 14 

# First step:

Copy the **.env.example** file and create an **.env** and set variables for your enviroment.

```
cp .env.example .env
```

# Usage

Start the container:
``` sh
docker-compose up
```

* Then open `localhost:8069` to access Odoo 14.0. If you want to start the server with a different port, change **8069** to another value in your enviroment file.

```
PORT_ODOO=
PORT_PGADMIN=
```
To view the database in PGadmin, remember to set the new server. To look at the database IP, you can run: 

```
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <nombre del contenedor>
```

Run Odoo container in detached mode (be able to close terminal without stopping Odoo):

```
docker-compose up -d
```

**If you get the permission issue**, change the folder permission to make sure that the container is able to access the directory:

``` sh
sudo chmod -R 774 addons
sudo chmod -R 774 etc
mkdir -p postgresql
sudo chmod -R 774 postgresql
```

Increase maximum number of files watching from 8192 (default) to **524288**. In order to avoid error when we run multiple Odoo instances. This is an *optional step*. These commands are for Ubuntu user:

```
$ if grep -qF "fs.inotify.max_user_watches" /etc/sysctl.conf; then echo $(grep -F "fs.inotify.max_user_watches" /etc/sysctl.conf); else echo "fs.inotify.max_user_watches = 524288" | sudo tee -a /etc/sysctl.conf; fi
$ sudo sysctl -p    # apply new config immediately
```

# Custom addons

The **addons/** folder contains custom addons. Just put your custom addons if you have any.

# Odoo configuration & log

* To change Odoo configuration, edit file: **etc/odoo.conf**.
* Log file: **etc/odoo-server.log**
* Default database password (**admin_passwd**) is `secret`

# Odoo container management

**Run Odoo**:

``` bash
docker-compose up -d
```

**Restart Odoo**:

``` bash
docker-compose restart
```

**Stop Odoo**:

``` bash
docker-compose down
```


# docker-compose.yml

* odoo:14.0
* postgres:13
