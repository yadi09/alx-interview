#!/usr/bin/python3
"UTF-8"


def validUTF8(data):
    """
    UTF-8 encoding.
    """
    num_bytes = 0

    mask_0 = 1 << 7
    mask_1 = 1 << 6

    for i in data:

        m_byte = 1 << 7

        if num_bytes == 0:

            while m_byte & i:
                num_bytes += 1
                m_byte = m_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (i & mask_0 and not (i & mask_1)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
