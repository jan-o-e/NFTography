from image_match.goldberg import ImageSignature
gis = ImageSignature()
a = gis.generate_signature('MonaLisa_Wikipedia.jpg')
b = gis.generate_signature('MonaLisa_WikiImages.jpg')
c = gis.generate_signature('Caravaggio_Wikipedia.jpg')
print('a = MonaLisa_Wikipedia.jpg\n','b = MonaLisa_WikiImages.jpg\n','c = Caravaggio_Wikipedia.jpg\n')
print("a,b",gis.normalized_distance(a, b) )
print("a,c",gis.normalized_distance(a, c) )
print("b,c",gis.normalized_distance(b, c) )

