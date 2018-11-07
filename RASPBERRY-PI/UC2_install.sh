#!/bin/sh

#set -x

self="$(basename "$0")"
info="[UC2] ${self}:"
OS_USER="$USER"

if [ "${OS_USER}" = "root" ]; then
 OS_USER="${SUDO_USER}"
fi

echo "${info} Identified user is: ${OS_USER}" 

#General variables
USER_HOME_DIR="/home/${OS_USER}"
WORKING_DIR="${USER_HOME_DIR}/UC2"
BACKUP_DIR="${WORKING_DIR}/backups"
IMAGES_DIR="${WORKING_DIR}/images"
INSERTS_FILE="${WORKING_DIR}/inserts"
PPS_APP_URL="none"
PPS_APP_DIR="${USER_HOME_DIR}/Programming"
APPS_PATH="${USER_HOME_DIR}/.local/share/applications"
APPLAUNCHER_FILE="${USER_HOME_DIR}/.config/lxpanel/LXDE-pi/panels/panel"
AUTOSTART_FILE="${USER_HOME_DIR}/.config/lxsession/LXDE-pi/autostart"
#AUTORUN_FILE="${WORKING_DIR}/autorun.sh"
DIR_NICs="/sys/class/net/"
IP_INFO=$(curl -s ipinfo.io)

ICON_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/images/uc2_logo.ico'
STATUS_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/status'
FUNCLIB_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/funclib'
INSERTS_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/inserts'
KIVY_UP_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/bring_kivy_up.py'
ICON_URL='https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/RASPBERRY-PI/images/uc2_logo.ico'


# Create backup folder if not present
if [ ! -d $BACKUP_DIR ]; then mkdir -p ${BACKUP_DIR}; fi

# Create images folder if not present
if [ ! -d $IMAGES_DIR ]; then mkdir -p ${IMAGES_DIR}; fi

# Fetch status file if not present
target_file="${WORKING_DIR}/status"
if [ ! -f $target_file ]; then
 wget -N -q --no-check-certificate --content-disposition ${STATUS_URL}
fi

# Fetch inserts file if not present
target_file="${WORKING_DIR}/inserts"
if [ ! -f $target_file ]; then
 wget -N -q --no-check-certificate --content-disposition ${INSERTS_URL}
fi

# Fetch function library if not present
target_file="${WORKING_DIR}/funclib"
if [ ! -f $target_file ]; then
 wget -N -q --no-check-certificate --content-disposition ${FUNCLIB_URL}
fi

# Fetch bring_kivy_up.py if not present
target_file="${WORKING_DIR}/bring_kivy_up.py"
if [ ! -f $target_file ]; then
 wget -N -q --no-check-certificate --content-disposition ${KIVY_UP_URL}
 chmod a+x $target_file
fi

# Fetch icon file if not present
target_file="${IMAGES_DIR}/uc2_logo.ico"
if [ ! -f $target_file ]; then
 wget -N -q --no-check-certificate --content-disposition ${ICON_URL} -P $target_file
fi

# import function library
. ${WORKING_DIR}/funclib


