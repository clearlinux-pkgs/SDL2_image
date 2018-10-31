#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_image
Version  : 2.0.2
Release  : 17
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.2.zip
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.2.zip
Source99 : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.2.zip.sig
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GPL-2.0 Libpng libtiff
Requires: SDL2_image-lib
BuildRequires : SDL2-dev
BuildRequires : SDL2-dev32
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : go
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(32libpng)
BuildRequires : pkgconfig(32libwebp)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)

BuildRequires : python3-dev
BuildRequires : scons
BuildRequires : sed
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


%package dev32
Summary: dev32 components for the SDL2_image package.
Group: Default
Requires: SDL2_image-lib32
Requires: SDL2_image-dev

%description dev32
dev32 components for the SDL2_image package.


%package lib
Summary: lib components for the SDL2_image package.
Group: Libraries

%description lib
lib components for the SDL2_image package.


%package lib32
Summary: lib32 components for the SDL2_image package.
Group: Default

%description lib32
lib32 components for the SDL2_image package.


%prep
%setup -q -n SDL2_image-2.0.2
pushd ..
cp -a SDL2_image-2.0.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508849340
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1508849340
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_image.h
/usr/lib64/libSDL2_image.so
/usr/lib64/pkgconfig/SDL2_image.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_image.so
/usr/lib32/pkgconfig/32SDL2_image.pc
/usr/lib32/pkgconfig/SDL2_image.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_image-2.0.so.0
/usr/lib64/libSDL2_image-2.0.so.0.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_image-2.0.so.0
/usr/lib32/libSDL2_image-2.0.so.0.2.0
