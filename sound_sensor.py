import time
try:
    import lgpio
except ImportError as exc:  # pragma: no cover - optional dependency
    raise ImportError("This script requires the lgpio package") from exc

DEFAULT_PIN = 17  # GPIO pin connected to the sensor OUT pin


def listen_for_sound(pin: int = DEFAULT_PIN) -> None:
    """Listen for sound events on the given pin and print a message."""
    handle = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_input(handle, pin)

    print("Listening for sound. Press Ctrl+C to exit.")
    try:
        while True:
            if lgpio.gpio_read(handle, pin):
                print("Sound detected!")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        lgpio.gpiochip_close(handle)
