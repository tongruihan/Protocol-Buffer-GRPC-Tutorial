# Protocol Buffer gRPC Tutorial

## What is it?
gRPC is a RPC platform developed by Google. The letters “gRPC” are a recursive acronym which means, gRPC Remote Procedure Call. In gRPC, a client application makes calles to a server application to enact a service or retrieve desired data. A gRPC defines services, methods, parameters, and return data. So your own application would call the gRPC client application, that would hit its server application, and return the desired result to your own application.

### Protocol Buffer
Protocol buffers are a flexible, efficient, automated mechanism for serializing structured data – think XML, but smaller, faster, and simpler. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages. Here's a quick intro of how it works.
[Protocol Buffer](https://developers.google.com/protocol-buffers/docs/overview)



## Why use it?
gRPC is used to handle multiple languages, and use and develop distributed services. By creating seperated, well defined services that can handle multiple languages, your application is more flexible, and scalable going in to the future. With gRPC we can define our service once in a .proto file and implement clients and servers in any of gRPC’s supported languages, which in turn can be run in environments ranging from servers inside Google to your own tablet - all the complexity of communication between different languages and environments is handled for you by gRPC (For example, you can easily create a gRPC server in Java with clients in Go, Python, or Ruby). We also get all the advantages of working with protocol buffers, including efficient serialization, a simple IDL, and easy interface updating.

## Languages
gRPC is compatable with:
- C++
- C#
- Dart
- Go
- Java
- Node.js
- Objective-C
- PHP
- Python
- Ruby
#### Note: Less used languages do not have as well documented GRPC.

## Installation
-- C++
```c++
#Copyright 2018 gRPC authors.
#
#Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
#cmake build file for C++ helloworld example.
#Assumes protobuf and gRPC have been installed using cmake.
#See cmake_externalproject/CMakeLists.txt for all-in-one cmake build
#that automatically builds all the dependencies before building helloworld.
#
cmake_minimum_required(VERSION 2.8)

project(HelloWorld C CXX)

if(NOT MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
else()
  add_definitions(-D_WIN32_WINNT=0x600)
endif()

if(GRPC_AS_SUBMODULE)
  # One way to build a projects that uses gRPC is to just include the
  # entire gRPC project tree via "add_subdirectory".
  # This approach is very simple to use, but the are some potential
  # disadvantages:
  # * it includes gRPC's CMakeLists.txt directly into your build script
  #   without and that can make gRPC's internal setting interfere with your
  #   own build.
  # * depending on what's installed on your system, the contents of submodules
  #   in gRPC's third_party/* might need to be available (and there might be
  #   additional prerequisites required to build them). Consider using
  #   the gRPC_*_PROVIDER options to fine-tune the expected behavior.
  #
  # A more robust approach to add dependency on gRPC is using
  # cmake's ExternalProject_Add (see cmake_externalproject/CMakeLists.txt).
  
  # Include the gRPC's cmake build (normally grpc source code would live
  # in a git submodule called "third_party/grpc", but this example lives in
  # the same repository as gRPC sources, so we just look a few directories up)
  add_subdirectory(../../.. ${CMAKE_CURRENT_BINARY_DIR}/grpc EXCLUDE_FROM_ALL)
  message(STATUS "Using gRPC via add_subdirectory.")
  
  # After using add_subdirectory, we can now use the grpc targets directly from
  # this build.
  set(_PROTOBUF_LIBPROTOBUF libprotobuf)
  set(_PROTOBUF_PROTOC $<TARGET_FILE:protoc>)
  set(_GRPC_GRPCPP_UNSECURE grpc++_unsecure)
  set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:grpc_cpp_plugin>)
else()
  # This branch assumes that gRPC and all its dependencies are already installed
  # on this system, so they can be located by find_package().

  # Find Protobuf installation
  # Looks for protobuf-config.cmake file installed by Protobuf's cmake installation.
  set(protobuf_MODULE_COMPATIBLE TRUE)
  find_package(Protobuf CONFIG REQUIRED)
  message(STATUS "Using protobuf ${protobuf_VERSION}")

  set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
  set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)

  # Find gRPC installation
  # Looks for gRPCConfig.cmake file installed by gRPC's cmake installation.
  find_package(gRPC CONFIG REQUIRED)
  message(STATUS "Using gRPC ${gRPC_VERSION}")

  set(_GRPC_GRPCPP_UNSECURE gRPC::grpc++_unsecure)
  set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)
endif()

# Proto file
get_filename_component(hw_proto "../../protos/helloworld.proto" ABSOLUTE)
get_filename_component(hw_proto_path "${hw_proto}" PATH)

# Generated sources
set(hw_proto_srcs "${CMAKE_CURRENT_BINARY_DIR}/helloworld.pb.cc")
set(hw_proto_hdrs "${CMAKE_CURRENT_BINARY_DIR}/helloworld.pb.h")
set(hw_grpc_srcs "${CMAKE_CURRENT_BINARY_DIR}/helloworld.grpc.pb.cc")
set(hw_grpc_hdrs "${CMAKE_CURRENT_BINARY_DIR}/helloworld.grpc.pb.h")
add_custom_command(
      OUTPUT "${hw_proto_srcs}" "${hw_proto_hdrs}" "${hw_grpc_srcs}" "${hw_grpc_hdrs}"
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
        -I "${hw_proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        "${hw_proto}"
      DEPENDS "${hw_proto}")

# Include generated *.pb.h files
include_directories("${CMAKE_CURRENT_BINARY_DIR}")

# Targets greeter_[async_](client|server)
foreach(_target
  greeter_client greeter_server
  greeter_async_client greeter_async_server)
  add_executable(${_target} "${_target}.cc"
    ${hw_proto_srcs}
    ${hw_grpc_srcs})
  target_link_libraries(${_target}
    ${_GRPC_GRPCPP_UNSECURE}
    ${_PROTOBUF_LIBPROTOBUF})
endforeach()
```
-- C#
```c#
c
```
-- Dart
```dart
d
```
-- Go
```go
g
```

-- Java

To use gPRC in Java, first you need to 
[setup the protobuf environemnt and obtain the protocol buffer complier](https://github.com/protocolbuffers/protobuf/tree/master/java).

For Maven users, add the gRPC dependencies in `pom.xml`
```xml
<project>
  ...
  <dependencies>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-netty</artifactId>
      <version>1.7.0</version>
    </dependency>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-protobuf</artifactId>
      <version>1.7.0</version>
    </dependency>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-stub</artifactId>
      <version>1.7.0</version>
    </dependency>
    ...
  </dependencies>
  ...
</project>
```
Then add the plugin:
```xml
<project>
  ...
  <dependencies>
    ...
  </dependencies>
  <build>
    <extensions>
      <extension>
        <groupId>kr.motd.maven</groupId>
        <artifactId>os-maven-plugin</artifactId>
        <version>1.5.0.Final</version>
      </extension>
    </extensions>
    <plugins>
      <plugin>
        <groupId>org.xolstice.maven.plugins</groupId>
        <artifactId>protobuf-maven-plugin</artifactId>
        <version>0.5.0</version>
        <configuration>
          <protocArtifact>com.google.protobuf:protoc:3.4.0:exe:${os.detected.classifier}</protocArtifact>
          <pluginId>grpc-java</pluginId>
          <pluginArtifact>io.grpc:protoc-gen-grpc-java:1.7.0:exe:${os.detected.classifier}</pluginArtifact>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>compile</goal>
              <goal>compile-custom</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```
This plugin will first detect the operating system and hardware architecture you are building the application from. Then, using this information, to download the right platform-specific binary that will be able to convert the proto file into Java code.

For Gradle and non-Android, add to dependency in build.gradle
```java
compile 'io.grpc:grpc-netty-shaded:1.20.0'
compile 'io.grpc:grpc-protobuf:1.20.0'
compile 'io.grpc:grpc-stub:1.20.0'
```
For Android client:
```java
compile 'io.grpc:grpc-okhttp:1.20.0'
compile 'io.grpc:grpc-protobuf-lite:1.20.0'
compile 'io.grpc:grpc-stub:1.20.0
```
For protobuf-based codegen integrated with the Gradle build system, you can use protobuf-gradle-plugin:
```java
apply plugin: 'com.google.protobuf'

buildscript {
  repositories {
    mavenCentral()
  }
  dependencies {
    classpath 'com.google.protobuf:protobuf-gradle-plugin:0.8.8'
  }
}

protobuf {
  protoc {
    artifact = "com.google.protobuf:protoc:3.7.1"
  }
  plugins {
    grpc {
      artifact = 'io.grpc:protoc-gen-grpc-java:1.20.0'
    }
  }
  generateProtoTasks {
    all()*.plugins {
      grpc {}
    }
  }
}
```


-- Node.js
```javascript
n
```
-- Objective-C
```objective-c
o
```
-- PHP
```php
p
```
-- Python
```python
python -m pip install grpcio
python -m pip install grpcio-tools
```
-- Ruby
```ruby
gem install grpc
gem install grpc-tools
```

## Getting Started Tutorial
There is a simple turtorial to implement a greeting service with Java.
you will learn:

- The Protocol Buffer Language
- How to implement a gRPC service using Java
- How to implement a gRPC client using Java

#### Create a gRPC Service:
create a new project with Maven:
```
$ mvn archetype:generate -DgroupId=com.example.grpc \
 -DartifactId=grpc-hello-server \
 -DarchetypeArtifactId=maven-archetype-quickstart \
 -DinteractiveMode=false
 ```
 
 direct to the project folder
 `$ cd grpc-hello-server`
 
## Simple example in python
 There is a simple example to implement a greeting service in python.
 You can download the file in the [example](https://github.com/tongruihan/Protocol-Buffer-GRPC-Tutorial/tree/master/example)
 To run the service, first you should make sure you already install grpc and grpc tool as it mentioned before.
 Then Go to the helloworld directory
 ```
 $ cd example/helloworld
 ```
 ### Run the gRPC example
 1.run the server
 ```
 $python greeter_server.py
 ```
 2. run the client
 ```
 $python greeter_client.py
 ``` 
 

### References
[gRPC Documentation](https://grpc.io/docs/)

[Intro to gRPC](https://container-solutions.com/introduction-to-grpc/)

[Protocol Buffer Guide](https://developers.google.com/protocol-buffers/docs/overview)

https://github.com/grpc/grpc-java

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

## Thank you for visiting our tutorial!
