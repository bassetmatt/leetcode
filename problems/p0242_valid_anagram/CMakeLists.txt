cmake_minimum_required(VERSION 3.10)
project(valid-anagram)

set(CMAKE_CXX_STANDARD 23)

add_executable(valid-anagram solution-0242.cpp)
target_compile_options(valid-anagram PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(valid-anagram fmt::fmt)
