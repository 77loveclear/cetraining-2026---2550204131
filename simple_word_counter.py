"""
简单的单词统计函数 - 统计文本文件中每个单词的出现次数
"""

import re
from collections import Counter


def count_words_in_text_file(file_path: str) -> dict:
    """
    统计文本文件中每个单词的出现次数

    参数:
        file_path: 文本文件的路径

    返回:
        包含单词和对应出现次数的字典

    功能说明:
        1. 读取文件内容
        2. 将文本转换为小写（不区分大小写）
        3. 移除标点符号
        4. 分割单词并统计出现次数
    """
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{file_path}'")
        return {}
    except UnicodeDecodeError:
        # 如果utf-8编码失败，尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                text = f.read()
        except:
            print(f"错误: 无法读取文件 '{file_path}'，请检查文件编码")
            return {}

    # 转换为小写（不区分大小写）
    text = text.lower()

    # 使用正则表达式提取单词
    # 匹配连续的字母、数字、连字符和撇号（用于处理如can't这样的单词）
    words = re.findall(r"\b[\w'-]+\b", text)

    # 统计单词出现次数
    word_counter = Counter(words)

    # 转换为普通字典
    return dict(word_counter)


def print_word_counts(word_counts: dict, top_n: int = None) -> None:
    """
    打印单词统计结果

    参数:
        word_counts: 单词统计字典
        top_n: 只显示前N个最常见的单词，None表示显示所有
    """
    if not word_counts:
        print("没有找到任何单词")
        return

    # 按出现次数降序排序
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    if top_n:
        sorted_words = sorted_words[:top_n]

    print(f"{'单词':<20} {'出现次数':<10}")
    print("-" * 30)

    total_words = sum(word_counts.values())
    unique_words = len(word_counts)

    for word, count in sorted_words:
        percentage = (count / total_words) * 100
        print(f"{word:<20} {count:<10} ({percentage:.1f}%)")

    print("-" * 30)
    print(f"总单词数: {total_words}")
    print(f"不同单词数: {unique_words}")


def save_word_counts_to_file(word_counts: dict, output_file: str) -> None:
    """
    将单词统计结果保存到文件

    参数:
        word_counts: 单词统计字典
        output_file: 输出文件路径
    """
    # 按出现次数降序排序
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("单词统计结果\n")
        f.write("=" * 40 + "\n")

        total_words = sum(word_counts.values())
        unique_words = len(word_counts)

        f.write(f"总单词数: {total_words}\n")
        f.write(f"不同单词数: {unique_words}\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'单词':<20} {'出现次数':<10} {'百分比':<10}\n")
        f.write("-" * 40 + "\n")

        for word, count in sorted_words:
            percentage = (count / total_words) * 100 if total_words > 0 else 0
            f.write(f"{word:<20} {count:<10} {percentage:.2f}%\n")


# 示例用法
if __name__ == "__main__":
    # 示例文本
    example_text = """
    Python is a popular programming language.
    Python is used for web development, data analysis, and artificial intelligence.
    Programming in Python is fun and productive.
    Python, python, PYTHON - all should be counted as the same word.
    """

    # 创建示例文件
    example_file = "example.txt"
    with open(example_file, 'w', encoding='utf-8') as f:
        f.write(example_text)

    print("示例: 统计文本文件中每个单词的出现次数")
    print("=" * 60)

    # 统计单词
    word_counts = count_words_in_text_file(example_file)

    if word_counts:
        print(f"文件 '{example_file}' 的单词统计结果:")
        print_word_counts(word_counts, top_n=10)

        # 保存结果到文件
        output_file = "word_counts.txt"
        save_word_counts_to_file(word_counts, output_file)
        print(f"\n详细结果已保存到 '{output_file}'")

    print("=" * 60)
    print("\n如何使用这个函数:")
    print("""
    1. 在你的代码中导入函数:
       from simple_word_counter import count_words_in_text_file

    2. 调用函数统计单词:
       word_counts = count_words_in_text_file("your_file.txt")

    3. 查看结果:
       for word, count in word_counts.items():
           print(f"{word}: {count}")
    """)