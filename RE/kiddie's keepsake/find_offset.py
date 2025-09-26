import marshal

filename = 'obfuscator'

try:
    with open(filename, 'rb') as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: Could not find the file '{filename}'")
    exit()

print("Searching for valid marshal data offset...")

for i in range(len(data)):
    try:
        # Try to load the marshal data starting from the current offset 'i'
        code_obj = marshal.loads(data[i:])
        
        print(f"\n[+] SUCCESS!")
        print(f"Found valid marshalled code object at offset: {i} (hex: 0x{i:x})")
        
        # We found it, so we can stop searching.
        break

    except (ValueError, EOFError, TypeError):
        # These errors are expected when the offset is wrong.
        # We just ignore them and try the next offset.
        continue
else: # This 'else' belongs to the 'for' loop
    print("\n[-] FAILED: Could not find any valid marshal data in the file.")
