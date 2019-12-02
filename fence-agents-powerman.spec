##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##

Name: fence-agents-powerman
Summary: Powerman Fence Agent
Version: 4.0.11
Release: 9%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for powerman-controlled devices
URL: https://github.com/ofaaland/fence-agents-powerman
Packager: Olaf Faaland <faaland1@llnl.gov>
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: python
Requires: fence-agents-common >= %{version}-%{release}
Requires: powerman >= 2.3.1-1

%description
Powerman Fence Agent is a script to enable pacemaker to handle power management
for clusters using powerman.

%prep
%setup -n %{name}-%{version}-%{release}

#%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/fence_powerman
%{_mandir}/man8/fence_powerman.8.gz

%changelog
* Mon Dec  2 2019 Olaf Faaland <faaland1@llnl.gov> - 4.0.11-9ch6
- fence_powerman: Fix error checking in monitor action
* Fri Sep 30 2016 Olaf Faaland <faaland1@llnl.gov> - 4.0.11-1ch6
- fence_powerman: Add new fence agent
