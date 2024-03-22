#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kdbusaddons
Version  : 6.0.0
Release  : 81
URL      : https://download.kde.org/stable/frameworks/6.0/kdbusaddons-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kdbusaddons-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kdbusaddons-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kdbusaddons-bin = %{version}-%{release}
Requires: kdbusaddons-data = %{version}-%{release}
Requires: kdbusaddons-lib = %{version}-%{release}
Requires: kdbusaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDBusAddons
Convenience classes for D-Bus
## Introduction
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package bin
Summary: bin components for the kdbusaddons package.
Group: Binaries
Requires: kdbusaddons-data = %{version}-%{release}
Requires: kdbusaddons-license = %{version}-%{release}

%description bin
bin components for the kdbusaddons package.


%package data
Summary: data components for the kdbusaddons package.
Group: Data

%description data
data components for the kdbusaddons package.


%package dev
Summary: dev components for the kdbusaddons package.
Group: Development
Requires: kdbusaddons-lib = %{version}-%{release}
Requires: kdbusaddons-bin = %{version}-%{release}
Requires: kdbusaddons-data = %{version}-%{release}
Provides: kdbusaddons-devel = %{version}-%{release}
Requires: kdbusaddons = %{version}-%{release}

%description dev
dev components for the kdbusaddons package.


%package lib
Summary: lib components for the kdbusaddons package.
Group: Libraries
Requires: kdbusaddons-data = %{version}-%{release}
Requires: kdbusaddons-license = %{version}-%{release}

%description lib
lib components for the kdbusaddons package.


%package license
Summary: license components for the kdbusaddons package.
Group: Default

%description license
license components for the kdbusaddons package.


%prep
%setup -q -n kdbusaddons-6.0.0
cd %{_builddir}/kdbusaddons-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709227548
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709227548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdbusaddons
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdbusaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kquitapp6
/usr/bin/kquitapp6

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kdbusaddons6_qt.qm
/usr/share/qlogging-categories6/kdbusaddons.categories
/usr/share/qlogging-categories6/kdbusaddons.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KDBusAddons/KDBusService
/usr/include/KF6/KDBusAddons/KDEDModule
/usr/include/KF6/KDBusAddons/KUpdateLaunchEnvironmentJob
/usr/include/KF6/KDBusAddons/kdbusaddons_export.h
/usr/include/KF6/KDBusAddons/kdbusaddons_version.h
/usr/include/KF6/KDBusAddons/kdbusservice.h
/usr/include/KF6/KDBusAddons/kdedmodule.h
/usr/include/KF6/KDBusAddons/kupdatelaunchenvironmentjob.h
/usr/lib64/cmake/KF6DBusAddons/KF6DBusAddonsConfig.cmake
/usr/lib64/cmake/KF6DBusAddons/KF6DBusAddonsConfigVersion.cmake
/usr/lib64/cmake/KF6DBusAddons/KF6DBusAddonsMacros.cmake
/usr/lib64/cmake/KF6DBusAddons/KF6DBusAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6DBusAddons/KF6DBusAddonsTargets.cmake
/usr/lib64/cmake/KF6DBusAddons/KF6dbus.service.in
/usr/lib64/libKF6DBusAddons.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6DBusAddons.so.6.0.0
/usr/lib64/libKF6DBusAddons.so.6
/usr/lib64/libKF6DBusAddons.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdbusaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdbusaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdbusaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdbusaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32
