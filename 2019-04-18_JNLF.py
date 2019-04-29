__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
DEBUG = True
DEBUG = False

fig_width = 12

import os
home = os.environ['HOME']
figpath_talk = 'figures'
def path2(fname):
    return os.path.join(figpath_talk, fname)
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
#
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

from academic import slugify

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .8 # use to make the figures fit on the screen

meta = dict(
 embed=False,
 draft=DEBUG, # show notes etc
 width=1600,
 height=1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin=.01, # 0.1618,#
 reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.7.0/',
 #reveal_path='https://s3.amazonaws.com/hakim-static/reveal-js/',
 theme='simple',
 bgcolor="white",
 author='Perrinet, Laurent U',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugify(tag)}/">Laurent Perrinet</a>',
 short_title='Des illusions aux hallucinations visuelles',
 title='Des illusions aux hallucinations visuelles: <BR> une porte sur la perception',
 conference_url='https://www.jnlf.fr/agenda/jnlf-lille-2019',
 short_conference='JNLF 2019',
 conference='JNLF 2019',
 location='Lille (France)',
 abstract="""Les illusions visuelles sont des créations d'artistes, de scientifiques et plus récemment, grâce aux réseaux sociaux, du grand public qui proposent des situations souvent incongrues, dans lesquelles l'eau remonte une cascade, les personnes volent dans les airs ou des serpents se mettent à tourner. Au-delà de leur indéniable coté ludique, ces illusions nous apprennent beaucoup sur le fonctionnement du cerveau, notamment quand celles-ci se transforment en hallucinations visuelles, dépassant ainsi les limites des capacités de notre perception. En tant que chercheur en Neurosciences à l'Institut de Neurosciences de la Timone à Marseille, je vous dévoilerai des aspects du fonctionnement du cerveau qui sont souvent méconnus. En particulier, nous verrons pourquoi un magicien peut tromper nos sens ou comment des objets peuvent voyager dans le temps. Surtout nous essaierons de comprendre le fonctionnement de notre perception visuelle sur les bases d'une théorie de la vision non pas comme une simple caméra qui enregistre des images mais comme un processus actif en relation avec le monde qui nous entoure.""",
 summary = """Les objectifs sont :
– mieux comprendre la fonction de la perception visuelle en explorant certaines limites ;
– mieux comprendre l’importance de l’aspect dynamique de la perception ;
– mieux comprendre le rôle de l’action dans la perception.
""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='anr-causal',
 time_start = '15:45:00',
 time_end = '16:30:00',
 url=f'https://laurentperrinet.github.io/talk/{slugify(tag)}',
 sections=['Illusions visuelles & hallucinations',
          'Coute que coute, prédire le présent',
          'Une neuro-anatomie fonctionnelle des illusions & hallucinations?',
          ]
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname_qr = path2('qr.png')
if not os.path.isfile(figname_qr):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname_qr, scale=5)

print(meta['sections'])
s = Slides(meta)

figpath_people = os.path.join(home, 'ownCNRS/2019-01_LACONEU/people')
Karl = s.content_imagelet(os.path.join(figpath_people, 'karl.jpg'), height_px)
Rick = s.content_imagelet(os.path.join(figpath_people, 'rick.jpg'), height_px)
Anna = s.content_imagelet(os.path.join(figpath_people, 'anna.jpg'), height_px)
# LM = s.content_imagelet(os.path.join(figpath_people, 'LM.png'), height_px)
# JB = s.content_imagelet(os.path.join(figpath_people, 'JB.jpg'), height_px)
Fredo = s.content_imagelet(os.path.join(figpath_people, 'fredo.png'), height_px)
# Python = s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px)
# <a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
s.meta['Acknowledgements'] =f"""
<small>
<h5>Acknowledgements:</h5>
<ul>
    <li>Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
    <li>Anna Montagnini  - INT</li>
    <li>Frédéric Chavane - INT</li>
</ul>
<BR>
{Rick}{Karl}{Anna}{Fredo}
<BR>
    This work was supported by ANR project "Horizontal-V1" N° ANR-17-CE37-0006.
</small>

"""
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 1 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################
i_section = 0
s.open_section()
###########################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)

# intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2)
intro += s.content_figures(
    [path2('troislogos.png')], bgcolor=meta['bgcolor'],
    height=s.meta['height']*.2)
#bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
###########################################################################
# s.add_slide(content=intro)
#
# s.add_slide(content=s.content_figures(
#     #[path2('qr.png')], bgcolor="black",
#     [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
#     height=s.meta['height']*1.),
#     #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
#     notes="""
# Check-list:
# -----------
#
# * (before) bring VGA adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
#  """)
#
# s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
#             notes="All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")
########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU

