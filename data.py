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

instructions = 'Welcome to the DC540 Tarot Badge.  Here you can play games and get a tarot reading and do all sorts of stuff stay tuned.  Bla bla foo.'  # noqa

boss_ids = []  # noqa
boss_ids.append('e66038b7137a9935')
boss_ids.append('e66038b7135fa935')
boss_ids.append('e66038b71316902f')
boss_ids.append('e66038b713338c2f')

boss_names = []  # noqa
boss_names.append('Baabalicious')
boss_names.append('Banter')
boss_names.append('Lyra')
boss_names.append('Kevin')

cards = {
    '0 The Fool':
        [
            'Taking a risk. Getting outside your comfort zone. Knowing the universe is looking after you.',
            'Foolishness. Making a stupid choice. Disregarding good advice. Getting in with a bad crowd.',
            '00-TheFool.raw',
        ],
    '1 The Magician':
        [
            'Feeling confident, assured. Having all the tools and resources at your disposal. Power.',
            'Deception, trickery, cunning. Scammer. Personality disorders such as narcissism. Lack of empathy.',
            '01-TheMagician.raw'
        ],
    '2 The High Priestess':
        [
            'Intuition. Going within. Inner knowing.',
            'Emerging from depression. Extreme shyness or over-confidence, denying intuition, predatory sexual behavior, superficiality, disclosure of secrets.',  # noqa
            '02-TheHighPriestess.raw'
        ],
    '3 The Empress':
        [
            'Growth, fertility, pregnancy, motherhood. New project. Dominant female.',
            'Famine, drought. Neglected land. Smother-love, living through your children. Vanity, empty nest syndrome, feeling useless, infidelity, unloving, unsupportive. Fertility issues. Failing business. Problems with adoption or step-parenting.',  # noqa
            '03-TheEmpress.raw'
        ],
    '4 The Emperor':
        [
            'Structure, organization, rules. Dominant male.',
            'Nature controlled. Urban sprawl and degeneration. Authoritarian, tyrant, dictator, domination, rigid, unyielding, fatherhood problems, loss of control, obstruction, misuse of power.',  # noqa
            '04-TheEmperor.raw'
        ],
    '5 The Hierophant':
        [
            'Learning path, religion, spirituality, spiritual mentor, guide.',
            'Rejection of the establishment. A mentor with ulterior motives. Expulsion, excommunication. Sexual misdemeanors. Inappropriate behavior. Rejecting one’s faith.',  # noqa
            '05-TheHierophant.raw'
        ],
    '6 The Lovers':
        [
            'Life-changing choice, turning point. Union with another, two as one.',
            'Inappropriate relationship. Immaturity, lack of love, possessiveness, infatuation/stalk. Lust rather than love. Bad choice, indecision, temptation, weakness, lack of trust.',   # noqa
            '06-TheLovers.raw'
        ],
    '7 The Chariot':
        [
            'Drive and determination. Autonomy. Mediation and negotiation.',
            'Ambition but at a cost. Personal life derailed. Travel problems. Stress, quarrels, accidents, delays. Failed negotiation.',  # noqa
            '07-TheChariot.raw'
        ],
    '8 Strength':
        [
            'Persuasion, gentle strength. Patience, control, compassion.',
            'Mental problems. Too overbearing or too weak. Not knowing when to stop. Government vs citizens. Cruelty. Disregarding the well-being of others in order to achieve your desire.',  # noqa
            '08-Strength.raw'
        ],
    '9 The Hermit':
        [
            'Knowing oneself, solitude. Understanding humanity, wisdom.',
            'Fear of being alone. Social withdrawal, paranoia, identity crisis, embittered. Worry about aging. Fear of having to depend on others.',  # noqa
            '09-TheHermit.raw'
        ],
    '10 Wheel Of Fortune':
        [
            'Change, good luck, destiny.',
            'Change. Good and bad luck. Destiny, chaos, uncertainty.',  # noqa
            '10-WheelOfFortune.raw'
        ],
    '11 Justice':
        [
            'Cause and effect, karma, fairness, legal issues.',
            'Cause and effect. Poetic justice, unfairness, disputes, legal problems. Bigotry, bias, intolerance. Liver damage.',  # noqa
            '11-Justice.raw'
        ],
    '12 The Hanged Man':
        [
            'On hold, nothing happening, stuck, letting go of the outcome.',
            'Ready to go but being held back. Hidden motives or agenda. Unfinished work or projects. About to move on from a friendship or relationship.',  # noqa
            '12-TheHangedMan.raw'
        ],
    '13 Death':
        [
            'Endings and new beginnings, transformation, transition. Death.',
            'Attempting to avoid an inevitable end. Chronic illness. Extreme depression or pessimism. Coming back from the dead (NDE). Obsession with death. Accident (narrowly escaping death).',  # noqa
            '13-Death.raw'
        ],
    '14 Temperance':
        [
            'Chemistry, moderation, balance. Getting it right.',
            'Out of balance, non-cooperation, conflicting ideas/positions. Emotional extremes. Procrastination. Digestive problems. Mind/body health out of whack.',  # noqa
            '14-Temperance.raw'
        ],
    '15 The Devil':
        [
            'Addiction, bad habits, co-dependency, materialism.',
            'Extremes of the upright meaning: Life-threatening addiction, psychopathic personality disorder. Abuse (mental and physical). Escape, release, moving forward, taking control of your problems and your life.',  # noqa
            '15-TheDevil.raw'
        ],
    '16 The Tower':
        [
            'Chaos, destruction, upheaval. Unexpected and possibly unwanted change.',
            'Weakened energy of upright card. Irritations, things going wrong, setbacks, pressure, stress. Accidents, cuts, burns, surgery. Need to visit the doctor. Can\'t see the way through all the problems.',  # noqa
            '16-TheTower.raw'
        ],
    '17 The Star':
        [
            'Renewed optimism, hope, serenity. Spiritual love and joy.',
            'Low self-esteem. Lack of clarity. Futility. Not feeling the love around you. Disappointment.',  # noqa
            '17-TheStar.raw'
        ],
    '18 The Moon':
        [
            'Insecurity, anxiety, illusion, fear, health issues.',
            'Resistance to anything spiritual. Self-delusion. Closed mind. Mental health issues, and things like fibromyalgia and urinary tract problems.',  # noqa
            '18-TheMoon.raw'
        ],
    '19 The Sun':
        [
            'Improvement, growth, positivity, love, abundance, joy.',
            'Weakened energy of upright card. Still positive but less so. Success is mediocre. Happiness on a lower scale.',  # noqa
            '19-TheSun.raw'
        ],
    '20 Judgment':
        [
            'Rebirth, calling, forgiveness.',
            'Problematic transitions. Resistance, rejection, alienation. Over critical and judgmental.',  # noqa
            '20-Judgement.raw'
        ],
    '21 The World':
        [
            'In the right place. Accomplishment, completion. Pause before the next stage.',
            'Slightly weakened energy of upright card so generally positive. Completion of projects delayed. Wanting to move forward but held back. Overdue birth. Issues with weight loss. Having to wait for test results.',  # noqa
            '21-TheWorld.raw'
        ],
    '22 Ace Of Wands':
        [
            'Rush of energy, inspiration, passion, creativity.',
            'Weakened energy of upright meaning. Inappropriate attraction/affair. Lack of growth and expansion.',  # noqa
            'Wands01.raw'
        ],
    '23 Two Of Wands':
        [
            'Planning, decisions, delays.',
            'Unexpected turn of events. A new perspective on an old problem. Reluctance, self-imposed restriction.',  # noqa
            'Wands02.raw'
        ],
    '24 Three Of Wands':
        [
            'Enterprise, entrepreneurial spirit, responsibility, opportunity. New job.',
            'Feeling blocked. Unable to get projects started or completed. Delayed results. Investment anxiety. Distrust.',  # noqa
            'Wands03.raw'
        ],
    '25 Four Of Wands':
        [
            'Community, celebration, domestic comfort, engagement, wedding, housewarming. A job well done.',
            'Not much different from upright. Celebration, reunions, break from hard work. Building of foundations, cementing of relationships. Sale of property.',  # noqa
            'Wands04.raw'
        ],
    '26 Five Of Wands':
        [
            'Arguments, disagreements, tension, competition, strife.',
            'Refusing to engage in hostility or conflict. Settling disputes. Inner conflicts, beset by inner demons.',  # noqa
            'Wands05.raw'
        ],
    '27 Six Of Wands':
        [
            'Victory, achievement. Good results in exams. Public acknowledgment.',
            'Treachery, betrayal. Short-lived victory. Pride before a fall. Embarrassment. Public humiliation.',  # noqa
            'Wands06.raw'
        ],
    '28 Seven Of Wands':
        [
            'Standing your ground, challenge, not giving up.',
            'Putting up barriers, refusing to negotiate. Obstinate. Biased.',  # noqa
            'Wands07.raw'
        ],
    '29 Eight Of Wands':
        [
            'Change, getting organized, motivation, travel, possible pregnancy.',
            'Unforeseen, difficult event. Shock. Family or business problems. Think of this reversal as the Tower’s baby brother.',  # noqa
            'Wands08.raw'
        ],
    '30 Nine Of Wands':
        [
            'Courage, determination, resilience.',
            'Overwhelmed. Ready to give up. Illness, nagging pain. Can’t see the the wood for the trees.',  # noqa
            'Wands09.raw'
        ],
    '31 Ten Of Wands':
        [
            'Responsibilities, stress, tough times.',
            'Hard labor; little results. Letting go of a goal or dream. Facing a difficult reality.',  # noqa
            'Wands10.raw'
        ],
    '32 Page Of Wands':
        [
            'Explorer, potential, free agent, no ties, messenger (or message arriving swiftly).',
            'Childishness, tantrums. Lacking concentration and determination. Bad news or a reprimand in the form of a message.',  # noqa
            'Wands11.raw'
        ],
    '33 Knight Of Wands':
        [
            'Lust, enthusiasm, entrepreneurial spirit, scattered energy.',
            'A rogue, a philanderer, a user. A brawler. A cheater. Over-enthusiasm, impatience, bad temper. Prone to violence.',  # noqa
            'Wands12.raw'
        ],
    '34 Queen Of Wands':
        [
            'Warmth, vibrancy, sexual enthusiasm.',
            'The other woman. A jealous, temperamental mistress. A rival in love or work. Promiscuity, extravagance. Fever, infections.',  # noqa
            'Wands13.raw'
        ],
    '35 King Of Wands':
        [
            'Leader, visionary, role model, temperamental, egotistical.',
            'Arrogant leader or boss. Inflated ego. Misuse of power. Almighty displays of anger. Heart problems or possible stroke.',  # noqa
            'Wands14.raw'
        ],
    '36 Ace Of Cups':
        [
            'Overwhelming romantic and spiritual love. New relationship, friendship. Compassion.',
            'Love seeping away. Setting emotional boundaries. Lost or unrequited love. Change in a relationship from romantic to routine. Possible drinking problem.',  # noqa
            'Cups01.raw'
        ],
    '37 Two Of Cups':
        [
            'Attraction, love, commitment.',
            'Difficulty making a romantic connection. Obstacles to love. Finding yourself in the friend-zone. Losing contact. Separation.',  # noqa
            'Cups02.raw'
        ],
    '38 Three Of Cups':
        [
            'Friendship, fun, community, girls’ night out, celebration.',
            'Over-indulgence. Bored with partying. Disenchanted with close friends. Lack of support or cooperation.',  # noqa
            'Cups03.raw'
        ],
    '39 Four Of Cups':
        [
            'Emotional stability, contemplation, meditation, inward focus.',
            'Ready to overcome depression. Looking for solutions. Preparing for a change. Restlessness. Mild insomnia. Tiredness, apathy. Psychic experiences.',  # noqa
            'Cups04.raw'
        ],
    '40 Five Of Cups':
        [
            'Loss, hurt, disappointment, bereavement, regret, pain. Emotional challenge.',
            'Healing rifts. Lessening of grief. Help from friends and loved ones. Acceptance.',  # noqa
            'Cups05.raw'
        ],
    '41 Six Of Cups':
        [
            'Memories of people and places. Childhood, children, grandchildren.',
            'Preoccupation with the past or future; failure to live in the present. Problems with a child or young person.',  # noqa
            'Cups06.raw'
        ],
    '42 Seven Of Cups':
        [
            'Fantasy, imagination, too many choices.',
            'Surmounting feelings of doubt and confusion. Making a proactive choice. Trusting your feelings.',  # noqa
            'Cups07.raw'
        ],
    '43 Eight Of Cups':
        [
            'Parting, leaving home. Emotional choice.',
            'Coming home. The prodigal returns. Embraced and accepted by family. Facing up to an emotional dilemma.',  # noqa
            'Cups08.raw'
        ],
    '44 Nine Of Cups':
        [
            'Emotional security. Comfort, satisfaction, happiness.',
            'Weakened energy of upright card. Contentment may be reduced, or satisfaction fleeting. Letting go of material concerns. Overcoming mistakes. Overindulgence of food and drink.',  # noqa
            'Cups09.raw'
        ],
    '45 Ten Of Cups':
        [
            'Family, harmony, fulfillment, peace, love.',
            'Relationship or family difficulties. Completion hard to reach. Break up or breakdown of a formerly happy home.',  # noqa
            'Cups10.raw'
        ],
    '46 Page Of Cups':
        [
            'Explorer of feelings, creative, messenger (or message arriving from overseas).',
            'Teen experiencing emotional distress. Possible gender confusion. Someone afraid of love, or emotional involvement. Young person not fitting in with family. An emotional and possibly upsetting message.',  # noqa
            'Cups11.raw'
        ],
    '47 Knight Of Cups':
        [
            'Romantic beau. Loves to love. Bisexual.',
            'Deceitful in love. Unfaithfulness. Obsession with another. LGBT issues or celebration. Coming out.',  # noqa
            'Cups12.raw'
        ],
    '48 Queen Of Cups':
        [
            'Intuitive, compassionate woman. Good friend.',
            'A delicate woman. Perhaps with health issues and/or emotional problems. Someone who needs physical and emotional support. Withdrawal of love from a partner.',  # noqa
            'Cups13.raw'
        ],
    '49 King Of Cups':
        [
            'Friendly, gentle man. Emotionally supportive.',
            'A man isolated emotionally. Possible alcoholic or drug addict. Depression and self pity causes relationship difficulties. Unable to express personal feelings.',  # noqa
            'Cups14.raw'
        ],
    '50 Ace Of Pentacles':
        [
            'Gift, manifestation, new house or project. Prosperity.',
            'Exaggerated energy of upright card. Treasure, wealth, fortune. Prosperity without happiness. Obsessed with making money. Corruption. Easy come, easy go.',  # noqa
            'Pentacles01.raw'
        ],
    '51 Two Of Pentacles':
        [
            'Making ends meet. Balancing time and resources.',
            'Paperwork/to-do list overload; too much to deal with. Data crashes. Learning difficulties. Student struggles with making ends meet, meeting deadlines, understanding the work.',  # noqa
            'Pentacles02.raw'
        ],
    '52 Three Of Pentacles':
        [
            'Collaboration, teamwork, pooling resources and ideas.',
            'Job or career related problems. Disputes with coworkers or boss. Mistakes, mediocrity, poor quality, shortcuts. Job shortages.',  # noqa
            'Pentacles03.raw'
        ],
    '53 Four Of Pentacles':
        [
            'Stability, security, isolation, holding on to resources.',
            'Resisting letting go of resources. Uneasiness outside of comfort zone. Blockages both mental and actual. Writer’s block. Hindrances and delays. Late payment.',  # noqa
            'Pentacles04.raw'
        ],
    '54 Five Of Pentacles':
        [
            'Material loss, destitution, poverty, financial or material challenge.',
            'A turning point. Slight improvement in situation. Access to help and support. Or things go from bad to worse. The unthinkable happens. Loss of everything.',  # noqa
            'Pentacles05.raw'
        ],
    '55 Six Of Pentacles':
        [
            'Generosity, giving and receiving support, charity, donation of resources.',
            'Taking advantage. Claiming under false pretenses. Greed, jealousy, disputes over money. Insurance refusing to pay. Lack of insurance. Unpaid debts or paying off a debt.',  # noqa
            'Pentacles06.raw'
        ],
    '56 Seven Of Pentacles':
        [
            'Slight dissatisfaction, underlying discontent, doing well but could do better. Wondering at missed opportunities.',  # noqa
            'Unemployment, lack of skills. Feeling let down by the system. Dissatisfaction with pay. Lack of ambition. Lazy and tardy.',  # noqa
            'Pentacles07.raw'
        ],
    '57 Eight Of Pentacles':
        [
            'Education, training/retraining, change of career, focus on the job in hand.',
            'Stuck in a dead-end job. Working on a factory line. Undervalued skills. Over-qual for the job. Boredom and tedium at work and life in general.',  # noqa
            'Pentacles08.raw'
        ],
    '58 Nine Of Pentacles':
        [
            'Independence, happy with own company. Self-sufficiency, appreciation.',
            'Goals attained but not as satisfying as expected. Trapped in a gilded cage. Looking for a way out. Needing a challenge. Lack of exercise. Lack of company.',  # noqa
            'Pentacles09.raw'
        ],
    '59 Ten Of Pentacles':
        [
            'Family structure, wealth, business, planning, inter-generational co-operation.',
            'Rejecting family. Disputes over inheritance or property. Family quarrels. Feeling like an outsider. Elderly relative needing care. Equity and savings devalued or lost. Gambling losses. Material insecurity.',  # noqa
            'Pentacles10.raw'
        ],
    '60 Page Of Pentacles':
        [
            'Student, curiosity, focus. Messenger, or message arriving by post.',
            'Lost interest in school or college. Underlying and hidden issues. Hating your choice of course. Preoccupied with material possessions and appearance. Stress and exhaustion caused by overwork.',  # noqa
            'Pentacles11.raw'
        ],
    '61 Knight Of Pentacles':
        [
            'Hard worker, loyal, reliable, quiet man with hidden depths.',
            'Workaholic or its opposite; work-shy and lazy. Obsession with one person or topic. Weight issues, lack of exercise, chronic fatigue. Bore. Socially inept.',  # noqa
            'Pentacles12.raw'
        ],
    '62 Queen Of Pentacles':
        [
            'Comforting, practical, efficient woman. Motherhood, career woman.',
            'Extremely house-proud, or extremely slovenly. Possessions mean more than people. Hoarder, or fixated on designer goods. Helicopter parenting. More concerned with children’s attainments than their well-being. Doubt, mistrust.',  # noqa
            'Pentacles13.raw'
        ],
    '63 King Of Pentacles':
        [
            'Businessman, magnanimous, proud, self-educated, self-made.',
            'Exploitive, mean, or ineffective employer. Misuse of power and money. Abuse of people for gain or personal gratification. Corruption. Overeating, indigestion, gout, rheumatism. Careless of the wellbeing of others. Unloved by family.',  # noqa
            'Pentacles14.raw'
        ],
    '64 Ace Of Swords':
        [
            'Clarity, decision made, insight, understanding, truth revealed.',
            'Restraint, patience. Writer’s block. Conception. Violation. Surgery.',  # noqa
            'Swords01.raw'
        ],
    '65 Two Of Swords':
        [
            'Indecision, not acknowledging the truth, afraid to face reality.',
            'Torn in two directions. Victim of lies, betrayal, duplicity. Ready to make a decision.',  # noqa
            'Swords02.raw'
        ],
    '66 Three Of Swords':
        [
            'Miscommunication, rejection, hurtful words, painful realization.',
            'Fast recovery after break-up or hiding the true extent of your pain.',  # noqa
            'Swords03.raw'
        ],
    '67 Four Of Swords':
        [
            'Withdrawal, resting the mind, time-out, meditation.',
            'Unwanted isolation. Insomnia. Lack of self-care. Strange dreams; out of body experience.',  # noqa
            'Swords04.raw'
        ],
    '68 Five Of Swords':
        [
            'Conflict, tension, mental challenge, bullying.',
            'Weakened or magnified energy of the upright card. Funeral. Mourning for situations or people.',  # noqa
            'Swords05.raw'
        ],
    '69 Six Of Swords':
        [
            'Transition, recovery, moving on, travel.',
            'Wanting to leave but unable. Travel delays or cancellations. Floods, storms, power outages.',  # noqa
            'Swords06.raw'
        ],
    '70 Seven Of Swords':
        [
            'Stealth, reclaiming something lost, mental trickery, betrayal, theft.',
            'Shame after trying to steal or deceive. Returning that which doesn’t belong to you. Community service. Giving back or paying forward.',  # noqa
            'Swords07.raw'
        ],
    '71 Eight Of Swords':
        [
            'Self-entrapment, perceived imprisonment, isolation.',
            'A new vision of the future. Able to see a way forward. Hard but rewarding work.',  # noqa
            'Swords08.raw'
        ],
    '72 Nine Of Swords':
        [
            'Anxiety, depression, nightmares, endless negative thought.',
            'Recovery from depression. Open to new ideas. Ready to explore possibilities.',  # noqa
            'Swords09.raw'
        ],
    '73 Ten Of Swords':
        [
            'Defeat, ending, death. End of life cycle/beginning of the next.',
            'Rebirth, recovery, relief. The end was not as bad as it seemed. New horizons.',  # noqa
            'Swords10.raw'
        ],
    '74 Page Of Swords':
        [
            'Mentally agile, restless, experimenting. Messenger (or message arriving fast).',
            'Slanderous, salacious gossip. Difficult childhood. Personality disorders.',  # noqa
            'Swords11.raw'
        ],
    '75 Knight Of Swords':
        [
            'Incisive, decisive, impulsive, political. Fights for the underdog.',
            'Fanatic. Fundamentalist. Delusional. Cruelty. Bad news arrives by text or email.',  # noqa
            'Swords12.raw'
        ],
    '76 Queen Of Swords':
        [
            'Perceptive, quick thinker, seeker of truth. Tells it like it is.',
            'Manipulative, self-centered woman. Narrow-mindedness, bigotry, intolerance.',  # noqa
            'Swords13.raw'
        ],
    '77 King Of Swords':
        [
            'Authoritative, intellectually powerful, truthful, direct.',
            'Dangerous, ill-intentioned man. Controlling and manipulative. Sadistic, perverse, inhumane.',  # noqa
            'Swords14.raw'
        ],
}

