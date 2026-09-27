import os
import time

def process_data():
    input_file = '/app/data/input.txt'
    output_file = '/app/data/output.txt'

    print("--- Starting CLI Data Processing ---")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Make sure you mount the volume correctly using -v!")
        return

    print(f"Reading data from {input_file}...")
    
    with open(input_file, 'r') as f:
        content = f.read()

    # Simple processing: count words and characters
    word_count = len(content.split())
    char_count = len(content)

    print("Simulating data processing time...")
    time.sleep(2)

    result_text = f"--- Processing Results ---\n"
    result_text += f"Total Words: {word_count}\n"
    result_text += f"Total Characters: {char_count}\n"
    result_text += f"Processed on: {time.ctime()}\n"

    print(f"Writing results to {output_file}...")
    
    with open(output_file, 'w') as f:
        f.write(result_text)

    print("--- Processing Complete! ---")
    print("Check the 'data' folder on your host machine for 'output.txt'")

if __name__ == "__main__":
    process_data()
