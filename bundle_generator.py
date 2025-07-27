import json
import random
from datetime import datetime
import os

def generate_bundle():
    # Список доступных криптоактивов
    assets = [
        {"name": "BTC", "color": "#f7931a"},
        {"name": "ETH", "color": "#627eea"},
        {"name": "SOL", "color": "#00d395"},
        {"name": "DOT", "color": "#5d78ff"},
        {"name": "BNB", "color": "#f3ba2f"},
        {"name": "ADA", "color": "#0033ad"},
        {"name": "XRP", "color": "#23292f"},
        {"name": "DOGE", "color": "#d07c16"},
        {"name": "SHIB", "color": "#ffc000"},
        {"name": "USDT", "color": "#26a17b"}
    ]
    
    # Выбираем 3 случайных актива
    selected = random.sample(assets, 3)
    
    # Генерируем проценты
    percentages = [random.randint(20, 70) for _ in range(3)]
    total = sum(percentages)
    percentages = [round(p/total*100) for p in percentages]
    
    # Корректируем сумму до 100%
    if sum(percentages) != 100:
        percentages[0] += 100 - sum(percentages)
    
    return {
        "id": random.randint(1000, 9999),
        "name": f"{selected[0]['name']}/{selected[1]['name']} Bundle",
        "profit": f"+{random.randint(5, 25)}.{random.randint(0,9)}%",
        "duration": f"{random.randint(1, 24)}h",
        "risk": random.choice(["Low", "Medium", "High"]),
        "assets": [
            {"name": selected[0]['name'], "percentage": percentages[0], "color": selected[0]['color']},
            {"name": selected[1]['name'], "percentage": percentages[1], "color": selected[1]['color']},
            {"name": selected[2]['name'], "percentage": percentages[2], "color": selected[2]['color']}
        ],
        "currentInvested": round(random.uniform(0, 15), 2),
        "timeRemaining": random.randint(60, 1800),  # 1-30 минут
        "generatedAt": datetime.utcnow().isoformat() + "Z"
    }

def generate_bundles_file():
    # Генерируем 6 случайных сборок
    bundles = [generate_bundle() for _ in range(6)]
    
    data = {
        "lastUpdated": datetime.utcnow().isoformat() + "Z",
        "bundles": bundles
    }
    
    # Сохраняем в файл
    with open("bundles.json", "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully generated {len(bundles)} bundles")

if __name__ == "__main__":
    generate_bundles_file()
