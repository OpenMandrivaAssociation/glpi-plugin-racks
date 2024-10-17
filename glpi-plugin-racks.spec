%if %mandriva_branch == Cooker
%define release 3
%else
%define subrel 1
%define release 1
%endif

Summary: SNMP agent plugin
Name: glpi-plugin-racks
Version: 1.2.0
Release: %{release}
License: GPL
Group: Monitoring
URL: https://forge.indepnet.net/projects/show/racks
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


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2012.0
+ Revision: 771131
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1
+ Revision: 771091
- 1.2.0

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 680284
- new version

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 554625
- import glpi-plugin-racks


