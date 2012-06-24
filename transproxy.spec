Summary:	Transparent proxy without cache
Summary(pl):	Prze�roczyste proxy bez cache
Name:		transproxy
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.nlc.net.au/pub/unix/transproxy/%{name}-%{version}.tgz
URL:		http://www.transproxy.nlc.net.au/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tproxy accepts HTTP requests and forwards them to a cache host. If the
HTTP request has been transparently re-directed, the URL is re-written
so that the cache host knows what web server to fetch the document
from. Tcp_wrappers is used to provide host access control.

%description -l pl
tproxy akceptuje pro�by HTTP i przekazuje je prawidziwemy proxy z
cache dyskowym. Je�li pro�ba HTTP zosta�a prze�roczy�cie przekierowana
adres URL jest przepisywany tak by host cache wiedzia� sk�d pobiera�
dokumenty. Do kontroli dost�pu nale�y u�y� tcpd.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install tproxy	$RPM_BUILD_ROOT%{_sbindir}
install *.8	$RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf CHANGELOG README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
