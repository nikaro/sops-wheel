cmake_minimum_required(VERSION 3.15)
file(READ "${CMAKE_SOURCE_DIR}/sops_version.txt" _ver)
string(STRIP ${_ver} _ver)
project(sops-wheel VERSION ${_ver})
include(ExternalProject)
if (UNIX)
    ExternalProject_Add(sops
        URL https://github.com/getsops/sops/archive/refs/tags/v${CMAKE_PROJECT_VERSION}.tar.gz
        BUILD_IN_SOURCE 1
        BUILD_COMMAND go build ./cmd/sops
        INSTALL_COMMAND ""
        USES_TERMINAL_DOWNLOAD true
        USES_TERMINAL_UPDATE true
        USES_TERMINAL_PATCH true
        USES_TERMINAL_CONFIGURE true
        USES_TERMINAL_BUILD true
        USES_TERMINAL_INSTALL true
        USES_TERMINAL_TEST true
    )
    install(
        FILES ${CMAKE_CURRENT_BINARY_DIR}/sops
        DESTINATION ${SKBUILD_PLATLIB_DIR}/sops_wheel
        PERMISSIONS
        OWNER_READ
        OWNER_WRITE
        OWNER_EXECUTE
        GROUP_READ
        GROUP_EXECUTE
        WORLD_READ
        WORLD_EXECUTE
    )
elseif(WIN32)
    ExternalProject_Add(sops
        URL https://github.com/getsops/sops/archive/refs/tags/v${CMAKE_PROJECT_VERSION}.tar.gz
        CONFIGURE_COMMAND ""
        BUILD_IN_SOURCE 1
        BUILD_COMMAND go build ./cmd/sops
        INSTALL_COMMAND ""
        USES_TERMINAL_DOWNLOAD true
        USES_TERMINAL_UPDATE true
        USES_TERMINAL_PATCH true
        USES_TERMINAL_CONFIGURE true
        USES_TERMINAL_BUILD true
        USES_TERMINAL_INSTALL true
        USES_TERMINAL_TEST true
    )
    install(
        FILES ${CMAKE_CURRENT_BINARY_DIR}/sops.exe
        DESTINATION ${SKBUILD_PLATLIB_DIR}/sops_wheel
        PERMISSIONS
        OWNER_READ
        OWNER_WRITE
        OWNER_EXECUTE
        GROUP_READ
        GROUP_EXECUTE
        WORLD_READ
        WORLD_EXECUTE
    )
else()
    message(FATAL_ERROR "Unsupported platform")
endif()
