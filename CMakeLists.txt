cmake_minimum_required(VERSION 3.10)
project(leetcode)

# Automatically add all C++ problems
file(GLOB problem_dirs "problems/*")
foreach(problem_dir ${problem_dirs})
    if(EXISTS "${problem_dir}/CMakeLists.txt")
        add_subdirectory(${problem_dir})
    endif()
endforeach()
