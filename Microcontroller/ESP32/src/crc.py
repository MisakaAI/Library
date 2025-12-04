# CRC16

def calc_crc16(buffer):
    crc = 0x0000

    for i in range(len(buffer)):
        for j in range(8):  # 处理每个字节的8位
            # 检查CRC最高位是否为1
            if crc & 0x8000:
                crc = (crc << 1) & 0xFFFF  # 左移1位，并确保为16位
                crc ^= 0x1021
            else:
                crc = (crc << 1) & 0xFFFF  # 左移1位，并确保为16位

            # 检查当前字节的当前位是否为1
            if buffer[i] & (0x80 >> j):
                crc ^= 0x1021

            # 确保CRC始终是16位
            crc &= 0xFFFF

    return crc


# CRC-16 CCITT (X.25)
CRC16_POLY = 0x1021
CRC16_INIT = 0x0000


# 预先计算 256 个可能的 8 位数据输入对应的 CRC 值
def generate_crc16_table(poly=CRC16_POLY):
    table = []
    for i in range(256):
        crc = i << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc = crc << 1
            crc &= 0xFFFF
        table.append(crc)
    return table


CRC16_TABLE = generate_crc16_table()


# 使用查表法计算 CRC-16
def calc_crc16_lut(buffer: bytes):
    table = CRC16_TABLE
    crc = CRC16_INIT  # 0x0000

    for byte in buffer:
        # 将当前 crc 的高 8 位与数据字节异或，得到查表索引
        index = (crc >> 8) ^ byte
        # 将 crc 左移 8 位 (丢弃高 8 位)，然后与查表结果异或
        crc = (crc << 8) ^ table[index]
        # 确保结果保持在 16 位
        crc &= 0xFFFF
    return f"{crc:04X}"



# 使用示例
if __name__ == "__main__":
    # 测试数据
    test_data = b"1234567890"
    result = calc_crc16(test_data)
    result_lut = calc_crc16_lut(test_data)

    print(f"测试数据: {test_data.decode('utf-8')}")
    print(f"数据长度: {len(test_data)}")
    print(f"CRC16: 0x{result:04X}")
    print(f"查表法: 0x{result_lut}")
