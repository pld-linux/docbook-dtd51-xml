Summary:	XML DocBook DTD 5.1
Summary(pl.UTF-8):	XML DocBook DTD 5.1
Name:		docbook-dtd51-xml
Version:	5.1
Release:	2
License:	Free
Group:		Applications/Publishing/XML
Source0:	https://docbook.org/xml/%{version}/docbook-v%{version}-os.zip
# Source0-md5:	d8bea8ddfc5743578a31cb18f9ae1f5a
Patch0:		%{name}-catalog.patch
URL:		https://docbook.org/
BuildRequires:	libxml2-progs
BuildRequires:	rpm-build >= 4.0.2-94
BuildRequires:	unzip
Requires(post,preun):	/usr/bin/xmlcatalog
Requires:	libxml2-progs >= 2.4.17-6
Requires:	sgml-common >= 0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dtd_path		%{_datadir}/sgml/docbook/xml-dtd-%{version}
%define		xmlcat_file		%{dtd_path}/catalog.xml

%description
DocBook is an XML/SGML vocabulary particularly well suited to books
and papers about computer hardware and software (though it is by no
means limited to only these applications).

This package contains DocBook 5.1 XML DTD.

%description -l pl.UTF-8
DocBook DTD jest zestawem definicji dokumentów XML/SGML przeznaczonych
do tworzenia dokumentacji technicznej. Stosowany jest do pisania
podręczników systemowych, instrukcji jak i wielu innych ciekawych
rzeczy.

Ten pakiet zawiera wersję DocBook 5.1 XML.

%prep
%setup -q -c

# update version number in catalog
%{__sed} -i -e 's/5\.1CR4/5.1/' schemas/catalog.xml

%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{dtd_path}

cp -pr schemas/* $RPM_BUILD_ROOT%{dtd_path}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q %{xmlcat_file} /etc/xml/catalog ; then
	%xmlcat_add %{xmlcat_file}

fi

%preun
if [ "$1" = "0" ] ; then
	%xmlcat_del %{xmlcat_file}
fi

%files
%defattr(644,root,root,755)
%doc docbook-v5.1-os.html
%{dtd_path}
