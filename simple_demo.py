"""
简单演示：单词统计功能
"""
from simple_word_counter import count_words_in_text_file, print_word_counts

print("单词统计功能演示")
print("=" * 60)

# 1. 创建测试文件
test_text = """Python is a popular programming language.
Python is used for web development and data analysis.
Programming in Python is fun and productive.
Let's learn Python programming together!"""

# 保存测试文件
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write(test_text)

print("测试文件内容:")
print("-" * 40)
print(test_text)
print("-" * 40)

# 2. 统计单词
print("\n单词统计结果:")
print("-" * 40)
word_counts = count_words_in_text_file("demo.txt")

if word_counts:
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)

    print(f"总单词数: {total_words}")
    print(f"不同单词数: {unique_words}")
    print(f"词汇丰富度: {unique_words/total_words*100:.1f}%")

    # 显示前10个单词
    print("\n前10个最常见单词:")
    print_word_counts(word_counts, top_n=10)

    # 3. 详细分析
    print("\n详细分析:")
    print("-" * 40)

    # 查找Python相关单词
    python_related = ["python", "programming", "language", "development"]
    python_count = 0

    for word in python_related:
        count = word_counts.get(word.lower(), 0)
        python_count += count
        if count > 0:
            print(f"单词 '{word}': {count}次")

    # 词长分析
    word_lengths = {}
    for word in word_counts.keys():
        length = len(word)
        word_lengths[length] = word_lengths.get(length, 0) + 1

    print("\n词长分布:")
    for length in sorted(word_lengths.keys()):
        count = word_lengths[length]
        print(f"  {length}字母单词: {count}个")

# 4. 创建总结
print("\n" + "=" * 60)
print("总结")
print("=" * 60)

if word_counts:
    # 找到最常出现的单词
    most_common = max(word_counts.items(), key=lambda x: x[1])
    least_common = min(word_counts.items(), key=lambda x: x[1])

    print(f"最常出现的单词: '{most_common[0]}' ({most_common[1]}次)")
    print(f"最少出现的单词: '{least_common[0]}' ({least_common[1]}次)")

    # 平均词频
    avg_frequency = total_words / unique_words
    print(f"平均每个单词出现频率: {avg_frequency:.2f}次")

    # 建议
    if avg_frequency > 3:
        print("建议: 文本中某些单词使用过于频繁")
    elif avg_frequency < 1.5:
        print("建议: 词汇多样性良好")
    else:
        print("建议: 词汇使用适中")

print("\n演示完成！")