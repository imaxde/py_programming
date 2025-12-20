from haffman import decode, encode


def bits_to_bytes(bits: str) -> tuple[bytes, int]:
    padding = (8 - len(bits) % 8) % 8
    # заполняем до нужного количества нулей
    bits += "0" * padding
    data = bytearray()
    for i in range(0, len(bits), 8):
        data.append(int(bits[i:i+8], 2))
    return bytes(data), padding


def bytes_to_bits(data: bytes, padding: int) -> str:
    bits = "".join(f"{b:08b}" for b in data)
    return bits[:-padding] if padding else bits


def compress_file(source_path: str, destination_path: str) -> None:
    with open(source_path, encoding="utf-8") as f:
        text = f.read()
    encoded, table = encode(text)
    # сохраняем таблицу, зашифрованную в utf8, в заголовок файла
    print(table)
    header = "\n-".join(f"{k}\t{v}" for k, v in table.items()).encode("utf-8")
    data, padding = bits_to_bytes(encoded)
    with open(destination_path, "wb") as f:
        # сохраняем длину заголовка и сам заголовок
        f.write(len(header).to_bytes(4, "big"))
        f.write(header)
        # сохраняем количество добавленных нулей
        f.write(bytes([padding]))
        f.write(data)


def decompress_file(source_path: str, destination_path: str) -> None:
    with open(source_path, "rb") as f:
        header_len = int.from_bytes(f.read(4), "big")
        header = f.read(header_len).decode("utf-8")
        table = {}
        for line in header.split("\n-"):
            print(line)
            ch, code = line.split("\t")
            table[ch] = code
        padding = f.read(1)[0]
        data = f.read()
    bits = bytes_to_bits(data, padding)
    text = decode(bits, table)
    with open(destination_path, "w", encoding="utf-8") as f:
        f.write(text)
