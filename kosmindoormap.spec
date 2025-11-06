#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KOSM
%define devname %mklibname -d KOSM

%global optflags %{optflags} -DPROTOBUF_USE_DLLS

%define stable %([ "%(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Indoor mapping application
Name:		kosmindoormap
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kosmindoormap/-/archive/%{gitbranch}/kosmindoormap-%{gitbranchd}.tar.bz2#/kosmindoormap-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kosmindoormap-%{version}.tar.xz
%endif
#Patch0:		kosmindoormap-22.12.3-protobuf-22.1.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KPublicTransport)
BuildRequires:	cmake(KOpeningHours)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(ZLIB)
BuildRequires:	cmake(FLEX)
BuildRequires:	cmake(BISON)
BuildRequires:	cmake(Protobuf)
BuildRequires:	cmake(absl)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	bison flex
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	osmctools
Requires:	osmctools
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%rename plasma6-kosmindoormap

%description
Public transport application for Plasma.

%package -n %{libname}
Summary:	Library for reading public transport information
Group:		System/Libraries
%rename %mklibname KOSM 20
%rename %mklibname KOSM 21

%description -n %{libname}
Library for reading public transport information.

%files -n %{libname} -f %{name}.lang
%{_libdir}/libKOSM.so.*
%{_libdir}/libKOSMIndoorMap.so.*
%{_libdir}/libKOSMIndoorRouting.so.*
%{_qtdir}/qml/org/kde/kosmindoormap
%{_qtdir}/qml/org/kde/kosmindoorrouting
%{_qtdir}/qml/org/kde/osm
%{_datadir}/qlogging-categories6/org_kde_kosmindoormap.categories

%package -n %{devname}
Summary:	Development files for %{libname}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{libname}.

%files -n %{devname}
%{_includedir}/KOSM
%{_includedir}/KOSMIndoorMap
%{_includedir}/KOSMIndoorRouting
%{_includedir}/kosm
%{_includedir}/kosmindoormap
%{_includedir}/kosmindoormap_version.h
%{_includedir}/kosmindoorrouting
%{_libdir}/libKOSM.so
%{_libdir}/libKOSMIndoorMap.so
%{_libdir}/libKOSMIndoorRouting.so
%{_libdir}/cmake/KOSMIndoorMap
