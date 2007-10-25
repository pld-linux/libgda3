#
# TODO: package dotnet-gda-sharp
#
# Conditional build:
%bcond_without	doc		# don't generate html documentation
%bcond_without	static_libs	# don't build static libraries
%bcond_with	gamin		# use gamin instead of fam library
#
%bcond_without	firebird	# build without firebird plugin
%bcond_without	freetds		# build without freetds plugin
%bcond_without	ldap		# build without ldap plugin
%bcond_without	mdb		# build without MDB plugin
%bcond_without	mysql		# build without MySQL plugin
%bcond_without	odbc		# build without unixODBC
%bcond_without	pgsql		# build without PostgreSQL plugin
%bcond_without	sqlite		# build without sqlite plugin
%bcond_without	xbase		# build without xbase plugin
#
%ifnarch %{ix86} sparc sparcv9 alpha
%undefine	with_firebird
%endif
Summary:	GNU Data Access library
Summary(pl.UTF-8):   Biblioteka GNU Data Access
Name:		libgda3
Version:	3.1.2
Release:	1
License:	LGPL v2/GPL v2
Group:		Applications/Databases
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgda/3.1/libgda-%{version}.tar.bz2
# Source0-md5:	fe299d264ddeb7fbc36276f74f1abfdc
Patch1:		%{name}-configure.patch
URL:		http://www.gnome-db.org/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
%{!?with_gamin:BuildRequires:	fam-devel}
BuildRequires:	flex
%{?with_freetds:BuildRequires:	freetds-devel >= 0.64}
%{?with_gamin:BuildRequires:	gamin-devel}
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:.2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	perl-base
BuildRequires:	popt-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.213
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3.5.0-2}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xbase:BuildRequires:	xbase-devel >= 2.0.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_libgdadir	libgda-%(echo %{version} | cut -d '.' -f 1-2 )
%define		_libgdadir	libgda-3.0
%define		_providersdir	%{_libdir}/%{_libgdadir}/providers

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%description -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych.

libgda była częścią projektu GNOME-DB, ale została wydzielona, aby
pozwolić na używanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development
Summary(pl.UTF-8):   Dla programistów GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{!?with_gamin:Requires:	fam-devel}
%{?with_gamin:Requires:	gamin-devel}
Requires:	glib2-devel >= 1:2.12.0
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 1:2.6.26
Requires:	libxslt-devel >= 1.1.17
Obsoletes:	libgda0-devel

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych. Ten podpakiet zawiera pliki dla
programistów używających libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl.UTF-8):   Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNU Data Access.

%package provider-db
Summary:	GDA Berkeley DB provider
Summary(pl.UTF-8):   Źródło danych Berkeley DB dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-db
This package contains the GDA Berkeley DB provider.

%description provider-db -l pl.UTF-8
Pakiet dostaczający dane z Berkeley DB dla GDA.

%package provider-firebird
Summary:	GDA Firebird provider
Summary(pl.UTF-8):   Źródło danych Firebird dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-firebird
This package contains the GDA Firebird provider.

%description provider-firebird -l pl.UTF-8
Pakiet dostarczający dane z Firebird dla GDA.

%package provider-freetds
Summary:	GDA FreeTDS provider
Summary(pl.UTF-8):   Źródło danych FreeTDS dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-freetds
This package contains the GDA FreeTDS provider.

%description provider-freetds -l pl.UTF-8
Pakiet dostarczający dane z FreeTDS dla GDA.

%package provider-ldap
Summary:	GDA LDAP provider
Summary(pl.UTF-8):   Źródło danych LDAP dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-ldap
This package contains the GDA LDAP provider.

%description provider-ldap -l pl.UTF-8
Pakiet dostarczający dane z LDAP dla GDA

%package provider-mdb
Summary:	GDA MDB provider
Summary(pl.UTF-8):   Źródło danych MDB
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	mdbtools-libs >= 0.6

%description provider-mdb
This package contains the GDA MDB provider.

%description provider-mdb -l pl.UTF-8
Pakiet dostarczający dane z MDB dla GDA.

%package provider-mysql
Summary:	GDA MySQL provider
Summary(pl.UTF-8):   Źródło danych MySQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-mysql0

%description provider-mysql
This package contains the GDA MySQL provider.

%description provider-mysql -l pl.UTF-8
Pakiet dostarczający dane z MySQL dla GDA.

%package provider-odbc
Summary:	GDA ODBC provider
Summary(pl.UTF-8):   Źródło danych ODBC dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-odbc
This package contains the GDA ODBC provider.

%description provider-odbc -l pl.UTF-8
Pakiet dostarczający dane z ODBC dla GDA.

%package provider-postgres
Summary:	GDA PostgreSQL provider
Summary(pl.UTF-8):   Źródło danych PostgreSQL dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-postgres0