# Declare additional functions
get_country(){
 IP_INFO=$(curl -s ipinfo.io)
 sleep 3s
 COUNTRY=${IP_INFO##*country}
 COUNTRY=${COUNTRY%%loc*}
 COUNTRY=$(echo $COUNTRY | sed "s/[^a-zA-Z]//g")
 COUNTRY=$(echo $COUNTRY | tr -d ' ')
}

update_state(){
 sed -i "1s/.*/state: $1/" "${WORKING_DIR}/status"
 current_state="$1"
}

add_to_autostart(){

local runfile="${WORKING_DIR}/run_install.sh"
if [ ! -f $runfile ]; then
 touch $runfile
else
 echo -n > $runfile
fi

cat > $runfile  << EOF
#!/bin/sh

lxterminal --command="sudo /bin/sh -c '${WORKING_DIR}/UC2_install.sh; /bin/bash'"
EOF

chmod a+x $runfile
 
check_is_present "run_install" $AUTOSTART_FILE
if [ ! $is_present ]; then
 make_backup $AUTOSTART_FILE "lxde"
 echo $runfile >> $AUTOSTART_FILE
 echo "${info} Adding installation file to ${AUTOSTART_FILE}"
else
 echo "${info} Installation autostart is active."
fi
}

remove_from_autostart(){
 echo "$info this is remove from autostart function doing nothing"
}

todo(){
 local diff=$(($current_state-$state))
 if [ $diff -lt 0 ]; then echo true; else echo false; fi
}

# get current installation progress
current_state=$(head -n 1 "${WORKING_DIR}/status")
current_state=${current_state##*:}
echo "${info} current_state: ${current_state}"

state="0"
#Check for most recently created new user
if $(todo); then

 echo "${info} Checking for most recently created new user..."
 target_file="/var/log/auth.log"
 search_string=': new user: name='
 check_is_present "$search_string" $target_file
 if [ $is_present ]; then
  newusername=$(tac $target_file | sed -n "/${search_string}/{p;q}")
  newusername=${newusername##*$search_string}
  newusername=${newusername%%, *}
  newusername=$(echo $newusername | tr -d ' ')
  echo "${info} Found user: ${newusername}"
  echo "${info} Preparing installation for ${newusername}..."
  usermod $newusername -a -G pi,adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,spi,i2c,gpio
  target_file="/etc/sudoers"
  make_backup $target_file "etc"
  check_is_present "${newusername} ALL=(ALL) NOPASSWD:ALL" $target_file
  if [ ! $is_present ]; then
   echo "${newusername} ALL=(ALL) NOPASSWD:ALL" | sudo EDITOR='tee -a' visudo >/dev/null
  fi
  target_file="/etc/lightdm/lightdm.conf"
  find_line_no 'autologin-user=pi' $target_file
  if [ $line_no -gt 0 ]; then
   sed -i "${line_no}s/.*/autologin-user=${newusername}/" $target_file
  fi

  target_file='/etc/systemd/system/autologin@.service'
  find_line_no 'ExecStart=-/sbin/agetty' $target_file
  if [ $line_no -gt 0 ]; then
   sed -i -e "${line_no}s/pi/${newusername}/g" $target_file
  fi

  source_file="${USER_HOME_DIR}/.config/lxsession/LXDE-pi/autostart"
  USER_HOME_DIR="/home/${newusername}"
  cp -r ${WORKING_DIR} $USER_HOME_DIR
  WORKING_DIR="${USER_HOME_DIR}/UC2"
  AUTOSTART_FILE="${USER_HOME_DIR}/.config/lxsession/LXDE-pi/autostart"
  AUTOSTART_DIR=$(dirname "${AUTOSTART_FILE}")
  mkdir -p $AUTOSTART_DIR
  chown -R $newusername $USER_HOME_DIR
  cp -r $source_file $AUTOSTART_FILE
 else
  echo "${info} No newly created user found. Proceeding with currently logged in user ${OS_USER} after reboot..."
 fi
 add_to_autostart
 update_state $state
 sleep 5s
 reboot
fi

state="1"
if $(todo); then
 sleep 5s
 datetime=$(date)
 echo "${info} Updating and upgrading installed packages."
 echo "START: ${datetime}" | sudo tee --append "${WORKING_DIR}/status" > /dev/null
 apt-get -y update
 apt-get -y dist-upgrade
 update_state $state
fi

#check python version
state="2"
if $(todo); then
 user=$(echo $SUDO_USER)
 target_version="2.7"
 python_version=$(python --version 2>&1)
 echo "${info} Checking default Python version."
 case $python_version in
  *"$target_version"*)  echo "${info} Python 2.7 is already default" ;;
  *)                    echo "${info} Changing default Python version to Python 2.7"
			make_backup "${WORKING_DIR}/.bashrc" "home"
                        echo "${info} alias python=\"/usr/bin/python\"" >> "/home/${OS_USER}/.bashrc" ;;
 esac
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#install Kivy dependencies
state="3"
if $(todo); then
 sleep 5s
 echo "${info} Installing Kivy dependencies."
 apt-get -y install libsdl2-dev
 apt-get -y install libsdl2-image-dev
 apt-get -y install libsdl2-mixer-dev
 apt-get -y install libsdl2-ttf-dev
 apt-get -y install pkg-config
 apt-get -y install libgl1-mesa-dev
 apt-get -y install libgles2-mesa-dev
 apt-get -y install python-setuptools
 apt-get -y install libgstreamer1.0-dev
 apt-get -y install git-core
 apt-get -y install gstreamer1.0-plugins-bad
 apt-get -y install gstreamer1.0-plugins-base
 apt-get -y install gstreamer1.0-plugins-good
 apt-get -y install gstreamer1.0-plugins-ugly
 apt-get -y install gstreamer1.0-omx
 apt-get -y install gstreamer1.0-alsa
 apt-get -y install python-dev
 apt-get -y install libmtdev-dev
 apt-get -y install xclip
 apt-get -y install xsel
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#install Cython
state="4"
if $(todo); then
 sleep 5s
 apt autoremove -y
 echo "${info} Updating and upgrading installed packages."
 apt-get -y update
 apt-get -y dist-upgrade
 echo "${info} Installing Cython... (approx. 30min on RaspberryPi 3B+)"
 pip install -U Cython==0.28.2
 echo "${info} Forcing pip, virtualenv and setuptools update in pip"
 pip install --upgrade pip
 pip install --upgrade virtualenv
 pip install --upgrade setuptools
 echo "${info} Installing pygments and docutils via pip (prior to Kivy)"
 #pip install -U pygments
 #pip install -U docutils
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#Preparation of Kivy installation
state="5"
if $(todo); then
 sleep 15s
 echo "${info} Updating /boot/config.txt (required by Kivy/SDL2)"
 boot_config="/boot/config.txt"
 make_backup $boot_config "boot"

 #Deleting prior existing entries
 search_and_delete 'dtparam=i2c_arm' $boot_config
 search_and_delete 'dtparam=audio' $boot_config
 search_and_delete 'start_x=' $boot_config
 search_and_delete 'gpu_mem=' $boot_config
 search_and_delete 'enable_uart=' $boot_config

 #Insert new configurations at bottom of file
 line_no=$(wc -l $boot_config | awk '{ print $1 }')
 insert_text $INSERTS_FILE 19 23 $boot_config $line_no
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#Installation of Kivy
state="6"
if $(todo); then
 echo "${info} Installing Kivy... (approx. 30min on RaspberryPi 3B+)"
 sleep 5s
 pip install Kivy==1.10.1
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#check kivy is correctly installed and callable for user
state="7"
if $(todo); then
 sleep 15s
 apt -y autoremove
 sudo -H -u "${OS_USER}" python "${WORKING_DIR}/bring_kivy_up.py"
 update_state $state
fi

state="8"
if $(todo); then
 echo "${info} Adding touchscreen provider to Kivy config-file"
 kivy_config="${USER_HOME_DIR}/.kivy/config.ini"
 make_backup $kivy_config "kivy"
 search_string="\[input\]"
 find_line_no "$search_string" $kivy_config
 strt=$next_line_no
 stop=$((next_line_no + 1))
 delete_text $strt $stop $kivy_config
 insert_text $INSERTS_FILE 14 16 $kivy_config $line_no
 update_state $state
fi

state="9"
if $(todo); then
 echo "${info} Fetching PPS-app specific dependencies from apt-get and pip..."
 apt-get -y install libffi-dev
 #python -m pip install cffi
 python -m pip install smbus-cffi
 python -m pip install unipath
 python -m pip install pyusb
 python -m pip install safe-cast
 python -m pip install ruamel.yaml
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

#install opencv
state="10"
if $(todo); then
 echo "${info} Installing OpenCV and its dependencies..."
 apt autoremove -y
 apt-get -y install libtiff5-dev
 apt-get -y install libjasper-dev
 apt-get -y install libpng12-dev
 apt-get -y install libjpeg-dev
 apt-get -y install libavcodec-dev
 apt-get -y install libavformat-dev
 apt-get -y install libswscale-dev
 apt-get -y install libv4l-dev
 apt-get -y install libgtk2.0-dev
 apt-get -y install libatlas-base-dev 
 apt-get -y install gfortran
 apt-get -y install libopencv-dev
 apt-get -y install python-opencv
 apt-get -y install python-picamera
 update_state $state
 echo "${info} Rebooting..."
 sleep 5s
 reboot
fi

state="11"
if $(todo); then
 sleep 10s
 echo "${info} Scanning for WiFi-interfaces..."
 interface="wlan"
 interface_state="down"

 for path in "${DIR_NICs}"*; do
  folder=$(basename "${path}")
  case "${folder}" in "${interface}"*) iface="${folder}" break;; *) iface="none";; esac
 done

 if [ "${iface}" = "none" ]; then
  echo "${info} No active physical interface with name \"${interface}*\" in ${DIR_NICs} found."
  echo "${info} Skipping virtual access point creation..."
  update_state $state
 else
  interface_state=$(cat "${DIR_NICs}/${iface}/operstate")
  interface_state=$(echo "${interface_state}"|tr '/a-z/' '/A-Z/')
  i=$(echo -n "${iface}" | tail -c 1)
  if $(todo); then
   echo "Found active physical interface ${iface}. Virtual access point will be created upon interface ${iface}."
  fi
  IFACE="${iface}"
  IFACE_IP=$(ip -o -f inet addr show "${IFACE}" | awk '/scope global/ {print $4}')
  MACADDR=$(cat "${DIR_NICs}/${IFACE}/address")
  #IFACE_CHANNEL=$(iwlist "${IFACE}" channel)
  #IFACE_CHANNEL=$(echo "${IFACE_CHANNEL#*\(}" | sed 's/[^0-9]*//g')
  NETMASK=$(echo "${IFACE_IP}" | tail -c 3)
  AP="ap${i}"
  AP_IP="192.168.50.1"
  AP_BROADCAST=${AP_IP%.*}

  echo "${info} Setting up virtual access point..."
  target_file="/etc/udev/rules.d/70-persistent-net.rules"

  if [ ! -f $target_file ]; then
   touch $target_file
   printf "ACTION==\"add\", SUBSYSTEM==\"ieee80211\", KERNEL=\"phy0\", \\ \n" >> $target_file
   printf "RUN+=\"/sbin/iw phy %%k interface add ${AP} type __ap\", \\ \n" >> $target_file
  fi

  mkdir -p /var/log/journal
  systemd-tmpfiles --create --prefix /var/log/journal
  apt -y install rng-tools
  apt -y install hostapd
  systemctl stop hostapd

  systemctl stop networking.service
  systemctl stop dhcpcd.service
  systemctl mask networking.service
  systemctl mask dhcpcd.service

  target_file="/etc/network/interfaces"
  make_backup $target_file "etc_net"
  mv $target_file "${target_file}~"

  target_file="/etc/resolvconf.conf"
  make_backup $target_file "etc"
  sed -i '1i resolvconf=NO' $target_file

  systemctl enable systemd-networkd.service
  systemctl enable systemd-resolved.service
  ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf

  target_file="/etc/systemd/network/08-${IFACE}.network"

