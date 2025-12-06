def closest_subset_sum(numbers, target):
    best_sum = None
    best_subset = []

    def backtrack(i, current_sum, subset):
        nonlocal best_sum, best_subset

        # اگر بهترین جمع پیدا نشده یا جمع فعلی به هدف نزدیک‌تر است
        if best_sum is None or abs(target - current_sum) < abs(target - best_sum):
            best_sum = current_sum
            best_subset = subset.copy()

        # اگر از هدف خیلی دور شد یا اعداد تمام شد → برگشت
        if i == len(numbers):
            return

        # انتخاب کردن عدد i
        backtrack(i + 1, current_sum + numbers[i], subset + [numbers[i]])

        # انتخاب نکردن عدد i
        backtrack(i + 1, current_sum, subset)

    backtrack(0, 0, [])
    return best_sum, best_subset


# ------------------------------
# مثال استفاده:
numbers = [1438050000,
2609150000,
664850000,
1036250000,
679500000,
826000000,
450000000,
135000000,
219900000,
7000000
]
target = 1780000000


best_sum, best_subset = closest_subset_sum(numbers, target)

print("بهترین جمع:", best_sum)
print("ترکیب انتخاب‌شده:", best_subset)
