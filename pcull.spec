%global pkgname pcull
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (0%{?suse_version} && 0%{?suse_version} >=1210)

Name: %{pkgname}
Summary: process culling daemon
Version: 0.0.3
Release: 20180621
License: BSD
Group: System/Management
Source0: %{pkgname}-%{version}.tar.gz

%if %{use_systemd}
Requires: systemd
BuildRequires: systemd
%else
Requires:           initscripts >= 8.36
Requires(postun):   initscripts
Requires(post):     chkconfig
Requires(preun):    chkconfig
%endif

%description
%{pkgname} is used to kill or renice processes that are overusing resources.

%prep
%setup -q -n %{pkgname}-%{version}

%install
%{__install} -D -m 755 usr/sbin/%{pkgname} %{buildroot}%{_sbindir}/%{pkgname}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/%{pkgname}
cp -r etc/%{pkgname} %{buildroot}%{_sysconfdir}/
%if %{use_systemd}
# install systemd-specific files
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 usr/lib/systemd/system/%{pkgname}.service \
    %{buildroot}%{_unitdir}/%{pkgname}.service
%else
# install SYSV init stuff
%{__install} -D -m 755 etc/init.d/%{pkgname} %{buildroot}%{_initrddir}/%{pkgname}
%endif

%post
%if %use_systemd
    /usr/bin/systemctl preset %{pkgname}.service >/dev/null 2>&1 ||:
%else
    /sbin/chkconfig --add %{pkgname}
%endif
%preun
%if %use_systemd
    /usr/bin/systemctl --no-reload disable %{pkgname}.service >/dev/null 2>&1 || :
    /usr/bin/systemctl stop %{pkgname}.service >/dev/null 2>&1 ||:
%else
    /sbin/service %{pkgname} stop > /dev/null 2>&1
    /sbin/chkconfig --del %{pkgname}
%endif


%postun
%if %use_systemd
    /usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:
%endif

%files
%{_sbindir}/%{pkgname}
%if %{use_systemd}
%{_unitdir}/%{pkgname}.service
%else
%{_initrddir}/%{pkgname}
%endif

%config(noreplace)
%{_sysconfdir}/%{pkgname}