* (OBJECTIVE)

Nous allons ici montrer comment les limites de la perception permettent et peuvent nous aider à mieux comprendre le fonctionnement du cerveau et de ses pathologies. En partant des illusions visuelles, nous allons ensuite explorer différentes hypothèses pour comprendre ses illusions, mais aussi pour aborder une neuro-anatomie fonctionnelle des hallucinations et illusions visuelles.


- Mieux comprendre les bases neurales des hallucinations;


* Let's me first describe the motivation of this work...



* (SHOW TITLE)

""")

url =  '<a href https://en.wikipedia.org/wiki/Hering_illusion">Hering illusion</a>'
for suff in ['', '_without']:
    s.add_slide(content=s.content_figures([path2('Hering_illusion' + suff + '.svg')],
        title=None, #'Classical visual illusions',
        height=s.meta['height']*height_ratio) + url,
notes="""
L’étymologie du mot illusion réfère à la tromperie et nous permet de définir les illusions visuelles comme une stimulation visuelle qui induit une perception décalée par rapport à la réalité physique (le stimulus proximal). Dans l’illusion classique dit de Hering par exemple (voir Figure @fig:hering), deux lignes parallèles placés sur un faisceau de lignes convergente semble courbées comme si le centre de l’image avait gonflé par rapport à sa périphérie. Cette illusion est robuste même si l’on prend une règle pour vérifier physiquement le parallélisme des lignes (ou simplement en enlevant les lignes fuyante): Il n’est pas possible de ne **pas** la percevoir. Ainsi, pour cette illusion comme pour une grande variété d’autres illusions visuelles statique ou dynamique ou sur d’autres modalités (comme le toucher), les illusions visuelles marquent tout d’abord par ce caractère quasi universel et intuitif, c’est-à-dire sans qu’il faille expliquer un mode d’emploi pour les illusions.


""")


url =  '<a href https://en.wikipedia.org/wiki/The_dress">#TheDress</a>: #whiteandgold or #blackandblue ?'

s.add_slide(content=s.content_figures(
    [
    path2('The_Dress_(viral_phenomenon).png'),
    path2('Wikipe-tan_wearing_The_Dress.svg'),
    ], fragment=True,
        title=None, height=s.meta['height']*height_ratio) + url,
notes="""

https://en.wikipedia.org/wiki/The_dress
À ce titre, une illusion récente est remarquable à bien des égards. En effet, certaines illusions illusions comme le cube de Necker sont multi-stable, dans le sens où la perception peut alterner autour de plusieurs interprétations possibles de la même image. Dans le cas de #LaRobe, nous avons une image qui a le pouvoir de diviser une population entre des perceptions alternatives. De plus, au lieu d’être créée par des scientifiques, cette illusion est née par [sérendipité](https://fr.wikipedia.org/wiki/S%C3%A9rendipit%C3%A9) à partir d’une simple photo prise lors de la préparation d’une cérémonie de mariage. Postée sur les réseaux sociaux, cette photo a eu un destin fulgurant et mondial grâce a l’ambiguïté sur l'interprétation de la couleur de la robe. Ainsi si je vous demande de donner vous-même votre avis à partir de la Figure @fig:larobe, pensez-vous qu’elle est blanche et or ou alors qu’elle est bleu avec des bandes noires ? Même si le débat fait toujours rage, les explications scientifiques (entre autres articles scientifiques ou sessions spéciales de conférence) convergent sur une perception de la couleur de la figure qui est modifiée par le contexte du fond. En effet notre système visuel doit pouvoir identifier la couleur d’un objet (par exemple pour évaluer la maturité d’un fruit comme une balade) quelque soit les conditions lumineuses, un matin le midi avec une lumière crue ou le crépuscule avec une lumière orangée du soir. Ici le fond est surexposé et rend cette interprétation ambiguë et deux interprétations sont possibles pour cette image comme illustré dans la figure de droite. Je peux vous dévoiler que sur un échantillon représentatif une courte majorité voilà la robe bleue et noir. Un aspect remarquable de cette illusion et d’une part sa stabilité et d’autre part la difficulté de changer d’interprétation une fois une première interprétation formée, c’est-à-dire de passer une couleur bleue à une perception d’une couleur blanche. Cette illusion est à mes yeux d’autant plus puissante car elle met en évidence que les images sont interprétées par notre système visuel. Celà apporte aussi ce message universel qu'une propriété de nos fonctions cognitives et de pouvoir interpréter la même objet physique de différentes façons, et réconcilier des groupes humains qui peuvent avoir des façons contrastées de voir des objets physiques qui sont identiques. Pour reprendre le célèbre proverbe on pourrait dire que « l’illusion est humaine »!

