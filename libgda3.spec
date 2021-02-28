# TODO: ibmdb2 provider
#
# Conditional build:
%bcond_without	apidocs		# API documentation build
%bcond_without	static_libs	# static libraries build
%bcond_with	gamin		# use gamin instead of fam library
%bcond_without	gnomevfs	# gnome-vfs support
%bcond_without	gnome		# (convenience alias for gnomevfs)
# - database plugins:
%bcond_without	firebird	# Firebird plugin
%bcond_with	freetds		# FreeTDS plugin
%bcond_without	ldap		# LDAP plugin
%bcond_without	mdb		# MDB plugin
%bcond_without	mysql		# MySQL plugin
%bcond_with	oci		# Oracle DB plugin
%bcond_without	odbc		# unixODBC plugin
%bcond_without	pgsql		# PostgreSQL plugin
%bcond_without	sqlite		# SQLite plugin
%bcond_without	sybase		# sybase plugin
%bcond_without	xbase		# xbase plugin

%if %{without gnome}
%undefine	with_gnomevfs
%endif
%ifnarch %{ix86} sparc sparcv9 alpha
%undefine	with_firebird
%endif
Summary:	GNU Data Access library
Summary(pl.UTF-8):	Biblioteka GNU Data Access
Name:		libgda3
Version:	3.1.5
Release:	21
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda/3.1/libgda-%{version}.tar.bz2
# Source0-md5:	eb7da5286a112e7cff3111c89fba4456
Patch0:		%{name}-configure.patch
Patch1:		%{name}-am.patch
Patch2:		glib232.patch
Patch3:		format-security.patch
Patch4:		mdb-0.7.patch
Patch5:		x32.patch
URL:		http://www.gnome-db.org/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	docbook-dtd412-xml
%{!?with_gamin:BuildRequires:	fam-devel}
BuildRequires:	flex
%{?with_freetds:BuildRequires:	freetds-devel = 0.64}
%{?with_sybase:BuildRequires:	freetds-devel >= 0.82}
%{?with_gamin:BuildRequires:	gamin-devel >= 0.1.8}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-common >= 2.12.0
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.20}
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
%{?with_oci:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.213
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3.5.0-2}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xbase:BuildRequires:	xbase-devel >= 2.0.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libgdadir	libgda-3.0
%define		providersdir	%{_libdir}/%{libgdadir}/providers

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
Summary:	GNU Data Access development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{!?with_gamin:Requires:	fam-devel}
%{?with_gamin:Requires:	gamin-devel >= 0.1.8}
Requires:	glib2-devel >= 1:2.12.0
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.20}
Requires:	libgcrypt-devel >= 1.1.42
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
Summary(pl.UTF-8):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNU Data Access.

%package apidocs
Summary:	GNU Data Access API documentation
Summary(pl.UTF-8):	Dokumentacja API GNU Data Access
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GNU Data Access API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GNU Data Access.

%package provider-db
Summary:	GDA Berkeley DB provider
Summary(pl.UTF-8):	Źródło danych Berkeley DB dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-db
This package contains the GDA Berkeley DB provider.

%description provider-db -l pl.UTF-8
Pakiet dostarczający dane z Berkeley DB dla GDA.

%package provider-firebird
Summary:	GDA Firebird provider
Summary(pl.UTF-8):	Źródło danych Firebird dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-firebird
This package contains the GDA Firebird provider.

%description provider-firebird -l pl.UTF-8
Pakiet dostarczający dane z Firebird dla GDA.

%package provider-freetds
Summary:	GDA FreeTDS provider
Summary(pl.UTF-8):	Źródło danych FreeTDS dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-freetds
This package contains the GDA FreeTDS provider.

%description provider-freetds -l pl.UTF-8
Pakiet dostarczający dane z FreeTDS dla GDA.

%package provider-ldap
Summary:	GDA LDAP provider
Summary(pl.UTF-8):	Źródło danych LDAP dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-ldap
This package contains the GDA LDAP provider.

%description provider-ldap -l pl.UTF-8
Pakiet dostarczający dane z LDAP dla GDA.

%package provider-mdb
Summary:	GDA MDB provider
Summary(pl.UTF-8):	Źródło danych MDB
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mdbtools-libs >= 0.6

%description provider-mdb
This package contains the GDA MDB provider.

%description provider-mdb -l pl.UTF-8
Pakiet dostarczający dane z MDB dla GDA.

%package provider-mysql
Summary:	GDA MySQL provider
Summary(pl.UTF-8):	Źródło danych MySQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-mysql0

%description provider-mysql
This package contains the GDA MySQL provider.

%description provider-mysql -l pl.UTF-8
Pakiet dostarczający dane z MySQL dla GDA.

%package provider-odbc
Summary:	GDA ODBC provider
Summary(pl.UTF-8):	Źródło danych ODBC dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-odbc
This package contains the GDA ODBC provider.

%description provider-odbc -l pl.UTF-8
Pakiet dostarczający dane z ODBC dla GDA.

%package provider-oracle
Summary:	GDA Oracle provider
Summary(pl.UTF-8):	Źródło danych Oracle dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-oracle
This package contains the GDA Oracle provider.

%description provider-oracle -l pl.UTF-8
Pakiet dostarczający dane z bazy Oracle dla GDA.

%package provider-postgres
Summary:	GDA PostgreSQL provider
Summary(pl.UTF-8):	Źródło danych PostgreSQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgda-postgres0

