Name: pcull
Summary: process culling daemon
Version: 0.0.2
Release: 20130610
License: GPL
Group: System/Management
Prefix: /

%description
pcull is used to kill or renice processes that are overusing resources.

%files
/etc/init.d/pcull
/usr/sbin/pcull

%config(noreplace)
/etc/pcull