Two ways in which the photograph of The dress may be perceived:
* black and blue under a yellow-tinted illumination (left figure) or
* white and gold under a blue-tinted illumination (right figure).

""")


bib = s.content_bib("Cydonia Mensae", "1976", 'Viking Orbiter image', url="Viking Orbiter image")
s.add_slide(content=s.content_figures(
        [path2(fname) for fname in ['Face-on-mars.jpg', 'Viking_moc_face_20m_low.png', 'Viking_moc_face_20m_high.png']], fragment=True,
            title="Paréidolie", height=s.meta['height']*.5) + bib,
    notes="""
Pour aller plus loin, il est intéressant de considérer cette image prise en 1971 par la sonde Viking d’une partie de la surface de la planète Mars (Figure @fig:viking). L’image est relativement floue, et les points noirs sont des erreurs de mesure  mais l’on distingue très clairement un visage de type humain comme une sculpture géante laisser là par une civilisation extraterrestre. Quelques 20 ans plus tard, de nouvelles images ont été réalisés par de nouvelles sondes spatiales et montrent aussi une forme de visage. Mais une fois la résolution de l’image affinée, les détails du relief révèlent qu’il n’y a pas physiquement de sculpture de ce type mais seulement un simple rocher. C’est un cas de [paréidolie](https://fr.wikipedia.org/wiki/Par%C3%A9idolie) : quelque chose est perçu alors qu’il est physiquement absent. De la même façon, on peut voir un cheval courir dans les nuages, ou le visage du Christ dans un toast, le constat est le même : le système visuel et en particulier la perception qui en découlent non seulement interprète les images, mais sur surtout, il ne peut pas faire autrement que de générer une interprétation à partir d’images, et comme on vient de le voir même si elles ne font pas a priori sens. Dans ce genre d’illusion on se rapproche donc d’une hallucination, qui peut être définie comme une perception sans objet.

Pour résumer, les illusions visuelles, en plus de leur côté ludique, nous révèlent des caractéristiques essentielles de notre perception visuelle tant sur leurs caractéristiques universelles que sur les variabilités inter et intra individuelles. Malgré la diversité des formes des illusions visuelles et la diversité des explications qu’on peut leur faire correspondre, existe-t-il des points communs qui permettraient d’en avoir une compréhension unifiée ? Quelles pourraient être les liens profonds entre illusions visuelles avec des hallucinations aussi bien chez les sujets neuro-typique que dans des pathologies psychologiques?
    """)


    # TODO : add vasarely / etienne
s.close_section()

i_section += 1
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 2 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
Avant d’essayer de donner une réponse à ces questions, rappelons une contrainte fondamentale à laquelle notre cerveau est confronté : l’environnement et dynamique et notre cerveau est (relativement) lent pour traiter ces informations.
""")

s.hide_slide(content=s.content_figures(
   [path2('scheme_thorpe.jpg')], bgcolor="black",
   height=s.meta['height']*height_ratio),
notes="""
 En effet les travaux de Simon Thorpe à Toulouse au Cerco ont montré des capacités ultra-rapide de catégorisation d’image chez les primates. Cette vitesse peut atteindre environ 100 ms chez l’humain [@tag:Kirchner06] et 80 ms chez le singe.
 """)


s.hide_slide(content=s.content_figures(
    [path2('tsonga.png')], bgcolor="black",
    height=s.meta['height']*height_ratio),
    notes="""
C’est remarquablement rapide mais relativement long si l'on considère cette fois-ci une tâche simple d’interception d’un objet en mouvement. Considérons par exemple un agent qui suit une balle de tennis lancée à une vitesse de 20 m/s à une distance de 1 m devant son regard.
  """)

