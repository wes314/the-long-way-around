#!/usr/bin/env python3

import sys

def rearrange_byte(b, invert=False):
    if invert:
        b ^= 0xFF

    return (
        ((b >> 0) & 1) << 0 |
        ((b >> 5) & 1) << 1 |
        0 << 2 |                  # force output bit 2 = 0
        ((b >> 4) & 1) << 3 |
        ((b >> 3) & 1) << 4 |
        ((b >> 2) & 1) << 5 |
        ((b >> 1) & 1) << 6 |
        ((b >> 6) & 1) << 7
    )

def convert_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    if len(data) != 2048:
        raise ValueError(f"Expected 2048 bytes, got {len(data)}")

    converted = bytearray()

    for char in range(256):
        for row in range(8):
            b = data[char * 8 + row]

            # invert characters below 0x40
            invert = char < 0x40

            converted.append(rearrange_byte(b, invert))

    with open(output_file, "wb") as f:
        f.write(converted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.bin output.bin")
        sys.exit(1)

    convert_file(sys.argv[1], sys.argv[2])