tarot_trivia = {
    'How many cards are there in a standard Rider-Waite tarot deck?':
        [
            'A. 22',
            'B. 56',
            'C. 78',
            'D. 84',
            2
        ],
    'What tarot suit is associated with thought intelligence?':
        [
            'A. Wands',
            'B. Swords',
            'C. Clubs',
            'D. Pentacles',
            2
        ],
    'What tarot suit is associated with emotion or love?':
        [
            'A. Wands',
            'B. Pentacles',
            'C. Spades',
            'D. Cups',
            3
        ],
    'Who is the artist behind the Waite tarot deck?':
        [
            'A. Frida Kahlo',
            'B. Berthe Moriso',
            'C. Mary Cassatt',
            'D. Pamela Coleman Smith',
            3
        ],
    'What tarot suit is associated with the element, Earth?':
        [
            'A. Swords',
            'B. Pentacles',
            'C. cups',
            'D. wands',
            1
        ],
    'Which is the older tarot deck?':
        [
            'A. Thoth',
            'B. Marseilles',
            'C. Rider-Waite-Smith',
            'D. Petit Etteilla',
            1
        ],
    'Like common playing cards, what is the term of using only the suit symbol for identifying rank?':
        [
            'A. PIP',
            'B. POP',
            'C. Rank',
            'D. ANK',
            0
        ],
    'Which tarot suit of the Tarot Marselle does not typically number they cards?':
        [
            'A. Swords',
            'B. Coins',
            'C. Cups',
            'D. Wands',
            1
        ],
    'The major arcana is commonly referred to as the?':
        [
            'A. The Fools Journey',
            'B. Fortune Telling',
            'C. Cosmic Egg',
            'D. English Method',
            0
        ],
    'Fortune telling with common playing cards is sometimes known as?':
        [
            'A. The Fools Journey',
            'B. Fortune Telling',
            'C. English Method',
            'D. Divination',
            2
        ],
    'How many points, Sephiroths, are on the Tree of Life?':
        [
            'A. 22',
            'B. 78',
            'C. 12',
            'D. 10',
            3
        ],
    'The major arcana tarot cards represent the what forces rather than individual people?':
        [
            'A. Archetype',
            'B. Cosmic',
            'C. Trumps',
            'D. Eminations',
            0
        ],
    'Sephiroth 1 of the Tree of Life represents Upper Crown?':
        [
            'A. Binah',
            'B. Hod',
            'C. Kether',
            'D. Tiphereth',
            2
        ],
    'Sephiroth 4 of the Tree of Life represents Love?':
        [
            'A. Binah',
            'B. Hescd',
            'C. Hod',
            'D. Tiphereth',
            1
        ],
    'Sephiroth 6 of the Tree of Life represents Tiphereth?':
        [
            'A. Love',
            'B. Glory',
            'C. Beauty',
            'D. Intelligence',
            2
        ],
    'On the Tree of Life, which major arcana tarot card represents the path (11) from Kethor to Chormah?':
        [
            'A. The Magician',
            'B. Strength',
            'C. The Emperor',
            'D. The Fool',
            3
        ],
    'On the Tree of Life, which major arcana tarot card represents the path (16) from Chormah to Chesed?':
        [
            'A. The Hierophant',
            'B. The Magician',
            'C. The Fool',
            'D. The Emperor',
            0
        ],
    'On the Tree of Life, which major arcana tarot card represents the path (20) from Chesed to Tifereth?':
        [
            'A. The Fool',
            'B. The Magician',
            'C. The Hermit',
            'D. The Hierophant',
            2
        ],
}

