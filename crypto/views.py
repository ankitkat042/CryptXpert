from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .algorithms.md5 import generate_md5
from .algorithms.SHA256 import generate_sha256
from .algorithms.SHA512 import generate_sha512
from .algorithms.RSA import RSA
from .algorithms.DES import DES
from .algorithms.AES import AES
from .algorithms.blowfish import blowfish_encrypt, blowfish_decrypt
from .algorithms.Triple_DES import TripleDES
from .algorithms.elgamal import ElGamal
from .algorithms.RC4 import RC4

import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def aes_encrypt_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data.get("key")
            plaintext = data.get("plaintext")
            if not key or not plaintext:
                return JsonResponse({"error": "'key' and 'plaintext' are required."}, status=400)
            if len(key) != 16:
                return JsonResponse({"error": "Key must be of 16 characters."}, status=400)
            if len(plaintext) != 16:
                return JsonResponse({"error": "Plaintext must be of 16 characters."}, status=400)
            aes = AES(key)
            ciphertext = aes.encrypt(plaintext)
            return JsonResponse({"ciphertext": ciphertext})
        except Exception as e:
            logging.error(f"Encryption error: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)


@csrf_exempt
def aes_decrypt_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data.get("key")
            ciphertext = data.get("ciphertext")
            if not key or not ciphertext:
                return JsonResponse(
                    {"error": "Both 'key' and 'ciphertext' are required."}, status=400
                )

            aes = AES(key)
            plaintext = aes.decrypt(ciphertext)
            return JsonResponse({"plaintext": plaintext})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)


@csrf_exempt
def des_encrypt_view(request):
    if request.method == "POST":
        try:
            # Try parsing JSON data if content-type is application/json
            if request.content_type == "application/json":
                data = json.loads(request.body)
                plaintext = data.get("plaintext")
                key = data.get("key")
            else:  # Fallback to form-encoded data
                plaintext = request.POST.get("plaintext")
                key = request.POST.get("key")

            print("Plaintext:", plaintext)
            print("Key:", key)

            # Validate inputs
            if not plaintext or not key:
                return JsonResponse({"error": "Plaintext and key are required."})
            if len(plaintext) != 16 or len(key) != 16:
                return JsonResponse(
                    {"error": "Plaintext and key must be 16 hexadecimal characters."}
                )

            # Encryption process
            des = DES(key)
            encrypted = des.encrypt(plaintext)
            return JsonResponse({"ciphertext": encrypted})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload."})
        except ValueError as e:
            return JsonResponse({"error": str(e)})
        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."})


