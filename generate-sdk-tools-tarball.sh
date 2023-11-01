#!/bin/bash
# This script generates the source code for the python-azure-sdk-tools
# Fedora package.
set -euxo pipefail

CURRENT_DIR=$(pwd)
COMMIT=$1
SHORTCOMMIT=${COMMIT:0:7}
TMP_DIR=$(mktemp -d)

USER=azure
PROJECT=azure-sdk-for-python

pushd $TMP_DIR
    wget https://github.com/${USER}/${PROJECT}/archive/${COMMIT}/azure-sdk-for-python-${SHORTCOMMIT}.tar.gz
    tar xf azure-sdk-for-python-${SHORTCOMMIT}.tar.gz
    # Bring over the license from the root of the repository.
    cp azure-sdk-for-python-${COMMIT}/LICENSE azure-sdk-for-python-${COMMIT}/tools/azure-sdk-tools/
    pushd azure-sdk-for-python-${COMMIT}/tools/azure-sdk-tools
        tar -cz -f ${CURRENT_DIR}/azure-sdk-tools-${COMMIT}.tar.gz .
    popd
popd

rm -rf $TMP_DIR
