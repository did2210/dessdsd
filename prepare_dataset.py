import pandas as pd
import json
from sklearn.model_selection import train_test_split

# Читаем Excel
df = pd.read_excel(r"C:\Users\Administrator\Desktop\server\data\product.xlsx")

# Создаём датасет
dataset = []

for _, row in df.iterrows():
    instruction = "Расшифруй название товара и верни в формате JSON с полями: category, brand, litrag, proizvod, pack"
    input_text = str(row['xname'])  # например: "Творог 5% 180г"
    
    output_json = {
        "category": str(row['category']),
        "brand": str(row['brand']),
        "litrag": str(row['litrag']),
        "proizvod": str(row['proizvod']),
        "pack": str(row['pack'])
    }
    
    dataset.append({
        "instruction": instruction,
        "input": input_text,
        "output": json.dumps(output_json, ensure_ascii=False)
    })

# Сохраняем в JSON
with open("training_data.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

# Разделяем на тренировочную и тестовую выборки
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)

with open("train.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, ensure_ascii=False, indent=2)

with open("test.json", "w", encoding="utf-8") as f:
    json.dump(test_data, f, ensure_ascii=False, indent=2)

print(f"✅ Созданы файлы: train.json ({len(train_data)} записей), test.json ({len(test_data)} записей)")