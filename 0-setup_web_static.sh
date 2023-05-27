#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static. It must:

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p  /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo touch /var/www/html/404.html
echo "Ceci n'est pas une page" > /var/www/html/404
content='<!DOCTYPE html>
<html lang="en">
        <head>
                <title>Fake website</title>
        </head>
        <body>Just testing</body>
</html>'
echo "$content" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

config="server {
        listen 80 default_server;
        listen [::]:80 default_server;
	root /var/www/html;
	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	add_header X-Served-By $HOSTNAME;

	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
			rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
        location /hbnb_static {
                alias /data/web_static/current;
        }
	error_page 404 /404.html;
	location = /404.html{
		internal;
	}
}"

echo -e "$config" > /etc/nginx/sites-enabled/default
sudo service nginx restart
