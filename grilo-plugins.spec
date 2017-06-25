#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grilo-plugins
Version  : 0.3.4
Release  : 2
URL      : http://ftp.gnome.org/pub/gnome/sources/grilo-plugins/0.3/grilo-plugins-0.3.4.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/grilo-plugins/0.3/grilo-plugins-0.3.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: grilo-plugins-lib
Requires: grilo-plugins-data
Requires: grilo-plugins-doc
Requires: grilo-plugins-locales
BuildRequires : gettext
BuildRequires : gmime-dev
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(oauth)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(totem-plparser)
BuildRequires : pkgconfig(totem-plparser-mini)

%description
Thanks for using Grilo!
=== What is Grilo? ===
Grilo is a framework for browsing and searching media content from various
sources using a single API.

%package data
Summary: data components for the grilo-plugins package.
Group: Data

%description data
data components for the grilo-plugins package.


%package doc
Summary: doc components for the grilo-plugins package.
Group: Documentation

%description doc
doc components for the grilo-plugins package.


%package lib
Summary: lib components for the grilo-plugins package.
Group: Libraries
Requires: grilo-plugins-data

%description lib
lib components for the grilo-plugins package.


%package locales
Summary: locales components for the grilo-plugins package.
Group: Default

%description locales
locales components for the grilo-plugins package.


%prep
%setup -q -n grilo-plugins-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1498399477
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1498399477
rm -rf %{buildroot}
%make_install
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
/usr/share/grilo-plugins/grl-lua-factory/grl-metrolyrics.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-musicbrainz.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-pocket.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-pocket.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
/usr/share/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-spotify-cover.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
/usr/share/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%files doc
%defattr(-,root,root,-)
/usr/share/help/C/examples/example-tmdb.c
/usr/share/help/C/grilo-plugins/grilo-plugins.xml
/usr/share/help/C/grilo-plugins/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/grilo-0.3/libgrldleyna.so
/usr/lib64/grilo-0.3/libgrlfilesystem.so
/usr/lib64/grilo-0.3/libgrlflickr.so
/usr/lib64/grilo-0.3/libgrlgravatar.so
/usr/lib64/grilo-0.3/libgrljamendo.so
/usr/lib64/grilo-0.3/libgrlluafactory.so
/usr/lib64/grilo-0.3/libgrlmagnatune.so
/usr/lib64/grilo-0.3/libgrlmetadatastore.so
/usr/lib64/grilo-0.3/libgrlopensubtitles.so
/usr/lib64/grilo-0.3/libgrloptical-media.so
/usr/lib64/grilo-0.3/libgrlraitv.so
/usr/lib64/grilo-0.3/libgrlshoutcast.so
/usr/lib64/grilo-0.3/libgrltmdb.so
/usr/lib64/grilo-0.3/libgrlvimeo.so
/usr/lib64/grilo-0.3/libgrlyoutube.so

%files locales -f grilo-plugins.lang
%defattr(-,root,root,-)

