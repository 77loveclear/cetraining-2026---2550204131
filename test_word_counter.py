"""
测试单词统计功能
"""

from simple_word_counter import count_words_in_text_file, print_word_counts

# 测试1：使用现有的example.txt文件
print("测试1：使用 example.txt 文件")
print("=" * 50)

word_counts = count_words_in_text_file("example.txt")
if word_counts:
    print("\n前10个最常见单词:")
    print_word_counts(word_counts, top_n=10)

# 测试2：创建新的测试文件
print("\n\n测试2：创建新测试文件")
print("=" * 50)

test_text = """Hello world! Hello Python.
This is a test file for word counting.
Counting words in a file is fun.
Word, word, WORD - all should be counted as one.
Can't, won't, and don't are contractions.
Test-test, well-known, and state-of-the-art are hyphenated words.
Numbers 123, 456, 789 are also considered as words.
"""

# 写入测试文件
with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write(test_text)

print("测试文件内容:")
print("-" * 40)
print(test_text)
print("-" * 40)

# 统计测试文件
print("\n单词统计结果:")
word_counts2 = count_words_in_text_file("test_file.txt")
print_word_counts(word_counts2, top_n=15)

# 测试3：分析特定单词
print("\n\n测试3：特定单词分析")
print("=" * 50)

specific_words = ["hello", "word", "test", "123", "can't"]
for word in specific_words:
    count = word_counts2.get(word, 0)
    print(f"单词 '{word}' 出现次数: {count}")

# 测试4：总览统计信息
total_words = sum(word_counts2.values())
unique_words = len(word_counts2)
most_common_word = max(word_counts2.items(), key=lambda x: x[1])

print("\n\n测试4：总体统计")
print("=" * 50)
print(f"总单词数: {total_words}")
print(f"不同单词数: {unique_words}")
print(f"词汇丰富度: {unique_words/total_words*100:.1f}% (不同单词/总单词)")
print(f"最常见单词: '{most_common_word[0]}' 出现了 {most_common_word[1]} 次")
print(f"平均词频: {total_words/unique_words:.1f} (总单词/不同单词)")

# 测试5：写入结果文件
print("\n\n测试5：保存详细结果")
print("=" * 50)

from simple_word_counter import save_word_counts_to_file
save_word_counts_to_file(word_counts2, "test_results.txt")
print("结果已保存到 'test_results.txt'")

# 显示文件内容
with open("test_results.txt", "r", encoding="utf-8") as f:
    print("\n文件前10行:")
    lines = f.readlines()
    for line in lines[:10]:
        print(line.strip())