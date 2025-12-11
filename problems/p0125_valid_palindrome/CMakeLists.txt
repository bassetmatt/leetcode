cmake_minimum_required(VERSION 3.10)
project(valid-palindrome)

set(CMAKE_CXX_STANDARD 23)

add_executable(valid-palindrome solution-0125.cpp)
target_compile_options(valid-palindrome PRIVATE -Wall -Wextra -Wpedantic)

find_package(fmt)
target_link_libraries(valid-palindrome fmt::fmt)
