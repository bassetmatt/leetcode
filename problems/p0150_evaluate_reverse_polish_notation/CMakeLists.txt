cmake_minimum_required(VERSION 3.10)
project(evaluate-reverse-polish-notation)

set(CMAKE_CXX_STANDARD 23)

add_executable(evaluate-reverse-polish-notation solution-0150.cpp)
target_compile_options(evaluate-reverse-polish-notation PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(evaluate-reverse-polish-notation fmt::fmt)