%description provider-postgres
This package contains the GDA PostgreSQL provider.

%description provider-postgres -l pl.UTF-8
Pakiet dostarczający dane z PostgreSQL dla GDA.

%package provider-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):	Źródło danych SQLite dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sqlite
This package contains the GDA SQLite provider.

%description provider-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%package provider-sybase
Summary:	GDA Sybase provider
Summary(pl.UTF-8):	Źródło danych Sybase dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sybase
This package contains the GDA Sybase provider.

%description provider-sybase -l pl.UTF-8
Pakiet dostarczający dane z Sybase dla GDA.

%package provider-xbase
Summary:	GDA xBase provider
Summary(pl.UTF-8):	Źródło danych xBase dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-xbase
This package contains the GDA xBase (dBase, Clipper, FoxPro) provider.

%description provider-xbase -l pl.UTF-8
Pakiet dostarczający dane z xBase (dBase, Clippera, FoxPro) dla GDA.

%prep
%setup -q -n libgda-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%if %{without gamin}
%{__sed} -i -e 's#PKG_CHECK_MODULES(GAMIN.*)#have_fam=no#g' configure.in
%endif
%if %{without gnomevfs}
%{__sed} -i -e 's#PKG_CHECK_MODULES(GNOMEVFS.*)#have_gnomevfs=no#g' configure.in
%endif

%build
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--with-firebird%{!?with_firebird:=no} \
	--with-ldap%{!?with_ldap:=no} \
	--with-mdb%{!?with_mdb:=no} \
	--with-mysql%{!?with_mysql:=no} \
	--with-odbc%{!?with_odbc:=no} \
	--with-oracle%{!?with_oci:=no} \
	--with-postgres%{!?with_pgsql:=no} \
	--with-sqlite%{!?with_sqlite:=no} \
	%{?with_sybase:--with-sybase=/usr} \
	--with-tds%{!?with_freetds:=no} \
	--with-xbase%{!?with_xbase:=no}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

# modules dlopened by *.so through libgmodule
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{providersdir}/*.a
%endif
%{__rm} $RPM_BUILD_ROOT{%{providersdir},%{_libdir}}/*.la

mv -f $RPM_BUILD_ROOT%{_localedir}/{sr@Latn,sr@latin}

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
%attr(755,root,root) %ghost %{_libdir}/libgda-3.0.so.3
%attr(755,root,root) %{_libdir}/libgda-report-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-report-3.0.so.3
%attr(755,root,root) %{_libdir}/libgda-xslt-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-xslt-3.0.so.0
%attr(755,root,root) %{_libdir}/libgdasql-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdasql-3.0.so.3
%dir %{_libdir}/%{libgdadir}
%dir %{providersdir}
%dir %{_datadir}/libgda-3.0
%{_datadir}/libgda-3.0/dtd
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
%attr(755,root,root) %{_bindir}/gda-sql-3.0
%attr(755,root,root) %{_bindir}/gda-test-connection-3.0
%attr(755,root,root) %{_libdir}/libgda-3.0.so
%attr(755,root,root) %{_libdir}/libgda-report-3.0.so
%attr(755,root,root) %{_libdir}/libgda-xslt-3.0.so
%attr(755,root,root) %{_libdir}/libgdasql-3.0.so
%{_includedir}/libgda-3.0
%{_pkgconfigdir}/libgda-3.0.pc
%{_pkgconfigdir}/libgda-*-3.0.pc
%{_sysconfdir}/libgda-3.0/sales_test.db

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-3.0.a
%{_libdir}/libgda-report-3.0.a
%{_libdir}/libgda-xslt-3.0.a
%{_libdir}/libgdasql-3.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgda-3.0
%endif

%files provider-db
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-bdb.so
%{_datadir}/libgda-3.0/bdb_specs_*.xml

%if %{with firebird}
%files provider-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-firebird.so
%{_datadir}/libgda-3.0/firebird_specs_*.xml
%endif

%if %{with freetds}
%files provider-freetds
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-freetds.so
%{_datadir}/libgda-3.0/freetds_specs_*.xml
%endif

%if %{with ldap}
%files provider-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-ldap.so
%{_datadir}/libgda-3.0/ldap_specs_*.xml
%endif

%if %{with mdb}
%files provider-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-mdb.so
%{_datadir}/libgda-3.0/mdb_specs_*.xml
%endif

%if %{with mysql}
%files provider-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-mysql.so
%{_datadir}/libgda-3.0/mysql_specs_*.xml
%endif

%if %{with odbc}
%files provider-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-odbc.so
%{_datadir}/libgda-3.0/odbc_specs_*.xml
%endif

%if %{with oci}
%files provider-oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-oracle.so
%{_datadir}/libgda-3.0/oracle_specs_*.xml
%endif

%if %{with pgsql}
%files provider-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-postgres.so
%{_datadir}/libgda-3.0/postgres_specs_*.xml
%endif

%if %{with sqlite}
%files provider-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-sqlite.so
%{_datadir}/libgda-3.0/sqlite_specs_*.xml
%endif

%if %{with sybase}
%files provider-sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-sybase.so
%{_datadir}/libgda-3.0/sybase_specs_*.xml
%endif

%if %{with xbase}
%files provider-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-xbase.so
%{_datadir}/libgda-3.0/xbase_specs_*.xml
%endif
