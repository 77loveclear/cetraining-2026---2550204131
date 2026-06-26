"""
交互式测试：手动测试单词统计功能
"""

from simple_word_counter import count_words_in_text_file, print_word_counts

def create_test_cases():
    """创建各种测试用例"""
    test_cases = []

    # 测试用例1：简单英文文本
    test1 = {
        "name": "简单英文",
        "text": "Hello world. Hello everyone. How are you?",
        "expected_words": 7  # hello(2), world(1), everyone(1), how(1), are(1), you(1)
    }

    # 测试用例2：带标点的复杂文本
    test2 = {
        "name": "复杂标点",
        "text": "Mr. & Mrs. Smith's car, it's red! Isn't it nice?",
        "expected_words": 10  # mr, mrs, smith's, car, it's, red, isn't, it, nice
    }

    # 测试用例3：带数字的文本
    test3 = {
        "name": "数字文本",
        "text": "I have 3 apples, 2 bananas, and 1.5 oranges. Version 2.0 is out!",
        "expected_words": 12  # i, have, 3, apples, 2, bananas, and, 1.5, oranges, version, 2.0, is, out
    }

    # 测试用例4：连字符词
    test4 = {
        "name": "连字符词",
        "text": "The well-known author wrote a state-of-the-art book for self-learning.",
        "expected_words": 9  # the, well-known, author, wrote, a, state-of-the-art, book, for, self-learning
    }

    test_cases.extend([test1, test2, test3, test4])
    return test_cases

def run_interactive_test():
    """运行交互式测试"""
    print("交互式单词统计测试")
    print("=" * 60)

    test_cases = create_test_cases()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*50}")
        print(f"测试 {i}: {test_case['name']}")
        print(f"{'='*50}")

        # 创建临时文件
        filename = f"test_case_{i}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(test_case['text'])

        # 显示测试文本
        print(f"测试文本:")
        print(f"  {test_case['text']}")
        print(f"\n期望不同单词数: {test_case.get('expected_words', '未知')}")

        # 运行单词统计
        word_counts = count_words_in_text_file(filename)

        if word_counts:
            print(f"\n实际统计结果:")
            print(f"  不同单词数: {len(word_counts)}")
            print(f"  总单词数: {sum(word_counts.values())}")

            # 显示前5个单词
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            print(f"  最常见单词 (前5):")
            for word, count in sorted_words[:5]:
                print(f"    {word}: {count}次")

            # 验证期望值
            expected = test_case.get('expected_words')
            if expected:
                if len(word_counts) == expected:
                    print(f"  ✓ 通过: 不同单词数符合预期 ({expected})")
                else:
                    print(f"  ✗ 失败: 不同单词数 {len(word_counts)} ≠ 预期 {expected}")
        else:
            print("  ✗ 错误: 无法统计单词")

        # 询问用户是否继续
        if i < len(test_cases):
            print("\n" + "-" * 50)
            user_choice = input(f"按回车继续测试{i+1}，或输入'q'退出: ")
            if user_choice.lower() == 'q':
                break

def analyze_user_input():
    """分析用户输入的文本"""
    print("\n" + "=" * 60)
    print("自定义文本分析")
    print("=" * 60)

    while True:
        print("\n输入要分析的文本 (输入 'quit' 退出):")
        user_text = input("> ")

        if user_text.lower() == 'quit':
            break

        if not user_text.strip():
            print("请输入有效文本")
            continue

        # 保存到临时文件
        with open("user_input.txt", 'w', encoding='utf-8') as f:
            f.write(user_text)

        # 分析文本
        word_counts = count_words_in_text_file("user_input.txt")

        if word_counts:
            print(f"\n分析结果:")
            print_word_counts(word_counts, top_n=10)

            # 额外分析
            total_words = sum(word_counts.values())
            unique_words = len(word_counts)

            print(f"\n统计摘要:")
            print(f"  字符数: {len(user_text)}")
            print(f"  单词数: {total_words}")
            print(f"  不同单词: {unique_words}")
            print(f"  平均词长: {sum(len(word) for word in word_counts)/unique_words:.1f}")

            # 找出最长单词
            longest_word = max(word_counts.keys(), key=len)
            print(f"  最长单词: '{longest_word}' ({len(longest_word)}个字母)")

            # 建议
            if unique_words/total_words < 0.3:
                print("  词汇多样性: 较低 (考虑使用更多不同的词汇)")
            elif unique_words/total_words < 0.6:
                print("  词汇多样性: 中等")
            else:
                print("  词汇多样性: 较高")
        else:
            print("  无法分析文本")

if __name__ == "__main__":
    print("=" * 60)
    print("单词统计功能交互式测试")
    print("=" * 60)

    # 运行预定义测试用例
    run_interactive_test()

    # 运行自定义分析
    analyze_user_input()

    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)

    # 清理临时文件
    import os
    for i in range(1, 5):
        filename = f"test_case_{i}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"清理文件: {filename}")

    if os.path.exists("user_input.txt"):
        os.remove("user_input.txt")
        print(f"清理文件: user_input.txt")