def calculate_average(numbers):
    """计算列表的平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 测试一下
data = [10, 20, 30, 40, 50]
print(f"平均值是: {calculate_average(data)}")