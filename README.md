# Kicad HomeFab plugin
Verzija: 0.1.1
Datum: 16. 09. 2024

Python program, ki se bo s časom (verjetno) razvil v vtičnik za program KiCad. 
trenutno program združi Gerber datoteko z vezjem in Gerber datoteko za vrtanje v eno datoteko.

## Zahteve
- testirano na Python _3.12.0_

## Uporaba 
1. program mora biti v isti mapi kot so Gerber datoteke
2. datoteka z vezjem mora biti poimenovana z _gerber.gbr_
3. datoteka za vrtanje mora biti poimenovana z _dril.gbr_
4. poženi program, ki bo ustvaril datoteko _homefab\_gerber.gbr_

## Spremembe
- _v0.1.1_ (16. 09. 2024):
    - spremenjena velikost luknje na 0.8 mm 
    - odstranjena neuporabljena knjižnica _time_