# Convert bytes into KB, MB and GB.
bytes = int(input("Enter number of bytes:"))
kb = bytes / 1000
mb = kb/1000
gb = mb/1000
print(f"{bytes} Bytes = {kb} KB = {mb} MB = {gb} GB")