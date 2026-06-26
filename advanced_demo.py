"""
高级演示：展示单词统计功能的各种应用
"""

from word_counter import count_words_in_file, get_top_words, save_word_counts_to_file
from simple_word_counter import count_words_in_text_file, print_word_counts

def demonstrate_advanced_features():
    """展示高级功能"""
    print("高级演示：单词统计功能的各种应用")
    print("=" * 60)

    # 1. 分析不同的文件
    print("1. 分析不同的文本文件")
    print("-" * 40)

    files_to_analyze = [
        ("example.txt", "Python编程示例文件"),
        ("sample_text.txt", "完整版单词统计示例文件"),
        ("test_file.txt", "测试文件")
    ]

    total_stats = {}

    for filename, description in files_to_analyze:
        try:
            counts = count_words_in_text_file(filename)
            total_words = sum(counts.values())
            unique_words = len(counts)

            print(f"\n文件: {filename} ({description})")
            print(f"  总单词数: {total_words:,}")
            print(f"  不同单词数: {unique_words:,}")
            print(f"  词汇丰富度: {unique_words/total_words*100:.1f}%")

            # 汇总统计信息
            total_stats[filename] = {
                'total_words': total_words,
                'unique_words': unique_words,
                'description': description
            }

        except Exception as e:
            print(f"  无法分析文件 '{filename}': {e}")

    # 2. 对比大小写敏感 vs 不敏感
    print("\n2. 大小写敏感与不敏感对比")
    print("-" * 40)

    test_cases = [
        ("Python", "python", "PYTHON", "不同大小写的相同单词"),
        ("Word", "word", "WORD", "另一个示例")
    ]

    # 使用完整版函数测试example.txt
    case_sensitive_counts = count_words_in_file("example.txt", case_sensitive=True)
    case_insensitive_counts = count_words_in_file("example.txt", case_sensitive=False)

    for word1, word2, word3, description in test_cases:
        sens_count = case_sensitive_counts.get(word1, 0) + \
                     case_sensitive_counts.get(word2, 0) + \
                     case_sensitive_counts.get(word3, 0)

        insens_count = case_insensitive_counts.get(word1.lower(), 0)

        print(f"{description}:")
        print(f"  大小写敏感统计: {sens_count} 次")
        print(f"  大小写不敏感统计: {insens_count} 次")
        print(f"  差异: {sens_count - insens_count}")

    # 3. 不同排名范围的结果
    print("\n3. 不同排名范围的结果对比")
    print("-" * 40)

    for n in [5, 10, 15, 20]:
        top_words = get_top_words("sample_text.txt", n=n)
        if top_words:
            total_count = sum(count for _, count in top_words)
            all_counts = count_words_in_file("sample_text.txt")
            total_all_words = sum(all_counts.values())
            coverage = total_count / total_all_words * 100

            print(f"前 {n:2d} 个单词:")
            print(f"  累计次数: {total_count}/{total_all_words} ({coverage:.1f}%)")
            print(f"  单词示例: {', '.join(word for word, _ in top_words[:3])}...")

    # 4. 创建特定主题的分析
    print("\n4. 特定主题关键词分析")
    print("-" * 40)

    themes = {
        "编程": ["python", "programming", "language", "java", "c++", "logic", "coding"],
        "测试": ["test", "testing", "sample", "example", "file"],
        "计数": ["word", "counting", "count", "words", "handling"]
    }

    overall_counts = count_words_in_file("sample_text.txt")

    for theme, keywords in themes.items():
        theme_total = 0
        matches = []

        for keyword in keywords:
            if keyword in overall_counts:
                count = overall_counts.get(keyword, 0)
                if count > 0:
                    theme_total += count
                    matches.append(f"{keyword}({count})")

        if matches:
            print(f"{theme}主题:")
            print(f"  关键词: {', '.join(matches)}")
            print(f"  总出现次数: {theme_total}")

    # 5. 创建词汇分布图表示例
    print("\n5. 词汇分布图表示例")
    print("-" * 40)

    counts = count_words_in_file("sample_text.txt")
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    print("词汇频率分布:")
    for i, (word, count) in enumerate(sorted_items[:15], 1):
        bar_width = int(count * 40 / max(counts.values()))
        bar = "▓" * bar_width + "░" * (40 - bar_width)
        print(f"  {i:2d}. {word:15s}: {bar} {count}")

    # 6. 词长分析
    print("\n6. 词长分析 (单词长度统计)")
    print("-" * 40)

    word_lengths = {}
    for word in counts.keys():
        length = len(word)
        word_lengths[length] = word_lengths.get(length, 0) + 1

    print("单词长度分布:")
    for length in sorted(word_lengths.keys()):
        count = word_lengths[length]
        bar = "▓" * count
        print(f"  {length:2d} 字母的单词: {bar} ({count}个)")

    # 7. 多种统计方法比较
    print("\n7. 自定义统计参数比较")
    print("-" * 40)

    # 使用完整版函数的不同参数
    configs = [
        ("默认配置", {"case_sensitive": False, "remove_punctuation": True}),
        ("区分大小写", {"case_sensitive": True, "remove_punctuation": True}),
        ("保留标点", {"case_sensitive": False, "remove_punctuation": False})
    ]

    for name, kwargs in configs:
        result = count_words_in_file("sample_text.txt", **kwargs)
        print(f"{name}:")
        print(f"  不同单词数: {len(result)}")
        print(f"  示例单词数量变化: ", end="")

        test_words = ["the", "can't", "word", "123"]
        for test_word in test_words:
            original = test_word
            if not kwargs.get("case_sensitive", False):
                test_word = test_word.lower()
            count = result.get(test_word, 0)
            print(f"{original}({count}) ", end="")
        print()

    print("\n" + "=" * 60)
    print("演示完成！")

