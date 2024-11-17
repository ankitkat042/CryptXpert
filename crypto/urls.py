from django.urls import path
from .views import md5_view
from .views import sha256_view
from .views import sha512_view
from .views import rsa_generate_keys_view, rsa_encrypt_view, rsa_decrypt_view
from .views import des_encrypt_view, des_decrypt_view
from .views import blowfish_encrypt_view, blowfish_decrypt_view
from .views import aes_encrypt_view, aes_decrypt_view
from .views import triple_des_encrypt_view, triple_des_decrypt_view
from .views import elgamal_encrypt_view, elgamal_decrypt_view, elgamal_generate_keys_view
from .views import rc4_encrypt_view, rc4_decrypt_view
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('md5/', md5_view, name='md5'),
    path('sha256/', sha256_view, name='sha256'),
    path('sha512/', sha512_view, name='sha512'),
    path('rsa/generate_keys/', rsa_generate_keys_view, name='rsa_generate_keys'),
    path('rsa/encrypt/', rsa_encrypt_view, name='rsa_encrypt'),
    path('rsa/decrypt/', rsa_decrypt_view, name='rsa_decrypt'),
    path('des/encrypt/', des_encrypt_view, name='des_encrypt'),
    path('des/decrypt/', des_decrypt_view, name='des_decrypt'),
    path('blowfish/encrypt/', blowfish_encrypt_view, name='blowfish_encrypt'),
    path('blowfish/decrypt/', blowfish_decrypt_view, name='blowfish_decrypt'),
    path("aes/encrypt/", aes_encrypt_view, name="aes_encrypt"),
    path("aes/decrypt/", aes_decrypt_view, name="aes_decrypt"),
    path("3des/encrypt/", triple_des_encrypt_view, name="triple_des_encrypt"),
    path("3des/decrypt/", triple_des_decrypt_view, name="triple_des_decrypt"),
    path("elgamal/encrypt/", elgamal_encrypt_view, name="elgamal_encrypt"),
    path("elgamal/decrypt/", elgamal_decrypt_view, name="elgamal_decrypt"),
    path("elgamal/generate_keys/", elgamal_generate_keys_view, name="elgamal_generate_keys"),
    path('rc4/encrypt/', rc4_encrypt_view, name='rc4_encrypt'),
    path('rc4/decrypt/', rc4_decrypt_view, name='rc4_decrypt'),  
]
