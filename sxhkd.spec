#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sxhkd
Version  : 0.5.9
Release  : 2
URL      : https://github.com/baskerville/sxhkd/archive/0.5.9.tar.gz
Source0  : https://github.com/baskerville/sxhkd/archive/0.5.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sxhkd-license = %{version}-%{release}
BuildRequires : libxcb-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev

%description
## Description
*sxhkd* is an X daemon that reacts to input events by executing commands.

%package license
Summary: license components for the sxhkd package.
Group: Default

%description license
license components for the sxhkd package.


%prep
%setup -q -n sxhkd-0.5.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541546084
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1541546084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sxhkd
cp LICENSE %{buildroot}/usr/share/package-licenses/sxhkd/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sxhkd/LICENSE