flash_cards = {
    '00-TheFool.raw':
        [
            'A. The Emperor',
            'B. The Fool',
            'C. The Priestess',
            'D. The High Priestess',
            1
        ],
    '01-TheMagician.raw':
        [
            'A. The Hierophant',
            'B. The Fool',
            'C. The Magician',
            'D. The High Priestess',
            2
        ],
    '02-TheHighPriestess.raw':
        [
            'A. The Hierophant',
            'B. The Lovers',
            'C. The Magician',
            'D. The High Priestess',
            3
        ],
    '03-TheEmpress.raw':
        [
            'A. The Emperor',
            'B. The Empress',
            'C. The Lovers',
            'D. The High Priestess',
            1
        ],
    '04-TheEmperor.raw':
        [
            'A. The Emperor',
            'B. The Empress',
            'C. The Lovers',
            'D. The High Priestess',
            0
        ],
    '05-TheHierophant.raw':
        [
            'A. The Lovers',
            'B. The Empress',
            'C. The High Priest',
            'D. The Hierophant',
            3
        ],
    '06-TheLovers.raw':
        [
            'A. The Hermit',
            'B. The Empress',
            'C. The Lovers',
            'D. The Hierophant',
            2
        ],
    '07-TheChariot.raw':
        [
            'A. Strength',
            'B. The Hermit',
            'C. The Chariot',
            'D. Justice',
            2
        ],
    '08-Strength.raw':
        [
            'A. Wheel of Fortune',
            'B. Death',
            'C. Justice',
            'D. Strength',
            3
        ],
    '09-TheHermit.raw':
        [
            'A. Death',
            'B. The Hermit',
            'C. The High Priest',
            'D. The Hierophant',
            1
        ],
    '10-WheelOfFortune.raw':
        [
            'A. The Hanged Man',
            'B. The Hermit',
            'C. Wheel of Fortune',
            'D. Temperance',
            2
        ],
    '11-Justice.raw':
        [
            'A. The Devil',
            'B. Justice',
            'C. Death',
            'D. The Star',
            1
        ],
    '12-TheHangedMan.raw':
        [
            'A. Death',
            'B. The Hermit',
            'C. The Devil',
            'D. The Hanged Man',
            3
        ],
    '13-Death.raw':
        [
            'A. Death',
            'B. The Hermit',
            'C. The Devil',
            'D. The Hanged Man',
            0
        ],
    '14-Temperance.raw':
        [
            'A. The Tower',
            'B. The Hermit',
            'C. Temperance',
            'D. The Star',
            2
        ],
    '15-TheDevil.raw':
        [
            'A. The Hanged Man',
            'B. Death',
            'C. The Devil',
            'D. Strength',
            2
        ],
    '16-TheTower.raw':
        [
            'A. The Hanged Man',
            'B. Death',
            'C. The Devil',
            'D. Strength',
            2
        ],
    '17-TheStar.raw':
        [
            'A. The Hanged Man',
            'B. Death',
            'C. The Devil',
            'D. Strength',
            2
        ],
    '18-TheMoon.raw':
        [
            'A. The Hanged Man',
            'B. Death',
            'C. The Devil',
            'D. Strength',
            2
        ],
    '19-TheSun.raw':
        [
            'A. The Hanged Man',
            'B. Death',
            'C. The Devil',
            'D. Strength',
            2
        ],
    'Swords14.raw':
        [
            'A. King of Swords',
            'B. Queen of Swords',
            'C. Page of Swords',
            'D. Ten of Swords',
            3
        ],
}

