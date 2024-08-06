import socket
import struct
import cv2
import time

# Drone IP address and port
DRONE_IP = "192.168.29.1"
DRONE_PORT = 80

# Initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect to drone
sock.connect((DRONE_IP, DRONE_PORT))

# 27-byte command (replace with actual command bytes)
command = b'\x00' * 27 

# Send the command before receiving video
sock.sendto(command, (DRONE_IP, DRONE_PORT))

try:
    start_time = time.time()
    frame_count = 0
    while True:
        # Receive video data
        data, addr = sock.recvfrom(65535)

        # Debug: Print received data size and timestamp
        print(f"Received {len(data)} bytes at {time.time() - start_time:.2f} seconds")

        # Decode H.264 stream
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

        # Debug: Check if frame was decoded successfully
        if frame is None:
            print("Error decoding frame")
            continue

        # Display video frame
        cv2.imshow("Syma X22W Video", frame)

        # Real-time stats
        frame_count += 1
        fps = frame_count / (time.time() - start_time)
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    sock.close()
    cv2.destroyAllWindows()