cat > $target_file <<EOF
[Match]
Name=${IFACE}

[Network]
DHCP=ipv4
IPv6AcceptRA=no
LinkLocalAddressing=no
IPForward=yes
IPMasquerade=yes
DNS=8.8.8.8

[DHCP]
RouteMetric=20
UseDomains=yes
EOF

  target_file="/etc/systemd/network/12-${AP}.network"

cat > $target_file <<EOF
[Match]
Name=${AP}

[Network]
DHCPServer=yes
LinkLocalAddressing=no
#IPv6AcceptRA=no
IPForward=yes
IPMasquerade=yes

[Address]
Address=${AP_IP}/${NETMASK}
Broadcast=${AP_BROADCAST}.255

[DHCPServer]
PoolOffset=10
PoolSize=100
EmitDNS=yes
DNS=8.8.8.8
EOF

#  target_file="/etc/systemd/network/04-wired.network"
#
#cat > $target_file <<EOF
#[Match]
#Name=eth*
#
#[Network]
#DHCP=yes
#EOF

  cp -r /etc/wpa_supplicant/wpa_supplicant.conf "/etc/wpa_supplicant/wpa_supplicant-${IFACE}.conf"
  chmod 600 "/etc/wpa_supplicant/wpa_supplicant-${IFACE}.conf"
  systemctl disable wpa_supplicant.service
  systemctl enable "wpa_supplicant@${IFACE}.service"

  target_file="$APPLAUNCHER_FILE"

  #replace (future inactive) dhcpcd-icon with netstat-icon
  search_string="type=dhcpcdui"
  check_is_present $search_string $target_file
  if [ $is_present ]; then
   make_backup $target_file "lxde"
   find_line_no $search_string $target_file
   del_strt=$((line_no - 1))
   del_stop=$((line_no + 3))
   delete_text $del_strt $del_stop $target_file
   echo "${info} Removed \"Wireless & Wired Networks\" (dhcpcdui) icon from lxpanel."
   ins_strt=$((del_strt - 1))
   insert_text $INSERTS_FILE 7 11 $target_file $ins_strt
   echo "${info} Added \"Manage Networks\" (netstat) icon to lxpanel."
  else
   echo "${info} No \"Wireless & Wired Network\" (dhcpcdui) entry in lxpanel found"
  fi

  target_file="/etc/hostapd/hostapd.conf"
  rnd=$(shuf -i 0-100000 -n 1)
  AP_network="UC2_RaspberryPi_AP${rnd}"
  AP_pass="UCInsecurity2"
  get_country
  sleep 1s

