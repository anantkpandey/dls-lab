import time
import serial

PORT = "/dev/ttyUSB0"
BAUD = 115200

with serial.Serial(PORT, BAUD, timeout=2) as arduino:
    # The Arduino Uno may reset when the serial port opens.
    time.sleep(2)
    arduino.reset_input_buffer()

    for command in ("ON", "OFF", "ON", "OFF"):
        arduino.write(f"{command}\n".encode("utf-8"))

        response = arduino.readline().decode(
            "utf-8", errors="replace"
        ).strip()

        print(f"Sent: {command:3} | Received: {response}")
        time.sleep(1)
