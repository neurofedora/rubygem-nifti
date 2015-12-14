%global gem_name nifti

Name:          rubygem-%{gem_name}
Version:       0.0.2
Release:       3%{?dist}
Summary:       A pure Ruby API to the NIfTI Neuroimaging Format
License:       LGPLv3+
URL:           https://github.com/brainmap/%{gem_name}
Source0:       https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(rspec2)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(narray)
BuildRequires: rubygem(simplecov)
BuildArch: noarch


%description
Ruby NIfTI is a pure-ruby library for handling NIfTI data in Ruby.
NIfTI (Neuroimaging Informatics Technology Initiative) is an image format 
designed primarily for the storage and analysis of MRI & PET imaging data.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
  sed -i "s/config.color_enabled =/config.color =/g" spec/spec_helper.rb
  rspec2 -Ilib spec
popd

%files
%dir  %{gem_instdir}
%exclude  %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/features
%{gem_libdir}
%exclude  %{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%exclude  %{gem_instdir}/nifti.gemspec
%exclude  %{gem_instdir}/spec
%exclude  %{gem_docdir}/rdoc



%changelog
* Mon Dec 14 2015 Ilya Gradina <ilya.gradina@gmai.com> - 0.0.2-3
- change check and description section

* Fri Dec 11 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.2-2
- change license, delete group

* Wed Dec 09 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.2-1
- Initial package
