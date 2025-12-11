cmake_minimum_required(VERSION 3.10)
project(top-k-frequent-elements)

set(CMAKE_CXX_STANDARD 23)

add_executable(top-k-frequent-elements solution.cpp)
target_compile_options(top-k-frequent-elements PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(top-k-frequent-elements fmt::fmt)
