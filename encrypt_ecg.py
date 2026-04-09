from cryptography.fernet import Fernet
import os

# 1. Generer en nøgle
key = Fernet.generate_key()

# 2. Gem nøglen lokalt i VS Code 
with open('filekey.key', 'wb') as f:
    f.write(key)

# 3. Indlæser nøglen
fernet = Fernet(key)

# 4. Stien til billedet (Jeg bruger den lange sti her, da billedet ligger i en undermappe)
file_path = r'C:\Users\ralfa\OneDrive\Skrivebord\ECG\Normal Person\Normal(1).png'

if os.path.exists(file_path):
    # 5. Læs billedet
    with open(file_path, 'rb') as file:
        original = file.read()

    # 6. Krypterer billedet
    encrypted = fernet.encrypt(original)

    # 7. Gem det krypterede billede lokalt i VS Code
    with open('Normal(1)_encrypted.png', 'wb') as file:
        file.write(encrypted)
    
    print("--- FÆRDIG ---")
else:
    print("Fejl: Kunne ikke finde billedet på skrivebordet.")