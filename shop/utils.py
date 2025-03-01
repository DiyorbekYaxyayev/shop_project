import qrcode

repo_url = "https://github.com/DiyorbekYaxyayev/shop_project"
qr = qrcode.make(repo_url)
qr.show()  # QR kodni ekranda ochadi
qr.save("shop_project_qr.png")  # QR kodni fayl sifatida saqlaydi