# user will be shown 'A' and will input '... - ..' and if correct get a successful answer - no game
morse_code_practice_easy = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'H': 'H',
    'I': 'I',
    'J': 'J',
    'K': 'K',
    'L': 'L',
    'M': 'M',
    'N': 'N',
    'O': 'O',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

# user will be shown 'A' and will input '... - ..' and if correct get a successful answer - no game
morse_code_practice_medium = {
    'sos': 'SOS', # betsy you can do 'SOS' or '--- ... ---'
    'hello': 'HELLO',
    'DEFCON30': 'DEFCON30'
}

# user will be shown 'A' and will input '... - ..' and if correct get a successful answer - no game
morse_code_practice_advanced = {
    'MAJOR ARCANE': 'MAJOR ARCANE', # betsy change this
    'WHEEL OF FORTUNE': 'WHEEL OF FORTUNE',
    'THE HANGED MAN': 'THE HANGED MAN',
}


morse_code_game = {
    'Decode This Answer': 'FOO',
}

# there will be instructions - decipher all three ciphers and put them in order
# press A BUTTON to submit answer
ciphers101_game = {
    'Cipher 1': 'Hsle td esp yfxmpc ehpyej-escpp',
    'Cipher 2': 'dGhlIGFuc3dlciB0byBsaWZlIHRoZSB1bml2ZXJzZSBhbmQgZXZlcnl0aGluZw==',
    'Cipher 3': 'this will be a vignere cipher',
}





stego_game2_answer = {
    'Please enter the answer for Game 1': '343421',
}
reenactment_game3_answer = {
    'Please enter the answer for Game 2': '441211'
}
SavengerHunt_game4_answer = {
    'Please enter the answer for Game 3': '141431'
}
ShittyDeck_game7_answer = {
    'Please enter the answer for Game 4': '333212',
}
morsecode_game8_answer = {
    'Please enter the answer for Game 5 ': '442132',
}
ciphers101_game10_answer = {
    'Please enter the answer for Game 9': '234222',
}