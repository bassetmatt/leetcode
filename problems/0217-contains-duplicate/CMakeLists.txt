cmake_minimum_required(VERSION 3.10)
project(contains-duplicate)

set(CMAKE_CXX_STANDARD 23)

add_executable(contains-duplicate solution.cpp)
target_compile_options(contains-duplicate PRIVATE -Wall -Wextra -Wpedantic)
