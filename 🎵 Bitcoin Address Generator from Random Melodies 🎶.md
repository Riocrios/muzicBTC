# 🎵 Bitcoin Address Generator from Random Melodies 🎶

This unique Python script combines the world of music and cryptocurrency by generating Bitcoin addresses and private keys based on randomly created melodies. It also includes features to play the generated melody and check the balances of the generated addresses using the Blockchain API.

---

## 🌟 Features

- **Generate random melodies:** Use musical notes to create unique sound waves.
- **Bitcoin address generation:** Derive both legacy (`BTC(u)`) and compressed (`BTC(c)`) Bitcoin addresses from the melody's hash.
- **Play melodies:** Listen to the generated melodies in real-time.
- **Balance check:** Check the Bitcoin balance of generated addresses using Blockchain's API.
- **File logging:** Save addresses, private keys, and balances to a file if any funds are detected.

---

## 📦 Dependencies

Before running the script, ensure you have the following Python libraries installed:

- `numpy`: For mathematical calculations.
- `sounddevice`: To play generated melodies.
- `ecdsa`: For elliptic curve cryptography (used in Bitcoin key generation).
- `base58`: To encode Bitcoin addresses.
- `requests`: To interact with the Blockchain API.

Install all dependencies using pip:

```bash
pip install numpy sounddevice ecdsa base58 requests

🚀 How to Use
Clone the repository or download the script:

bash
Копировать код
git clone https://github.com/your-username/bitcoin-melody-generator.git
cd bitcoin-melody-generator
Run the script:

bash
install code
python melody_to_bitcoin.py
Follow the prompts to:

Specify the number of notes for the melody.
Set an optional starting note.
Choose whether to play the melody or not.
View generated Bitcoin addresses and private keys. If balances are found, they are saved in the REZZZZZ.txt file.

🎼 Example
Generated Melody: ['A', 'E', 'G']
Legacy Address (BTC(u)): 1DF2QKhtN6D6juBP8MseopzfMkE7tgHtSH
Compressed Address (BTC(c)): 19U1WAyA8h8yfAPjq7uDiHYxLbLzWH3avg
Private Key (Hex): 760c29cbe9611967c28af6c06867dd5112267f21ea4a0be9679dc1a92f27c4ee
Melody Hash (SHA-256): d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2
Balance BTC(u): 0.0 BTC
Balance BTC(c): 0.0 BTC

🔗 Resources
Bitcoin Address Generation
Elliptic Curve Cryptography
Blockchain API
Sound Device Documentation https://python-sounddevice.readthedocs.io/en/0.5.1/

❤️ Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance this project.  
BTC - 1M8xKWXJdNUqv2Yn4jsJsJPrZZVRfRqyUr
ETH-  0x22aD64862711D256E6BCD1E0b33c967553919015
SOL-  BV2kxP5ADuHbFwz9D8K6o1sYGHgHYSp4Uy1NnTtT8jqy
Doge- DTDZnK5b4WdnubyQ4M8UkmUFXCnJohjKhw
