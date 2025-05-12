def text_to_binary(text):
    # Chuyển văn bản thành chuỗi nhị phân (8 bit mỗi ký tự)
    return ''.join(format(ord(c), '08b') for c in text)

def hide_message(cover_text, binary_message):
    # Tách văn bản phủ thành các câu
    sentences = cover_text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Kiểm tra số câu có "and"
    and_sentences = [s for s in sentences if ' and ' in s]
    if len(and_sentences) < len(binary_message):
        raise ValueError(f"Không đủ câu chứa 'and' để giấu thông điệp. Cần {len(binary_message)} câu, tìm thấy {len(and_sentences)}.")
    
    result = []
    binary_index = 0
    
    for sentence in sentences:
        if ' and ' in sentence and binary_index < len(binary_message):
            parts = sentence.rsplit(' and ', 1)
            bit = binary_message[binary_index]
            if bit == '1':
                modified = parts[0] + ', and ' + parts[1]
            else:
                modified = parts[0] + ' and ' + parts[1]
            result.append(modified)
            binary_index += 1
        else:
            result.append(sentence)
    
    return '. '.join(result) + '.'

# Nhập thông điệp trực tiếp
print("Nhập thông điệp cần giấu (ví dụ: 'ok', tối đa 16 ký tự):")
message = input().strip()

if not message:
    print("Lỗi: Thông điệp không được để trống!")
else:
    # Chuyển thông điệp thành nhị phân
    binary_message = text_to_binary(message)
    if len(binary_message) > 16:
        print(f"Lỗi: Thông điệp quá dài! Cần tối đa 16 bit, bạn nhập {len(binary_message)} bit.")
    else:
        try:
            # Đọc văn bản phủ từ text1.txt
            with open("text1.txt", "r") as f:
                cover_text = f.read().strip()
            
            print(f"\nThông điệp: {message}")
            print(f"Chuỗi nhị phân: {binary_message} ({len(binary_message)} bit)")
            
            # Mã hóa
            encoded_text = hide_message(cover_text, binary_message)
            print("\nVăn bản mã hóa:")
            print(encoded_text)
            
            # Lưu văn bản mã hóa vào text2.txt
            with open("text2.txt", "w") as f:
                f.write(encoded_text)
            print("\nĐã lưu văn bản mã hóa vào text2.txt")
        except FileNotFoundError:
            print("Lỗi: Không tìm thấy text1.txt!")
        except ValueError as e:
            print(f"Lỗi: {e}")
