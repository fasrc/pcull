Name: pcull
Summary: process culling daemon
Version: 0.0.3
Release: 20180621
License: BSD
Group: System/Management
Prefix: /

%description
pcull is used to kill or renice processes that are overusing resources.

%files
/usr/sbin/pcull
/usr/lib/systemd/system/pcull.service

%config(noreplace)
/etc/pcull
