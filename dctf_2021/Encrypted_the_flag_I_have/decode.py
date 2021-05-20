# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

# 画像にテキストを埋め込み
path = "./EncryptedTheFlagIHave.png"
# 画像に隠蔽されたテキストを読み込み
secret_text = Steganography.decode(path)
print(secret_text)