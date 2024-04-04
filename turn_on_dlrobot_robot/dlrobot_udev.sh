echo  'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60",ATTRS{serial}=="0002", MODE:="0777", GROUP:="dialout", SYMLINK+="dlrobot_controller"' >/etc/udev/rules.d/dlrobot_controller.rules
echo  'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60",ATTRS{serial}=="0001", MODE:="0777", GROUP:="dialout", SYMLINK+="dlrobot_laser"' >/etc/udev/rules.d/rplidar_laser.rules
echo  'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60",ATTRS{serial}=="0003", MODE:="0777", GROUP:="dialout", SYMLINK+="dlrobot_laser"' >/etc/udev/rules.d/ld14.rules
echo  'KERNEL=="ttyCH343USB*", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d4",ATTRS{serial}=="0002", MODE:="0777", GROUP:="dialout", SYMLINK+="dlrobot_controller"' >/etc/udev/rules.d/dlrobot_dlrobot.rules

service udev reload
sleep 2
service udev restart


