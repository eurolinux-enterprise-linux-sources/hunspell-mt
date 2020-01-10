Name: hunspell-mt
Summary: Maltese hunspell dictionaries
%define upstreamid 20020708
Version: 0.%{upstreamid}
Release: 9%{?dist}
Group: Applications/Text
Source: http://linux.org.mt/downloads/spellcheck-mt-0.3.tar.gz
URL: http://linux.org.mt/node/62
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Maltese hunspell dictionaries.

%prep
%setup -q -c

%build
export LANG=mt_MT.utf8
iconv -f ISO-8859-3 -t UTF-8 words.iso8859-3 > maltese.words
wordlist2hunspell maltese.words mt_MT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mt_MT.dic mt_MT.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc readme.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20020708-9
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Caolan McNamara <caolanm@redhat.com> - 0.20020708-3
- spurious extra .aff file packaged

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20020708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Caolan McNamara <caolanm@redhat.com> - 0.20020708-1
- initial version
