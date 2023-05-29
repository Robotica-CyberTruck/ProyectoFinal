// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_service_pkg:srv/SetTrajectoryFile.idl
// generated code does not contain a copyright notice

#ifndef MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_HPP_
#define MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Request __declspec(deprecated)
#endif

namespace my_service_pkg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetTrajectoryFile_Request_
{
  using Type = SetTrajectoryFile_Request_<ContainerAllocator>;

  explicit SetTrajectoryFile_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->file_path = "";
    }
  }

  explicit SetTrajectoryFile_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : file_path(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->file_path = "";
    }
  }

  // field types and members
  using _file_path_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _file_path_type file_path;

  // setters for named parameter idiom
  Type & set__file_path(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->file_path = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Request
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Request
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetTrajectoryFile_Request_ & other) const
  {
    if (this->file_path != other.file_path) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetTrajectoryFile_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetTrajectoryFile_Request_

// alias to use template instance with default allocator
using SetTrajectoryFile_Request =
  my_service_pkg::srv::SetTrajectoryFile_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_service_pkg


#ifndef _WIN32
# define DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Response __declspec(deprecated)
#endif

namespace my_service_pkg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetTrajectoryFile_Response_
{
  using Type = SetTrajectoryFile_Response_<ContainerAllocator>;

  explicit SetTrajectoryFile_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit SetTrajectoryFile_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Response
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_service_pkg__srv__SetTrajectoryFile_Response
    std::shared_ptr<my_service_pkg::srv::SetTrajectoryFile_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetTrajectoryFile_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetTrajectoryFile_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetTrajectoryFile_Response_

// alias to use template instance with default allocator
using SetTrajectoryFile_Response =
  my_service_pkg::srv::SetTrajectoryFile_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_service_pkg

namespace my_service_pkg
{

namespace srv
{

struct SetTrajectoryFile
{
  using Request = my_service_pkg::srv::SetTrajectoryFile_Request;
  using Response = my_service_pkg::srv::SetTrajectoryFile_Response;
};

}  // namespace srv

}  // namespace my_service_pkg

#endif  // MY_SERVICE_PKG__SRV__DETAIL__SET_TRAJECTORY_FILE__STRUCT_HPP_
