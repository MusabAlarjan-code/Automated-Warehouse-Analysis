import pandas as pd

# 1. قاعدة البيانات الخام للمستودع
parts_data = {
    'كود_القطعة': [501, 502, 501, 503, 502],
    'اسم_القطعة': ['فلتر زيت', 'فحمات بريك', 'فلتر زيت', 'بطارية', 'فحمات بريك'],
    'الكمية': [10, 5, 10, 2, 5]
}
df = pd.DataFrame(parts_data)

# 2. تطهير المستودع وحذف التكرار
df_clean = df.drop_duplicates()

# 3. إعادة ترتيب وتصفير الفهرس
df_clean = df_clean.reset_index(drop=True)

# 4. الذكاء التحليلي والعمليات الحسابية
total_parts = df_clean['الكمية'].sum()
average_parts = df_clean['الكمية'].mean()

# 5. العرض النهائي الفاخر للتقرير
print("--- 📦 تقرير المستودع النهائي النظيف ---")
print(df_clean)
print("-" * 40)
print(f"📊 إجمالي عدد القطع المتوفرة: {total_parts} قطعة")
print(f"📈 متوسط الكمية لكل صنف: {average_parts:.2f} قطعة")
print("-" * 40)
