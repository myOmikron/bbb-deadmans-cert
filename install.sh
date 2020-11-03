#!/bin/bash

adduser bbb-deadmans-cert
apt install python3 python3-pip
python3 -m pip install -r requirements.txt

cp bbb-deadmans-cert.service /usr/lib/systemd/system/
ln -s /usr/lib/systemd/system/bbb-deadmans-cert.service /etc/systemd/system/multi-user.target.wants/
systemctl daemon-reload
systemctl enable bbb-deadmans-cert

cp -r bbb_deadmans_cert /home/bbbb-deadmans-cert/
chown -R bbb-deadmans-cert:bbb-deadmans-cert /home/bbb-deadmans-cert/bbb_deadmans_cert

cp bbb-deadmans-cert.nginx /etc/bigbluebutton/nginx/
systemctl reload nginx
