%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: SNMP agent plugin
Name: glpi-plugin-racks
Version: 1.2.0
Release: %{release}
License: GPL
Group: Monitoring
URL: http://forge.indepnet.net/projects/show/racks
Source0: https://forge.indepnet.net/attachments/download/883/glpi-racks-%{version}.tar.gz
BuildArch: noarch

%description
This plugin allows you to create bays. Manage the placement of your materials
in your bays. And so know the space and its power consumption and heat
dissipation.

%prep

%setup -q -n racks

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/racks
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/racks

%files
%{_datadir}/glpi/plugins/racks