def demonstrate_api_usage():
    """展示API使用方法"""
    print("\n\nAPI使用方法演示")
    print("=" * 60)

    print("1. 导入功能:")
    print("""
   # 导入完整版功能
   from word_counter import (
       count_words_in_file,
       get_top_words,
       save_word_counts_to_file,
       create_sample_text_file
   )

   # 导入简化版功能
   from simple_word_counter import (
       count_words_in_text_file,
       print_word_counts,
       save_word_counts_to_file
   )
    """)

    print("\n2. 基本使用示例:")
    print("""
   # 统计单词
   counts = count_words_in_file("my_text.txt")

   # 获取前10个最常见单词
   top_10 = get_top_words("my_text.txt", n=10)

   # 保存结果
   save_word_counts_to_file(counts, "results.txt")

   # 区分大小写统计
   case_sensitive_counts = count_words_in_file("my_text.txt", case_sensitive=True)
    """)

    print("\n3. 自定义分析示例:")
    print("""
   # 查找特定单词
   counts = count_words_in_file("document.txt")
   specific_words = ["python", "programming", "algorithm"]
   for word in specific_words:
       if word in counts:
           print(f"{word}: {counts[word]}次")

   # 按词频范围过滤
   filtered = {word: count for word, count in counts.items() if count >= 5}

   # 按词长分析
   long_words = [word for word in counts if len(word) > 8]
    """)

    print("\n4. 批量处理多个文件:")
    print("""
   import os
   from word_counter import count_words_in_file

   def analyze_directory(directory):
       results = {}
       for filename in os.listdir(directory):
           if filename.endswith('.txt'):
               path = os.path.join(directory, filename)
               counts = count_words_in_file(path)
               results[filename] = len(counts)  # 不同单词数
       return results
    """)

if __name__ == "__main__":
    demonstrate_advanced_features()
    demonstrate_api_usage()

    # 创建汇总报告
    print("\n\n词汇统计汇总报告")
    print("=" * 60)

    all_counts = {}
    files = ["example.txt", "sample_text.txt", "test_file.txt"]

    for file in files:
        try:
            counts = count_words_in_text_file(file)
            if counts:
                for word, count in counts.items():
                    all_counts[word] = all_counts.get(word, 0) + count
                print(f"✓ {file}: {len(counts)}个不同单词")
        except:
            print(f"✗ {file}: 无法处理")

    if all_counts:
        print(f"\n所有文件汇总:")
        print(f"总单词数: {sum(all_counts.values()):,}")
        print(f"不同单词总数: {len(all_counts):,}")

        # 保存汇总结果
        save_word_counts_to_file(all_counts, "all_files_combined.txt")
        print("汇总结果已保存到 'all_files_combined.txt'")