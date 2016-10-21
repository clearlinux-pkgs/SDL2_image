#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL2_image
Version  : 2.0.1
Release  : 6
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.1.zip
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.1.zip
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GPL-2.0 IJG Libpng Zlib libtiff
Requires: SDL2_image-lib
BuildRequires : SDL2-dev
BuildRequires : cmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)
BuildRequires : python-dev
BuildRequires : scons
BuildRequires : setuptools

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package dev
Summary: dev components for the SDL2_image package.
Group: Development
Requires: SDL2_image-lib
Provides: SDL2_image-devel

%description dev
dev components for the SDL2_image package.


%package lib
Summary: lib components for the SDL2_image package.
Group: Libraries

%description lib
lib components for the SDL2_image package.


%prep
%setup -q -n SDL2_image-2.0.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_image.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
