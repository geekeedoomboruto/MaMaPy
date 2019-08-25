class Maman:
    def __init__(self, enfants_a_soccuper=1):
        self.enfants_a_soccuper = enfants_a_soccuper

maman = Maman(6)
if maman.enfants_a_soccuper < 1:
    print("Maman s'occupe d'aucun enfants")
elif maman.enfants_a_soccuper == 1:
    print("Maman s'occupe d'un enfant")
else:
    print(f"Maman s'occupe de {maman.enfants_a_soccuper} enfants")