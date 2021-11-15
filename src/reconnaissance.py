from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()

    max_sim = 0
    nc_max = 0
    for nc in range(10):
        im_resized = image_localisee.resize(liste_modeles[nc].H, liste_modeles[nc].W)
        simili = im_resized.similitude(liste_modeles[nc])
        print(' modele ',nc,' sim = ', simili)
        if(simili > max_sim):
            max_sim = simili
            nc_max = nc
            print (" chiffre lu = ", nc_max) 
    return(nc_max)

