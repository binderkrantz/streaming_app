
import random
from string import ascii_lowercase, digits
import datetime
import time

def create_data():
    yield {
        'id': ''.join([random.choice(ascii_lowercase[:5]),random.choice(digits)]),
        'timestamp': datetime.datetime.now(datetime.UTC).isoformat(),
        'dimension_1': random.choice(ascii_lowercase[:5]),
        'dimension_2': random.choice(ascii_lowercase[:5]),
        'measure_1': random.randint(1, 100_000),
        'measure_2': round(100 / random.randint(1, 100), 2)
    }

def task():
    value = round(2 / random.randint(1, 20), 2) # between .2 and 2 seconds
    time.sleep(value)
    yield from create_data()

def generate_stream(seconds_to_run=2):
    assert seconds_to_run > 0, 'Argument must be positive integer.'
    start = time.time()
    while True:
        now = time.time()
        if now - start > seconds_to_run:
            break
        t = task()
        nt = next(t)
        print(nt)

def main():
    generate_stream(10)


if __name__ == "__main__":
    main()
