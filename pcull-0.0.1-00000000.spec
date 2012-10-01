Name: pcull
Summary: process culling daemon
Version: 0.0.1
Release: 00000000
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
