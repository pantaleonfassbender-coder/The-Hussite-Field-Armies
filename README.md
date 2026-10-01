# The Hussite Field Armies

A documentary apparatus for the Hussite field armies, 1420–1434: how did an army of peasants and townsmen beat five crusades, and why was it destroyed at Lipany? Public-domain sources with the original (Czech, Latin, German) beside the English, a timeline linked into the texts, and a list of what is still to come.

Its thesis, to be tested against the texts: the ordinance won every battle, and the day it was broken, everything was lost. Jan Žižka's military ordinance of 1423 bound lords, townsmen and peasants to the same discipline and the same penalties; at Lipany on 30 May 1434 the foot left their wagons against their captains' order, and the field armies were destroyed by the lords of Bohemia.

It continues [The Hussite Beginning](https://github.com/pantaleonfassbender-coder/The-Hussite-Beginning) (1409–1420), which ends at Vítkov.

Stage 1 (in progress) carries six modules:

- **Žižka's military ordinance (1423)** — Czech from H. Toman, *Husitské válečnictví za doby Žižkovy a Prokopovy* (Prague 1898), pp. 392–394; English by Count Lützow, *The Hussite Wars* (London 1914), Appendix II, pp. 366–371. Both read against the page images.
- **The Empire's war orders (1426–1429)** — the Nuremberg proposals (1426), thirteen articles of the Frankfurt diet (1427), the Nuremberg wagon order (1428) and five articles of the Silesian wagon order (1429), German as printed by Toman (1898), pp. 395–404, read against the page images, with a working translation.
- **Laurence of Březová, the Prague chronicle (1420–1421)** — seventeen passages from August 1420 to April 1421, Latin from *Fontes rerum Bohemicarum* V (1893), pp. 400–478, read against the page images of the Czech Academy's FONTES portal, with a working translation.
- **The song of the victory at Domažlice (1431)** — nine passages of the Latin poem attributed to Laurence of Březová, *Fontes rerum Bohemicarum* V (1893), pp. 545–550, read against the page images, with a line-for-line translation.
- **Bartošek of Drahonice: Malešov and Lipany (1424, 1434)** — eight passages from the royalist squire's Latin chronicle, *Fontes rerum Bohemicarum* V (1893), pp. 592 and 613–615, read from the page images, with a working translation.
- **The crusade bull of 1421** — Martin V to Cardinal Branda, 13 April 1421, seven passages from F. Palacký, *Urkundliche Beiträge* I (1873), no. 74, pp. 70–75, read against the page images, with a working translation.

Planned (see `data/modules.json`): Hussite manifestos and Žižka's letters, Andreas of Regensburg, the Compacts of Basel (1436).

The companion game *Řádné poslušenství* ("orderly obedience", https://radne-poslusenstvi.netlify.app/) takes its title from the ordinance's preamble.

Live: https://the-hussite-field-armies.netlify.app/

## Building the data

```
python tools/build-zizka.py
python tools/build-orders.py
python tools/build-brezova.py
python tools/build-domazlice.py
python tools/build-bartosek.py
python tools/build-bull.py
```

## Running locally

Any static server, e.g. `python -m http.server 8142`.

Licences: see `LICENSES.md`.
