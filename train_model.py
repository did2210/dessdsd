import subprocess
import sys

def run_training():
    """Запускает обучение модели через Ollama"""
    
    # Команда для обучения
    cmd = [
        "ollama", "create", "my_brand_model",
        "-f", "Modelfile"
    ]
    
    print("🚀 Запускаем обучение модели...")
    print(f"Команда: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        # Запускаем процесс с выводом в реальном времени
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        # Читаем вывод в реальном времени
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(f"📝 {output.strip()}")
        
        # Проверяем ошибки
        stderr = process.stderr.read()
        if stderr:
            print(f"❌ Ошибки: {stderr}")
        
        # Проверяем результат
        return_code = process.poll()
        if return_code == 0:
            print("✅ Обучение завершено успешно!")
        else:
            print(f"❌ Обучение завершилось с кодом: {return_code}")
            
    except Exception as e:
        print(f"❌ Ошибка при запуске: {e}")

if __name__ == "__main__":
    run_training()