#!/bin/bash
#set -x

. ./00-UC2_Prerequisites.sh

if [ "$ARCHITECTURE" = "armv7l" ]; then
 BERRYCONDA_URL='https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh'
 BERRYCONDA_VERSION="3"
 echo -e 'BERRYCONDA_VERSION="3"' >> 00-UC2_Prerequisites.sh
elif [ "$ARCHITECTURE" = "armv6l" ]; then
 BERRYCONDA_URL='https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv6l.sh'
 BERRYCONDA_VERSION="2"
 echo -e 'BERRYCONDA_VERSION="2"' >> 00-UC2_Prerequisites.sh
else
 echo "Unsuitable processor architecture ($ARCHITECTURE). Exiting."
 echo 'BERRYCONDA_VERSION="0"' >> 00-UC2_Prerequisites.sh
 exit 1
fi

echo "[UC2] Downloading Berryconda (Python). Please wait..."
wget "${BERRYCONDA_URL}" -N -q --no-check-certificate --show-progress --progress=bar:force 2>&1
BERRYCONDA_FILE="${WORKING_DIR}/${BERRYCONDA_URL##*/}"
echo "[UC2] Installing Berryconda (Python)."
chmod +x ${BERRYCONDA_FILE}
/bin/bash ${BERRYCONDA_FILE} -bf

echo -e "\n# Added by UC2-installer/Berryconda (Python)" >> "${USER_HOME_DIR}/.bashrc"
echo -e "export PATH=\"${USER_HOME_DIR}/berryconda${BERRYCONDA_VERSION}/bin:"'$PATH"' >> ${USER_HOME_DIR}/.bashrc
echo "[UC2] Please reboot and continue afterwards with 02-UC2_CreateEnvironment.sh if you like."
