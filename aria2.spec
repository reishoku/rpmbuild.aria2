%define binname aria2c

Name:           aria2
Version:        1.6.2
Release:        1%{?dist}
Summary:        High speed download utility with resuming and segmented downloading
Group:          Applications/Internet
License:        GPLv2+ with exceptions
URL:            http://aria2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
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
%setup -q

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
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README doc/aria2c.1.html
%{_bindir}/%{binname}
%{_mandir}/man*/*

%changelog
* Sat Oct 10 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.2-1
- Minor bug fixes and switch XZ compressed source 
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1586

* Thu Oct 08 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.1-1
- Fixes memory leak in HTTP/FTP downloads and other minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1569

* Wed Sep 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1544

* Mon Aug 24 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.2-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1504

* Mon Jul 26 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.1-2
- update source

* Mon Jul 26 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.1-1
- Minor bug fixes
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1494
- Fixed the license tag

* Sun Jul 26 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.0-1
- Mostly minor bug fixes 
- WEB-Seeding support for multi-file torrent
- http://aria2.svn.sourceforge.net/viewvc/aria2/trunk/NEWS?revision=1476

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Robert Scheck <robert@fedoraproject.org> - 1.3.1-1
- Upgrade to 1.3.1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Michał Bentkowski <mr.ecik at gmail.com> - 1.0.1-2
- New version, 1.0.1
- Forgot to add changelog in last release...

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
