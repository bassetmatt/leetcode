cmake_minimum_required(VERSION 3.10)
project(group-anagrams)

set(CMAKE_CXX_STANDARD 23)

add_executable(group-anagrams solution-0049.cpp)
target_compile_options(group-anagrams PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(group-anagrams fmt::fmt)
