#!/usr/bin/env python3

import sys

ROM_SIZE = 2048

def rearrange_byte(b):
    return (
        ((b >> 0) & 1) << 0 |
        ((b >> 1) & 1) << 1 |
        ((b >> 3) & 1) << 2 |
        ((b >> 4) & 1) << 3 |
        ((b >> 5) & 1) << 4 |
        ((b >> 6) & 1) << 5 |
        ((b >> 7) & 1) << 6 |
        ((b >> 2) & 1) << 7
    )

def print_labels(char_row):
    line = ""
    for char_col in range(16):
        ch = char_row * 16 + char_col
        line += f"{ch:02X}".center(8) + "  "
    print(line)
    
def print_charset(data):
    for char_row in range(16):
        print_labels(char_row)

        # Print 8 scanlines for this row of 16 characters
        for scanline in range(8):
            line = ""

            for char_col in range(16):
                ch = char_row * 16 + char_col
                b = rearrange_byte(data[ch * 8 + scanline])

                # Display bits 1..7 (bit 0 is unused on your board)
                for bit in range(0, 8):
                    line += "." if not (b & (1 << bit)) else "#"

                line += "  "    # gap between characters

            print(line)

        print()    # blank line between character rows

def main(filename):
    with open(filename, "rb") as f:
        data = f.read()

    if len(data) != ROM_SIZE:
        raise ValueError(f"Expected {ROM_SIZE} bytes, got {len(data)}")

    print_charset(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} rom.bin")
        sys.exit(1)

    main(sys.argv[1])
