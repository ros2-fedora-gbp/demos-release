%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-demo-nodes-cpp
Version:        0.30.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS demo_nodes_cpp package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-example-interfaces
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-launch-xml
Requires:       ros-rolling-rcl
Requires:       ros-rolling-rcl-interfaces
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-rcutils
Requires:       ros-rolling-rmw
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-example-interfaces
BuildRequires:  ros-rolling-rcl
BuildRequires:  ros-rolling-rcl-interfaces
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-rcutils
BuildRequires:  ros-rolling-rmw
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-pytest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-testing
BuildRequires:  ros-rolling-launch-testing-ament-cmake
BuildRequires:  ros-rolling-launch-testing-ros
%endif

%description
C++ nodes which were previously in the ros2/examples repository but are now just
used for demo purposes.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Jun 12 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.30.0-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.29.0-1
- Autogenerated by Bloom

* Thu May 11 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.28.1-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.28.0-1
- Autogenerated by Bloom

* Thu Apr 13 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.27.0-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.26.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.25.0-3
- Autogenerated by Bloom

