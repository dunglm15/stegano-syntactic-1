def binary_to_text(binary):
    # Chuyển chuỗi nhị phân thành văn bản
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def extract_message(text, message_length=16):
    # Tách văn bản thành các câu
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Kiểm tra số câu có "and"
    and_sentences = [s for s in sentences if ' and ' in s]
    if len(and_sentences) < message_length:
        raise ValueError(f"Không đủ câu chứa 'and'. Cần {message_length} câu, tìm thấy {len(and_sentences)}.")
    
    binary_message = ''
    for sentence in sentences:
        if ' and ' in sentence:
            if ', and ' in sentence:
                binary_message += '1'
            else:
                binary_message += '0'
        if len(binary_message) >= message_length:
            break
    
    # Chuyển nhị phân thành văn bản
    text_message = binary_to_text(binary_message)
    return binary_message, text_message

# Đọc văn bản mã hóa
try:
    with open("text2.txt", "r") as f:
        encoded_text = f.read().strip()
    
    # Giải mã
    binary_message, extracted_message = extract_message(encoded_text)
    print(f"Chuỗi nhị phân: {binary_message}")
    print(f"Thông điệp giải mã: {extracted_message}")
    
    # Lưu thông điệp vào text3.txt
    with open("text3.txt", "w") as f:
        f.write(extracted_message)
    print("Đã lưu thông điệp vào text3.txt")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy text2.txt!")
except ValueError as e:
    print(f"Lỗi: {e}")
