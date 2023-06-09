%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KOSM
%define devname %mklibname -d KOSM

%global optflags %{optflags} -DPROTOBUF_USE_DLLS

%define stable %([ "%(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Indoor mapping application
Name:		kosmindoormap
Version:	23.04.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kosmindoormap-22.12.3-protobuf-22.1.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KPublicTransport)
BuildRequires:	cmake(KOpeningHours)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(ZLIB)
BuildRequires:	cmake(FLEX)
BuildRequires:	cmake(BISON)
BuildRequires:	cmake(Protobuf)
BuildRequires:	cmake(absl)
BuildRequires:	bison flex
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	osmctools
Requires:	osmctools

%description
Public transport application for Plasma.

%package -n %{libname}
Summary:	Library for reading public transport information
Group:		System/Libraries
%rename %mklibname KOSM 20
%rename %mklibname KOSM 21

%description -n %{libname}
Library for reading public transport information.

%files -n %{libname} -f kosmindoormap.lang
%{_libdir}/libKOSM.so.*
%{_libdir}/libKOSMIndoorMap.so.*
%{_libdir}/qt5/qml/org/kde/kosmindoormap
%{_datadir}/qlogging-categories5/org_kde_kosmindoormap.categories

%package -n %{devname}
Summary:	Development files for %{libname}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{libname}.

%files -n %{devname}
%{_includedir}/KOSM
%{_includedir}/KOSMIndoorMap
%{_includedir}/kosm
%{_includedir}/kosmindoormap
%{_includedir}/kosmindoormap_version.h
%{_libdir}/libKOSM.so
%{_libdir}/libKOSMIndoorMap.so
%{_libdir}/cmake/KOSMIndoorMap

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kosmindoormap
