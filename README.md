# DLS Lab — Distributed & Large-Scale Systems

A hands-on engineering laboratory exploring systems programming, distributed communication, robotics middleware, embedded systems, and performance measurement.

The goal is to learn by building, testing, measuring, and documenting working systems.

## Current Experiments

### 1. Arduino Uno R3 — LED Control

**Status:** Working

Control the Arduino Uno R3's built-in LED through USB serial communication.

- Platform: Arduino Uno R3
- Serial interface: USB serial (`/dev/ttyUSB0` on the current Linux setup)
- Baud rate: 115200
- Commands: `ON` and `OFF`
- Firmware: Arduino C++

### 2. ROS 2 + Arduino Integration

**Status:** Working prototype

A ROS 2 Python subscriber receives commands on `/arduino/led` and forwards them to the Arduino over USB serial.

**Architecture:**

```text
ROS 2 Topic
/arduino/led
     |
     v
Python Subscriber
     |
     v
USB Serial
     |
     v
Arduino Uno R3
     |
     v
Built-in LED
```

Example commands:

```bash
ros2 topic pub --once /arduino/led std_msgs/msg/String "{data: 'ON'}"
```

```bash
ros2 topic pub --once /arduino/led std_msgs/msg/String "{data: 'OFF'}"
```

The ROS 2 node and Arduino firmware must be running, and the serial port must be available.

### 3. HTTP Service — Experiment 01

**Status:** Working prototype

A Python HTTP server returns JSON responses and records basic request timing information.

- HTTP server using Python's standard library
- JSON response serialization
- Request logging
- Client-side latency measurement

Run the server:

```bash
python3 experiment-01/server.py
```

Test it:

```bash
curl -i http://127.0.0.1:8080/
```

Run the sequential latency benchmark in another terminal:

```bash
python3 experiment-01/benchmark.py
```

The initial local benchmark completed 1,000 measured requests without failures. Results are machine- and environment-specific and should not be interpreted as maximum server capacity.

## Technology Stack

- **Languages:** Python, C++
- **Robotics:** ROS 2
- **Embedded systems:** Arduino Uno R3
- **Communication:** USB serial, HTTP, JSON
- **Operating system:** Ubuntu Linux
- **Tools:** Git, GitHub, Arduino CLI

## Repository Structure

```text
dls-lab/
├── arduino/
│   └── blink/
│       └── blink.ino
└── experiment-01/
    ├── server.py
    └── benchmark.py
```

The ROS 2 workspace is currently maintained separately under `~/ros2_ws`.

## Learning Roadmap

- [x] Arduino LED control through serial commands
- [x] ROS 2 topic-to-Arduino LED control
- [x] Basic HTTP JSON service
- [x] Sequential HTTP latency benchmark
- [ ] Arduino button events published through ROS 2
- [ ] Sensor telemetry through ROS 2 topics
- [ ] ROS 2 services and launch files
- [ ] Concurrent HTTP request experiments
- [ ] Failure handling and repeatable performance tests
- [ ] Documentation and reproducible experiment results

## Engineering Principles

1. Build small, independently testable components.
2. Verify communication before integrating components.
3. Measure performance rather than guessing.
4. Document experimental conditions and limitations.
5. Preserve working implementations as the lab evolves.

## Contributing

This is a personal learning laboratory. Suggestions, issues, and discussions about systems engineering, ROS 2, embedded systems, and reproducible experiments are welcome.

## License

A license has not yet been selected. Until one is added, the repository should not be assumed to grant broad permission to reuse, modify, or redistribute its code.
