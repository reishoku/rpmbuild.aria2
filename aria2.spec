%define binname aria2c

Name:           aria2
Version:        1.0.1
Release:        1%{?dist}
Summary:        High speed download utility with resuming and segmented downloading
Group:          Applications/Internet
License:        GPLv2
URL:            http://aria2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{binname}/%{binname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bison
BuildRequires:  c-ares-devel cppunit-devel
BuildRequires:  gettext gnutls-devel
BuildRequires:  libgcrypt-devel libxml2-devel
BuildRequires:  sqlite-devel

%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent. It also supports Metalink
version 3.0.

Currently it has following features:
- HTTP/HTTPS GET support
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- FTP support(active, passive mode)
- FTP through HTTP proxy(GET command or tunneling)
- Segmented download
- Cookie support(currently aria2 ignores "expires")
- It can run as a daemon process.
- BitTorrent protocol support with fast extension.
- Selective download in multi-file torrent
- Metalink version 3.0 support(HTTP/FTP/BitTorrent).
- Limiting download/upload speed

%prep
%setup -q -n %{binname}-%{version}

%build
%configure --enable-bittorrent \
           --enable-metalink \
           --enable-epoll\
           --disable-rpath \
           --with-gnutls \
           --with-libcares \
           --with-libxml2 \
           --with-openssl \
           --with-libz \
           --with-sqlite3 \
           --disable-dependency-tracking \


make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang aria2c
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{binname}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f aria2c.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README doc/aria2c.1.html
%{_bindir}/%{binname}
%{_mandir}/man*/*



%changelog
* Tue Jun 24 2008 Tomas Mraz <tmraz@redhat.com> - 0.12.0-5
- rebuild with new gnutls

* Fri Feb 22 2008 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-4
- Add patch

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12.0-3
- Autorebuild for GCC 4.3

* Mon Dec 31 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-2
- Get rid of odd locale.alias

* Mon Dec 31 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.12.0-1
- 0.12.0

* Thu Sep 20 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.3-1
- 0.11.3

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.2-1
- 0.11.2
- Fix License tag

* Mon Jul 09 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.11.1-1
- Update to 0.11.1

* Sat Apr 28 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.10.2+1-1
- Update to 0.10.2+1

* Tue Feb 20 2007 Michał Bentkowski <mr.ecik at gmail.com> - 0.10.1-1
- Update to 0.10.1

* Sun Dec 31 2006 Michał Bentkowski <mr.ecik at gmail.com> - 0.9.0-2
- Small fix in Summary

* Sat Dec 30 2006 Michał Bentkowski <mr.ecik at gmail.com> - 0.9.0-1
- Initial release
