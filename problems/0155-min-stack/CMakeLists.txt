cmake_minimum_required(VERSION 3.10)
project(min-stack)

set(CMAKE_CXX_STANDARD 23)

add_executable(min-stack solution.cpp)
target_compile_options(min-stack PRIVATE -Wall -Wextra -Wpedantic)
