# Copy ipupdater.py to /usr/local/bin/
mkdir /usr/local/bin/ipupdater
cp -f ipupdater.py /usr/local/bin/ipupdater/
chmod 755 /usr/local/bin/ipupdater/ipupdater.py

# Copy ipupdater shell script to /etc/init.d/
cp -f ipupdater /etc/init.d/
chmod 755 /etc/init.d/ipupdater

# Configure auto start on boot
update-rc.d ipupdater defaults
