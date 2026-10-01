"""Build data/orders.json: the Empire's war orders against the Hussites, 1426-1429.

German as printed by H. Toman, Husitské válečnictví za doby Žižkovy a Prokopovy (Prague 1898),
book V, nos. II-V, pp. 395-404; internet archive husitske_valecnictvi-toman, leaf = page + 16.
Read against the page images; the machine OCR is not used. Toman's square brackets give
variants and additions from the Deutsche Reichstagsakten (no. III) and from Windecke in
Altmann's edition (no. V). English: the site's working translation (CC0).
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "orders.json"

NUREMBERG = [
    dict(n=1, titel="Obedience to the captains", pg="395",
         orig="Item a) dass man ausrufen hat, wenn die hussen zusammenkommen werden, dass itzlicher den hauptleüten an den enden, do sie beschieden worden, gehorsam zu sein.",
         en="Item: that it be proclaimed, when the hosts come together, that everyone be obedient to the captains at the places to which they have been summoned.",
         note="Toman prints 'die hussen', which would mean 'the Hussites'; the sense of an order for the crusading army asks for 'the hosts' (perhaps 'huffen', troops), and so it is translated. The reading has not been checked against another edition. The first demand is the ordinance's first demand: obedience (Ordinance Preamble [2])."),
    dict(n=2, titel="Peace within the army; the captain punishes", pg="395",
         orig="b) und friedlichen unter enander zu leben, und wär einige fährde adir unwillen zwischen jemands, die soll gänzlichen gestillet, gefredet sin, bis itzliche parteie wieder zu sinen landen und heimwärts kummet, c) und wer ouch eine missethat thäte, dem soll der hauptmann, under dem her ist, strafen nach gelegenheit der sachen, und soll auch keiner, unter des befehlnisse solicher missethätiger wäre, ihn beschirmen, sunder behulfen darzu sein, dass der bestrafet werde.",
         en="b) and to live peaceably with one another; and if there were any feud or ill will between anyone, it shall be wholly stilled and at peace until each party comes back to its own lands and home; c) and whoever commits a misdeed, the captain under whom he is shall punish him according to the circumstances, and no one under whose command such an offender stands shall shield him, but shall help to see that he is punished.",
         note="Compare the ordinance's article 8, no quarrels in the army (Ordinance [8]). The difference is in the last clause: the electors must forbid lords to shield their own men, because in their army each man stands under his lord. The ordinance names its offenders by estate, 'prince, lord, knight, squire, townsman, craftsman or peasant', and excepts no one (Ordinance [7])."),
    dict(n=3, titel="No dice, no common women", pg="395",
         orig="Item d) soll man kein würfelspil gestattin, und e) keine gemeine frauen, besondere auch, wenn man zu felde ziehet, in das heer lassen.",
         en="Item: d) no game of dice shall be allowed, and e) no common women shall be let into the army, especially when it takes the field.",
         note="The ordinance's article 11 will not suffer 'kostkáři', dice-players, or 'smilnice', harlots, among the brethren (Ordinance [11]). The electors wrote this in June 1426, at Nuremberg, in the same weeks in which the field armies destroyed the Saxon army before Ústí (16 June)."),
    dict(n=4, titel="Rape; insults between contingents", pg="395",
         orig="f) Wäre dass einige fraue, magd odir jungfraue genotzüget würde, wer das thäte, den sall man strafen ahn alle gnade, als sich das gebürt. g) So soll auch niemand den anderen, die sulchen zog riten, sie wären von städten oder andere, schmähen mit worten oder werken; wer das dorobir thäte, der sulde gestraft werden als sich gebüret, und soliche strafunge soll umme niemands willen vorsehen werden.",
         en="f) If any woman, maid or virgin were violated, whoever did it shall be punished without any mercy, as is fitting. g) Nor shall anyone revile with words or deeds any of the others who ride on this campaign, whether they are from the towns or others; whoever does so all the same shall be punished as is fitting, and such punishment shall not be omitted for anyone's sake.",
         note="Article g) shows the fault line of the imperial army: the princes' men and the towns' contingents insulting each other. 'For no one's sake' is the electors' version of the ordinance's refrain, 'no person excepted'."),
]

FRANKFURT = [
    dict(n=1, titel="Article 3: obedience without contradiction", pg="396–397",
         orig="3. Item der fürsten, der man zu hauptleuten ist überkommen, sollen und mögen zu ihn nehmen sechs oder mehr, achte redelich, ob sie des ein notdurft bedeuchte etc. Aus andern fürsten, herren, die dar kämen, und die sollen setzen, machen, ordiniren und schicken, wie man ziehen und folgen sollde, auch zu bestellen und heissen zu thunde, als des not zu thunde ist, und alle die, die also folgen, ziehen und kommen, niemand ausgenommen, sollen denselben fürsten oder ihrer gewalt ganz gehorsam sein und gewarten, ahne alle widerrede.",
         en="3. Item: the princes who have been agreed upon as captains shall and may take to themselves six or more, eight honest men, if they think it needful, etc., from the other princes and lords who come there; and these shall set, make, ordain and arrange how the army shall march and follow, and also order and command what is needed to be done; and all who thus follow, march and come, no one excepted, shall be wholly obedient to these princes or to those holding their power, and attend on them, without any contradiction.",
         note="A council of six or eight beside the captains, chosen from the princes and lords: the imperial counterpart of the ordinance's 'elder captains' (Ordinance [1]). 'Niemand ausgenommen', no one excepted, is the ordinance's phrase."),
    dict(n=2, titel="Article 4: at one's own cost; food paid for", pg="397",
         orig="4. Item menglich soll ziehen uf sein selbs eigen koste und zehrunge, andern leuten ahne schaden. Doch wo man nit in städten und zu felde ist, mag man nehmen ein zemlich notdurft von heu und stroh ungefärlich; ob man das auch nicht gehaben möchte, es wäre futter oder speise, oder ze kauf bekomen, so mag man das wohl nehmen, wo man das mag gehaben, und man soll das redlich bezahlen nach der hauptleute, oder wen die dorzu schicken würden, erkentnisse.",
         en="4. Item: everyone shall march at his own cost and charges, without harm to other people. But where one is not in towns but in the field, one may take a reasonable need of hay and straw without fraud; and if one cannot otherwise have it, be it fodder or food, or get it by purchase, one may take it where one can have it, and shall pay for it honestly as the captains, or whomever they send for the purpose, decide.",
         note="The crusade is financed by each lord for his own men; the ordinance has no article on pay at all."),
    dict(n=3, titel="Article 6: robbery", pg="397",
         orig="6. Item wär dorüber jemand das sein nehm wider seinen willen oder raubte, dem soll man ohn gnade sein haubte abhauen, und wer da stiehlet, dem soll auch sein recht geschehen, und das soll niemand wehren, noch sich darwider setzen, thuen oder schicken, gethan werden.",
         en="6. Item: if anyone beyond this took a man's goods against his will, or robbed, his head shall be struck off without mercy; and whoever steals, justice shall be done on him too; and no one shall prevent this, or set himself against it, or do or arrange anything against it.",
         note="'No one shall prevent this': again the lords who might shield their men."),
    dict(n=4, titel="Article 7: no women, no gamblers", pg="397",
         orig="7. Item es soll auch keine frau, [spieler], noch kein ander püeberei, wie die genannt werden, mit ziehen oder nachfolgen.",
         en="7. Item: no woman [no gambler], nor any other knavery, whatever it is called, shall march with the army or follow it.",
         note="'Spieler' is added from the Reichstagsakten edition. The ordinance does not bar women from the army; among those it will not suffer it names harlots and adulteresses (Ordinance [11])."),
    dict(n=5, titel="Article 8: weekly confession", pg="397",
         orig="8. Item ein iglicher soll zum minsten all wochen einmal beichten, und ein iglich fürste, hauptmann etc. soll darzu die seinen halten, und messe hören, welichs tags sie die mögen gehaben, und dass do bei gotte demütiglich, inniglichen und mit ganzem fleiss gedienet werde.",
         en="8. Item: everyone shall confess at least once every week, and every prince, captain etc. shall hold his men to it, and they shall hear mass on whatever day they can have it, so that God be served there humbly, devoutly and with all diligence.",
         note="Against the brethren who kneel before the Sacrament before every march (Ordinance [4]), the crusaders are bound to weekly confession and mass. Both armies march under God."),
    dict(n=6, titel="Article 9: oaths and curses", pg="397",
         orig="9. Item wer auch frevelich mit ufsatz swüre oder bös flüchte thäte gen einem andern menschen oder schulte, den sall man offentlichen sliessen in einem pranger, bis auf der hauptleute genade, oder soll den zu stund ausjagen blöss mit geiseln oder gärten.",
         en="9. Item: whoever wantonly and wilfully swears, or utters evil curses against another person, or reviles him, shall be locked publicly in a pillory until the captains show him grace, or shall at once be driven out naked with whips or rods.",
         note="The ordinance's 'lajci', those who curse (Ordinance [11]), are punished here by the pillory or by being whipped out of the camp."),
    dict(n=7, titel="Article 10: drawing a weapon", pg="397",
         orig="10. Item wer auch sein swert, messer, beile oder ander wehre oder waffen über einen andern zückte oder ruckte frevelich, der soll ane gnade ein hand verloren han. Wäre aber, dass er darzu jemand wundete, dem soll das haupt abgehauen werden.",
         en="10. Item: whoever wantonly draws or pulls his sword, knife, axe or other arms or weapons on another shall lose a hand without mercy. But if he also wounds someone, his head shall be struck off.",
         note="Compare Ordinance [9], which leaves the penalty for striking, wounding or killing to 'God's law, as God permits'."),
    dict(n=8, titel="Article 12: no foraging and no burning without the banner", pg="397–398",
         orig="12. Item niemand soll im lande zu Beheim mit volk nach futter oder icht reiten, gehn oder fahren, es sei dann dabei die banier, die von den haubtleuten davon geschickt ist oder der haubtleute geheisse etc., und niemand soll in demselben lande brennen oder anstossen, es werde es dann von den haubtleuten geheissen, oder es sei dann auch dobei die banier, die darzu ist gescheiden.",
         en="12. Item: no one shall ride, walk or drive with men in the land of Bohemia after fodder or anything else, unless the banner sent out for it by the captains is with them, or by the captains' command etc.; and no one shall burn or set fire in that land unless it is commanded by the captains, or unless the banner appointed for it is there too.",
         note="The closest echo of the ordinance. Its article 3 forbids burning except by 'those appointed to it' (Ordinance [3]); its article 5 keeps every troop 'under its banner' (Ordinance [5]). Burning in Bohemia is not forbidden; it is reserved to the captains."),
    dict(n=9, titel="Article 13: no killing, except of heretics", pg="398",
         orig="13. Item auch soll niemand keinen menschen morden oder abthun ohn redliche sach, es sei dann auf den rechten ketzern und die es mit ihn halten und ihn zulegunge thun, bei der obgenannten pöne des hals.",
         en="13. Item: no one shall murder or do away with any person without just cause, unless it be the true heretics and those who hold with them and give them support, on the penalty of the neck named above.",
         note="The exception that defines the war: the killing of heretics and their helpers is outside the peace of the camp. The ordinance's closing has its own counterpart, the shaming of 'all open or secret heretics and miscreants' (Ordinance Closing [2])."),
    dict(n=10, titel="Articles 15–16: watches, and no one moves without the banner", pg="398",
         orig="15. Item wem die hauptleute oder ihr mächtige gewalt wachen, warten oder reiten gebieten, der soll des gehorsam sein ahn alle widerrede. 16. Item es soll auch niemand aufbrechen, fur- oder nachziehen, es sei dann dabei die banier, die darzu geschickt, und wenn die hauptleut heissen fur- oder nachziehen oder aus ziehen zu storme, zum streit, zum laufen oder zum stehen, der soll des alles gehorsam sein.",
         en="15. Item: whomever the captains or those holding their power command to keep watch, stand guard or ride, he shall obey without any contradiction. 16. Item: no one shall break camp, march ahead or behind, unless the banner sent for it is with him; and when the captains command to march ahead or behind, or to go out to the assault, to battle, to run or to stand, everyone shall obey in all of it.",
         note="Article 16 is the ordinance's articles 1, 2 and 5 in one: no one ahead of the army, the march by order, each troop under its banner (Ordinance [1], [2], [5]). 'Zum laufen oder zum stehen', to run or to stand: the order to hold one's ground is the one the brethren broke at Lipany. Toman prints 'aust ziehen'; read 'aus ziehen'."),
    dict(n=11, titel="Article 31: food shared in equal parts", pg="400",
         orig="31. Item es soll niemand nach keinerlei viehe umb willen der speise reiten, fahren oder senden, es sei denn mit des hauptmann geheiss, daun soll man von allen herren darzu schicken, das eigenlich ordiniren, und also darnach einträchtiglich bestellen, und solich spise nach gleicher anzahl theilen.",
         en="31. Item: no one shall ride, drive or send after any cattle for food except by the captain's command; then men shall be sent for it from all the lords, it shall be properly ordered and arranged by common accord, and such food shall be shared out in equal numbers.",
         note="Food, but not booty, is pooled and shared. Toman prints 'daun' for 'dann'."),
    dict(n=12, titel="Articles 32–33: captured places, and prisoners to their lord", pg="400",
         orig="32. Item worden auch keinerlei sloss, städte, märkte oder vesten gewunnen, oder die sich ergeben worden, damit soll man es halten nach der hauptleut und der, die zu ihnen geschickt oder gegeben worden, erkenntnisse oder des mehren theils under ihn, und zu gute wenden. 33. Was auch ein jederman, der mit seinem herrn zu felde käme auf des herrn koste, versolden und zehrunge, gefangen gewönnen, die soll er demselben seinem herrn antworten und geben ahn widerrede. Was auch er sei, ritter oder knecht oder städte, der oder die auf ihr eigene koste, zehrung und ebenteuer gen Beheim zügen, gefangen ankämen, die mögen ihn sölich gefangen selber halten, oder damit thuen nach ihrem willen.",
         en="32. Item: if any castles, towns, markets or fortresses are won, or surrender, they shall be dealt with as the captains and those sent or given to them, or the greater part among them, decide, and turned to good use. 33. Whatever prisoners anyone takes who comes into the field with his lord at the lord's cost, pay and charges, he shall deliver and give to that same lord without contradiction. But whoever, knight or squire or towns, marches to Bohemia at his own cost, charges and risk, and takes prisoners, may keep such prisoners himself, or do with them as he will.",
         note="Here the two orders part. The ordinance pools all booty, 'be it much or little', and has it shared among rich and poor by elders chosen from every estate, peasants included (Ordinance [7]). The crusade gives the prisoner, and his ransom, to whoever paid for the man who took him."),
    dict(n=13, titel="Article 34: leaving the army", pg="400",
         orig="34. Item wer auch von den herren aus dem heere reiten wollte, der soll weder fried noch geleit haben, er hat dann der hauptleute [zeichen], kundschaft oder brief.",
         en="34. Item: whoever of the lords wishes to ride away from the army shall have neither peace nor safe conduct, unless he has the captains' [token], knowledge or letter.",
         note="The ordinance's article 10, with its 'sure token' (Ordinance [10]). But the imperial article names 'the lords', who could ride home with their men; the ordinance names every estate down to the peasant. 'Zeichen' is added from the Reichstagsakten edition."),
]

WAGONS = [
    dict(n=1, titel="Nuremberg, 23 April 1428: a war wagon", pg="402",
         orig="§ VII. 1. Item einen streitwagen zu bestellen. 2. Item in den städten 10 mann zu einem wagen. 3. Item auf den dörfern 20 mann zu einem wagen. 4. Item zu iglichem wagen zween büchsenschützen mit pulver und bleis genug. 5. Item zween schützen mit armbrust, iglicher schütz 2 schock pfeil. 6. Item 2 mann mit drischeln. 7. Item 2 mann mit spiessen, die hinden an der tülle ein eisen schneidende haken haben. 8. Item 2 mann mit stabschleudern. 9. Item vier starker pferde zu einem wagen. 10. Item 2 stark fuhrmann, die ihre wehre haben. 11. Item ein kurb uf den wagen, da man stein einlist. 12. Item 1 eisene schaufeln, 1 hauen, 1 mulden, 1 axt, 1 steinpickel. 13. Item ein wagenketten, die als lang sei, als sunst ander drei sind.",
         en="§ VII. 1. Item: to provide a war wagon. 2. Item: in the towns, 10 men to one wagon. 3. Item: in the villages, 20 men to one wagon. 4. Item: to each wagon two handgunners with powder and lead enough. 5. Item: two shooters with crossbows, each with 2 threescore bolts. 6. Item: 2 men with flails. 7. Item: 2 men with pikes that have a cutting iron hook at the back of the socket. 8. Item: 2 men with staff slings. 9. Item: four strong horses to a wagon. 10. Item: 2 strong drivers who have their arms. 11. Item: a basket on the wagon in which stones are gathered. 12. Item: 1 iron shovel, 1 hoe, 1 trough, 1 axe, 1 stone pick. 13. Item: a wagon chain as long as three others.",
         note="Eight years after Žižka's wagons held at Sudoměř (1420), the imperial diet orders its own: flails, hooked pikes, handguns, a basket of stones, and a long chain to bind wagon to wagon. Towns raise one wagon for every ten men, villages for every twenty."),
    dict(n=2, titel="Silesia, May 1429: eighteen men to a wagon", pg="403",
         orig="1. Item zu einem stritwagen sollen gehören sechs schutzen, und zu jetlichem armbrost vier schock pfile, zween mann mit handbuchsen, zu jeglicher vier schock kugelin (klötz) und pulvers gnüg; vier mann mit haken, vier mann mit drischeln, zwo hacken, zwo schufeln, zwo kilhoven oder grabschit [schufeln]. 2. Item zu jetlichem [wagen] vier stark hengst, welcher aber nit starker pferd [hengest] hant, der nehm sünst sechs; dass doch jeglicher wagen zween fürmann habe [wohl] gewappent. 3. Item die schufeln, grabschit und hacken dörfen nit [hon] sunder lüte, sunder wird man ihr dörfen, so nimmt man sie [wohl] aus dem hufen, da lut genug sin werden. Summa zu einem wagen 18 [48] person, die sich von dem wagen nit sullen scheiden, es si denne mit des hauptmanns geheiss [und auch sine willen].",
         en="1. Item: to a war wagon shall belong six shooters, and to each crossbow four threescore bolts; two men with handguns, to each four threescore balls (pellets) and powder enough; four men with hooks, four men with flails, two hoes, two shovels, two picks or spades. 2. Item: to each [wagon] four strong stallions; but whoever does not have strong horses shall take six instead; so that every wagon has two drivers, [well] armed. 3. Item: the shovels, spades and hoes need no men of their own; if they are needed, men are taken from the troop, where there will be people enough. In sum, to one wagon 18 [48] persons, who shall not leave the wagon except by the captain's command [and also his will].",
         note="Toman's brackets give Windecke's text in Altmann's edition; his footnote counts the eighteen: six crossbowmen, two handgunners, four with hooked pikes, four flailmen and two drivers, who may not leave their wagon without the captain's leave. Windecke's '48' is a slip."),
    dict(n=3, titel="Silesia, May 1429: how the wagon is built", pg="403",
         orig="4. Item sölicher starker wagen soll sin in fassonswise [eine messung wit] mit hohen leitern, gethariast von dem sels [felde] zwischen den leitern und under den leitern mit [guten] hangenden brettern an starken widen oder ketten. 5. Item zu jetlichem wagen sullen ketten sein, dieselben zu binden, ob es sin not wird [not sin wurde.]",
         en="4. Item: such a strong wagon shall be made [of one measure in width], with high ladder sides, boarded from the ground between the ladders and under the ladders with [good] hanging boards on strong withies or chains. 5. Item: to each wagon there shall be chains to bind them together, if need be.",
         note="Toman explains the article in his chapter on the wagons (pp. 187–188); the translation follows his bracketed variants where the first text is unclear ('fassonswise', 'sels'). 'Gethariast', boarded or shielded, is uncertain."),
    dict(n=4, titel="Silesia, May 1429: captains of ten, a hundred, a thousand", pg="404",
         orig="12. Item es soll unter dem volk eine söliche ordnung sein, dass je zehn mann einen hoptmann haben, und hundert einen, und tusend einen, und also immer mehr für sich bis uf den obersten hoptmann, als man der lute genügig haben wird, die söliche sache und schickung wohl ordnen können, und dass je ein hoptmann uf den andern sehe, als denn [dann] ein gewohnheit ist.",
         en="12. Item: there shall be such an order among the people that every ten men have a captain, and every hundred one, and every thousand one, and so on upwards to the highest captain, as far as there are enough people who can order such a matter and arrangement well; and that each captain look to the other, as is the custom.",
         note="A chain of command by numbers, from ten men up. The ordinance knows no ranks of this kind; it names 'the elder captains' and 'the communities' (Ordinance [6])."),
    dict(n=5, titel="Silesia, May 1429: the disobedient as helpers of heretics", pg="404",
         orig="16. Item wer sich in den obgeschrieben sachen ungehorsam finden liesse, zu des lieb und gut man grifen soll, als zu einem zuleger und helfer der ketzer, ohn all gefährde.",
         en="16. Item: whoever is found disobedient in the matters written above, his body and goods shall be seized, as those of a supporter and helper of the heretics, without fraud.",
         note="The ordinance's penalty, 'in goods and in neck' (Ordinance [1]), with a different charge: disobedience in the crusading army makes a man a friend of the heretics."),
]

doc = {
    "id": "orders",
    "titel": "The Empire's war orders against the Hussites",
    "autor": "The electors at Nuremberg (1426), the imperial diet at Frankfurt (1427) and at Nuremberg (1428), the Silesian estates (1429)",
    "jahr": "1426–1429",
    "sprache": "en",
    "orig_sprache": "de",
    "pg_label": "Toman p.",
    "quelle": "German texts as printed in Hugo Toman, Husitské válečnictví za doby Žižkovy a Prokopovy (Prague: Královská česká společnost nauk, 1898), book V, nos. II–V, pp. 395–404 (internet archive: husitske_valecnictvi-toman). Toman takes the bracketed variants of no. III from the Deutsche Reichstagsakten, and those of no. V from Eberhart Windecke's memoirs in W. Altmann's edition (1893). English: the site's working translation.",
    "hinweis": "Toman prints the German orders after Žižka's ordinance, as the enemy's answer to it. The site carries the Nuremberg proposals of June 1426 whole, thirteen of the forty-eight articles of the Frankfurt diet of 1427 (those on discipline, food, booty and leaving the army; the lists of guns and contingents are left out), the Nuremberg wagon order of April 1428 whole, and five of the eighteen articles of the Silesian wagon order of May 1429. The German was read against the page images and is kept with Toman's spelling and his square brackets; obvious misprints are named in the notes. Where the German is uncertain, the translation says so.",
    "sections": [
        {"id": "nuremberg", "titel": "Nuremberg, June 1426", "zk": "Orders 1426",
         "blurb": "From the proposals of the electors at Nuremberg, 7–10 June 1426, article 17: what is to be proclaimed in the crusading army. Obedience to the captains, peace within the camp, no dice, no common women.",
         "units": NUREMBERG},
        {"id": "frankfurt", "titel": "Frankfurt, spring 1427", "zk": "Orders 1427",
         "blurb": "From the resolution of the imperial estates at Frankfurt, shortly before 4 May 1427, for the campaign that fled from Tachov that August: the articles on obedience, robbery, women, confession, weapons, foraging and burning, the banner, food, prisoners and leaving the army.",
         "units": FRANKFURT},
        {"id": "wagons", "titel": "The wagons, 1428–1429", "zk": "Orders Wagons",
         "blurb": "The Empire builds its own wagon forts: the Nuremberg resolution of 23 April 1428 on the war wagon, and the Silesian order of May 1429 on its crew, its building and its captains.",
         "units": WAGONS},
    ],
}

OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("orders.json:", sum(len(s["units"]) for s in doc["sections"]), "units")
