# Creates a 50 GB file instantly 
GB1 = 1024 * 1024 * 1024  # 1 GB
size = 100  # GB
filename = 'test_file'

with open(filename, 'wb') as fout:
    fout.seek(size * GB1 - 1)
    fout.write(b'\0')

print(f"Created {filename} of size {size} GB instantly (sparse file)")
