#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grilo-plugins
Version  : 0.3.10
Release  : 14
URL      : https://download.gnome.org/sources/grilo-plugins/0.3/grilo-plugins-0.3.10.tar.xz
Source0  : https://download.gnome.org/sources/grilo-plugins/0.3/grilo-plugins-0.3.10.tar.xz
Summary  : A collection of plugins for the Grilo framework
Group    : Development/Tools
License  : LGPL-2.1
Requires: grilo-plugins-data = %{version}-%{release}
Requires: grilo-plugins-lib = %{version}-%{release}
Requires: grilo-plugins-license = %{version}-%{release}
Requires: grilo-plugins-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gmime-dev
BuildRequires : gnome-online-accounts-dev
BuildRequires : gperf
BuildRequires : gstreamer-dev
BuildRequires : json-glib-dev
BuildRequires : libarchive-dev
BuildRequires : liboauth-dev
BuildRequires : libsoup-dev
BuildRequires : lua-dev
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(oauth)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(totem-plparser)
BuildRequires : pkgconfig(totem-plparser-mini)
BuildRequires : pkgconfig(tracker-sparql-2.0)
BuildRequires : sqlite-autoconf-dev

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
%setup -q -n grilo-plugins-0.3.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568318007
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/grilo-plugins
cp COPYING %{buildroot}/usr/share/package-licenses/grilo-plugins/COPYING
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
/usr/share/grilo-plugins/grl-lua-factory/grl-spotify-cover.lua
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
/usr/share/help/cs/examples/example-tmdb.c
/usr/share/help/cs/grilo-plugins/grilo-plugins.xml
/usr/share/help/cs/grilo-plugins/legal.xml
/usr/share/help/de/examples/example-tmdb.c
/usr/share/help/de/grilo-plugins/grilo-plugins.xml
/usr/share/help/de/grilo-plugins/legal.xml
/usr/share/help/es/examples/example-tmdb.c
/usr/share/help/es/grilo-plugins/grilo-plugins.xml
/usr/share/help/es/grilo-plugins/legal.xml
/usr/share/help/pl/examples/example-tmdb.c
/usr/share/help/pl/grilo-plugins/grilo-plugins.xml
/usr/share/help/pl/grilo-plugins/legal.xml
/usr/share/help/pt_BR/examples/example-tmdb.c
/usr/share/help/pt_BR/grilo-plugins/grilo-plugins.xml
/usr/share/help/pt_BR/grilo-plugins/legal.xml
/usr/share/help/sv/examples/example-tmdb.c
/usr/share/help/sv/grilo-plugins/grilo-plugins.xml
/usr/share/help/sv/grilo-plugins/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/grilo-0.3/libgrlchromaprint.so
/usr/lib64/grilo-0.3/libgrldleyna.so
/usr/lib64/grilo-0.3/libgrlfilesystem.so
/usr/lib64/grilo-0.3/libgrlflickr.so
/usr/lib64/grilo-0.3/libgrlgravatar.so
/usr/lib64/grilo-0.3/libgrljamendo.so
/usr/lib64/grilo-0.3/libgrlluafactory.so
/usr/lib64/grilo-0.3/libgrlmagnatune.so
/usr/lib64/grilo-0.3/libgrlmetadatastore.so
/usr/lib64/grilo-0.3/libgrlopensubtitles.so
/usr/lib64/grilo-0.3/libgrlopticalmedia.so
/usr/lib64/grilo-0.3/libgrlpodcasts.so
/usr/lib64/grilo-0.3/libgrlraitv.so
/usr/lib64/grilo-0.3/libgrlshoutcast.so
/usr/lib64/grilo-0.3/libgrltmdb.so
/usr/lib64/grilo-0.3/libgrltracker.so
/usr/lib64/grilo-0.3/libgrlvimeo.so
/usr/lib64/grilo-0.3/libgrlyoutube.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grilo-plugins/COPYING

%files locales -f grilo-plugins.lang
%defattr(-,root,root,-)

