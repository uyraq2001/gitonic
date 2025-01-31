%define _unpackaged_files_terminate_build 1
%define pypi_name gitonic

# there are no tests provided by the author
%def_without check

Name: %pypi_name
Version: 0.0.15
Release: alt1
Summary: gitonic simplifies working with multiple git repositories.
License: AGPL-3.0
Group: Development/Tools
Url: https://pypi.org/project/%pypi_name
Vcs: https://github.com/kr-g/%pypi_name
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pytkfaicons python3-modules-tkinter python3-module-tkinter-tooltip
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/%pypi_name
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 25 2024 Yuri Kozyrev <kozyrevid@altlinux.org> 0.0.15-alt1
- initial build
