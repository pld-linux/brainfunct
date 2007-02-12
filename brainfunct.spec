Summary:	Brainf*** language interpreter and compiler
Summary(pl.UTF-8):	Kompilator i interpreter języka Brainf***
Name:		brainfunct
Version:	1
Release:	1
License:	?
Group:		Development/Languages
Source0:	http://download.sourcemage.org/mirror/stable/%{name}.tar.gz
# Source0-md5:	1953aa43bb9f3f06e99bca7a15b90e62
#Source0:	http://www.catseye.mb.ca/esoteric/bf/%{name}.tar.gz
#URL:		http://www.catseye.mb.ca/esoteric/bf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an interpreter and a compiler for Brainf***
language. Brainf*** is a minimal language developed by Urban Mueller.
While it only has a total of eight instructions, it can solve any
solvable mathematical problem.

%description -l pl.UTF-8
Ten pakiet zawiera interpreter i kompilator języka Brainf***.
Brainf*** to minimalny język stworzony przez Urbana Muellera. Pomimo
że ma tylko osiem instrukcji, może rozwiązać każdy rozwiązywalny
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
