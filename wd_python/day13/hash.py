"""
hash 哈希表

Author:LXQing
Date:2023/7/8
"""

MAXKEY = 1000


def elf_hash(hash_str):
    h, g = 0, 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        # ~g是给g按位取反的意思
        h &= ~g
    return h % MAXKEY


def use_hash():
    str_list = ['lee', 'wang', 'zhang', 'zhao', 'liu']
    hash_table = [None] * MAXKEY  # 哈希表初始化
    for i in str_list:
        hash_table[elf_hash(i)] = i
        print('哈希冲突')
    else:
        hash_table[elf_hash(i)] = i
    pass


if __name__ == '__main__':
    use_hash()
    pass
