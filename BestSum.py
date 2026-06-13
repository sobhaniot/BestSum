

input_string = """187,075,644
156,967,734
736,385,265
128,902,515
61,716,375
19,362,000
"""

target = 1071725424

# 1. تقسیم رشته به خطوط
lines = input_string.split("\n")

# 2. و 3. حذف کاماها و تبدیل به عدد صحیح
numbers_list = []
for line in lines:
    # حذف کاماها
    cleaned_line = line.replace(",", "")
    # تبدیل به عدد صحیح و اضافه کردن به لیست
    try:
        number = int(cleaned_line)
        numbers_list.append(number)
    except ValueError:
        print(f"خطا در تبدیل خط: {line}") # در صورت وجود خط خالی یا غیرعددی

print(numbers_list)

best_sum = None
best_subset = []
n = len(numbers_list)

# ----------- بررسی تمام ترکیب‌ها با بیت‌ماسک -----------
for mask in range(1 << n):  # از 0 تا 2^n
    current_sum = 0
    subset = []

    for i in range(n):
        if mask & (1 << i):  # اگر بیت i روشن باشد → عدد i انتخاب شده
            current_sum += numbers_list[i]
            subset.append(numbers_list[i])

    # اگر جمع دقیقاً برابر target شد → برگرد
    if current_sum == target:
        best_sum = current_sum
        best_subset = subset
        break

    # اگر بهتر از قبل بود (نزدیک‌تر به تارگت)
    if best_sum is None or abs(target - current_sum) < abs(target - best_sum):
        best_sum = current_sum
        best_subset = subset

print("بهترین جمع:", best_sum)
print("ترکیب انتخاب‌شده:", best_subset)