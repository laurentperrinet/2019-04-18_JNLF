__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
DEBUG = True
DEBUG = False

fig_width = 12

import os
home = os.environ['HOME']
figpath_talk = 'figures'
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
height_ratio = .7

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
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
          'Hallucinations: quand les illusions deviennenty réelles',
          'Une neuro-anatomie fonctionnelle des illusions?',
          ]
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname_qr = os.path.join(figpath_talk, 'qr.png')
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
LM = s.content_imagelet(os.path.join(figpath_people, 'LM.png'), height_px)
JB = s.content_imagelet(os.path.join(figpath_people, 'JB.jpg'), height_px)
Fredo = s.content_imagelet(os.path.join(figpath_people, 'fredo.png'), height_px)
Python = s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px)
s.meta['Acknowledgements'] =f"""
<small>
<h5>Acknowledgements:</h5>
<ul>
    <li>Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
    <li>Jean-Bernard Damasse, Laurent Madelain and Anna Montagnini  - ANR REM</li>
    <li>Frédéric Chavane - INT</li>
</ul>
<BR>
{Rick}{Karl}{JB}{LM}{Anna}{Fredo}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
<BR>
    This work was supported by ANR project "Horizontal-V1" N° ANR-17-CE37-0006.
</small>

"""
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 1 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################
i_section = 0
s.open_section()
###############################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
###############################################################################
# s.add_slide(content=intro)
#
# s.add_slide(content=s.content_figures(
#     #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
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

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU

* (OBJECTIVE)


* Let's me first describe the motivation of this work...



* (SHOW TITLE)

""")

bib = s.content_bib("Akiyoshi KITAOKA", "2010", 'wwww', url="http://www.ritsumei.ac.jp/~akitaoka/index-e.html")

s.add_slide(content=s.content_figures(
['https://www.illusionsindex.org/images/illusions/Rotating-Snakes/42_rotsnakes_main.jpg'],
        title=' Rotating snakes ', height=s.meta['height']*.825) + bib,
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

url =  '<a href https://en.wikipedia.org/wiki/The_dress">#TheDress</a>'

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'The_Dress_(viral_phenomenon).png')],
        title=None, height=s.meta['height']*.825) + url,
notes="""

https://en.wikipedia.org/wiki/The_dress

The dress is a photograph that became a viral internet sensation on 26 February 2015, when viewers disagreed over whether the dress pictured was coloured blue and black, or white and gold. The phenomenon revealed differences in human colour perception, which have been the subject of ongoing scientific investigations into neuroscience and vision science, with a number of papers published in peer-reviewed science journals.

The photo originated from a washed-out colour photograph of a dress posted on the social networking service Tumblr. Within the first week after the surfacing of the image, more than 10 million tweets mentioned the dress, using hashtags such as #thedress, #whiteandgold, and #blackandblue. Although the actual colour was eventually confirmed as blue and black,[3][4] the image prompted many discussions, with users debating their opinions on the colour and how they perceived the dress in the photograph as a certain colour. Members of the scientific community began to investigate the photo for fresh insights into human color vision.

