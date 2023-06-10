a = """Duis consequat lorem nec risus tincidunt auctor. Nulla ultricies, nunc quis vehicula suscipit, metus sem posuere justo, eu posuere nulla justo id est. Duis at urna egestas, auctor ipsum sed, fermentum lectus. Vestibulum aliquam convallis auctor. Nunc ac maximus libero, nec suscipit metus. Nam ornare a diam quis sollicitudin. Fusce convallis luctus arcu, a dignissim nisl gravida ut. In ante est, volutpat non ligula at, convallis fringilla dolor. Aenean in velit at eros maximus viverra ut a nibh."""
print(a)
print(len(a))
print(a.replace(" ", "KK")) # 77 szó van benne.
b = ("""DuisKKconsequatKKloremKKnecKKrisusKKtinciduntKKauctor.KKNullaKKultricies,KKnuncKKquisKKvehiculaKKsuscipit,KKmetusKKsemKKposuereKKjusto,KKeuKKposuereKKnullaKKjustoKKidKKest.KKDuisKKatKKurnaKKegestas,KKauctorKKipsumKKsed,KKfermentumKKlectus.KKVestibulumKKaliquamKKconvallisKKauctor.KKNuncKKacKKmaximusKKlibero,KKnecKKsuscipitKKmetus.KKNamKKornareKKaKKdiamKKquisKKsollicitudin.KKFusceKKconvallisKKluctusKKarcu,KKaKKdignissimKKnislKKgravidaKKut.KKInKKanteKKest,KKvolutpatKKnonKKligulaKKat,KKconvallisKKfringillaKKdolor.KKAeneanKKinKKvelitKKatKKerosKKmaximusKKviverraKKutKKaKKnibh.""")
print(len(b))
print("est" in a) # van benne "est" szó. 
print(a.replace("est", "ffff"))
c = """Duis consequat lorem nec risus tincidunt auctor. Nulla ultricies, nunc quis vehicula suscipit, metus sem posuere justo, eu posuere nulla justo id ffff. Duis at urna egffffas, auctor ipsum sed, fermentum lectus. Vffffibulum aliquam convallis auctor. Nunc ac maximus libero, nec suscipit metus. Nam ornare a diam quis sollicitudin. Fusce convallis luctus arcu, a dignissim nisl gravida ut. In ante ffff, volutpat non ligula at, convallis fringilla dolor. Aenean in velit at eros maximus viverra ut a nibh."""
print(c)
print(len(c)) # 4 darab "est" van benne.
