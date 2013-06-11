#
# spec file for package libixion
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname libixion-0_6-0

Name:           libixion
Version:        0.5.0
Release:        1.2
Summary:        Threaded multi-target formula parser & interpreter
License:        MIT
Group:          Productivity/Publishing/Word
Url:            http://gitorious.org/ixion
Source:         http://kohei.us/files/ixion/src/%{name}-%{version}.tar.bz2
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  mdds-devel >= 0.7.1
BuildRequires:  pkg-config
BuildRequires:  boost-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package -n %{libname}
Summary:        Threaded multi-target formula parser & interpreter
Group:          System/Libraries

%description -n %{libname}
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package devel
Summary:        Threaded multi-target formula parser & interpreter
Group:          Development/Libraries/C and C++
Requires:       %libname = %version

%description devel
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package tools
Summary:        Spreadsheet file processing library
Group:          Productivity/Publishing/Word
Requires:       %libname = %version

%description tools
Tools to use ixion parser and interpreter from cli.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--docdir=%_docdir/%name
make %{?_smp_mflags}

%check
make check

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed May 15 2013 cfarrell@suse.com
- license update: MIT
  The SPDX shortname for the license described in the COPYING file is MIT
* Sat Apr 20 2013 tchvatal@suse.com
- Add URL path for the download.
- Update the package to be matching the released tarball.
- Do not force autoreconf as it is not really needed with released
  package.
* Wed Mar 27 2013 kyoshida@suse.com
- Updated the package which includes the boost patch and several
  others.
- Removed distro-specific patch.
* Tue Mar 26 2013 tchvatal@suse.com
- Cleanup a bit more for factory inclusion.
* Tue Mar 26 2013 jengelh@inai.de
- Fix wrong order of patch application and broken sed substitution
  in %%prep stage
- Runtime boost dependency is automatic and not needed
* Tue Mar 26 2013 tchvatal@suse.com
- Beautify a bit.
* Tue Mar 26 2013 tchvatal@suse.com
- Fix boost m4 macro to pass configure stage.
* Tue Mar 26 2013 kyoshida@suse.com
- Updated to the 0.5.0 pre-release version.
* Tue Jan 31 2012 jengelh@medozas.de
- Remove redundant tags/sections per specfile guideline suggestions
- Add autotools BuildRequires for factory/12.2
* Thu Oct 27 2011 kyoshida@suse.com
- Initial package.
