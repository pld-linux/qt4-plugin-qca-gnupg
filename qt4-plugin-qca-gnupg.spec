%define		rname qca-gnupg
#
%define	snap	20070904
Summary:	Qt Cryptographic Architecture (QCA) GNU Privacy Guard plugin
Summary(pl.UTF-8):	Wtyczka GNU Privacy Guard dla Qt Cryptographic Architecture (QCA)
Name:		qt4-plugin-%{rname}
Version:	0.1
Release:	0.%{snap}.4
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/download/qca/2.0/test4/qca-gnupg-%{version}-%{snap}.tar.bz2
# Source0-md5:	8a2ba2a8ac51363d2933c05a100c530e
URL:		http://delta.affinix.com/qca/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-qmake >= 4.3.3-3
%requires_eq	QtCore
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_libdir}/qt4/plugins/crypto

# chrpath stripping fails
%define		no_install_post_chrpath	1

%description
A plugin to provide GNU Privacy Guard capability to programs that
utilize the Qt Cryptographic Architecture (QCA).

%description -l pl.UTF-8
Wtyczka pozwalająca wykorzystać możliwości GNU Privacy Guard w
programach korzystających z Qt Cryptographic Architecture (QCA).

%prep
%setup -qn %{rname}-%{version}-%{snap}

%build
export QTDIR=%{_libdir}/qt4
./configure

qmake-qt4 %{rname}.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*.so
