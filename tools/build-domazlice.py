"""Build data/domazlice.json: the song of the victory at Domazlice (1431), attributed to Laurence of Brezova.

Latin verse: Fontes rerum Bohemicarum V, ed. J. Goll (Prague 1893), pp. 545-563 (excerpts from 545-550).
Page images: FONTES portal, book 1103, image n = page + 46. Two columns of verse per page;
read left column, then right. Every line below read against the page image.
English: the site's working translation (CC0), line for line.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "domazlice.json"

FLIGHT = [
    dict(n=1, titel="They flee at the sound of the wagons", pg="545",
         orig="""Currus linquunt, clenodia,
vestes, arma, tentoria,
bombardas et pecunias,
machinas, rerum copias,
plaustra cum comeatibus
multis indicibilibus,
ut exuti oneribus
forent parati cursibus.
Honoris iam inmemores
divites necnon pauperes
metu vexilla deserunt
et ut amentes fugiunt
nondum conspecto agmine,
hostis obvii specie,
nam mei tunc ab hostibus
tribus distabant millibus,
solo audito strepitu
rede, equorum sonitu
tumultuque horribili
vociferantis populi,
classicorum sonancium,
populorum cantancium.""",
         en="""They leave their wagons, their jewels,
clothes, arms, tents,
guns and money,
engines, stores of goods,
carts with provisions
beyond all telling,
so that, stripped of their burdens,
they might be ready to run.
Forgetting honour now,
rich and poor alike
desert their banners in fear
and flee like madmen,
the host not yet in sight,
at the mere look of an enemy coming;
for my men were then
three miles from the enemy:
only the noise was heard
of wagons, the sound of horses,
and the horrible tumult
of a people shouting,
of trumpets sounding,
of peoples singing.""",
         note="Bohemia speaks: 'mei', my men, are the Hussite army. 'Reda' is a wagon. The beginning of the poem is lost in the only manuscript; the edition prints rows of dots and gives four opening lines from Dobner's older printing: 'Let Bohemia now tell in these new songs the great wonders done by God's grace.' The poem says only that the crusaders heard 'peoples singing'; the later tradition that names the song as 'Ktož jsú boží bojovníci' is not in it."),
    dict(n=2, titel="'Not men, but women'", pg="546",
         orig="""O formido militaris!
A transactis nusquam talis
est audita iam seculis
tocius orbis populis.
Suntne ast isti milites,
pape, regis sathalites?
Non sunt viri, sed femine,
capre fugaces misere,
ymo paventes lepores
aut exturbate volucres.
Ac re mei sunt ditati,
tuo dono munerati
armis et auro, curribus,
machinis, rebus pluribus.
Fodientes nam foveam
iam inciderunt in eam
hostes mei sevissimi
manu censoris maximi.""",
         en="""O soldierly fear!
Never in ages past
has the like been heard
among the peoples of the whole world.
Are these, then, soldiers,
the pope's and the king's men-at-arms?
They are not men, but women,
wretched skittish goats,
or rather trembling hares
or startled birds.
And my men were made rich in goods,
rewarded by your gift
with arms and gold, wagons,
engines and many things.
For, digging a pit,
my cruellest enemies
have now fallen into it
by the hand of the greatest judge.""",
         note="'Your gift': Bohemia addresses God. The booty of Domažlice is a gift; the ordinance had laid down how such gifts were to be shared (Ordinance [7]). The edition's note cites Psalm 5 and Proverbs 26 for the pit."),
    dict(n=3, titel="The legate's cross and keys", pg="547",
         orig="""Legatus summi presulis,
crux, claves in labaris,
crux afixa omnibus,
magnis necnon minoribus,
licet illis tunc aderant,
ast nichil illis proderant:
rapta cruce cum clavibus,
bullis, thesauris omnibus
nudum remittunt nuncium
ad primum patrem presulum.""",
         en="""The legate of the highest prelate,
the cross, the keys on the banners,
the cross fixed upon all,
on great and small,
though these were with them then,
were of no use to them at all:
the cross seized with the keys,
the bulls and all the treasure,
they send the messenger back naked
to the first father of prelates.""",
         note="The crusaders wore the cross; the papal banner bore the keys of Peter. The legate is Cardinal Julian Cesarini, whom the poem now makes speak."),
]

ROME = [
    dict(n=1, titel="Cesarini reports to the pope", pg="547",
         orig="""Ast quid dicat Julianus,
