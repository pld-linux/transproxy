Summary:	Transparent proxy without cache
Summary(pl.UTF-8):	Przezroczyste proxy bez cache
Name:		transproxy
Version:	1.5
Release:	1
License:	GPL
Group:		Networking/Daemons/HTTP
Source0:	ftp://ftp.nlc.net.au/pub/unix/transproxy/%{name}-%{version}.tgz
# Source0-md5:	7a66f317cd0adeb4e4beaf2931da493e
URL:		http://www.transproxy.nlc.net.au/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tproxy accepts HTTP requests and forwards them to a cache host. If the
HTTP request has been transparently re-directed, the URL is re-written
so that the cache host knows what web server to fetch the document
from. Tcp_wrappers is used to provide host access control.

%description -l pl.UTF-8
tproxy akceptuje prośby HTTP i przekazuje je prawdziwemu proxy z
cache dyskowym. Jeśli prośba HTTP została przezroczyście przekierowana
adres URL jest przepisywany tak by host cache wiedział skąd pobierać
dokumenty. Do kontroli dostępu należy użyć tcpd.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install tproxy	$RPM_BUILD_ROOT%{_sbindir}
install *.8	$RPM_BUILD_ROOT%{_mandir}/man8


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
