// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_service_pkg:srv/SetTrajectoryFile.idl
// generated code does not contain a copyright notice

#ifndef MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_H_
#define MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'file_path'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetTrajectoryFile in the package my_service_pkg.
typedef struct my_service_pkg__srv__SetTrajectoryFile_Request
{
  rosidl_runtime_c__String file_path;
} my_service_pkg__srv__SetTrajectoryFile_Request;

// Struct for a sequence of my_service_pkg__srv__SetTrajectoryFile_Request.
typedef struct my_service_pkg__srv__SetTrajectoryFile_Request__Sequence
{
  my_service_pkg__srv__SetTrajectoryFile_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_service_pkg__srv__SetTrajectoryFile_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetTrajectoryFile in the package my_service_pkg.
typedef struct my_service_pkg__srv__SetTrajectoryFile_Response
{
  bool success;
} my_service_pkg__srv__SetTrajectoryFile_Response;

// Struct for a sequence of my_service_pkg__srv__SetTrajectoryFile_Response.
typedef struct my_service_pkg__srv__SetTrajectoryFile_Response__Sequence
{
  my_service_pkg__srv__SetTrajectoryFile_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_service_pkg__srv__SetTrajectoryFile_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_H_
