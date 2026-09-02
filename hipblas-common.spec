# Common headers for hipBLAS / hipBLASLt (TheRock 10.0). Header-only.

Name:		hipblas-common
Version:	10.0.0
Release:	1
Summary:	Common headers for hipBLAS libraries
License:	MIT
Group:		Development/C++
URL:		https://github.com/ROCm/rocm-libraries
Source0:	https://github.com/ROCm/rocm-libraries/releases/download/therock-10.0/hipblas-common.tar.gz#/hipblas-common-%{version}.tar.gz

BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	rocm-cmake
BuildArch:	noarch

%description
Shared type definitions and headers used by hipBLAS and hipBLASLt
(hipblasStatus_t, hipblasOperation_t, compute types, etc.). Header-only.

%package devel
Summary:	Development files for hipblas-common
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}
Provides:	hipblas-common-devel = %{EVRD}
# Upstream package version string is 1.4.0; satisfy hipBLAS RPM deps
Provides:	hipblas-common-devel = 1.4.0
# noarch installs cmake under /usr/lib (not %{_libdir}); auto-generators
# may miss that path on 64-bit builders — explicit Provides for hipblas-devel
Provides:	cmake(hipblas-common) = %{version}
Provides:	cmake(hipblas-common) = 1.4.0

%description devel
Headers and CMake package for hipblas-common (INTERFACE library).

%prep
%autosetup -n hipblas-common

# noarch: install cmake under lib (not lib64) so generated paths match
%cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	-DINCLUDE_PATH_COMPATIBILITY=OFF \
	-DROCM_SYMLINK_LIBS=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_PREFIX_PATH=%{_prefix} \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.md
%doc README.md
%exclude %{_docdir}/hipblas-common/LICENSE.md

%files devel
%{_includedir}/hipblas-common/
/usr/lib/cmake/hipblas-common/
