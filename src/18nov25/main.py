from file_haffman import compress_file, decompress_file


compress_file("sample_text.txt", "sample.haffmancompressed")
decompress_file("sample.haffmancompressed", "sample_text2.txt")
# 8 мб -> 6 мб