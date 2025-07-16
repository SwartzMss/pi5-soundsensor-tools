import time
import RPi.GPIO as GPIO

DEFAULT_PIN = 17  # GPIO pin connected to the sensor OUT pin


def listen_for_sound(pin: int = DEFAULT_PIN) -> None:
    """Listen for sound events on the given pin and print a message."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

    print("Listening for sound. Press Ctrl+C to exit.")
    try:
        while True:
            if GPIO.input(pin):
                print("Sound detected!")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