The dress itself, which was identified as a product of the retailer Roman Originals, experienced a major surge in sales as a result of the incident. The retailer also produced a one-off version of the dress in white and gold as a charity campaign.
""")


bib = s.content_bib("Cydonia Mensae", "1976", 'Viking Orbiter image', url="Viking Orbiter image")
for fname in ['Face-on-mars.jpg', 'Viking_moc_face_20m.gif']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, fname)],
            title="Paréidolie", height=s.meta['height']*.825) + url,
    notes="""
    Cydonia was first imaged in detail by the Viking 1 and Viking 2 orbiters. Eighteen images of the Cydonia region were taken by the orbiters, of which seven have resolutions better than 250 m/pixel (820 ft/pixel). The other eleven images have resolutions that are worse than 550 m/pixel (1800 ft/pixel) and are of limited use for studying surface features. Of the seven good images, the lighting and time at which two pairs of images were taken are so close as to reduce the number to five distinct images. The Mission to Mars: Viking Orbiter Images of Mars CD-ROM set image numbers for these are: 035A72 (VO-1010), 070A13 (VO-1011), 561A25 (VO-1021), 673B54 & 673B56 (VO-1063), and 753A33 & 753A34 (VO-1028).[11][12]

    In one of the images taken by Viking 1 on July 25, 1976, a two-kilometre-long (1.2 mi) Cydonian mesa, situated at 40.75° north latitude and 9.46° west longitude,[13] had the appearance of a humanoid face. When the image was originally acquired, Viking chief scientist Gerry Soffen dismissed the "Face on Mars" in image 035A72[14] as a "trick of light and shadow".[15][16] However, a second image, 070A13, also shows the "face", and was acquired 35 Viking orbits later at a different sun-angle from the 035A72 image. This latter discovery was made independently by Vincent DiPietro and Gregory Molenaar, two computer engineers at NASA's Goddard Space Flight Center. DiPietro and Molenaar discovered the two misfiled images, Viking frames 035A72 and 070A13, while searching through NASA archives.[17]
    2.1 Later imagery

    More than 20 years after the Viking 1 images were taken, a succession of spacecraft visited Mars and made new observations of the Cydonia region. These spacecraft have included NASA's Mars Global Surveyor (1997–2006) and Mars Reconnaissance Orbiter (2006–),[18] and the European Space Agency's Mars Express probe (2003–).[19] In contrast to the relatively low resolution of the Viking images of Cydonia, these new platforms afford much improved resolution. For instance, the Mars Express images are at a resolution of 14 m/pixel (46 ft/pixel) or better. By combining data from the High Resolution Stereo Camera (HRSC) on the Mars Express probe and the Mars Orbiter Camera (MOC) on board NASA's Mars Global Surveyor it has been possible to create a three-dimensional representation of the "Face on Mars".[20]
    """)
s.close_section()

i_section += 1
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 2 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
Indeed, these raw psycholophysical results are encouraging but since we used a generative model for generating the sequence, let's see if we can build a Bayesian model which would be optimal wrt to this generative model.

Indeed, such a model already exists, the onlin BCP, and we will adapt it for our specific setting.
""")


url =  'full code @ <a href="https://github.com/chloepasturel/AnticipatorySPEM">github.com/chloepasturel/AnticipatorySPEM</a>'

s.add_slide(content=s.content_figures(
   [os.path.join(figpath_talk, 'scheme_thorpe.jpg')], bgcolor="black",
   height=s.meta['height']*.90),
notes="""

 * today, I would like  to focus on a particular problem which will help us unravel the dynamics of decision making: oculomotor delays.
 *
  The central nervous system has to contend with axonal delays, both at the sensory and the motor levels. For instance, in the human visuo-oculomotor system, it takes approximately $ \tau_s=50~ms$ for the retinal image to reach the visual areas implicated in motion detection, and a further $ \tau_m=40~ms $ to reach the oculomotor muscles.

 * how does this impact behaviour? Indeed, one challenge for modelling is to understand EMs using AI as a problem of optimal motor control under axonal delays.
 """)


s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'tsonga.png')], bgcolor="black",
    height=s.meta['height']*.90),
    notes="""
 * let's move to a human, in particular a tennis player ---here (highly trained) Jo-Wilfried Tsonga at Wimbledon---...

 * ...  trying to intercept a passing-shot ball at a (conservative) speed of $20~m.s^{-1}$, the position sensed on the retinal space corresponds to the instant when its image formed on the photoreceptors of the retina and reaches our hypothetical motion perception area behind:

  """)

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'figure-tsonga.png')], bgcolor="black",
    height=s.meta['height']*.90),
    #image_fname=os.path.join(figpath, 'figure-tsonga.png'), embed=False,
        notes="""

 * and at this instant, the sensed physical position is lagging behind (as represented here by $\tau_s \cdot v 1~m$ ), that is, approximately at $45$ degrees of eccentricity (red dotted line),

 * while the  position at the moment of emitting the motor command will be $.8~m$ ahead of its present physical position ($\tau_m \cdot v$).

 * As a consequence, note that the player's gaze is directed to the ball at its **present** position (red  line), in anticipatory fashion. Optimal control directs action (future motion  of the eye) to the expected position (red dashed line) of the ball in the  future --- and the racket (black dashed line) to the expected position of the  ball when motor commands reach the periphery (muscles). This is obviously an interesting challenge for modelling an optimal control theory.

 """)


fle_bib = s.content_bib("Khoei, Masson and LP", "2017", 'PLoS CB', url="http://invibe.net/LaurentPerrinet/Publications/KhoeiMassonPerrinet17")

