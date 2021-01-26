from flask import Flask, request
from py3dbp import Packer, Bin, Item

app = Flask (__name__)

packer = Packer()

packer.add_bin(Bin('Moto-Ogi', 52.0, 36.0, 52.0, 20.0))
packer.add_bin(Bin('moto-Lala', 35.0, 40.0, 30.0, 20.0))
packer.add_bin(Bin('fiorino-Lala', 188.0, 133.0, 108.0, 500.0))
packer.add_bin(Bin('carreto-Lala', 300.0, 180.0, 200.0, 1500.0))



for b in packer.bins:
    print (b.string())

    print("Coube:")
    for item in b.items:
        print (" ", item.string())

    print("Não coube:")
    for item in b.unfitted_items:
        print (" ", item.string())






