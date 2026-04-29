# 🤖 Autonomous Robot (Neo)

This repository contains the **Neo ROS 2 package**, a complete autonomous robot simulation system built using ROS 2.

The robot can be launched in **Gazebo and RViz**, supports multiple sensors, and can be controlled using teleoperation.

---<img width="1920" height="1080" alt="Screenshot from 2026-04-24 18-19-40" src="https://github.com/user-attachments/assets/82154230-4044-4518-8747-5757b0c89cd8" />


## 🚀 Features

* ✅ Full robot simulation in Gazebo
* ✅ Visualization in RViz
* ✅ Differential drive robot control
* ✅ Teleoperation support
* ✅ Sensor integration:

  * LiDAR
  * Camera & Depth Camera
  * IMU
  * GPS
  * Magnetometer
* ✅ ROS 2 Control integration
* ✅ Multiple simulation environments (worlds)

---

## 📁 Project Structure

```bash
neo/
 ├── CMakeLists.txt
 ├── package.xml
 ├── launch/
 │    ├── simulation.launch.py
 │    ├── display.launch.py
 │    ├── gazebo.launch.xml
 │    ├── mygazebo.launch.xml
 │    ├── controller.launch.xml
 │    ├── online_async_launch.py
 │    └── master.py
 │
 ├── urdf/
 │    ├── myrobot.xacro
 │    └── robot_ros2_control.xacro
 │
 ├── config/
 │    ├── controller.yaml
 │    ├── nav2_params.yaml
 │    ├── gz_bridge.yaml
 │    └── gzz_bridge.yaml
 │
 ├── rviz/
 │    ├── neo.rviz
 │    └── urdf_config.rviz
 │
 ├── worlds/
 │    ├── demo_world.sdf
 │    ├── test_world.sdf
 │    └── warehouse_world.sdf
 │
 └── maps/
```

---

## ⚙️ Requirements

* ROS 2 (Humble recommended)
* Gazebo
* RViz2
* colcon build system
* Ubuntu 22.04

---

## 🔧 Installation

Clone the repository into your ROS 2 workspace:

```bash
cd ~/ros_ws/src
git clone https://github.com/Mugilan-Theroboticist/autonomous_robot.git
```

Build the workspace:

```bash
cd ~/ros_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## ▶️ Running the Robot

### 🔹 Launch full simulation (Gazebo + RViz)

```bash
ros2 launch neo simulation.launch.py
```

---

### 🔹 Launch only RViz visualization

```bash
ros2 launch neo display.launch.py
```

---

### 🔹 Control the robot (Teleop)

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## 🌍 Simulation Worlds

* `demo_world.sdf`
* `test_world.sdf`
* `warehouse_world.sdf`

You can modify launch files to load different environments.

---

## 🧠 Sensors Integrated

The robot includes:

* LiDAR for obstacle detection
* Camera & Depth Camera for vision
* IMU for orientation
* GPS for positioning
* Magnetometer for heading

---

## 🔮 Future Improvements

* Autonomous navigation using Nav2
* SLAM integration
* Object detection using computer vision
* Real robot hardware deployment

---

## 👨‍💻 Author

**Mugilan**
Robotics & Automation Engineer

---

## 📌 Notes

This project demonstrates a complete ROS 2 robot simulation pipeline including modeling, control, sensing, and visualization.
