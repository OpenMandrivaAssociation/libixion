%define api 0.18
# Usually, but not always:
# %(echo %{version} |cut -d. -f1-2)
%define major 0
%define oldlibname %mklibname ixion 0.18 0
%define libname %mklibname ixion
%define devname %mklibname ixion -d
%define _disable_rebuild_configure 1
#define _disable_lto 1

Summary:	Threaded multi-target formula parser & interpreter
Name:		libixion
Version:	0.19.0
Release:	3
License:	MIT
Group:		Publishing
Url:		http://gitlab.com/ixion/ixion
Source0:	https://gitlab.com/ixion/ixion/-/archive/%{version}/ixion-%{version}.tar.bz2
Patch0:		ixion-0.17.0-fix-missing-include.patch
BuildRequires:	libtool
BuildRequires:	boost-devel >= 1.72.0
BuildRequires:	libstdc++-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig(mdds-2.1)
BuildRequires:	pkgconfig(spdlog)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(vulkan)

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
%rename %{oldlibname}

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
%autosetup -p1 -n ixion-%{version}
./autogen.sh
%configure \
	--enable-python \
	--enable-vulkan

%build
%make_build PYTHON_LIBS=-lpython%{pyver}

export LD_LIBRARY_PATH=`pwd`/src/libixion/.libs:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'parser' -o ixion-parser.1 ./src/ixion-parser
help2man -N -n 'sorter' -o ixion-sorter.1 ./src/ixion-sorter

%if 0
# FIXME restore checks -- ATM they fail in ABF but work locally
# Possibly vulkan/GPU related?
%check
export LD_LIBRARY_PATH=`pwd`/src/libixion/.libs:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check
%endif

%install
%make_install

%files tools
%{_bindir}/*
%{py3_platsitedir}/*.so

%files -n %{libname}
%{_libdir}/libixion-%{api}.so.%{major}*
%{_libdir}/libixion

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
