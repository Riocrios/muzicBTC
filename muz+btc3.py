import os
import hashlib
import base58
import numpy as np
import sounddevice as sd
import requests
import ecdsa

# Встановлення параметрів
sample_rate = 44100  # Частота дискретизації
duration = 2.0  # Тривалість сигналу в секундах

# Частоти нот (в герцах)
frequencies = {
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
    'D': 587.33,
    'E': 659.25,
    'C': 523.25,
    'F': 349.23
}

# Функція для генерації синусоїдального сигналу
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

# Генерація випадкової мелодії
def generate_random_melody(note_count, initial_note=None):
    notes = []
    if initial_note and initial_note in frequencies:
        notes.append(initial_note)
        note_count -= 1
    notes += list(np.random.choice(list(frequencies.keys()), note_count))
    melody = np.concatenate([generate_sine_wave(frequencies[note], duration, sample_rate) for note in notes])
    return melody, notes

# Генерація біткоїн-адреси
def generate_bitcoin_addresses(data):
    # Хеш мелодії
    sha256_hash = hashlib.sha256(data).digest()

    # Генерація приватного ключа
    private_key = sha256_hash[:32]

    # Генерація публічного ключа
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()

    # Хешування публічного ключа (для legacy-адреси BTC(u))
    sha256_bpk = hashlib.sha256(public_key).digest()
    ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
    hashed_public_key = b'\x00' + ripemd160_bpk

    # Контрольна сума
    checksum = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()[:4]
    address_legacy = base58.b58encode(hashed_public_key + checksum).decode()

    # Хешування для compressed-адреси BTC(c)
    compressed_public_key = b'\x02' + vk.to_string()[:32] if vk.to_string()[32] % 2 == 0 else b'\x03' + vk.to_string()[:32]
    sha256_compressed = hashlib.sha256(compressed_public_key).digest()
    ripemd160_compressed = hashlib.new('ripemd160', sha256_compressed).digest()
    hashed_compressed_key = b'\x00' + ripemd160_compressed
    checksum_compressed = hashlib.sha256(hashlib.sha256(hashed_compressed_key).digest()).digest()[:4]
    address_compressed = base58.b58encode(hashed_compressed_key + checksum_compressed).decode()

    return address_legacy, address_compressed, private_key.hex(), sha256_hash.hex()

# Перевірка балансу через API
def check_balance(address):
    try:
        url = f"https://blockchain.info/rawaddr/{address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("final_balance", 0) / 1e8  # Баланс у BTC
    except Exception as e:
        print(f"Помилка перевірки балансу: {e}")
    return 0

# Основна програма
if __name__ == "__main__":
    try:
        # Введення налаштувань
        note_count = int(input("Введіть кількість нот для мелодії (мінімум 1): "))
        if note_count < 1:
            print("Кількість нот має бути більше 0. Встановлено 1 за замовчуванням.")
            note_count = 1

        initial_note = input("Введіть початкову ноту (або натисніть 0, щоб пропустити): ")
        if initial_note == "0" or initial_note not in frequencies:
            initial_note = None

        play_melody = input("Чи бажаєте прослухати мелодію? (y/n): ").strip().lower() == "y"

        # Безперервна робота
        while True:
            melody, notes = generate_random_melody(note_count, initial_note)
            print("Згенерована мелодія:", notes)

            if play_melody:
                sd.play(melody, sample_rate)
                sd.wait()

            # Генерація адрес
            address_legacy, address_compressed, private_key, melody_hash = generate_bitcoin_addresses(melody.tobytes())
            print("Legacy-адреса BTC(u):", address_legacy)
            print("Compressed-адреса BTC(c):", address_compressed)
            print("Приватний ключ:", private_key)
            print("Хеш мелодії:", melody_hash)

            # Перевірка балансу
            balance_legacy = check_balance(address_legacy)
            balance_compressed = check_balance(address_compressed)
            print(f"Баланс BTC(u): {balance_legacy} BTC")
            print(f"Баланс BTC(c): {balance_compressed} BTC")

            # Запис у файл, якщо знайдено баланс
            if balance_legacy > 0 or balance_compressed > 0:
                with open("REZZZZZ.txt", "a") as file:
                    file.write(f"Legacy-адреса BTC(u): {address_legacy}\n")
                    file.write(f"Compressed-адреса BTC(c): {address_compressed}\n")
                    file.write(f"Приватний ключ: {private_key}\n")
                    file.write(f"Хеш мелодії: {melody_hash}\n")
                    file.write(f"Баланс BTC(u): {balance_legacy} BTC\n")
                    file.write(f"Баланс BTC(c): {balance_compressed} BTC\n")
                    file.write("=" * 50 + "\n")
                print("Результат записано у файл REZZZZZ.txt")
    except KeyboardInterrupt:
        print("\nПрограма зупинена.")
    except Exception as e:
        print(f"Помилка: {e}")
