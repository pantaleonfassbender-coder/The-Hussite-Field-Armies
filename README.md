# The Hussite Field Armies

A documentary apparatus for the Hussite field armies, 1420–1434: how did an army of peasants and townsmen beat five crusades, and why was it destroyed at Lipany? Public-domain sources with the original (Czech, Latin, German) beside the English, a timeline linked into the texts, and a list of what is still to come.

Its thesis, to be tested against the texts: the ordinance won every battle, and the day it was broken, everything was lost. Jan Žižka's military ordinance of 1423 bound lords, townsmen and peasants to the same discipline and the same penalties; at Lipany on 30 May 1434 the foot left their wagons against their captains' order, and the field armies were destroyed by the lords of Bohemia.

It continues [The Hussite Beginning](https://github.com/pantaleonfassbender-coder/The-Hussite-Beginning) (1409–1420), which ends at Vítkov.

Stage 1 (in progress) carries one module:

- **Žižka's military ordinance (1423)** — Czech from H. Toman, *Husitské válečnictví za doby Žižkovy a Prokopovy* (Prague 1898), pp. 392–394; English by Count Lützow, *The Hussite Wars* (London 1914), Appendix II, pp. 366–371. Both read against the page images.

Planned (see `data/modules.json`): the Empire's war orders (1426–1431), Laurence of Březová (1420–1421), the crusade bull of 1421, Hussite manifestos and Žižka's letters, the song of Domažlice (1431), Andreas of Regensburg, Bartošek of Drahonice (Lipany), the Compacts of Basel (1436).

The companion game *Řádné poslušenství* ("orderly obedience") takes its title from the ordinance's preamble.

## Building the data

```
python tools/build-zizka.py
```

## Running locally

Any static server, e.g. `python -m http.server 8142`.

Licences: see `LICENSES.md`.