cardinalis iam Romanus,
regressus hoc de prelio,
illi pape Eugenio,
qui relinquens heremum
assumpsit decus presulum
mallens Marte officio
fungi in dei populo,
quam Marie silencio
plus complacere domino?
Hic flens dicit: Pater sancte,
non sunt vise res nunc tante
neque cernentur amodo,
ut reor, in hoc seculo,
res stupende atque dure
coram vobis fors secure,
quas sensi in Bohemica
illa gente funestica.
Cum gregassem gentes multas
vi et armis bene fultas
ex partibus Almanie
Ungarie, Ytalie,
de terrisque conterminis,
cristianismi populis,
quarum vigor orbem terre
repugnantem posset ferre,
virorum multitudinem,
pugnancium fortitudinem:
tunc, que metas custodivit,
gens Bohema, ut pervidit
tam grandem multitudinem,
reliquit terre limitem.
Nos ingressi per potentem
manum nullum resistentem
in hac terra comperimus,
ferro, igne vastavimus
fere per mensis spacium
exercentes dominium.
Tandem illi scismatici
gentis Boemie rustici
congesserunt exercitum
paucum, inermem, frivolum.
Mira tunc res peragitur,
nec ei par conspicitur
in tota sacra pagina,
orbis regnorum cronica.""",
         en="""But what does Julian say,
now a Roman cardinal,
returning from this battle
to that Pope Eugene
who, leaving the hermitage,
took up the dignity of prelates,
preferring to serve by the office of Mars
among the people of God
rather than please the Lord the more
by Mary's silence?
Weeping, he says: Holy Father,
such things have not been seen till now
nor will be seen hereafter,
I think, in this age:
astonishing and hard things,
before you, perhaps, untroubled,
which I suffered from that
deadly Bohemian people.
When I had gathered many peoples,
well furnished with force and arms,
from the lands of Germany,
of Hungary, of Italy,
and from the neighbouring lands,
peoples of Christendom,
whose strength could bear
the whole world fighting against it,
a multitude of men,
a strength of fighters:
then the Bohemian people,
which guarded the frontier, seeing
so great a multitude,
left the border of the land.
We went in with a strong hand
and found no one resisting
in that land;
we laid it waste with iron and fire
for nearly the space of a month,
exercising lordship.
At last those schismatic
peasants of the Bohemian people
gathered an army,
small, unarmed, worthless.
Then a wondrous thing was done,
whose like is not seen
in all the sacred page
or the chronicle of the kingdoms of the world.""",
         note="'Marte officio' plays on Martha and Mars: the pope who left the contemplative life of Mary for the active life of Martha now serves Mars. The line 'coram vobis fors secure' is uncertain; the manuscript reads 'for' and the editor 'fors'. Cesarini's month of burning in Bohemia before the battle is the crusade's own violence, told by its leader."),
    dict(n=2, titel="The red cope", pg="548",
         orig="""Cum nobis appropinquaret,
per tres leucasque distaret
ille malignus populus,
totus iniquus, frivolus,
tanto horrore quatimur
timoreque convincimur;
exulavit auxilium,
spes fugit et consilium,
terra tremente tremimus,
nil nisi fugam querimus,
agente hoc dyabolo,
certe ipsorum domino.
Nequivimus subsistere,
coacti sumus fugere.
Multa illic reliquimus,
que nobiscum inveximus:
bullas, indulta, labarum,
insigne decus presulum.
Meamque cappam rubeam,
quam ibidem relinqueram,
unus illorum induens
benedixit insaniens
crucisque per signaculum
nostrum ridens officium,
latro cruentus, perfidus,
cui aplausit populus,
et quod reor nepharium
corruptivumque iurium
ac clavium ecclesie
in despectum katholice.""",
         en="""When that wicked people,
wholly iniquitous, worthless,
was drawing near to us
and was three leagues away,
we were shaken by such horror
and overcome by fear:
help was banished,
hope and counsel fled,
the earth trembling, we trembled,
we sought nothing but flight,
the devil doing this,
surely their lord.
We could not stand,
we were forced to flee.
We left much there
that we had brought with us:
bulls, indults, the banner,
the noble ornament of prelates.
And my red cope,
which I had left there,
one of them put on
and, raving, gave the blessing,
and with the sign of the cross,
mocking our office,
a bloody, faithless robber,
and the people applauded him;
which I hold a wicked thing,
corrupting the rights
and the keys of the church,
in contempt of the catholic one.""",
         note="The crusade fled at three leagues, without seeing the enemy: Laurence puts the admission in the legate's own mouth. A Hussite in the cardinal's red cope, blessing the crowd, is the scene the poem makes its centre."),
    dict(n=3, titel="Robbed by their own men", pg="548",
         orig="""Nam nostro de exercitu
