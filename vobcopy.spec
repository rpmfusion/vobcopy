Summary: Utility to copy DVD .vob files to disk
Name: vobcopy
Version: 1.2.0
Release: 6%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://vobcopy.org/
Source: http://vobcopy.org/download/vobcopy-%{version}.tar.bz2
Patch0: vobcopy-1.2.0-Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libdvdread-devel

%description
Vobcopy copies DVD .vob files to disk, decrypting them on the way (thanks to
libdvdread and libdvdcss) and merges them into file(s) with the name extracted
from the DVD. There is one drawback though: at the moment vobcopy doesn't deal
with multi-angle-dvd's. But since these are rather sparse this shouldn't
matter much.


%prep
%setup -q
%patch0 -p1 -b .Makefile


%build
%{__make} \
    CFLAGS="%{optflags}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}"


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    DESTDIR="%{buildroot}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}"
# Remove the docs we include ourselves as %%doc
%{__rm} -rf %{buildroot}/usr/local/share/doc


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING Changelog README Release-Notes TODO
%doc alternative_programs.txt
%{_bindir}/vobcopy
%{_mandir}/man1/vobcopy.1*
%lang(de) %{_mandir}/de/man1/vobcopy.1*


%changelog
* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.2.0-2
- rebuilt

* Wed Aug 11 2010 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0 (#1051).

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.1.2-3
- rebuild for new F11 features

* Sun Oct 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.1.2-1
- Update to 1.1.2
- drop vobcopy-1.1.1-gcc43.patch

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.1.1-2
- rebuild for RPM Fusion

* Tue May 13 2008 Matthias Saou <http://freshrpms.net/> 1.1.1-1
- Update to 1.1.1.
- Include gcc 4.3 patch.

* Mon Jan 14 2008 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0.

* Sun Jun 24 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Mon Nov 27 2006 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.
- Remove no longer needed gcc change in the Makefile patch.

* Tue Apr 18 2006 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0.
- Add s/gcc-3.4/gcc/ to the Makefile patch.

* Mon Mar 27 2006 Matthias Saou <http://freshrpms.net/> 0.5.16-1
- Major spec file cleanup.

* Fri Jan 6 2006 Robos  <robos@muon.de>
- 0.5.16: -see changelog

* Fri Jul 29 2005 Robos  <robos@muon.de>
- 0.5.15: -option to skip already present files with -m.
  copying of dvd's with files ending in ";?" should work now.

* Sun Oct 24 2004 Robos  <robos@muon.de>
- 0.5.14-rc1: - misc *bsd fixes and first straight OSX support

* Mon Mar 7 2004 Robos  <robos@muon.de>
- 0.5.12-1: -m off-by-one error fixed

* Mon Jan 19 2004 Robos <robos@muon.de>
- 0.5.10-1: -O now works
  cleanup

* Wed Nov 13 2003 Robos <robos@muon.de>
- 0.5.9-1: -F now accepts factor number
  cleanups and small bugfix
  new vobcopy.spec

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- 0.5.8-2: libdvdread is now a pre-requisite

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- first package, 0.5.8-1