s.add_slide(content=s.content_figures(
    [path2('figure-tsonga.png')], bgcolor="black",
    height=s.meta['height']*height_ratio),
    #image_fname=os.path.join(figpath, 'figure-tsonga.png'), embed=s.meta['embed'],
        notes="""
 Au moment de passer dans l’axe de vision du joueur de tennis, la balle va être perçue en arrière de la trajectoire à cause du délai sensoriel. Plus précisément la balle est placé à l’instant où l’image est prise à environ 45° d’angle visuel en retard sur la position réelle actuelle de la balle. À noter que la position de la balle est sur l’axe de vision (telle celle figurée par cette position des yeux), mais que pour le système sensoriel, cette position au temps présent doit être anticipée. Notons aussi notons aussi que la position de la balle, dans cette représentation rétinienne, au moment où l’action sera réalisé (après le délai sensorimoteur total) pourra être estimé à partir de la continuité du mouvement de la balle. C’est-à-dire qu’elle sera encore environ à 45° d’angle visuel mais cette fois ci en avant de la trajectoire, dans son futur. Il semble incroyable que ce genre de voyage dans le temps puisse s’opérer dans notre cerveau, mais une simple illusion visuelle permet de mettre ces mécanismes en évidence.
 """)

figname='flash_lag.mp4'

fle_bib = s.content_bib("Khoei, Masson and LP", "2017", 'PLoS CB', url="http://invibe.net/LaurentPerrinet/Publications/KhoeiMassonPerrinet17")

s.add_slide(content="""
 <video controls autoplay loop width=99%/>
   <source type="video/mp4" src="{}">
 </video>
 """.format(path2(figname)) + fle_bib,
notes="""

En effet, l’illusion du flash retardé ("Flash Lag Effect" en anglais) permet de mettre en évidence des dynamiques de traitement dans le système visuel. Dans cette illusion, l’observateur doit fixer environ au centre de l’écran. Une cible en mouvement horizontal apparaît et quand elle passe aux environs du centre de l’écran, un bref flash est présenté immédiatement au-dessous du centre de l'image. Perceptivement, on observe chez une vaste majorité d’observateurs que la cible en mouvement est perçue, au moment du flash, *en avant* de la trajectoire. L’hypothèse originale de Romi Nijhawan propose que la cible est perceptivement représentée de telle façon à ce qu’elle occupe sa position au temps présent, donc de manière anticipée. Par contre, le flash est imprévu et sa position ne peut pas être anticipée. C’est ce que nous avons montré dans ce travail de modélisation qui montre une évaluation quantitative des production d’un tel modèle [@tag:KhoeiMassonPerrinet17].


""")


s.add_slide(content=s.content_figures(
    [path2('FLE_histogram.png')], title=title, embed=s.meta['embed'],
    height=s.meta['height']*height_ratio) + fle_bib,
   notes="""

Plus généralement, ce travail nous a conduit à émettre l’hypothèse que le cerveau utilise les régularité statistiques du monde pour arriver d’une façon ou d’une autre à compenser les contraintes de délai et par exemple à « prédire le présent ». Une telle hypothèse permet de formaliser un bon nombre d’illusions et en particulier l’illusion de Hering que nous avons défini ci-dessus. En effet, les lignes fuyantes donnent un contexte de perspective et induisent un mouvement écologiquement significatif, comme une marche vers le point de fuite. À ce titre, les courbes horizontales de la figure de Hering sont le plus probablement perpendiculaires à l’axe de vision et à celui de la marche. Au niveau perceptif, elles sont donc placées à des distances différentes de l’œil et sont alors anticipées dans l’espace rétinien de telle sorte à ce que leur position est prédite à l’instant présent, d’où la forme bombée caractéristique de la perception dans cette illusion. Une extension de cette hypothèse est que le cerveau construit par des processus prédictif une image mentale de la scène visuelle. Une telle hypothèse permet de développer un formalisme théorique complet qui peut être validé quantitativement vis à vis de notre compréhension actuelle du cerveau.

""")



bib = s.content_bib("Changizi et al", "2008", 'Cognitive Science', url="https://doi.org/10.1080/03640210802035191")
for suff in ['']:
    s.add_slide(content=s.content_figures([path2('Hering_illusion' + suff + '.svg')],
        title=None, #'Classical visual illusions',
        height=s.meta['height']*height_ratio) + bib,
notes="""


""")

