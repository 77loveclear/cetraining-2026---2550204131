"""
单词统计器 - 统计文本文件中每个单词的出现次数
"""

import re
from collections import Counter
from typing import Dict, List, Optional


def count_words_in_file(file_path: str,
                       case_sensitive: bool = False,
                       remove_punctuation: bool = True) -> Dict[str, int]:
    """
    统计文本文件中每个单词的出现次数

    参数:
        file_path (str): 文本文件的路径
        case_sensitive (bool): 是否区分大小写，默认为False（不区分）
        remove_punctuation (bool): 是否移除标点符号，默认为True

    返回:
        Dict[str, int]: 单词到出现次数的映射字典

    示例:
        >>> counts = count_words_in_file("sample.txt")
        >>> print(counts.get("the", 0))
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 '{file_path}' 不存在")
    except IOError as e:
        raise IOError(f"读取文件时出错: {e}")

    # 如果不区分大小写，将文本转换为小写
    if not case_sensitive:
        text = text.lower()

    if remove_punctuation:
        # 使用正则表达式移除标点符号，保留字母数字字符和连字符
        # 匹配单词字符（字母、数字、下划线）和连字符
        words = re.findall(r'\b[\w\'-]+\b', text)
    else:
        # 简单分割，不处理标点符号
        words = re.findall(r'\b\S+\b', text)

    # 过滤空字符串
    words = [word for word in words if word]

    # 使用Counter统计频率
    word_counts = Counter(words)

    # 转换为普通字典
    return dict(word_counts)


def get_top_words(file_path: str,
                  n: int = 10,
                  case_sensitive: bool = False) -> List[tuple]:
    """
    获取出现频率最高的前n个单词

    参数:
        file_path (str): 文本文件的路径
        n (int): 要返回的单词数量，默认为10
        case_sensitive (bool): 是否区分大小写，默认为False

    返回:
        List[tuple]: 元组列表，每个元组为(单词, 出现次数)，按频率降序排列
    """
    word_counts = count_words_in_file(file_path, case_sensitive)

    # 按频率降序排序
    sorted_words = sorted(word_counts.items(),
                         key=lambda x: x[1],
                         reverse=True)

    # 返回前n个单词
    return sorted_words[:n]


def save_word_counts_to_file(word_counts: Dict[str, int],
                           output_file: str,
                           sort_by_frequency: bool = True) -> None:
    """
    将单词统计结果保存到文件

    参数:
        word_counts (Dict[str, int]): 单词统计字典
        output_file (str): 输出文件路径
        sort_by_frequency (bool): 是否按频率排序，默认为True
    """
    items = word_counts.items()

    if sort_by_frequency:
        items = sorted(items, key=lambda x: x[1], reverse=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in items:
            file.write(f"{word}: {count}\n")


def create_sample_text_file() -> str:
    """
    创建一个示例文本文件用于测试

    返回:
        str: 创建的示例文件路径
    """
    sample_text = """The quick brown fox jumps over the lazy dog.
This is a sample text file for testing word counting.
It contains multiple sentences, some with repeated words.
The quick brown fox is quick and brown.
Programming is fun! Programming requires logic.
Python, Java, and C++ are programming languages.
Word counting should handle punctuation like commas, periods, and exclamation marks!
Let's test contractions like can't, won't, and don't.
Numbers like 123 and 456 should also be counted.
"""

    file_path = "sample_text.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(sample_text)

    return file_path


if __name__ == "__main__":
    print("单词统计程序示例")
    print("=" * 50)

    try:
        # 1. 创建示例文本文件
        print("1. 创建示例文本文件...")
        sample_file = create_sample_text_file()
        print(f"   示例文件已创建: {sample_file}")

        # 2. 统计所有单词
        print("\n2. 统计所有单词出现次数...")
        all_counts = count_words_in_file(sample_file)
        print(f"   总计发现 {len(all_counts)} 个不同的单词")

        # 3. 获取前10个最常出现的单词
        print("\n3. 前10个最常出现的单词:")
        top_words = get_top_words(sample_file, n=10)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"   {i:2d}. {word:15s}: {count:3d} 次")

        # 4. 区分大小写的统计示例
        print("\n4. 区分大小写的统计示例 (前5个单词):")
        case_sensitive_counts = count_words_in_file(sample_file, case_sensitive=True)
        top_case_sensitive = sorted(case_sensitive_counts.items(),
                                   key=lambda x: x[1],
                                   reverse=True)[:5]
        for word, count in top_case_sensitive:
            print(f"   {word:15s}: {count:3d} 次")

        # 5. 保存统计结果到文件
        print("\n5. 保存统计结果到文件...")
        save_word_counts_to_file(all_counts, "word_counts_output.txt")
        print("   结果已保存到: word_counts_output.txt")

        # 6. 显示文件内容预览
        print("\n6. 示例文件内容预览:")
        with open(sample_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines[:3], 1):
                print(f"   行 {i}: {line.strip()}")

        print("\n" + "=" * 50)
        print("示例程序执行完成!")

    except Exception as e:
        print(f"执行过程中出错: {e}")