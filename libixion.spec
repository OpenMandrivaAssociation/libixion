%define api 0.13
%define major 0
%define libname %mklibname ixion %{api} %{major}
%define devname %mklibname ixion -d
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Threaded multi-target formula parser & interpreter
Name:		libixion
Version:	0.13.0
Release:	4
License:	MIT
Group:		Publishing
Url:		http://gitlab.com/ixion/ixion
Source0:	https://gitlab.com/ixion/ixion/repository/%{version}/archive.tar.bz2
BuildRequires:	libtool
BuildRequires:	boost-devel >= 1.55
BuildRequires:	libstdc++-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig(mdds-1.2) >= 1.3.0
BuildRequires:	pkgconfig(python3)

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

%package tools
Summary:	Spreadsheet file processing library
Group:		Publishing

%description tools
Tools to use ixion parser and interpreter from cli.

%package -n %{libname}
Summary:	Threaded multi-target formula parser & interpreter
Group:		System/Libraries
Obsoletes:	%{mklibname ixion 0.6 0} < 0.7.0

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
%setup -qn ixion-%{version}-789a08ebc3e7fc2a3914fc34b2497bf476952bfc
./autogen.sh

%build
%configure

sed -i \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

export LD_LIBRARY_PATH=`pwd`/src/libixion/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'parser' -o ixion-parser.1 ./src/ixion-parser
help2man -N -n 'sorter' -o ixion-sorter.1 ./src/ixion-sorter

%check
export LD_LIBRARY_PATH=`pwd`/src/libixion/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check

%install
%makeinstall_std

%files tools
%{_bindir}/*
%{py3_platsitedir}/*.so

%files -n %{libname}
%{_libdir}/libixion-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
