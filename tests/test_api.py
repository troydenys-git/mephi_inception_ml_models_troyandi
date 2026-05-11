import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

X_TEST_PATH = BASE_DIR / "data" / "artifacts" / "X_test.csv"
Y_TEST_PATH = BASE_DIR / "data" / "artifacts" / "y_test.csv"

if __name__ == '__main__':
    
    print("\n[TEST] /health")

    health = requests.get('http://localhost:5000/health')

    print("status_code:", health.status_code)

    if health.status_code == 200:
        print("response:", health.json())
    else:
        print(health.text)
    
    print("\n[TEST] /predict")
        
    # загружаем тестовые данные
    X_test = pd.read_csv(X_TEST_PATH)
    y_test = pd.read_csv(Y_TEST_PATH)
    
    # берём случайный индекс
    idx = X_test.sample(1).index[0]

    # извлекаем сэмпл
    sample = X_test.loc[idx].to_dict()
    true_label = y_test.loc[idx].values[0]

    # отправляем запрос в сервис
    r = requests.post(
        'http://localhost:5000/predict',
        json=sample
    )

    # выводим статус
    print("status_code:", r.status_code)

    if r.status_code == 200:
        result = r.json()

        print("prediction:", result["prediction"])
        print("probability:", result["probability"])
        print("model_version:", result["model_version"])
        print("true_label:", true_label)

    else:
        print(r.text)