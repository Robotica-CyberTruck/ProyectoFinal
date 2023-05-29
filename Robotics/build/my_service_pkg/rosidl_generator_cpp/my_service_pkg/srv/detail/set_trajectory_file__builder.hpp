// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_service_pkg:srv/SetTrajectoryFile.idl
// generated code does not contain a copyright notice

#ifndef MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__BUILDER_HPP_
#define MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_service_pkg/srv/detail/set_trajectory_file__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_service_pkg
{

namespace srv
{

namespace builder
{

class Init_SetTrajectoryFile_Request_file_path
{
public:
  Init_SetTrajectoryFile_Request_file_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_service_pkg::srv::SetTrajectoryFile_Request file_path(::my_service_pkg::srv::SetTrajectoryFile_Request::_file_path_type arg)
  {
    msg_.file_path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_service_pkg::srv::SetTrajectoryFile_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_service_pkg::srv::SetTrajectoryFile_Request>()
{
  return my_service_pkg::srv::builder::Init_SetTrajectoryFile_Request_file_path();
}

}  // namespace my_service_pkg


namespace my_service_pkg
{

namespace srv
{

namespace builder
{

class Init_SetTrajectoryFile_Response_success
{
public:
  Init_SetTrajectoryFile_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_service_pkg::srv::SetTrajectoryFile_Response success(::my_service_pkg::srv::SetTrajectoryFile_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_service_pkg::srv::SetTrajectoryFile_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_service_pkg::srv::SetTrajectoryFile_Response>()
{
  return my_service_pkg::srv::builder::Init_SetTrajectoryFile_Response_success();
}

}  // namespace my_service_pkg

#endif  // MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__BUILDER_HPP_