freemove_bib = ''
freemove_bib += s.content_bib("Friston , Adams, LP and Breakspear", "2012", 'Frontiers in Psychology', url="https://laurentperrinet.github.io/publication/friston-12/")
freemove_bib += s.content_bib("Adams, LP and Friston", "2012", 'PLoS ONE', url="https://laurentperrinet.github.io/publication/adams-12/")
freemove_bib += s.content_bib("LP, Adams and Friston", "2015", 'Biological Cybernetics', url="https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/")


#for fname in ['figure1.png', 'figure2.png']:
# figpath_law = os.path.join(home, 'quantic/2016_science/2016-10-13_LAW/figures')
for fname, note in zip(['friston_figure1.png', 'friston_figure2.png'], ["""
Cette théorie a été formalisée par le professeur Karl Friston [@tag:Friston12] sous le terme de principe de minimisation de l’énergie libre. À ce jour, c'est le seul paradigme théorique qui soit aussi complet pour expliquer le fonctionnement global du cerveau. Sans rentrer dans les détails mathématiques de ce principe, cette théorie permet de formaliser des modèles génératif pour toute sensation qui est reçu par nos organes et de considérer une représentation interne comme un état dit caché, c’est-à-dire un état ou une représentation  interne que l’on va essayer d’estimer. L'ensemble de ces hypothèses définit un système dont on déduit ensuite une variable globale dite d’énergie libre, qui donne une borne supérieure à la surprise de l’agent connaissant un modèle génératif, des sensations, des états internes et des actions effectuées. L’agent peut alors minimiser cette variable propre pour prédire au mieux son état, comme la position d’une cible. On peut aussi considérer un agent qui puisse agir sur cette environnement et on parle alors d’inférence active. En utilisant cette formalisation, il est alors possible de l’exprimer sous forme d’équations qui reprennent la structure du passage d’information dans le graphe formé par les différentes régions cérébrales. Depuis les aires sensorielles comme la rétine aux aires associatives comme celle qui forment les voies visuelles jusqu’aux airs regroupant les motoneurones qui vont permettre de générer une action motrice et un comportement.

""","""

Nous avons contribué avec Rick Adams et Karl Friston à l’application de ce principe pour expliquer des différences entre des patients typiques et des schizophrènes. En se focalisant sur les mouvements des yeux, nous avons démontré que ce paradigme permet d’expliquer les différences dans les mouvements dit de poursuites lente [@tag:Adams12]. Il est alors remarquable d’observer en perturbant dans le modèle les gains synaptiques des voies descendantes, c’est-à-dire celle qui permet d’affiner le modèle interne de représentation du monde, ont répliqué des caractéristiques comportementales des patients schizophrènes. En particulier, ces mouvements sont expliquées dans ce modèle comme une forme de délusion, qui consiste à accorder un poids relatif exagéré aux croyances représenté par le cerveau par rapport à celle apportées par les sens. Cette approche est actuellement étendue par le docteur Richard Adams afin d’apporter à terme des solutions thérapeutiques et une meilleure compréhension de pathologies comme la schizophrénie.


"""]):
    s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, fname)], bgcolor="white",
#title=title,
 height=s.meta['height']*height_ratio*height_ratio) + freemove_bib,
notes=note)

s.close_section()

i_section += 1
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 3 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""


Au cours de notre description des mécanismes sous-tendant les illusions visuelles nous nous approchons progressivement des hallucinations. Mais à la différence des illusions visuelles, celles-ci émergent sans stimulation sensorielle. Mais comment peut-on expliquer la formation d’images hallucinées, comme celle induite par la prise de drogue ou de psychotropes? Peut-on alors identifier des mécanismes qui sont impliqués dans le cerveau, et définir une neuro-anatomie fonctionnelle qui puisse expliquer ces illusions et hallucinations dans un cadre unifié?

""")


url =  'Rotating Snakes - <a href http://www.ritsumei.ac.jp/~akitaoka/index-e.html">Akiyoshi KITAOKA</a>'

s.add_slide(content=s.content_figures(
[path2('42_rotsnakes_main.jpg')],
#['https://www.illusionsindex.org/images/illusions/Rotating-Snakes/42_rotsnakes_main.jpg'],
        title=None, #'Rotating snakes',
        height=s.meta['height']*height_ratio) + url,
notes="""
https://www.illusionsindex.org/i/rotating-snakes

See also Professor Kitaoka’s personal website at http://www.ritsumei.ac.jp/~akitaoka/index-e.html

The image consists of an arrangement of snake-like concentric circles, defined by contrasting regions of colour.


