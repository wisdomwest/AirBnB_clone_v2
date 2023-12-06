#!/usr/bin/env bash
#set up web server for deployment

#update and install nginx
apt-get update
apt-get install -y nginx
ufw allow 'Nginx HTTP'

#create dir in server
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>Hello World</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership to /data
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#configure nginx
host=$(hostname)
CONFIG=\
"server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    add_header X-Served-By \"$host\";
    
    location /hbnb_static {
	    alias /data/web_static/current;
	    index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error_404.html;

}"
bash -c "echo -e '$CONFIG' > /etc/nginx/sites-enabled/default"

service nginx restart
