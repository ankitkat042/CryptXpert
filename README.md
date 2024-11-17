# [CryptXpert: Online Encryption and Decryption Platform](https://github.com/ankitkat042/CryptXpert)
This project is part of [CSE546](https://techtree.iiitd.edu.in/viewDescription/filename?=CSE546)-Applied Cryptography course at IIIT-Delhi under the guidance of [Dr. Ravi Anand](https://www.iiitd.ac.in/ravianand). 
---

## Supported Algorithms

### Symmetric Key Encryption
- **AES**  
- **DES**  
- **Triple DES**  
- **Blowfish**  
- **RC4**  

### Asymmetric Key Encryption
- **RSA**  
- **ElGamal**  

### Hashing
- **MD5**  
- **SHA-256**  
- **SHA-512**  

---

## How to Run the Project

Follow these steps to set up and run the **CryptXpert** platform locally:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/CryptXpert.git
cd CryptXpert
```

### 2. Install the Required Dependencies
Install Django and Other Dependencies:
Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

### 3. Run the Development Server
```
python manage.py runserver
```
- Now visit http://127.0.0.1:8000/crypto/


For Input/Output, read [Example.md](./Example.md)

#### To read on individual algorithms, you can visit the readme of each algorithm in the following directories: for example [AES](./Readmes_for_all_algo/Readme_AES.md)    

## Current Limitations
- NO modes of operations have been implemented for the symmetric key algorithms.

- Some input validations are missing.

- The platform is not yet optimized for production use.

- The platform does not support file encryption/decryption.

## Future Enhancements
- Implement modes of operations for symmetric key algorithms.

- Add support for file encryption/decryption.

- Improve input validation and error handling.

- Consistent UI/UX across the platform with better responsiveness.

- Elgamal encryption/decryption is works default for 256 bit key size. 




## Contributors
- [Ankit Kumar]()
- [Ankit Bisht]()

