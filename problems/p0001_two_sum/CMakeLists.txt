cmake_minimum_required(VERSION 3.10)
project(two-sum)

set(CMAKE_CXX_STANDARD 23)

add_executable(two-sum solution-0001.cpp)
target_compile_options(two-sum PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(two-sum fmt::fmt)
