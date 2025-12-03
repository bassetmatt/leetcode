cmake_minimum_required(VERSION 3.10)
project(valid-parentheses)

set(CMAKE_CXX_STANDARD 23)

add_executable(valid-parentheses solution.cpp)
target_compile_options(valid-parentheses PRIVATE -Wall -Wextra -Wpedantic)
