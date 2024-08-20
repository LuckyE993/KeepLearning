cmake_minimum_required(VERSION 3.20)
project(CH7)

set(CMAKE_BUILD_TYPE "Debug")
add_definitions("-DENABLE_SSE")
set(CMAKE_CXX_FLAGS "-std=c++11 -O2 ${SSE_FLAGS} -msse4" )
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

find_package(OpenCV 4 REQUIRED)

include_directories(
        ${OpenCV_INCLUDE_DIRS}
        "usr/include/eigen3"
)

add_executable(orb_cv   orb_cv.cpp)
target_link_libraries(orb_cv ${OpenCV_LIBS})