@csrf_exempt
def des_decrypt_view(request):
    if request.method == "POST":
        try:
            # Parse the JSON body
            body = json.loads(request.body.decode("utf-8"))
            ciphertext = body.get("ciphertext")
            key = body.get("key")

            # Validate inputs
            if not ciphertext or not key:
                return JsonResponse(
                    {"error": "Ciphertext and key are required."}, status=400
                )
            if len(ciphertext) != 16 or len(key) != 16:
                return JsonResponse(
                    {"error": "Ciphertext and key must be 16 hexadecimal characters."},
                    status=400,
                )

            # Decrypt the ciphertext
            des = DES(key)
            decrypted = des.decrypt(ciphertext)
            return JsonResponse({"plaintext": decrypted}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(
                {"error": f"An unexpected error occurred: {str(e)}"}, status=500
            )


@csrf_exempt
def triple_des_encrypt_view(request):
    """
    Handles encryption requests for TripleDES.
    Expects JSON payload with plaintext, key1, and key2.
    """
    if request.method == "POST":
        try:
            # Parse request body
            data = json.loads(request.body)
            plaintext = data.get("plaintext")
            key1 = data.get("key1")
            key2 = data.get("key2")

            # Validate input
            if not all([plaintext, key1, key2]):
                return JsonResponse(
                    {"error": "Missing required fields (plaintext, key1, key2)"},
                    status=400,
                )

            # Encrypt plaintext
            triple_des = TripleDES(key1, key2)
            ciphertext = triple_des.encrypt(plaintext)
            return JsonResponse({"ciphertext": ciphertext}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid HTTP method. Use POST."}, status=405)


@csrf_exempt
def triple_des_decrypt_view(request):
    """
    Handles decryption requests for TripleDES.
    Expects JSON payload with ciphertext, key1, and key2.
    """
    if request.method == "POST":
        try:
            # Parse request body
            data = json.loads(request.body)
            ciphertext = data.get("ciphertext")
            key1 = data.get("key1")
            key2 = data.get("key2")

            # Validate input
            if not all([ciphertext, key1, key2]):
                return JsonResponse(
                    {"error": "Missing required fields (ciphertext, key1, key2)"},
                    status=400,
                )

            # Decrypt ciphertext
            triple_des = TripleDES(key1, key2)
            plaintext = triple_des.decrypt(ciphertext)
            return JsonResponse({"plaintext": plaintext}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid HTTP method. Use POST."}, status=405)


@csrf_exempt
def blowfish_encrypt_view(request):
    """
    View for Blowfish encryption.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            plaintext = body.get("plaintext", "")
            key = body.get("key", "")
            if not plaintext or not key:
                return JsonResponse(
                    {"error": "Plaintext and key are required"}, status=400
                )

            ciphertext = blowfish_encrypt(plaintext, key)
            return JsonResponse({"ciphertext": ciphertext})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(
                {"error": "An unexpected error occurred: " + str(e)}, status=500
            )
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def blowfish_decrypt_view(request):
    """
    View for Blowfish decryption.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            ciphertext = body.get("ciphertext", "")
            key = body.get("key", "")
            if not ciphertext or not key:
                return JsonResponse(
                    {"error": "Ciphertext and key are required"}, status=400
                )

            plaintext = blowfish_decrypt(ciphertext, key)
            return JsonResponse({"plaintext": plaintext})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse(
                {"error": "An unexpected error occurred: " + str(e)}, status=500
            )
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def rc4_encrypt_view(request):
    if request.method == "POST":
        try:
            # Parse JSON request body
            body = json.loads(request.body)
            key = body.get("key")
            plaintext = body.get("plaintext")

            # Validate inputs
            if not key or not plaintext:
                return JsonResponse(
                    {"error": "Key and plaintext are required."}, status=400
                )

            # Convert inputs to bytes
            key_bytes = key.encode("utf-8")
            plaintext_bytes = plaintext.encode("utf-8")

            # Perform RC4 encryption
            rc4 = RC4(key_bytes)
            ciphertext_bytes = rc4.encrypt(plaintext_bytes)
            ciphertext_hex = ciphertext_bytes.hex()  # Convert ciphertext to hex string

            return JsonResponse(
                {"plaintext": plaintext, "ciphertext": ciphertext_hex}, status=200
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def rc4_decrypt_view(request):
    if request.method == "POST":
        try:
            # Parse JSON request body
            body = json.loads(request.body)
            key = body.get("key")
            ciphertext = body.get("ciphertext")

            # Validate inputs
            if not key or not ciphertext:
                return JsonResponse(
                    {"error": "Key and ciphertext are required."}, status=400
                )

            # Convert inputs to bytes
            key_bytes = key.encode("utf-8")
            ciphertext_bytes = bytes.fromhex(ciphertext)  # Convert hex to bytes

            # Perform RC4 decryption
            rc4 = RC4(key_bytes)
            decrypted_bytes = rc4.decrypt(ciphertext_bytes)
            decrypted_text = decrypted_bytes.decode("utf-8")  # Convert bytes to string

            return JsonResponse({"plaintext": decrypted_text}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)


####################### Asymmetric Encryption ##############################


@csrf_exempt
def rsa_generate_keys_view(request):
    """
    View to generate RSA public and private keys.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            key_size = body.get("key_size", 512)  # Default to 512 bits
            public_key, private_key = RSA.generate_keys(key_size)
            return JsonResponse({"public_key": public_key, "private_key": private_key})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def rsa_encrypt_view(request):
    """
    View to encrypt plaintext using RSA public key.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            plaintext = body.get("plaintext", "")
            public_key = body.get("public_key", None)
            if not plaintext or not public_key:
                return JsonResponse(
                    {"error": "Plaintext and public_key are required"}, status=400
                )

            ciphertext = RSA.encrypt(plaintext, tuple(public_key))
            return JsonResponse({"ciphertext": ciphertext})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def rsa_decrypt_view(request):
    """
    View to decrypt ciphertext using RSA private key.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            ciphertext = body.get("ciphertext", None)
            private_key = body.get("private_key", None)
            if ciphertext is None or not private_key:
                return JsonResponse(
                    {"error": "Ciphertext and private_key are required"}, status=400
                )

            plaintext = RSA.decrypt(int(ciphertext), tuple(private_key))
            return JsonResponse({"plaintext": plaintext})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def elgamal_generate_keys_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            key_size = body.get("key_size", 256) 
            print(key_size)

            public_key, private_key = ElGamal.generate_keys(bits=key_size)
            return JsonResponse(
                {"key_size": key_size, "public_key": public_key, "private_key": private_key},
                status=200,
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def elgamal_encrypt_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            plaintext = body.get("plaintext")
            public_key = body.get("public_key")

            if not plaintext or not public_key:
                return JsonResponse(
                    {"error": "Plaintext and public_key are required."}, status=400
                )

            public_key = tuple(map(int, public_key))
            ciphertext = ElGamal.encrypt(plaintext, public_key)
            return JsonResponse(
                {"plaintext": plaintext, "ciphertext": ciphertext}, status=200
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def elgamal_decrypt_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            ciphertext = body.get("ciphertext")
            private_key = body.get("private_key")

            if not ciphertext or not private_key:
                return JsonResponse(
                    {"error": "Ciphertext and private_key are required."}, status=400
                )

            ciphertext = tuple(map(int, ciphertext))
            private_key = tuple(map(int, private_key))
            plaintext = ElGamal.decrypt(ciphertext, private_key)
            return JsonResponse(
                {"ciphertext": ciphertext, "decrypted": plaintext}, status=200
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)

####################### Hashing Algorithms ##############################


@csrf_exempt
def md5_view(request):
    if request.method == "POST":
        try:
            # Parse JSON payload
            body = json.loads(request.body.decode("utf-8"))
            message = body.get("message", "")
            if message:
                hash_result = generate_md5(message)
                return JsonResponse({"hash": hash_result})
            else:
                return JsonResponse({"error": "No message provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def sha256_view(request):
    if request.method == "POST":
        try:
            # Parse JSON payload
            body = json.loads(request.body.decode("utf-8"))
            message = body.get("message", "")
            if message:
                hash_result = generate_sha256(message)
                return JsonResponse({"hash": hash_result})
            else:
                return JsonResponse({"error": "No message provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def sha512_view(request):
    if request.method == "POST":
        try:
            # Parse JSON payload
            body = json.loads(request.body.decode("utf-8"))
            message = body.get("message", "")
            if message:
                hash_result = generate_sha512(message)
                return JsonResponse({"hash": hash_result})
            else:
                return JsonResponse({"error": "No message provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def home(request):
    return render(request, "index.html")
