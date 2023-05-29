// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_service_pkg:srv/SetTrajectoryFile.idl
// generated code does not contain a copyright notice

#ifndef MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__TRAITS_HPP_
#define MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_service_pkg/srv/detail/set_trajectory_file__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_service_pkg
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTrajectoryFile_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: file_path
  {
    out << "file_path: ";
    rosidl_generator_traits::value_to_yaml(msg.file_path, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTrajectoryFile_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: file_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "file_path: ";
    rosidl_generator_traits::value_to_yaml(msg.file_path, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTrajectoryFile_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_service_pkg

namespace rosidl_generator_traits
{

[[deprecated("use my_service_pkg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_service_pkg::srv::SetTrajectoryFile_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_service_pkg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_service_pkg::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_service_pkg::srv::SetTrajectoryFile_Request & msg)
{
  return my_service_pkg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_service_pkg::srv::SetTrajectoryFile_Request>()
{
  return "my_service_pkg::srv::SetTrajectoryFile_Request";
}

template<>
inline const char * name<my_service_pkg::srv::SetTrajectoryFile_Request>()
{
  return "my_service_pkg/srv/SetTrajectoryFile_Request";
}

template<>
struct has_fixed_size<my_service_pkg::srv::SetTrajectoryFile_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_service_pkg::srv::SetTrajectoryFile_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_service_pkg::srv::SetTrajectoryFile_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace my_service_pkg
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTrajectoryFile_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTrajectoryFile_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTrajectoryFile_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_service_pkg

namespace rosidl_generator_traits
{

[[deprecated("use my_service_pkg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_service_pkg::srv::SetTrajectoryFile_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_service_pkg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_service_pkg::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_service_pkg::srv::SetTrajectoryFile_Response & msg)
{
  return my_service_pkg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_service_pkg::srv::SetTrajectoryFile_Response>()
{
  return "my_service_pkg::srv::SetTrajectoryFile_Response";
}

template<>
inline const char * name<my_service_pkg::srv::SetTrajectoryFile_Response>()
{
  return "my_service_pkg/srv/SetTrajectoryFile_Response";
}

template<>
struct has_fixed_size<my_service_pkg::srv::SetTrajectoryFile_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_service_pkg::srv::SetTrajectoryFile_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_service_pkg::srv::SetTrajectoryFile_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_service_pkg::srv::SetTrajectoryFile>()
{
  return "my_service_pkg::srv::SetTrajectoryFile";
}

template<>
inline const char * name<my_service_pkg::srv::SetTrajectoryFile>()
{
  return "my_service_pkg/srv/SetTrajectoryFile";
}

template<>
struct has_fixed_size<my_service_pkg::srv::SetTrajectoryFile>
  : std::integral_constant<
    bool,
    has_fixed_size<my_service_pkg::srv::SetTrajectoryFile_Request>::value &&
    has_fixed_size<my_service_pkg::srv::SetTrajectoryFile_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_service_pkg::srv::SetTrajectoryFile>
  : std::integral_constant<
    bool,
    has_bounded_size<my_service_pkg::srv::SetTrajectoryFile_Request>::value &&
    has_bounded_size<my_service_pkg::srv::SetTrajectoryFile_Response>::value
  >
{
};

template<>
struct is_service<my_service_pkg::srv::SetTrajectoryFile>
  : std::true_type
{
};

template<>
struct is_service_request<my_service_pkg::srv::SetTrajectoryFile_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_service_pkg::srv::SetTrajectoryFile_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__TRAITS_HPP_