Instructions

Allow your gaze to move naturally over the figure, coming to rest from time to time. Try fixing your gaze at a point and see what happens.
Effect

You should have a visual experience as of the 'snakes' rotating, when in fact they are stationary. When you fix your gaze this illusory motion ceases. Note that some snakes rotate clockwise, others anticlockwise.
The Rotating Snakes Illusion evokes a perceptual experience of illusory motion. It was invented by Japanese psychologist and academic Akiyoshi Kitaoka (Kitaoka and Ashida 2003). It is one of a class of peripheral drift illusions; whatever part of the figure is in the centre of our visual field appears motionless (as indeed it is), while the parts seen in our peripheral vision appear to move.

No-one is quite sure as to how the Rotating Snakes illusion works, although there is some consensus that it involves a difference in the processing latency of signals corresponding to different parts of the figure. Conway et al. (2003) propose that high-contrast areas are processed faster than low-contrast areas, where contrast is defined globally over the entire receptive field of an individual retinal neuron; in this case, the regions of highest contrast appear in the outermost ‘coil’ of the snakes. The illusory motion is then explained as an example of the reverse phi phenomenon first described in Anstis and Rogers (1974): a bright spot appearing and fading at some point in the visual field, subsequently followed by a dark spot appearing and fading at some other point, will create a sense of motion from the dark stimulus toward the light stimulus if this pattern is cycled. Looking closely at the figure, you will notice that adjacent ‘snakes’ are patterned so that the colours appear in the opposite order. If the reverse phi phenomenon explains illusory motion, the reversing patterns explain why some snakes rotate clockwise and others anticlockwise. A processing latency mechanism is consistent with the fact that the illusion ceases when our gaze is fixed, because in that case the signal from each part of the visual field is fairly constant. This suggests that blinks and small involuntary movements of the eye called ‘saccades’ may play an important role in triggering the illusion (Otero-Mill et al. 2012).

The Rotating Snakes Illusion is also interesting because it is relevant to debates about modularity, cognitive penetration, and the nature of experience. To explain: on the hypothesis that the mind is modular, a mental module is a kind of semi-independent department of the mind which deals with particular types of inputs, and gives particular types of outputs, and whose inner workings are not accessible to the conscious awareness of the person – all one can get access to are the relevant outputs. So, in the case of the Rotating Snakes Illusion, a standard way of explaining why experience of the illusion persists even though one knows that one is experiencing an illusion is that the module, or modules, which constitute the visual system are ‘cognitively impenetrable’ to some degree – i.e. their inner workings and outputs cannot be influenced by conscious awareness. For a general discussion of cognitive penetration, see Macpherson (2012).

Philosophers have also been interested in what illusions like the Rotating Snakes Illusion can tell us about the nature of experience. For example, in the case of experiencing the Rotating Snakes Illusion, it would seem to be that the one can know that nothing on the screen rotates whilst at the same time experiences rotating snakes. If so, then this might count against the claim the perceptual states are belief-like, because if perceptual states were belief like then, when experiencing the Rotating Snakes Illusion one would simultaneously believe that the snakes were, and were not, rotating. This would seem to entail that one was being irrational, because one would simultaneously be holding contradictory beliefs. But it seems highly implausible that one is being irrational when under going this illusion. For discussion of this general point about whether perceptions are like beliefs, see Crane & French (2016).


http://i2.cdn.cnn.com/cnnnext/dam/assets/150410134301-cat-going-up-or-down-super-169.jpg

""")

bib = s.content_bib("Bressloff et al", "2002", 'Neural Computation', url="http://homepage.ruhr-uni-bochum.de/Dirk.Jancke/line-motion-examples.html")

for no in ['2b', '2a', '3', '7']:
    s.add_slide(content=s.content_figures(
    [path2('Bressloff2002Fig' + no + '.png')], title=None, #title, embed=s.meta['embed'],
    height=s.meta['height']*height_ratio) + bib,
   notes="""

