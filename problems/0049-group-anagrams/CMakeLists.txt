cmake_minimum_required(VERSION 3.10)
project(group-anagrams)

set(CMAKE_CXX_STANDARD 23)

add_executable(group-anagrams solution.cpp)
target_compile_options(group-anagrams PRIVATE -Wall -Wextra -Wpedantic)
