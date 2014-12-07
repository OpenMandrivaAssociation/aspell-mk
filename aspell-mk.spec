%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-0
%define languageenglazy Macedonian
%define languagecode mk
%define lc_ctype mk_MK

Summary:	%{languageenglazy} files for aspell
Name:	aspell-%{languagecode}
Version:	0.50.0
Release:	20
Group:	System/Internationalization
License:	GPLv2
Url:	http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/aspell
mkdir -p %{buildroot}/%{_libdir}/aspell

chmod 644 Copyright README* 

%files
%doc README* Copyright 
%{_libdir}/aspell-*/*

