cmake_minimum_required(VERSION 3.10)
project(valid-anagram)

set(CMAKE_CXX_STANDARD 23)

add_executable(valid-anagram solution.cpp)
target_compile_options(valid-anagram PRIVATE -Wall -Wextra -Wpedantic)
