from controller import Robot, Motor, DistanceSensor, Camera

# Create the Robot instance
robot = Robot()

# Set the timestep and maximum speed
timestep = 20
MAX_SPEED = 3

# Get the left and right wheel motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the motor positions and initial velocities
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Initialize the list of distance sensors
distance_sensors = []
for ind in [0, 1, 2, 5, 6, 7]:
    sensor_name = 'ps' + str(ind)
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    distance_sensors.append(sensor)

# Get the camera device
camera = robot.getDevice('camera1')
camera.enable(timestep)
camera.recognitionEnable(timestep)

# Initialize variables for image processing
prev_image = None
counter = 0

# Main control loop
while robot.step(timestep) != -1:
    # Read the camera image
    image = camera.getImage()

    # Compare with the previous image
    if camera.getRecognitionNumberOfObjects() > 0 and image != prev_image:
        # Perform image recognition or processing here

        # Save the recognized image with a unique name
        image_name = f'recognized_image_{counter}.png'
        camera.saveImage(image_name, 'PNG')

        # Update the counter and previous image
        counter += 1
        prev_image = image

    # Process distance sensor data and control the motors
    left_speed = MAX_SPEED
    right_speed = MAX_SPEED
    
    for sensor in distance_sensors:
        sensor_value = sensor.getValue()

        if sensor_value > 100:
            left_speed = -MAX_SPEED

    # Set the motor velocities
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