quidam urgente strepitu,
de quo supra meminimus
et hoc vere comperimus,
currum nostrum rapuerunt,
quem ad sua deduxerunt,
onustum auri millibus,
caris atque iocalibus,
que pro Vestra Sanctitate
multa cum sagacitate
Almanie congessimus,
fida manu servavimus.
In quos tamquam sacrilegos
ecclesie notorios
anathema inveximus,
sed in nullo profecimus.
Dure cervicis populus,
cleri infestus emulus,
sue salutis inmemor
ac adamante durior,
quod rapit, tenet firmiter,
licetque damnabiliter.
Puto eos nequiores
nunc Boemis predatores:
illi nobis resistentes,
isti nobis assistentes;
illi quippe inimici,
isti nostri ac amici:
illi nostri vastatores,
isti nostri protectores.""",
         en="""For some of our own army,
as the noise pressed upon us,
of which we spoke above,
and this we have truly found,
seized our wagon
and took it off to their homes,
laden with thousands in gold,
with precious things and jewels,
which for Your Holiness
with much shrewdness
we had gathered in Germany
and kept with faithful hand.
On them, as notorious
robbers of the church,
we laid the anathema,
but achieved nothing.
A stiff-necked people,
hostile rival of the clergy,
heedless of its salvation
and harder than adamant,
holds fast what it seizes,
though to its damnation.
I think them worse
robbers now than the Bohemians:
those resisted us,
these stood by us;
those were enemies,
these our own and friends;
those our ravagers,
these our protectors.""",
         note="The crusade's war chest, the money collected in Germany for the pope, is carried off by the crusaders themselves. The imperial orders had given each man's plunder to his own lord (Orders 1427 [12]); the poem shows what that meant in a rout."),
    dict(n=4, titel="Three articles, by grace", pg="549",
         orig="""Meum est nunc consilium,
ut tam perdurum populum
mulceamus per graciam
prestantes indulgenciam,
ut tres illi articuli
scripture consentanei,
puta de potu calicis,
criminibus de publicis,
necnon de evangelio
interpretando populo:
ut bibant de calice
omnes plebes katholice,
ut arguant et predicent,
sed populum non concitent
adversus hanc ecclesiam,
sacramque elemosinam
iam datam a fidelibus
in hiis servent limitibus,
prout nunc et ante ea
conservavit ecclesia;
quibusque volunt, ritibus
utantur, sed fidelibus
non noceant ecclesiis
sacrisque monasteriis,
cum cunctis pacem habeant,
neque vicinos adeant
cum sua milicia
hostilique sevicia. —
Cardinales hoc laudarunt,
episcopi affirmarunt,
auditores causidici,
omnes pape domestici.""",
         en="""My counsel now is
