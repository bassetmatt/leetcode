cmake_minimum_required(VERSION 3.10)
project(two-sum)

add_executable(two-sum solution.cpp)
set(CMAKE_CXX_STANDARD 23)

find_package(fmt)
target_link_libraries(two-sum fmt::fmt)

target_compile_options(two-sum PRIVATE -Wall -Wextra -Wpedantic)