%description provider-postgres
This package contains the GDA PostgreSQL provider.

%description provider-postgres -l pl.UTF-8
Pakiet dostarczający dane z PostgreSQL dla GDA.

%package provider-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):   Źródło danych SQLite dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-sqlite
This package contains the GDA SQLite provider.

%description provider-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%package provider-xbase
Summary:	GDA xBase provider
Summary(pl.UTF-8):   Źródło danych xBase dla GDA
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description provider-xbase
This package contains the GDA xBase (dBase, Clipper, FoxPro) provider.

%description provider-xbase -l pl.UTF-8
Pakiet dostarczający dane z xBase (dBase, Clippera, FoxPro) dla GDA.

%prep
%setup -q -n libgda-%{version}
%patch1 -p1

%if ! %{with gamin}
sed -i -e 's#\(PKG_CHECK_MODULES(GAMIN.*\)#dnl \1#g' configure.in
%endif

%build
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_doc:--enable-gtk-doc} \
	%{!?with_static_libs:--enable-static=no} \
	--with-html-dir=%{_gtkdocdir} \
	--with%{!?with_firebird:out}-firebird \
	--with%{!?with_ldap:out}-ldap \
	--with%{!?with_mdb:out}-mdb \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_odbc:out}-odbc \
	--with%{!?with_pgsql:out}-postgres \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_freetds:out}-tds \
	--with%{!?with_xbase:out}-xbase \
	--without-oracle
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

# modules dlopened by *.so through libgmodule
# Needs to resolve problem with libgda-sqlite.la
# rm -f $RPM_BUILD_ROOT%{_providersdir}/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_providersdir}/*.a

%find_lang libgda-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgda-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-config-tool-3.0
%attr(755,root,root) %{_bindir}/gda-list-server-op-3.0
%attr(755,root,root) %{_libdir}/libgda-3.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgda-report-3.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgda-xslt-3.0.so.*.*.*
#%attr(755,root,root) %{_libdir}/libgda-virtual-3.0.so
%attr(755,root,root) %{_libdir}/libgdasql-3.0.so.*.*.*
%dir %{_libdir}/%{_libgdadir}
%dir %{_providersdir}
%{_datadir}/libgda-3.0
%dir %{_sysconfdir}/libgda-3.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libgda-3.0/config
%{_mandir}/man1/gda-config-tool-3.0.1*
%{_mandir}/man5/gda-config-3.0.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-author-dict-file-3.0
%attr(755,root,root) %{_bindir}/gda-bdb-test
%attr(755,root,root) %{_bindir}/gda-diagnose-3.0
%attr(755,root,root) %{_bindir}/gda-inspect-dict-file-3.0
%attr(755,root,root) %{_bindir}/gda-list-config-3.0
#%attr(755,root,root) %{_bindir}/gda-report-test-3.0
#%attr(755,root,root) %{_bindir}/gda-run-3.0
%attr(755,root,root) %{_bindir}/gda-sql-3.0
%attr(755,root,root) %{_bindir}/gda-test-connection-3.0
%attr(755,root,root) %{_libdir}/libgda-3.0.so
%attr(755,root,root) %{_libdir}/libgda-report-3.0.so
%attr(755,root,root) %{_libdir}/libgdasql-3.0.so
%{_libdir}/libgda-3.0.la
%{_libdir}/libgda-report-3.0.la
%{_libdir}/libgda-xslt-3.0.la
%{_libdir}/libgdasql-3.0.la
#%{_libdir}/libgda-virtual-3.0.la
%{_includedir}/libgda-3.0
%{_pkgconfigdir}/libgda-3.0.pc
%{_pkgconfigdir}/libgda-*-3.0.pc
%{?with_doc:%{_gtkdocdir}/libgda-3.0}
%{_sysconfdir}/libgda-3.0/sales_test.db

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-3.0.a
%{_libdir}/libgda-report-3.0.a
%{_libdir}/libgda-xslt-3.0.a
%{_libdir}/libgdasql-3.0.a
#%{_libdir}/libgda-virtual-3.0.a
%endif

%files provider-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-bdb.so

%if %{with firebird}
%files provider-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-firebird.so
%endif

%if %{with freetds}
%files provider-freetds
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-freetds.so
%endif

%if %{with ldap}
%files provider-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-ldap.so
%endif

%if %{with mdb}
%files provider-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-mdb.so
%endif

%if %{with mysql}
%files provider-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-mysql.so
%endif

%if %{with odbc}
%files provider-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-odbc.so
%endif

%if %{with pgsql}
%files provider-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-postgres.so
%endif

%if %{with sqlite}
%files provider-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-sqlite.so
%{_providersdir}/libgda-sqlite.la
%endif

%if %{with xbase}
%files provider-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-xbase.so
%endif