that we soften so hard a people
by grace,
granting indulgence:
that those three articles
which agree with Scripture,
namely the drinking of the chalice,
the public sins,
and the gospel
to be interpreted to the people,
[be granted]: that all the catholic commons
may drink from the chalice,
that they may reprove and preach,
but not stir up the people
against this church;
and that the holy alms
already given by the faithful
be kept within these bounds
as the church has kept them
now and before;
that they use what rites they will,
but do no harm to the faithful,
to churches and holy monasteries,
have peace with all,
and not go against their neighbours
with their soldiery
and hostile savagery. —
The cardinals praised this,
the bishops affirmed it,
the auditors, the advocates,
all the pope's household.""",
         note="Three of the Four Articles of Prague, the chalice, the punishment of public sins and free preaching, are granted; the fourth, that the clergy hold no worldly dominion, is answered by keeping 'the holy alms already given', the church's property, as it is. In the poem the cardinal proposes in 1431 what the Council of Basel and the Compacts of 1436 would grant. The two last demands, no harm to churches and no raids on the neighbours, are the price."),
    dict(n=5, titel="'Of the fourth, let them be silent'", pg="549–550",
         orig="""Pater sanctus deliberans,
rem tacitus considerans
promet sacro oraculo:
Adest deus hic populo,
quod liquet ex prodigiis
in gente nostra proditis
summi regis potencia,
cui subduntur omnia.
Durum est bellum gerere,
illi quoque resistere,
qui est deus omnipotens,
in manu cuncta continens.
[...]
Congregemus ecclesiam
sub tipo nunc katholicam,
tres ut illi articuli,
quos dixi, indevii
suum progressum habeant,
sed de quarto nunc taceant!
Nam omnis nostra dignitas,
ecclesie auctoritas
mox paulatim deficeret,
dum opes sic desereret.""",
         en="""The Holy Father, deliberating,
weighing the matter in silence,
brings forth from his holy oracle:
God is with this people,
as is clear from the wonders
shown upon our people
by the power of the highest king,
to whom all things are subject.
It is hard to wage war
and to resist him
who is God almighty,
holding all things in his hand.
[...]
Let us now gather the church
in the form of the catholic church,
so that those three articles
I spoke of may go forward
without straying from the way,
but of the fourth let them now be silent!
For all our dignity,
the church's authority,
would soon, little by little, fail
if it gave up its wealth like this.""",
         note="'Let us gather the church': a council. The Council of Basel had opened in July 1431, weeks before Domažlice; the historical Eugene IV tried to dissolve it that December. The poem's pope is Laurence's: he concedes three articles and keeps the fourth out of sight because the church's wealth is its authority. The omitted lines include 'Si sum Cristi vicarius, sim ipsi consentaneus': if I am Christ's vicar, let me be like him."),
    dict(n=6, titel="What the wives will say", pg="550",
         orig="""Hec amici et fautores,
domi relicte uxores
loquentur bellatoribus
ad sua redeuntibus:
Ubi honor, fides vestra,
ubi fortis viri dextra,
ubi vestrum iuramentum
pape, regi fide tentum?
Estne ista strenuitas,
bellantis magnanimitas,
estne ista fortitudo,
ymo turpis valitudo:
hoste absente fugere,
campum et res relinquere?
Mori foret honestius
in bello et robustius,
quam et aspectum fugere
gentis ignave, misere,
despecte nunc ab omnibus
Cristi veris fidelibus.
Ubi sunt et tentoria,
currus, arma, stipendia,
bombarde, vestes, machine,
grandesque victus copie?
Relicta sunt hec rusticis
perfidis ac Boemicis
in decus et presidium,
nobis damnum, obprobrium.""",
         en="""This the friends and patrons,
the wives left at home,
will say to the warriors
coming back to their homes:
Where is your honour, your faith,
where the strong man's right hand,
where the oath you swore
and kept to pope and king?
Is this valour,
a fighter's greatness of soul,
is this fortitude,
or rather a shameful sickness:
to flee with the enemy absent,
to leave the field and your goods?
It would be more honourable
and braver to die in war
than to flee even the sight
of a cowardly, wretched people,
now despised by all
the true faithful of Christ.
Where are the tents,
wagons, arms, pay,
guns, clothes, engines,
the great stores of food?
They are left to the faithless
Bohemian peasants
for their glory and their defence,
to us loss and shame.""",
         note="Still the pope's speech: he foresees the welcome at home. The list of what was left behind repeats Bohemia's own list (Domažlice Flight [1]), now as loss."),
]

doc = {
    "id": "domazlice",
    "titel": "The song of the victory at Domažlice (1431)",
    "autor": "Attributed to Laurence of Březová",
    "jahr": "1431",
    "sprache": "en",
    "orig_sprache": "la",
    "pg_label": "FRB V p.",
    "quelle": "Píseň o vítězství u Domažlic, ed. Jaroslav Goll, in Fontes rerum Bohemicarum V (Prague 1893), pp. 545–563; excerpts from pp. 545–550. Page images: Czech Academy of Sciences, 'Czech medieval sources FONTES' (book 1103). English: the site's working translation, line for line.",
    "hinweis": "A Latin rhymed poem on the fifth crusade, which broke and fled before the Hussite armies near Domažlice on 14 August 1431 without giving battle. The edition prints it with Laurence of Březová's chronicle as his work. Bohemia speaks first; then the legate, Cardinal Julian Cesarini, reports to Pope Eugene IV, and the pope answers. The opening is lost in the only manuscript. The verse is printed in two columns a page; the excerpts follow the left column, then the right. The Latin keeps the edition's spelling; the editor's corrections of the manuscript are adopted, and the omitted lines are marked [...]. The English follows the Latin line for line and does not rhyme.",
    "sections": [
        {"id": "flight", "titel": "Bohemia sings the flight", "zk": "Domažlice Flight",
         "blurb": "The crusade flees at the noise of the Hussite wagons, three miles off, leaving guns, money and banners; Bohemia mocks the pope's and the king's soldiers and counts the booty as God's gift.",
         "units": FLIGHT},
        {"id": "rome", "titel": "The cardinal and the pope", "zk": "Domažlice Rome",
         "blurb": "Cardinal Cesarini tells the pope how he burned Bohemia for a month and fled before 'a small, unarmed, worthless' army; a Hussite blessed the crowd in his red cope, his own men stole the war chest. He advises granting three of the Four Articles; the pope agrees, but 'of the fourth, let them be silent'.",
         "units": ROME},
    ],
}

OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("domazlice.json:", sum(len(s["units"]) for s in doc["sections"]), "units")
