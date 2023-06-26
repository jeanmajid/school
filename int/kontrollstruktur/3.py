def punkt_im_rechteck(x, y, rechteck_x1, rechteck_y1, rechteck_x2, rechteck_y2):
    if x > rechteck_x1 and x < rechteck_x2 and y > rechteck_y1 and y < rechteck_y2:
        return True
    else:
        return False

rechteckx1 = float(input("Bitte geben Sie die x-Koordinate der oberen linken Ecke des Rechtecks ein: "))
rechtecky1 = float(input("Bitte geben Sie die y-Koordinate der oberen linken Ecke des Rechtecks ein: "))
rechteckx2 = float(input("Bitte geben Sie die x-Koordinate der unteren rechten Ecke des Rechtecks ein: "))
rechtecky2 = float(input("Bitte geben Sie die y-Koordinate der unteren rechten Ecke des Rechtecks ein: "))

punkt_x = float(input("Bitte geben Sie die x-Koordinate des Punktes ein: "))
punkt_y = float(input("Bitte geben Sie die y-Koordinate des Punktes ein: "))

if punkt_im_rechteck(punkt_x, punkt_y, rechteckx1, rechtecky1, rechteckx2, rechtecky2):
    print("Der Punkt liegt innerhalb des Rechtecks.")
else:
    print("Der Punkt liegt nicht innerhalb des Rechtecks.")
