from . import utils

WINDOW_SIZE = 14


def sliding_window(sequence):
    for i in range(len(sequence) - WINDOW_SIZE + 1):
        yield (i + WINDOW_SIZE, sequence[i : i + WINDOW_SIZE])


def main(signal):
    windows = ((index, set(window)) for index, window in sliding_window(signal))
    for index, window in windows:
        if len(window) == WINDOW_SIZE:
            return index


if __name__ == "__main__":
    signal = utils.read_inputs_as_single_string(6)
    print(main(signal))