s.add_slide(content="""
 <video controls autoplay loop width=99%/>
   <source type="video/mp4" src="{}">
 </video>
 """.format(s.embed_video(os.path.join(figpath_talk, 'flash_lag.mp4'))) + fle_bib,
notes="""

so let's go back on earth

* ... but first let now apply this model compensating for the aforementioned visual delays using a well described visual illusion: the flash-lag effect:

a first stimulus moves continuously across the screen along the central horizontal axis. In the FLE, as this moving stimulus reaches the center of the screen, a second stimulus is flashed just above it and in perfect vertical alignment. Despite the fact that the respective horizontal positions of each stimulus are physically identical when the flash occurs, the moving stimulus is most often perceived *ahead* of the flashed one.

debate for 80 years revived recently

- motion extrapolation
- differential latency
- post-diction

we propose to extend the hypothesis previously proposed by Nihjawan that this effect is caused by the extrapolation of the stimulus' motion to compensate for the neural delay. However, this hypothesis was challenged by other hypothesis that this effect is due to either anatomy (differential latencies) or to the way visual awareness processes the sequence of events (the post-diction from Eagleman)

As a matter of fact, the motion extrapolation hypothesis was challenged because you can notice that the FLE is still present at initiation of the movement but this effect is not seen if the moving dot abruptly stops at the moment of the flash



""")


s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'FLE_histogram.png')], title=title, embed=False,
    height=s.meta['height']*.8) + fle_bib,
   notes="""

* For that, we replot the movies I have just shown by showing for the dot the Histogram of the estimated positions as a function of time for the source layer (Left) and the target layer (right). The left-hand column illustrates the predictive model before delay compensation. The right-hand column illustrates the motion extrapolation model with delay compensation. Histograms of the inferred horizontal positions (blueish bottom panel) and  horizontal speed (redish top panel) are shown in columns  as a function  of time. A darker level corresponds to a higher probability, while a light  color corresponds to an unlikely estimation. In particular, we focus on three  particular epochs along the trajectory, corresponding to the standard, flash  initiated and terminated cycles. The timing of these epochs flashes are indicated by  dashed vertical lines. In dark, the physical time and in green the delayed  input knowing $\tau=100~ms$.

* Activity in both models shows three different phases. First, there is a rapid  build-up of the precision of the target after the first appearance of the  moving dot (at $t=300~ms$). Consistently with the Frölich effect, the  beginning of the trajectory is seen ahead of its physical position. During the second phase, the moving dot is correctly tracked as both its velocity and position are correctly inferred. In the source layer, there is no extrapolation and the trajectory follows the delayed trajectory of the dot (green dotted line). In the target layer, motion extrapolation correctly predicts the position at the present time and the position follows the actual physical position of the dot (black dotted line). Finally, the third phase corresponds to  motion termination. The moving dot disappears and the corresponding activity vanishes in the source layer at $t=900~ms$. However, between $t=800~ms$ and $t=900~ms$, the dot position was extrapolated and predicted ahead of the terminal position. At $t=900~ms$, while motion information is absent, the position information is still transiently consistent and extrapolated using a broad, centered prior distribution of speeds. Although it is less precise, this position of the dot at flash termination is therefore not perceived as leading the flash.

* Interestingly, and thanks to the reviewers of the paper, we could extend our results to the estimation of the dot position from the dMBP model during the motion reversal experiment. In the motion reversal experiment, the moving dot reverses its direction  at the middle of the trajectory (i.e., at $t=500~ms$,  as indicated by the mid-point vertical dashed line).  In the left column (target layer) and as in previous slide, we show the histogram of inferred positions  during the dot motion and a trace of its position with the highest probability  as a function of time.  As expected, results are identical to that in the previous slide in the first half period.  At the moment of the motion reversal,  the model output is consistent with previous psychophysical reports.  First, the estimated position follows the extrapolated trajectory  until the (delayed) sensory information about the motion reversal reaches the system  (at $t=600~ms$, green vertical dashed line).  Then, the velocity is quickly reseted and converges to the new (reversed) motion  such that the estimated position ``jumps'' to a position corresponding  to the updated velocity.  In the right column (smoothed layer), we show the results of the same data  after a smoothing operation of $\tau_s=100~ms$ in subjective time.  This different read-out from the inferred positions  corresponds to the behavioral results obtained in some experiments,  such as that from~\citet{Whitney98}.

""")

s.close_section()

i_section += 1
###########################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 section no 3 🏄🏄🏄🏄🏄🏄🏄🏄
###########################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""

Jancke D, Chavane F, Na'aman S, Grinvald A (2004).

Imaging cortical correlates of illusion in early visual cortex.

Nature 428, 423-426. (see movies of the illusion and its cortical correlate)

""")

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'Jancke_etal2004.png')], title=title, embed=False,
    height=s.meta['height']*.8) + fle_bib,
   notes="""

""")

s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'Chemla_etal2019.png')], title=title, embed=False,
    height=s.meta['height']*.8) + fle_bib,
   notes="""

""")
s.close_section()

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
s.add_slide(content=intro,
            notes="""


* Thanks for your attention!
""")


s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code ")

s.close_section()

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


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