cat > "/etc/hostapd/hostapd.conf" <<EOF
interface=${AP}
driver=nl80211
ssid=${AP_network}
country_code=${COUNTRY}
hw_mode=g
channel=1
auth_algs=1
wpa=2
wpa_passphrase=${AP_pass}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF

  chmod 600 /etc/hostapd/hostapd.conf
  sed -i 's/^#DAEMON_CONF=.*$/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/' /etc/default/hostapd
  sed -i 's/^\(# Should-Start:\s*$network\)$/#\1/' /etc/init.d/hostapd

  target_file="/etc/systemd/system/hostapd.service.d/override.conf"
  target_folder=$(dirname $target_file)
  mkdir -p ${target_folder}

cat > $target_file <<EOF
[Unit]
Wants=wpa_supplicant@${IFACE}.service
EOF

  target_file="/etc/systemd/system/wpa_supplicant@wlan0.service.d/override.conf"
  target_folder=$(dirname $target_file)
  mkdir -p ${target_folder}

cat > $target_file <<EOF
[Unit]
BindsTo=hostapd.service
After=hostapd.service

[Service]
ExecStartPost=/sbin/iptables -t nat -A POSTROUTING -o ${IFACE} -j MASQUERADE
ExecStopPost=-/sbin/iptables -t nat -D POSTROUTING -o ${IFACE} -j MASQUERADE
EOF

  update_state $state
  echo "${info} Rebooting..."
  sleep 5s
  reboot
 fi
fi

state="12"
if $(todo); then
 auto_file="${USER_HOME_DIR}/.config/lxsession/LXDE-pi/autostart"
 check_is_present "run_install" $auto_file
 if [ $is_present ]; then
  echo "${info} Deleting autostart entries..."
  find_line_no "run_install" $auto_file
  delete_line $auto_file $line_no
 else
  echo "${info} No entry by UC2 found in $auto_file"
 fi
 chown -R $OS_USER $AUTOSTART_FILE
 echo "${info} INSTALLATION COMPLETE."
 echo 'PLEASE RUN "SUDO RASPI-CONFIG" AND ENABLE INTERFACES SSH, CAMERA AND I2C!'
 update_state $state
 datetime=$(date)
 echo "FINISH: ${datetime}" | sudo tee --append "${WORKING_DIR}/status" > /dev/null
fi
