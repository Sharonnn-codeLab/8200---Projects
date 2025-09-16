def File_encryption():
    filename = input("Enter the file name, full path recommended: ").strip('"')
    with open(filename, "rb") as f:
        content = f.read()

    key = 32
    result_bin = bytes(b ^ key for b in content)

    name_parts = filename.rsplit('.', 1)

    if filename.endswith(f".encrypted.{name_parts[1]}"):
        output_file = f"{name_parts[0].replace(".encrypted", "")}.decrypted.{name_parts[1]}"
    else:
        output_file = f"{name_parts[0]}.encrypted.{name_parts[1]}"

    with open(output_file, "wb") as f:
        f.write(result_bin)

    print(f"The file is saved as: {output_file}")

File_encryption()