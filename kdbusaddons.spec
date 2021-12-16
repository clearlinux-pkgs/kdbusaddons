#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdbusaddons
Version  : 5.89.0
Release  : 48
URL      : https://download.kde.org/stable/frameworks/5.89/kdbusaddons-5.89.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.89/kdbusaddons-5.89.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.89/kdbusaddons-5.89.0.tar.xz.sig
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
BuildRequires : qtbase-dev
BuildRequires : qtx11extras-dev

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
%setup -q -n kdbusaddons-5.89.0
cd %{_builddir}/kdbusaddons-5.89.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639674566
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639674566
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdbusaddons
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kdbusaddons-5.89.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kquitapp5

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kdbusaddons5_qt.qm
/usr/share/qlogging-categories5/kdbusaddons.categories
/usr/share/qlogging-categories5/kdbusaddons.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDBusAddons/KDBusConnectionPool
/usr/include/KF5/KDBusAddons/KDBusInterProcessLock
/usr/include/KF5/KDBusAddons/KDBusService
/usr/include/KF5/KDBusAddons/KDEDModule
/usr/include/KF5/KDBusAddons/KDEInitInterface
/usr/include/KF5/KDBusAddons/UpdateLaunchEnvironmentJob
/usr/include/KF5/KDBusAddons/kdbusaddons_export.h
/usr/include/KF5/KDBusAddons/kdbusconnectionpool.h
/usr/include/KF5/KDBusAddons/kdbusinterprocesslock.h
/usr/include/KF5/KDBusAddons/kdbusservice.h
/usr/include/KF5/KDBusAddons/kdedmodule.h
/usr/include/KF5/KDBusAddons/kdeinitinterface.h
/usr/include/KF5/KDBusAddons/updatelaunchenvironmentjob.h
/usr/include/KF5/kdbusaddons_version.h
/usr/lib64/cmake/KF5DBusAddons/KF5DBusAddonsConfig.cmake
/usr/lib64/cmake/KF5DBusAddons/KF5DBusAddonsConfigVersion.cmake
/usr/lib64/cmake/KF5DBusAddons/KF5DBusAddonsMacros.cmake
/usr/lib64/cmake/KF5DBusAddons/KF5DBusAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5DBusAddons/KF5DBusAddonsTargets.cmake
/usr/lib64/cmake/KF5DBusAddons/KF5dbus.service.in
/usr/lib64/libKF5DBusAddons.so
/usr/lib64/qt5/mkspecs/modules/qt_KDBusAddons.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5DBusAddons.so.5
/usr/lib64/libKF5DBusAddons.so.5.89.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdbusaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdbusaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdbusaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdbusaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdbusaddons/e458941548e0864907e654fa2e192844ae90fc32
