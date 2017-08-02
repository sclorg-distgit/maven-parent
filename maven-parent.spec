%{?scl:%scl_package maven-parent}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-parent
Version:        27
Release:        3.1%{?dist}
Summary:        Apache Maven parent POM
License:        ASL 2.0
URL:            http://maven.apache.org
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}apache-parent

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -n %{pkg_name}-%{version} -q
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 27-3.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 27-1
- Update to upstream version 27

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-1
- Update to upstream version 26

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 25-1
- Update to upstream version 25

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 24-2
- Rebuild to regenerate Maven auto-requires

* Wed Apr  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 24-1
- Update to upstream version 24

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-1
- Update to upstream version 23

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-6
- Rebuild to regenerate Maven provides

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-4
- Build with xmvn

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-4
- Add missing BR/R: apache-parent
- Update to current packaging guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 20-1
- Initial version of the package
