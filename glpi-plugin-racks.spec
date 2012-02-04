%define name glpi-plugin-racks
%define version 1.2.0
%define release %mkrel 1

Summary: SNMP agent plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: http://forge.indepnet.net/projects/show/racks
Source0: https://forge.indepnet.net/attachments/download/883/glpi-racks-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin allows you to create bays. Manage the placement of your materials
in your bays. And so know the space and its power consumption and heat
dissipation.

%prep
%setup -q -n racks
find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/racks
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/racks

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/racks
