import argparse
import sys
import time
from solution import max_value_common_subsequence
 
 
def parse_input(stream):
    # Read and parse the problem input from any text stream.
    lines = [line.rstrip('\n') for line in stream if line.strip() != '']
    
    # Check that we have at least 3 lines: one for K, at least one for the alphabet, and two for the strings
    if len(lines) < 3:
        raise ValueError("Input too short: expected K, K alphabet lines, and two strings.")
    
    # Parse K and the character values
    idx = 0
    K = int(lines[idx].strip())
    idx += 1
    
    # Check that we have enough lines for the alphabet and the two strings
    if len(lines) < 1 + K + 2:
        raise ValueError(f"Expected {K} alphabet lines plus 2 strings, got {len(lines) - 1} remaining.")
    
    # Parse the character values into a dictionary
    char_values = {}
    for _ in range(K):
        parts = lines[idx].strip().split()
        if len(parts) != 2:
            raise ValueError(f"Bad alphabet line: {lines[idx]!r}. Expected '<char> <int>'.")
        char, v = parts[0], int(parts[1])
        char_values[char] = v
        idx += 1
    
    # Parse the two strings A and B
    A = lines[idx].strip()
    idx += 1
    B = lines[idx].strip()
    
    return K, char_values, A, B
 
 
def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Compute the maximum-value common subsequence of two strings."
    )

    # Allow the user to specify an input file, or read from stdin if not provided
    parser.add_argument(
        "-f", "--file",
        metavar="FILE",
        help="Path to input file (default: read from stdin)",
    )

    parser.add_argument(
    "-t", "--time",
    action="store_true",
    help="Print runtime after solving",
    )
    
    args = parser.parse_args()
 
    # Open the requested source
    if args.file:
        try:
            stream = open(args.file, 'r')
        except OSError as e:
            sys.exit(f"Error opening '{args.file}': {e}")
    else:
        stream = sys.stdin
 
    try:
        K, char_values, A, B = parse_input(stream)
    except ValueError as e:
        sys.exit(f"Input error: {e}")
    finally:
        if args.file:
            stream.close()

    # Compute the maximum value and the longest common subsequence
    start = time.perf_counter()
    max_val, subseq = max_value_common_subsequence(K, char_values, A, B)
    elapsed = time.perf_counter() - start
    
    # Print the results
    print(max_val)
    print(subseq)

    if args.time:
        print(f"Runtime: {elapsed:.6f}s", file=sys.stderr)
 
 
if __name__ == "__main__":
    main()
