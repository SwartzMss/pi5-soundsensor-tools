import time
import RPi.GPIO as GPIO

PIN_SOUND = 17  # GPIO pin connected to the sensor OUT pin


def main() -> None:
    """Listen for sound events and print a message."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_SOUND, GPIO.IN)

    print("Listening for sound. Press Ctrl+C to exit.")
    try:
        while True:
            if GPIO.input(PIN_SOUND):
                print("Sound detected!")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
