#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_image
Version  : 2.0.5
Release  : 26
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz
Source1 : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz.sig
Summary  : Simple DirectMedia Layer - Sample Image Loading Library
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GPL-2.0 IJG Libpng MIT Zlib libtiff
Requires: SDL2_image-lib = %{version}-%{release}
Requires: SDL2_image-license = %{version}-%{release}
BuildRequires : SDL2-dev32
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-scons
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libpng)
BuildRequires : pkgconfig(32libwebp)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwebp)
BuildRequires : sed
Patch1: CVE-2019-13616.patch

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package dev
Summary: dev components for the SDL2_image package.
Group: Development
Requires: SDL2_image-lib = %{version}-%{release}
Provides: SDL2_image-devel = %{version}-%{release}
Requires: SDL2_image = %{version}-%{release}

%description dev
dev components for the SDL2_image package.


%package dev32
Summary: dev32 components for the SDL2_image package.
Group: Default
Requires: SDL2_image-lib32 = %{version}-%{release}
Requires: SDL2_image-dev = %{version}-%{release}

%description dev32
dev32 components for the SDL2_image package.


%package lib
Summary: lib components for the SDL2_image package.
Group: Libraries
Requires: SDL2_image-license = %{version}-%{release}

%description lib
lib components for the SDL2_image package.


%package lib32
Summary: lib32 components for the SDL2_image package.
Group: Default
Requires: SDL2_image-license = %{version}-%{release}

%description lib32
lib32 components for the SDL2_image package.


%package license
Summary: license components for the SDL2_image package.
Group: Default

%description license
license components for the SDL2_image package.


%prep
%setup -q -n SDL2_image-2.0.5
%patch1 -p1
pushd ..
cp -a SDL2_image-2.0.5 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564515152
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1564515152
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_image
cp COPYING.txt %{buildroot}/usr/share/package-licenses/SDL2_image/COPYING.txt
cp VisualC/external/lib/x64/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.jpeg.txt
cp VisualC/external/lib/x64/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.png.txt
cp VisualC/external/lib/x64/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.tiff.txt
cp VisualC/external/lib/x64/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.webp.txt
cp VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.zlib.txt
cp VisualC/external/lib/x86/LICENSE.jpeg.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.jpeg.txt
cp VisualC/external/lib/x86/LICENSE.png.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.png.txt
cp VisualC/external/lib/x86/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.tiff.txt
cp VisualC/external/lib/x86/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.webp.txt
cp VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.zlib.txt
cp Xcode/Frameworks/webp.framework/Versions/A/Resources/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL2_image/Xcode_Frameworks_webp.framework_Versions_A_Resources_LICENSE.webp.txt
cp debian/copyright %{buildroot}/usr/share/package-licenses/SDL2_image/debian_copyright
cp external/libpng-1.6.37/LICENSE %{buildroot}/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_LICENSE
cp external/libpng-1.6.37/contrib/gregbook/COPYING %{buildroot}/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_gregbook_COPYING
cp external/libpng-1.6.37/contrib/gregbook/LICENSE %{buildroot}/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_gregbook_LICENSE
cp external/libpng-1.6.37/contrib/pngminus/LICENSE.txt %{buildroot}/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_pngminus_LICENSE.txt
cp external/libwebp-1.0.2/COPYING %{buildroot}/usr/share/package-licenses/SDL2_image/external_libwebp-1.0.2_COPYING
cp external/tiff-4.0.9/COPYRIGHT %{buildroot}/usr/share/package-licenses/SDL2_image/external_tiff-4.0.9_COPYRIGHT
cp external/zlib-1.2.11/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/SDL2_image/external_zlib-1.2.11_contrib_dotzlib_LICENSE_1_0.txt
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
/usr/lib64/libSDL2_image-2.0.so.0.2.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_image-2.0.so.0
/usr/lib32/libSDL2_image-2.0.so.0.2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_image/COPYING.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.jpeg.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.png.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.tiff.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.webp.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x64_LICENSE.zlib.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.jpeg.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.png.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.tiff.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.webp.txt
/usr/share/package-licenses/SDL2_image/VisualC_external_lib_x86_LICENSE.zlib.txt
/usr/share/package-licenses/SDL2_image/Xcode_Frameworks_webp.framework_Versions_A_Resources_LICENSE.webp.txt
/usr/share/package-licenses/SDL2_image/debian_copyright
/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_LICENSE
/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_gregbook_COPYING
/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_gregbook_LICENSE
/usr/share/package-licenses/SDL2_image/external_libpng-1.6.37_contrib_pngminus_LICENSE.txt
/usr/share/package-licenses/SDL2_image/external_libwebp-1.0.2_COPYING
/usr/share/package-licenses/SDL2_image/external_tiff-4.0.9_COPYRIGHT
/usr/share/package-licenses/SDL2_image/external_zlib-1.2.11_contrib_dotzlib_LICENSE_1_0.txt
