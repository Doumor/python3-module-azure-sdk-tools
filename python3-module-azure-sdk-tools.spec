%define pypi_name   azure-sdk-tools
%define commit      67d46b9c4292c267c14833b50bb313c077e63cd5
%define shortcommit 67d46b9


Name:    python3-module-%pypi_name
Version: 1.0.%{shortcommit}
Release: alt1

Summary: Microsoft Azure Subscription Management Client Library for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/azure-sdk-tools/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup
# Some tools are only used for the Azure SDK CI system and there's no need
# to package those.
rm -rf packaging_tools pypi_tools

# There's a dangling empty setup.py in the devtools_testutils directory.
rm -f devtools_testutils/setup.py

%build
%pyproject_build

%install
%pyproject_install
## BZ 2048083: The package metadata causes a provides for version 0.0.0.
#rm -rf %{buildroot}%{python3_sitelib}/azure_sdk_tools-0.0.0.dist-info

# Some provided executables are only used internally in Azure SDK's CI.
rm -f %{buildroot}/%{_bindir}/{auto_codegen,auto_package,generate_package,generate_sdk,sdk_generator,sdk_package}

%files
%doc changelog_generics.md LICENSE
%python3_sitelibdir/devtools_testutils
%python3_sitelibdir/testutils


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 1.0.67d46b9-alt1
- Initial build for Sisyphus
