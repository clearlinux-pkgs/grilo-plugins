#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: a19cdc79b421
#
Name     : grilo-plugins
Version  : 0.3.16
Release  : 26
URL      : https://download.gnome.org/sources/grilo-plugins/0.3/grilo-plugins-0.3.16.tar.xz
Source0  : https://download.gnome.org/sources/grilo-plugins/0.3/grilo-plugins-0.3.16.tar.xz
Summary  : Plugins for the Grilo Framework
Group    : Development/Tools
License  : LGPL-2.1
Requires: grilo-plugins-data = %{version}-%{release}
Requires: grilo-plugins-lib = %{version}-%{release}
Requires: grilo-plugins-license = %{version}-%{release}
Requires: grilo-plugins-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gmime-dev
BuildRequires : gperf
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(oauth)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(totem-plparser)
BuildRequires : pkgconfig(totem-plparser-mini)
BuildRequires : pkgconfig(tracker-sparql-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# grilo-plugins
Thanks for using Grilo!
## What is Grilo?
Grilo is a framework for browsing and searching media content from various
sources using a single API.

%package data
Summary: data components for the grilo-plugins package.
Group: Data

%description data
data components for the grilo-plugins package.


%package dev
Summary: dev components for the grilo-plugins package.
Group: Development
Requires: grilo-plugins-lib = %{version}-%{release}
Requires: grilo-plugins-data = %{version}-%{release}
Provides: grilo-plugins-devel = %{version}-%{release}
Requires: grilo-plugins = %{version}-%{release}

%description dev
dev components for the grilo-plugins package.


%package doc
Summary: doc components for the grilo-plugins package.
Group: Documentation

%description doc
doc components for the grilo-plugins package.


%package lib
Summary: lib components for the grilo-plugins package.
Group: Libraries
Requires: grilo-plugins-data = %{version}-%{release}
Requires: grilo-plugins-license = %{version}-%{release}

%description lib
lib components for the grilo-plugins package.


%package license
Summary: license components for the grilo-plugins package.
Group: Default

%description license
license components for the grilo-plugins package.


%package locales
Summary: locales components for the grilo-plugins package.
Group: Default

%description locales
locales components for the grilo-plugins package.


%prep
%setup -q -n grilo-plugins-0.3.16
cd %{_builddir}/grilo-plugins-0.3.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727740107
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
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

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
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/grilo-plugins
cp %{_builddir}/grilo-plugins-%{version}/COPYING %{buildroot}/usr/share/package-licenses/grilo-plugins/caeb68c46fa36651acf592771d09de7937926bb3 || :
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang grilo-plugins

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/grilo-plugins/grl-lua-factory/grl-acoustid.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-appletrailers.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-appletrailers.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-euronews.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-euronews.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-itunes-podcast.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-itunes-podcast.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-lastfm-cover.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-musicbrainz-coverart.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-steam-store.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-theaudiodb-cover.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/grilo-plugins-0.3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/examples/example-tmdb.c
/usr/share/help/C/grilo-plugins/grilo-plugins.xml
/usr/share/help/C/grilo-plugins/legal.xml
/usr/share/help/ca/examples/example-tmdb.c
/usr/share/help/ca/grilo-plugins/grilo-plugins.xml
/usr/share/help/ca/grilo-plugins/legal.xml
/usr/share/help/cs/examples/example-tmdb.c
/usr/share/help/cs/grilo-plugins/grilo-plugins.xml
/usr/share/help/cs/grilo-plugins/legal.xml
/usr/share/help/da/examples/example-tmdb.c
/usr/share/help/da/grilo-plugins/grilo-plugins.xml
/usr/share/help/da/grilo-plugins/legal.xml
/usr/share/help/de/examples/example-tmdb.c
/usr/share/help/de/grilo-plugins/grilo-plugins.xml
/usr/share/help/de/grilo-plugins/legal.xml
/usr/share/help/es/examples/example-tmdb.c
/usr/share/help/es/grilo-plugins/grilo-plugins.xml
/usr/share/help/es/grilo-plugins/legal.xml
/usr/share/help/eu/examples/example-tmdb.c
/usr/share/help/eu/grilo-plugins/grilo-plugins.xml
/usr/share/help/eu/grilo-plugins/legal.xml
/usr/share/help/gl/examples/example-tmdb.c
/usr/share/help/gl/grilo-plugins/grilo-plugins.xml
/usr/share/help/gl/grilo-plugins/legal.xml
/usr/share/help/hu/examples/example-tmdb.c
/usr/share/help/hu/grilo-plugins/grilo-plugins.xml
/usr/share/help/hu/grilo-plugins/legal.xml
/usr/share/help/nl/examples/example-tmdb.c
/usr/share/help/nl/grilo-plugins/grilo-plugins.xml
/usr/share/help/nl/grilo-plugins/legal.xml
/usr/share/help/pl/examples/example-tmdb.c
/usr/share/help/pl/grilo-plugins/grilo-plugins.xml
/usr/share/help/pl/grilo-plugins/legal.xml
/usr/share/help/pt_BR/examples/example-tmdb.c
/usr/share/help/pt_BR/grilo-plugins/grilo-plugins.xml
/usr/share/help/pt_BR/grilo-plugins/legal.xml
/usr/share/help/sv/examples/example-tmdb.c
/usr/share/help/sv/grilo-plugins/grilo-plugins.xml
/usr/share/help/sv/grilo-plugins/legal.xml
/usr/share/help/uk/examples/example-tmdb.c
/usr/share/help/uk/grilo-plugins/grilo-plugins.xml
/usr/share/help/uk/grilo-plugins/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/grilo-0.3/libgrlchromaprint.so
/usr/lib64/grilo-0.3/libgrldleyna.so
/usr/lib64/grilo-0.3/libgrlfilesystem.so
/usr/lib64/grilo-0.3/libgrlflickr.so
/usr/lib64/grilo-0.3/libgrlgravatar.so
/usr/lib64/grilo-0.3/libgrlluafactory.so
/usr/lib64/grilo-0.3/libgrlmagnatune.so
/usr/lib64/grilo-0.3/libgrlmetadatastore.so
/usr/lib64/grilo-0.3/libgrlopticalmedia.so
/usr/lib64/grilo-0.3/libgrlpodcasts.so
/usr/lib64/grilo-0.3/libgrlraitv.so
/usr/lib64/grilo-0.3/libgrlshoutcast.so
/usr/lib64/grilo-0.3/libgrltmdb.so
/usr/lib64/grilo-0.3/libgrltracker3.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grilo-plugins/caeb68c46fa36651acf592771d09de7937926bb3

%files locales -f grilo-plugins.lang
%defattr(-,root,root,-)

