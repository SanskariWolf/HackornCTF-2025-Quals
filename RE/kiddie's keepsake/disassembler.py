import marshal
import dis

# The name of the challenge file
filename = 'obfuscator'

try:
    with open(filename, 'rb') as f:
        # The first few bytes of this specific file are not part of the marshal data.
        # We need to skip them. After some analysis, the magic number
        # seems to indicate we need to skip the first 8 bytes.
        f.seek(7)
        
        # Load the raw marshalled code object
        code_obj = marshal.load(f)

        # Disassemble the code object and print the human-readable instructions
        print(f"--- Disassembly for {filename} ---")
        dis.dis(code_obj)

except Exception as e:
    print(f"An error occurred: {e}")
