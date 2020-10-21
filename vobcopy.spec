Summary: Utility to copy DVD .vob files to disk
Name: vobcopy
Version: 1.2.0
Release: 16%{?dist}
License: GPLv2+
URL: http://vobcopy.org/
Source: http://vobcopy.org/download/vobcopy-%{version}.tar.bz2
Patch0: vobcopy-1.2.0-Makefile.patch

BuildRequires: gcc
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
%{__make} install \
    DESTDIR="%{buildroot}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}"
# Remove the docs we include ourselves as %%doc
%{__rm} -rf %{buildroot}/usr/local/share/doc


%files
%doc Changelog README Release-Notes TODO
%doc alternative_programs.txt
%license COPYING
%{_bindir}/vobcopy
%{_mandir}/man1/vobcopy.1*
%lang(de) %{_mandir}/de/man1/vobcopy.1*


%changelog
* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.2.0-16
- Rebuild for new libdvdread

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.2.0-13
- rebuild for libdvdread ABI bump

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

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

