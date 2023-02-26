[Unit]
Description=Aria2
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/aria2c --conf-path=/etc/aria2/aria2.conf
ExecStop=/bin/kill -s STOP \$MAINPID
ExecReload=/bin/kill -s HUP \$MAINPID

[Install]
WantedBy=multi-user.target