Une hypothèse novatrice proposée par Paul Bressloff et collègues en 2002 [@tag:Bressloff02] est de voir l’origine de certaines illusions ou hallucinations dans l'interaction entre la structure de la représentation rétinienne et des représentations de cette espace visuel dans l’aire visuelle primaire. En effet, la représentation rétinienne de l’espace visuel est organisés de façon radiale depuis le point de fixation (polaire) avec une forte densité de photorécepteurs près de l’axe de vision. La représentation corticale d’une ligne est un segment dans l’espace cortical et inversement un segment dans l’espace cortical va apparaître et être perçu comme une spirale une fois re-projetée dans l’espace visuel codé par l’espace rétinien. En se basant sur une modélisation des connexions latérales entre des populations voisines de neurones de l’aire visuelle primaire, ces auteurs ont alors établi dans un modèle de champ neural qui régit la dynamique de la carte d’activité l’émergence structurée de représentations privilégiées. Comme nous l’avons décrit à l’échelle macroscopique avec notre modèle d’agent schizophrénique [@tag:Adams12], ces auteurs ont alors analysé mathématiquement les états du système quand on perturbe certains paramètres du système, notamment les poids synaptiques régissant les interactions dans la carte corticale.
Ils ont alors montré un point essentiel : à partir d’un certain seuil de prise de drogue, des « hallucinations » peuvent émerger comme des structures stables dans la carte corticale. Étonnamment, ces états une fois un re-projetés sur l’espace visuel dessinent des spirales et des ensembles de lignes qui sont très proches des hallucinations telles qu’elles ont été rapportées après la prise de drogues diverses allant de la marijuana au peyotl ou à la mescaline. Ce type de modélisation permet d’un côté d’expliquer la formation d’hallucinations, mais aussi de définir une « neuro-géométrie », c’est-à-dire un formalisme mathématique reliant neurosciences et la géométrie des relations existant entre des sous module de l’aire visuelle primaire. On peut aussi imaginer alors des hallucinations plus complexes émerger de réseaux plus complexes qui représentent par exemple des superpositions de visages.
""")


bib = s.content_bib("Jancke, Chavane, Naaman and Grinvald", "2004", 'Nature', url="http://homepage.ruhr-uni-bochum.de/Dirk.Jancke/line-motion-examples.html")

def create_movie(figname, duration=1.5,
                radius=1/18, length=.618,
                fps=50, W=1000, H=600):
    import gizeh as gz
    import moviepy.editor as mpy

    r = W*radius
    s = dict(fill=(1, 1, 1), ly=r)
    def make_frame(t):
        surface = gz.Surface(W, H, bg_color=(0, 0, 0))
        if t > duration/3:
            if t < duration*2/3:
                x = W/2. - length*W/2 + r/2
                rect = gz.rectangle(xy=(x, H/2.),
                                 lx=r, **s)
            else:
                rect = gz.rectangle(xy=(W/2., H/2.),
                                    lx=length*W, **s)
            rect.draw(surface)
        return surface.get_npimage()

    clip = mpy.VideoClip(make_frame, duration=duration)
    clip.write_videofile(path2(figname), fps=fps)
    return 'ok'

figname='line_motion.mp4'
if not os.path.isfile(path2(figname)): create_movie(figname)

s.add_slide(content="""
 <video controls autoplay loop width=99%/>
   <source type="video/mp4" src="{}">
 </video>
 """.format(s.embed_video(path2(figname))) ,
notes="""

Line motion illusion.

""")


s.add_slide(content=s.content_figures(
    [path2('Jancke_etal2004.png')], title=title, embed=s.meta['embed'],
    height=s.meta['height']*height_ratio) + bib,
   notes="""

Imaging cortical correlates of illusion in early visual cortex.

Nature 428, 423-426. (see movies of the illusion and its cortical correlate)

""")


def create_movie(figname, duration=1.5,
                radius=1/13, length=1/8,
                fps=50, W=1000, H=600):
    import gizeh as gz
    import moviepy.editor as mpy

    r = W*radius
    def make_frame(t):
        surface = gz.Surface(W, H, bg_color=(0, 0, 0))
        if t > duration/3:
            if t < duration*2/3:
                x = W/2. - length*W/2
            else:
                x = W/2. + length*W/2
            rect = gz.rectangle(xy=(x, H/2.),
                                fill=(1, 1, 1), lx=r, ly=r)
            rect.draw(surface)
        return surface.get_npimage()

    clip = mpy.VideoClip(make_frame, duration=duration)
    clip.write_videofile(path2(figname), fps=fps)
    return 'ok'

figname='phi_motion.mp4'
if not os.path.isfile(path2(figname)): create_movie(figname)

s.add_slide(content="""
 <video controls autoplay loop width=99%/>
   <source type="video/mp4" src="{}">
 </video>
 """.format(s.embed_video(path2(figname))) ,
notes="""


