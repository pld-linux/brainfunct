Summary:	Brainf*** language interpreter and compiler
Summary(pl):	Kompilator i interpreter j�zyka Brainf***
Name:		brainfunct
Version:	1
Release:	1
License:	?
Group:		Development/Languages
Source0:	http://www.catseye.mb.ca/esoteric/bf/%{name}.tar.gz
URL:		http://www.catseye.mb.ca/esoteric/bf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an interpreter and a compiler for Brainf***
language. Brainf*** is a minimal language developed by Urban Mueller.
While it only has a total of eight instructions, it can solve any
solvable mathematical problem.

%description -l pl
Ten pakiet zawiera interpreter i kompilator j�zyka Brainf***.
Brainf*** to minimalny j�zyk stworzony przez Urbana Muellera. Pomimo
�e ma tylko osiem instrukcji, mo�e rozwi�za� ka�dy rozwi�zywalny
problem matematyczny.

%prep
%setup -q -n bf

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install bfc bfi $RPM_BUILD_ROOT%{_bindir}
install *.b $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}