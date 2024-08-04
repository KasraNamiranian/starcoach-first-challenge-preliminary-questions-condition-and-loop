def create_triangle(rows):
    # تعداد حروف الفبا
    num_letters = 26
    # حروف الفبا
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # ایجاد مثلث
    for i in range(rows):
        # نمایش حروف الفبا تا ستون i
        for j in range(i + 1):
            print(alphabet[j], end=' ')
        print()

# دریافت ورودی از کاربر
try:
    rows = int(input("تعداد سطرها را وارد کنید: "))
    create_triangle(rows)
except ValueError:
    print("لطفاً یک عدد صحیح وارد کنید.")