""")


bib = s.content_bib("Chemla, Reynaud, diVolo, Zerlaut, Perrinet, Destexhe and Chavane", "2019", 'Journal of Neuroscience', url="https://laurentperrinet.github.io/publication/chemla-19/")
bib = s.content_bib("Chemla et al", "2019", 'Journal of Neuroscience', url="https://laurentperrinet.github.io/publication/chemla-19/")

s.add_slide(content=s.content_figures(
    [path2('Chemla_etal2019.png')], title=title, embed=s.meta['embed'],
    height=s.meta['height']*height_ratio) + bib,
   notes="""

Pour aller plus loin dans cette direction, peut-on étendre cette méthodologie à la dynamique présente dans certaines illusions, comme celle du « Point-Ligne » ? En effet, en présentant un simple point puis une ligne on induit une perception d’une expansion du point pour « remplir » la ligne (un mouvement dit Phi). L’originalité de l’étude de Jancke et collègues est d'utiliser une technique d’imagerie qui permet d’enregistrer l’activité sur le cortex visuel primaire (ici du chat anesthésié) lors de la présentation de cette illusion d’optique. À noter qu’en comparant l’activité produite par les deux éléments présentés séparément ou conjointement, on met en évidence une activité différentielle qui est caractéristique de la perception de cette illusion. Une même  méthodologie permet de mettre en évidence un mécanisme original. Pour cela on utilise cette fois une illusion encore plus simple qui consiste à montrer un point à une position de l’espace visuel puis un autre point exactement similaire mais à une distance proche (mais supérieure à la taille de ce point). On perçoit alors un et un seul point qui se déplace de la première à la seconde position. Au niveau des enregistrements (cette fois chez le macaque) la réponse différentielle montre que relativement à un traitement indépendant des deux points, il existe une vague d’activité qui se déplace sur le cortex qui en particulier supprime une partie de l’activité [@tag:Chemla19]. Une modélisation sur ordinateur a permis de montrer qu'une fonction de cette vague de suppression est de lever les ambiguïtés sur les différents mouvements possibles représentés sur la carte. Dans ce cas particulier, la vague permet de supprimer la représentation d’un mouvement dans le sens opposé. Toutefois, beaucoup de questions restent en suspens. Ces résultats montrent le rôle potentiel des vagues d’activité sur la surface du cortex comme un outil potentiel de traitement de l’information et de sa modulation [@tag:Muller18]. Ces vagues peuvent en effet induire facilitations ou suppressions dans l'espace et le temps et produire une forme de « calcul » pour représenter au mieux l’image visuelle.

""")
s.close_section()

############################################################################ 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
######################################################################################################################################################s.open_section()
s.add_slide(content=intro,
            notes="""
Pour résumer, les illusions et hallucinations nous ouvre une porte sur les possibilités de la perception mais aussi sur une compréhension des mécanismes cérébraux qui les induisent. La modélisation, notamment celle que nous proposons, offre une opportunité nouvelles d’appréhender ces mécanismes. Les outils théoriques permettant de progresser dans cette voie de recherche existent mais ne sont pas pour le moment exploités à leur plein potentiel. Ils seront essentiels pour une meilleure compréhension des illusions visuelles, des hallucinations et de ce qui peut la provoquer, mais aussi du cerveau en général.

* Thanks for your attention!
""")


s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code ")

s.close_section()

########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

if slides_filename is None:
    with open("README.md", "w") as text_file:
        text_file.write("""\
# {title}

* What:: talk @ [{conference}]({conference_url})
* Who:: {author}
* Where: {location}, see {url}
* When: {DD:02d}/{MM:02d}/{YYYY}, time: {time_start}-{time_end}

* What:
  * Slides @ https://laurentperrinet.github.io/{tag}
  * Code for slides @ https://github.com/laurentperrinet/{tag}/
  * Abstract: {abstract}

""".format(**meta))

    with open("/tmp/talk.bib", "w") as text_file:
        text_file.write("""\
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}",
    Title = "{title}",
    Abstract = "{abstract}",
    Year = "{YYYY}",
    Date = "{YYYY}-{MM:02d}-{DD:02d}",
    location = "{location}",
    projects = "{projects}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_start}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_end}",
    url = "{url}",
    url_slides = "https://laurentperrinet.github.io/{tag}",
    url_code = "https://github.com/laurentperrinet/{tag}/",
}}

""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
