# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
#
# Copyright (c) 2022 DC540 Defcon Group
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

cards = {
    '0 Fool':
        [
            'Taking a risk. Getting outside your comfort zone. Knowing the universe is looking after you.',
            'Foolishness. Making a stupid choice. Disregarding good advice. Getting in with a bad crowd.'
            '00-TheFool.png',
        ],
    '1 Magician':
        [
            'Feeling confident, assured. Having all the tools and resources at your disposal. Power.',
            'Deception, trickery, cunning. Scammer. Personality disorders such as narcissism. Lack of empathy.',
            '01-TheMagician.png'
        ],
    '2 High Priestess':
        [
            'Intuition. Going within. Inner knowing.',
            'Emerging from depression. Extreme shyness or over-confidence, denying intuition, predatory sexual behavior, superficiality, disclosure of secrets.',  # noqa
            '02-TheHighPriestess.png'
        ],
    '3 Empress':
        [
            'Growth, fertility, pregnancy, motherhood. New project. Dominant female.',
            'Famine, drought. Neglected land. Smother-love, living through your children. Vanity, empty nest syndrome, feeling useless, infidelity, unloving, unsupportive. Fertility issues. Failing business. Problems with adoption or step-parenting.',  # noqa
            '03-TheEmpress.png'
        ],
    '4 Emperor':
        [
            'Structure, organization, rules. Dominant male.',
            'Nature controlled. Urban sprawl and degeneration. Authoritarian, tyrant, dictator, domination, rigid, unyielding, fatherhood problems, loss of control, obstruction, misuse of power.',  # noqa
            '04-TheEmperor.png'
        ],
    '5 Hierophant':
        [
            'Learning path, religion, spirituality, spiritual mentor, guide.',
            'Rejection of the establishment. A mentor with ulterior motives. Expulsion, excommunication. Sexual misdemeanors. Inappropriate behavior. Rejecting one’s faith.',  # noqa
            '05-TheHierophant.png'
        ],
    '6 Lovers':
        [
            'Life-changing choice, turning point. Union with another, two as one.',
            'Inappropriate relationship. Immaturity, lack of love, possessiveness, infatuation/stalking. Lust rather than love. Bad choice, indecision, temptation, weakness, lack of trust, separation. Endless obsessive search for non-existent soul-mate.',   # noqa
            '06-TheLovers.png'
        ],
    '7 Chariot':
        [
            'Drive and determination. Autonomy. Mediation and negotiation.',
            'Ambition but at a cost. Personal life derailed. Travel problems. Stress, quarrels, accidents, delays. Failed negotiation.',  # noqa
            '07-TheChariot.png'
        ],
    '8 Strength':
        [
            '',
            '',  # noqa
            ''
        ],
    '9 Hermit':
        [
            '',
            '',  # noqa
            ''
        ],
    '10 Wheel Of Fortune':
        [
            '',
            '',  # noqa
            ''
        ],
    '11 Justice':
        [
            '',
            '',  # noqa
            ''
        ],
    '12 Hanged Man':
        [
            '',
            '',  # noqa
            ''
        ],
    '13 Death':
        [
            '',
            '',  # noqa
            ''
        ],
    '14 Temperance':
        [
            '',
            '',  # noqa
            ''
        ],
    '15 Devil':
        [
            '',
            '',  # noqa
            ''
        ],
    '16 Tower':
        [
            '',
            '',  # noqa
            ''
        ],
    '17 Star':
        [
            '',
            '',  # noqa
            ''
        ],
    '18 Moon':
        [
            '',
            '',  # noqa
            ''
        ],
    '19 Sun':
        [
            '',
            '',  # noqa
            ''
        ],
    '20 Judgment':
        [
            '',
            '',  # noqa
            ''
        ],
    '21 World':
        [
            '',
            '',  # noqa
            ''
        ],
    '22 Ace Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '23 Two Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '24 Three Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '25 Four Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '26 Five Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '27 Six Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '28 Seven Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '29 Eight Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '30 Nine Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '31 Ten Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '32 Page Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '33 Knight Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '34 Queen Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '35 King Of Wands':
        [
            '',
            '',  # noqa
            ''
        ],
    '36 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '37 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '38 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '39 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '40 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '41 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '42 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '43 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '44 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '45 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '46 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '47 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '48 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '49':
        [
            '',
            '',  # noqa
            ''
        ],
    '50 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '51 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '52 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '53 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '54 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '55 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '56 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '57 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '58 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '59 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '60 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '61 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '62 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '63 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '64 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '65 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '66 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '67 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '68 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '69 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '70 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '71 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '72 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '73 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '74 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '75 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '76 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '77 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '78 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '79 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '80 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '81 ':
        [
            '',
            '',  # noqa
            ''
        ],
    '82 ':
        [
            '',
            '',  # noqa
            ''
        ],
}

ham_radio_questions = {
    'What is the name for the distance a radio wave travels during one complete cycle?':
        [
            'A. Wave Speed',
            'B. Waveform',
            'C. Wavelength',
            'D. Wave Spread',
            2
        ],
    'What year was the first computer invented?':
        [
            'A. 1954',
            'B. 1943',
            'C. 1961',
            'D. 1948',
            1
        ],
    'How fast does a radio wave travel through free space?':
        [
            'A. At the speed of light.',
            'B. At the speed of sound.',
            'C. Its speed is inversely proportional to its wavelength.',
            'D. Its speed increases as the frequency increases.',
            0
        ],
    'How does the wavelength of a radio wave relate to its frequency?':
        [
            'A. The wavelength gets longer as the frequency increases.',
            'B. The wavelength gets shorter as the frequency increases.',
            'C. There is no relationship between wavelength and frequency.',
            'D. The wavelength depends on the bandwidth of the signal.',
            1
        ]
}
