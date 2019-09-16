<<<<<<< HEAD
#!/bin/bash
#set -x

. ./00-UC2_Prerequisites.sh

pyv="$(python -V 2>&1)"
PYTHON_VERSION="${pyv##* }"
echo "PYTHON_VERSION=\"$PYTHON_VERSION\"" >> 00-UC2_Prerequisites.sh

echo "[UC2] Creating UC2-Python-Environment."
conda create -n ${UC2_ENVIRONMENT_NAME} python=$PYTHON_VERSION -y
echo "[UC2] Exporting UC2-Python-Environment. Please wait..."
conda env export -n ${UC2_ENVIRONMENT_NAME} > UC2_Environment.yml
echo "[UC2] Activating UC2-Environment"
source "${USER_HOME_DIR}/berryconda${BERRYCONDA_VERSION}/bin/activate" ${UC2_ENVIRONMENT_NAME}
#source ${USER_HOME_DIR}/berryconda${BERRYCONDA_VERSION}/envs/${UC2_ENVIRONMENT_NAME}/bin/activate
=======
#!/bin/bash
#set -x

. ./00-UC2_Prerequisites.sh

pyv="$(python -V 2>&1)"
PYTHON_VERSION="${pyv##* }"
echo "PYTHON_VERSION=\"$PYTHON_VERSION\"" >> 00-UC2_Prerequisites.sh

echo "[UC2] Creating UC2-Python-Environment."
conda create -n ${UC2_ENVIRONMENT_NAME} python=$PYTHON_VERSION -y
echo "[UC2] Exporting UC2-Python-Environment. Please wait..."
conda env export -n ${UC2_ENVIRONMENT_NAME} > UC2_Environment.yml
echo "[UC2] Activating UC2-Environment"
source "${USER_HOME_DIR}/berryconda${BERRYCONDA_VERSION}/bin/activate" ${UC2_ENVIRONMENT_NAME}
#source ${USER_HOME_DIR}/berryconda${BERRYCONDA_VERSION}/envs/${UC2_ENVIRONMENT_NAME}/bin/activate
>>>>>>> 7bb6688d6039d8293b16428beaec2cfef9e8fe5e
