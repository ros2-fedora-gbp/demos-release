%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-topic-monitor
Version:        0.25.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS topic_monitor package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-launch
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
%endif

%description
Package containing tools for monitoring ROS 2 topics.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Mar 01 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.25.0-1
- Autogenerated by Bloom

* Fri Feb 24 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.24.1-1
- Autogenerated by Bloom

* Tue Feb 14 2023 Aditya Pande <aditya.pande@openrobotics.org> - 0.24.0-1
- Autogenerated by Bloom

* Wed Nov 02 2022 Audrow Nash <audrow@openrobotics.org> - 0.23.0-1
- Autogenerated by Bloom

* Tue Sep 13 2022 Audrow Nash <audrow@openrobotics.org> - 0.22.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Audrow Nash <audrow@openrobotics.org> - 0.21.0-1
- Autogenerated by Bloom

* Fri Apr 08 2022 Audrow Nash <audrow@openrobotics.org> - 0.20.1-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Audrow Nash <audrow@openrobotics.org> - 0.20.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Audrow Nash <audrow@openrobotics.org> - 0.19.0-2
- Autogenerated by Bloom

