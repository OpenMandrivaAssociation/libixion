%define api	0.6
%define major	0
%define libname	libixion %{api} %{major}
%define devname	libixion -d

Summary:	Threaded multi-target formula parser & interpreter
Name:		libixion
Version:	0.5.0
Release:	1
License:	MIT
Group:		Productivity/Publishing/Word
Url:		http://gitorious.org/ixion
Source0:	http://kohei.us/files/ixion/src/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mdds-devel

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package tools
Summary:	Spreadsheet file processing library
Group:		Productivity/Publishing/Word

%description tools
Tools to use ixion parser and interpreter from cli.

%package -n %{libname}
Summary:	Threaded multi-target formula parser & interpreter
Group:		System/Libraries

%description -n %{libname}
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package -n %{devname}
Summary:	Threaded multi-target formula parser & interpreter
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%check
make check

%install
%makeinstall_std

%files tools
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libixion-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

