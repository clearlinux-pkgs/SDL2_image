#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2_image
Version  : 2.8.4
Release  : 35
URL      : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.8.4.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.8.4.tar.gz
Source1  : https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.8.4.tar.gz.sig
Source2  : 30A59377A7763BE6.pkey
Summary  : image loading library for Simple DirectMedia Layer
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause Zlib libtiff
Requires: SDL2_image-lib = %{version}-%{release}
Requires: SDL2_image-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : llvm
BuildRequires : pkgconfig(libavif)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpdemux)
BuildRequires : pkgconfig(sdl2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SDL_image 2.0
The latest version of this library is available from GitHub:
https://github.com/libsdl-org/SDL_image/releases

%package dev
Summary: dev components for the SDL2_image package.
Group: Development
Requires: SDL2_image-lib = %{version}-%{release}
Provides: SDL2_image-devel = %{version}-%{release}
Requires: SDL2_image = %{version}-%{release}

%description dev
dev components for the SDL2_image package.


%package lib
Summary: lib components for the SDL2_image package.
Group: Libraries
Requires: SDL2_image-license = %{version}-%{release}

%description lib
lib components for the SDL2_image package.


%package license
Summary: license components for the SDL2_image package.
Group: Default

%description license
license components for the SDL2_image package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 30A59377A7763BE6' gpg.status
%setup -q -n SDL2_image-2.8.4
cd %{_builddir}/SDL2_image-2.8.4
pushd ..
cp -a SDL2_image-2.8.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735596284
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735596284
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2_image
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x64/LICENSE.avif.txt %{buildroot}/usr/share/package-licenses/SDL2_image/a9d86e47cc323e86f14cec25506362f750a877d7 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x64/LICENSE.dav1d.txt %{buildroot}/usr/share/package-licenses/SDL2_image/4f6bb845e36328fa89de127c56773dbfd9c90042 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x64/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL2_image/f1a98d8f62af0ecf27736e2117608360013aea61 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x64/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL2_image/00a7d2da8ecfab54b7859887e65ff57c71774f84 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x86/LICENSE.avif.txt %{buildroot}/usr/share/package-licenses/SDL2_image/a9d86e47cc323e86f14cec25506362f750a877d7 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x86/LICENSE.dav1d.txt %{buildroot}/usr/share/package-licenses/SDL2_image/4f6bb845e36328fa89de127c56773dbfd9c90042 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x86/LICENSE.tiff.txt %{buildroot}/usr/share/package-licenses/SDL2_image/f1a98d8f62af0ecf27736e2117608360013aea61 || :
cp %{_builddir}/SDL2_image-%{version}/VisualC/external/optional/x86/LICENSE.webp.txt %{buildroot}/usr/share/package-licenses/SDL2_image/00a7d2da8ecfab54b7859887e65ff57c71774f84 || :
cp %{_builddir}/SDL2_image-%{version}/Xcode/iOS/SDL2.framework/License.txt %{buildroot}/usr/share/package-licenses/SDL2_image/56855624d497345923d749f17502a18029d72631 || :
cp %{_builddir}/SDL2_image-%{version}/Xcode/macOS/SDL2.framework/Versions/A/Resources/License.txt %{buildroot}/usr/share/package-licenses/SDL2_image/56855624d497345923d749f17502a18029d72631 || :
cp %{_builddir}/SDL2_image-%{version}/Xcode/tvOS/SDL2.framework/License.txt %{buildroot}/usr/share/package-licenses/SDL2_image/56855624d497345923d749f17502a18029d72631 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL_image.h
/usr/lib64/cmake/SDL2_image/sdl2_image-config-version.cmake
/usr/lib64/cmake/SDL2_image/sdl2_image-config.cmake
/usr/lib64/libSDL2_image.so
/usr/lib64/pkgconfig/SDL2_image.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libSDL2_image-2.0.so.0.800.4
/usr/lib64/libSDL2_image-2.0.so.0
/usr/lib64/libSDL2_image-2.0.so.0.800.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2_image/00a7d2da8ecfab54b7859887e65ff57c71774f84
/usr/share/package-licenses/SDL2_image/4f6bb845e36328fa89de127c56773dbfd9c90042
/usr/share/package-licenses/SDL2_image/56855624d497345923d749f17502a18029d72631
/usr/share/package-licenses/SDL2_image/a9d86e47cc323e86f14cec25506362f750a877d7
/usr/share/package-licenses/SDL2_image/f1a98d8f62af0ecf27736e2117608360013aea61
