#!/usr/bin/env python

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import re
import os.path
from io import open
from setuptools import find_packages, setup

# Change the PACKAGE_NAME only to change folder and different name
PACKAGE_NAME = "{{package_name}}"
PACKAGE_PPRINT_NAME = "{{package_pprint_name}}"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace('-', '/')
# a-b-c => a.b.c
namespace_name = PACKAGE_NAME.replace('-', '.')

# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, 'version.py')
          if os.path.exists(os.path.join(package_folder_path, 'version.py'))
          else os.path.join(package_folder_path, '_version.py'), 'r') as fd:
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', encoding='utf-8') as f:
    readme = f.read()
with open('CHANGELOG.md', encoding='utf-8') as f:
    changelog = f.read()

setup(
    name=PACKAGE_NAME,
    version=version,
    description='Microsoft Azure {} Client Library for Python'.format(PACKAGE_PPRINT_NAME),
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Microsoft Corporation',
    author_email='azpysdkhelp@microsoft.com',
    url='https://github.com/Azure/azure-sdk-for-python',
    keywords="azure, azure sdk",  # update with search keywords relevant to the azure service / product
    classifiers=[
        '{{classifier}}',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    packages=find_packages(exclude=[
        'tests',
        # Exclude packages that will be covered by PEP420 or nspkg
        {%- for nspkg_name in nspkg_names %}
        '{{ nspkg_name }}',
        {%- endfor %}
    ]),
    include_package_data=True,
    package_data={
        'pytyped': ['py.typed'],
    },
    install_requires=[
        'msrest>=0.6.21',
        {%- if need_msrestazure %}
        'msrestazure>=0.4.32,<2.0.0',
        {%- endif %}
        'azure-common~=1.1',
        {%- if need_azurecore %}
        'azure-core>=1.6.0,<2.0.0',
        {%- endif %}
        {%- if need_azuremgmtcore %}
        'azure-mgmt-core>=1.3.0,<2.0.0',
        {%- endif %}
    ],
    python_requires=">=3.6"
)