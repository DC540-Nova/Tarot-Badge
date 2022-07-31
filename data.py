# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
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

badge_instructions_1 = 'There are more details can be found on the webpage dc540.org. Some games require you to submit to the DC540 discord channel.'  # noqa
badge_instructions_2 = 'For those you will be sent a code to input. Other games are automatic.'  # noqa
badge_instructions_3 = 'Stuff' # noqa
tarot_trivia_game_instructions = 'Answer 15 of the 20 trivia questions correctly to pass this game.'
stego_game_instructions = 'Go to the DC540 website and find the game labeled stego.'
reenactment_game_instructions = 'Re-enact a Tarot Card picture using yourself. Take a picture and submit on the DC540 Tartot badge channel'  # noqa
scavenger_hunt_game_instructions = 'Find ten items that can be found on the tarot deck. Submit a picture of all ten items to the DC540 Tarot badge channel'  # noqa
flash_cards_game_instructions = 'Answer 15 of the 20 flashcards correctly to pass this game.'
fun_deck_game_instructions = 'We at DC540 created our own terrible Tarot deck. Create your own original deck and post to our DC540 discord #Tarot channel.'  # noqa
morse_code_game_instructions = 'complete all three morse code challenges to pass this game'
decryption_game_instructions = 'decode these three encryptions and add them together for the answer'
help_someone_game_instructions = 'find another player wearing this badge and offer to help them'
boss_pairing_instructions = 'Find a DC540 Boss badge and we will give you the code you need to pass this challenge'

boss_ids = []  # noqa
boss_ids.append('e66038b7137a9935')
boss_ids.append('e66038b7135fa935')
boss_ids.append('e66038b71316902f')
boss_ids.append('e66038b71340a735')
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
            'Emerging from depression. Extreme shyness or over-confidence, denying intuition, predatory sexual behavior, disclosure of secrets.',  # noqa
            '02-TheHighPriestess.raw'
        ],
    '3 The Empress':
        [
            'Growth, fertility, pregnancy, motherhood. New project. Dominant female.',
            'Famine, drought. smother love. Vanity, feeling useless, infidelity, unloving, unsupportive. Fertility issues. Failing business.',  # noqa
            '03-TheEmpress.raw'
        ],
    '4 The Emperor':
        [
            'Structure, organization, rules. Dominant male.',
            'Nature controlled. Urban sprawl and degeneration. Tyrant, dictator, domination, rigid, unyielding, loss of control, misuse of power.',  # noqa
            '04-TheEmperor.raw'
        ],
    '5 The Hierophant':
        [
            'Learning path, religion, spirituality, spiritual mentor, guide.',
            'Rejection of the establishment. A mentor with ulterior motives. Expulsion. Sexual misdemeanors. Inappropriate behavior. Rejecting faith.',  # noqa
            '05-TheHierophant.raw'
        ],
    '6 The Lovers':
        [
            'Life-changing choice, turning point. Union with another, two as one.',
            'Inappropriate relationship. Immaturity, lack of love, possessiveness, lust rather than love. Bad choice, indecision, temptation, weakness, lack of trust.',   # noqa
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
            'Mental problems. Too overbearing or too weak. Not knowing when to stop. Government vs citizens. Cruelty. Disregarding the well-being of others.',  # noqa
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
            'Attempting to avoid an inevitable end. Chronic illness. Extreme depression or pessimism. Obsession with death. Accident (narrowly escaping death).',  # noqa
            '13-Death.raw'
        ],
    '14 Temperance':
        [
            'Chemistry, moderation, balance. Getting it right.',
            'Out of balance, conflicting ideas & positions. Emotional extremes. Procrastination. Digestive problems. Mind & body health out of whack.',  # noqa
            '14-Temperance.raw'
        ],
    '15 The Devil':
        [
            'Addiction, bad habits, co-dependency, materialism.',
            'Extremes, life threatening addiction, psychopathic personality disorder. Abuse. Escape, release, moving forward, taking control of your problems and your life.',  # noqa
            '15-TheDevil.raw'
        ],
    '16 The Tower':
        [
            'Chaos, destruction, upheaval. Unexpected and possibly unwanted change.',
            'Weakened energy of upright card. Irritations, things going wrong, setbacks, pressure, stress. Accidents, cuts, burns, surgery. Need to visit the doctor.',  # noqa
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
            'Resistance to anything spiritual. Delusion. Closed mind. Mental health issues, and things like fibromyalgia and urinary tract problems.',  # noqa
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
            'Slightly weakened energy of upright card so generally positive. Wanting to move forward but held back. Overdue birth. Issues with weight loss.',  # noqa
            '21-TheWorld.raw'
        ],
    '22 Ace Of Wands':
        [
            'Rush of energy, inspiration, passion, creativity.',
            'Weakened energy of upright meaning. Inappropriate attraction or affair. Lack of growth and expansion.',  # noqa
            'Wands01.raw'
        ],
    '23 Two Of Wands':
        [
            'Planning, decisions, delays.',
            'Unexpected turn of events. A new perspective on an old problem. Reluctance.',  # noqa
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
            'Unforeseen, difficult event. Shock. Family or business problems.',  # noqa
            'Wands08.raw'
        ],
    '30 Nine Of Wands':
        [
            'Courage, determination, resilience.',
            'Overwhelmed. Ready to give up. Illness, nagging pain. Cannot see the the wood for the trees.',  # noqa
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
            'Difficulty making a romantic connection. Obstacles to love. Finding yourself in the friend zone. Losing contact. Separation.',  # noqa
            'Cups02.raw'
        ],
    '38 Three Of Cups':
        [
            'Friendship, fun, community, girls night out, celebration.',
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
            'Weakened energy of upright card. Letting go of material concerns. Overcoming mistakes. Overindulgence of food and drink.',  # noqa
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
            'Teen experiencing emotional distress. Possible gender confusion. Someone afraid of love, or emotional involvement.',  # noqa
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
            'A delicate woman. Perhaps with health issues or emotional problems. Someone who needs physical and emotional support. Withdrawal of love from a partner.',  # noqa
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
            'Paperwork. Too much to deal with. Data crashes. Learning difficulties. Student struggles with making ends meet, meeting deadlines, understanding the work.',  # noqa
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
            'Resisting letting go of resources. Uneasiness outside of comfort zone. Blockages both mental and actual. Writers block. Hindrances and delays. Late payment.',  # noqa
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
            'Stuck in a dead-end job. Working on a factory line. Undervalued skills. Overqualified for the job. Boredom and tedium at work and life in general.',  # noqa
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
            'Rejecting family. Disputes over inheritance or property. Family quarrels. Feeling like an outsider. Elderly relative needing care. Gambling losses. Material insecurity.',  # noqa
            'Pentacles10.raw'
        ],
    '60 Page Of Pentacles':
        [
            'Student, curiosity, focus. Messenger, or message arriving by post.',
            'Lost interest in school or college. Underlying and hidden issues. Preoccupied with material possessions and appearance. Stress and exhaustion caused by overwork.',  # noqa
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
            'Extremely house proud, or extremely slovenly. Possessions mean more than people. Hoarder, or fixated on designer goods. Helicopter parenting. Doubt, mistrust.',  # noqa
            'Pentacles13.raw'
        ],
    '63 King Of Pentacles':
        [
            'Businessman, magnanimous, proud, self-educated, self-made.',
            'Misuse of power and money. Abuse of people for gain or personal gratification. Corruption. Overeating, indigestion. Careless of the wellbeing of others. Unloved by family.',  # noqa
            'Pentacles14.raw'
        ],
    '64 Ace Of Swords':
        [
            'Clarity, decision made, insight, understanding, truth revealed.',
            'Restraint, patience. Writers block. Conception. Violation. Surgery.',  # noqa
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
            'Shame after trying to steal or deceive. Returning that which does not belong to you. Community service. Giving back or paying forward.',  # noqa
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

tarot_trivia_game = {
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
    'On the Tree of Life, which major arcana tarot card represents the path (16) from Chormah to Chesed?':
        [
            'A. The Hierophant',
            'B. The Magician',
            'C. The Fool',
            'D. The Emperor',
            0
        ],
    'What tarot suite is associated with the element, Water?':
        [
            'A. Swords',
            'B. Pentacles',
            'C. Cups',
            'D. Wands',
            2
        ],
    'What tarot suite is associated with the element, Fire?':
        [
            'A. Swords',
            'B. Pentacles',
            'C. Cups',
            'D. Wands',
            3
        ],
    'What tarot suite is associated with the element, Air?':
        [
            'A. Swords',
            'B. Pentacles',
            'C. Cups',
            'D. Wands',
            0
        ],
    'How many cards are there in the major arcana Rider-Waite tarot deck?':
        [
            'A. 22',
            'B. 56',
            'C. 78',
            'D. 84',
            0
        ],
    'How many cards are there in the minor arcana Rider-Waite tarot deck?':
        [
            'A. 22',
            'B. 56',
            'C. 78',
            'D. 84',
            1
        ],
    'How many cards are in each of the four suites of minor arcana?':
        [
            'A. 84',
            'B. 14',
            'C. 56',
            'D. 22',
            1
        ],
    'Which card typically replaces the female Pope from earlier Tarot decks?':
        [
            'A. Hierophant',
            'B. Strength',
            'C. Temperance',
            'D. High Priestess',
            3
        ],
    'What is the first card of the major arcana?':
        [
            'A. The Magician',
            'B. The Fool',
            'C. The Empress',
            'D. Death',
            1
        ],
    'What is the last card of the major arcana?':
        [
            'A. World',
            'B. King',
            'C. Tower',
            'D. justice',
            0
        ],
    'Which of the following cards is not considered a court card?':
        [
            'A. King',
            'B. Ace',
            'C. Page',
            'D. Knight',
            1
        ],
    'The planet associated with the Fool in the major arcana?':
        [
            'A. Moon',
            'B. Mars',
            'C. Uranus',
            'D. Venus',
            2
        ],
    'The planet associated with the Magician in the major arcana?':
        [
            'A. Mercury',
            'B. Mars',
            'C. Uranus',
            'D. Moon',
            0
        ],
}

flash_cards_game = {
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
    '20-Judgement.raw':
        [
            'A. Divination',
            'B. Death',
            'C. Wisdom',
            'D. Judgment',
            3
        ],
    '21-TheWorld.raw':
        [
            'A. The World',
            'B. The Moon',
            'C. The Universe',
            'D. The Sun',
            0
        ],
    'Wands01.raw':
        [
            'A. Two of Wands',
            'B. Page of Wands',
            'C. Ace of Wands',
            'D. Knight of Wands',
            2
        ],
    'Wands03.raw':
        [
            'A. Two of Wands',
            'B. Page of Wands',
            'C. Queen of Wands',
            'D. Three of Wands',
            3
        ],
    'Wands04.raw':
        [
            'A. Two of Wands',
            'B. Four of Wands',
            'C. Three of Wands',
            'D. Ace of Wands',
            1
        ],
    'Wands06.raw':
        [
            'A. Six of Wands',
            'B. Five of Wands',
            'C. Seven of Wands',
            'D. Four of Wands',
            0
        ],
    'Wands08.raw':
        [
            'A. Ace of Wands',
            'B. Page of Wands',
            'C. Seven of Wands',
            'D. Eight of Wands',
            3
        ],
    'Wands10.raw':
        [
            'A. Jack of Wands',
            'B. Page of Wands',
            'C. Ten of Wands',
            'D. Knight of Wands',
            2
        ],
    'Wands11.raw':
        [
            'A. King of Wands',
            'B. Page of Wands',
            'C. Queen of Wands',
            'D. Knight of Wands',
            1
        ],
    'Wands12.raw':
        [
            'A. Knight of Wands',
            'B. Page of Wands',
            'C. King of Wands',
            'D. Queen of Wands',
            0
        ],
    'Wands13.raw':
        [
            'A. Queen of Wands',
            'B. Page of Wands',
            'C. King of Wands',
            'D. Ace of Wands',
            0
        ],
    'Wands14.raw':
        [
            'A. Ace of Wands',
            'B. King of Wands',
            'C. Page of Wands',
            'D. Knight of Wands',
            1
        ],
    'Cups01.raw':
        [
            'A. Ace of Cups',
            'B. Page of Cups',
            'C. Queen of Goblets',
            'D. Ace of Goblets',
            0
        ],
    'Cups02.raw':
        [
            'A. Ace of Cups',
            'B. Two of Cups',
            'C. Page of Goblets',
            'D. Ace of Goblets',
            1
        ],
    'Cups06.raw':
        [
            'A. Six of Cups',
            'B. Eight of Cups',
            'C. Queen of Cups',
            'D. Ace of Cups',
            0
        ],
    'Cups07.raw':
        [
            'A. Seven of Goblets',
            'B. Six of Goblets',
            'C. Six of Cups',
            'D. Seven of Cups',
            3
        ],
    'Cups09.raw':
        [
            'A. Nine of Goblets',
            'B. Nine of Chalices',
            'C. Nine of Cups',
            'D. Nine of Mugs',
            2
        ],
    'Cups10.raw':
        [
            'A. Ten of Goblets',
            'B. Ten of Chalices',
            'C. Page of Cups',
            'D. Ten of Cups',
            3
        ],
    'Cups11.raw':
        [
            'A. Seven of Pages',
            'B. Seven of Goblets',
            'C. Page of Cups',
            'D. Queen of Cups',
            2
        ],
    'Cups12.raw':
        [
            'A. Knight of Cups',
            'B. Night of Goblets',
            'C. Night of Cups',
            'D. Knight of Goblets',
            0
        ],
    'Cups13.raw':
        [
            'A. Knight of Chalices',
            'B. Queen of Cups',
            'C. King of Goblets',
            'D. Ace of Chalices',
            1
        ],
    'Cups14.raw':
        [
            'A. King of Cups',
            'B. Queen of Goblets',
            'C. Jack of Goblets',
            'D. Page of Cups',
            0
        ],
    'Pentacles01.raw':
        [
            'A. Ace of Cups',
            'B. Ace of Goblets',
            'C. Ace of Pentacles',
            'D. Ace of Swords',
            2
        ],
    'Pentacles02.raw':
        [
            'A. Two of Cups',
            'B. Two of Pentacles',
            'C. Two of Wands',
            'D. Two of Towers',
            1
        ],
    'Pentacles04.raw':
        [
            'A. Four of Pentacles',
            'B. Four of Stars',
            'C. Four of Temperance',
            'D. Four of Kings',
            0
        ],
    'Pentacles05.raw':
        [
            'A. Ace of Cups',
            'B. Five of Swords',
            'C. Ace of Pentacles',
            'D. Five of Pentacles',
            3
        ],
    'Pentacles07.raw':
        [
            'A. Ace of Pentacles',
            'B. King of Pentacles',
            'C. Knight of Pentacles',
            'D. Seven of Pentacles',
            3
        ],
    'Pentacles10.raw':
        [
            'A. Ace of Pentacles',
            'B. King of Pentacles',
            'C. Knight of Pentacles',
            'D. Page of Pentacles',
            3
        ],
    'Pentacles11.raw':
        [
            'A. Queen of Pentacles',
            'B. Page of Pentacles',
            'C. Knight of Pentacles',
            'D. Ace of Pentacles',
            1
        ],
    'Pentacles12.raw':
        [
            'A. Ace of Pentacles',
            'B. King of Pentacles',
            'C. Knight of Pentacles',
            'D. Seven of Pentacles',
            2
        ],
    'Pentacles13.raw':
        [
            'A. Queen of Pentacles',
            'B. King of Pentacles',
            'C. Knight of Pentacles',
            'D. Seven of Pentacles',
            0
        ],
    'Pentacles14.raw':
        [
            'A. Ace of Pentacles',
            'B. King of Pentacles',
            'C. Knight of Pentacles',
            'D. Queen of Pentacles',
            1
        ],
    'Swords01.raw':
        [
            'A. Ace of Swords',
            'B. King of Swords',
            'C. Knight of Swords',
            'D. Seven of Swords',
            0
        ],
    'Swords03.raw':
        [
            'A. Three of Swords',
            'B. Seven of Swords',
            'C. Four of Swords',
            'D. Eight of Swords',
            0
        ],
    'Swords05.raw':
        [
            'A. Twelve of Swords',
            'B. Four of Swords',
            'C. Six of Swords',
            'D. Five of Swords',
            3
        ],
    'Swords08.raw':
        [
            'A. Three of Swords',
            'B. Eight of Swords',
            'C. Ace of Swords',
            'D. Two of Swords',
            1
        ],
    'Swords09.raw':
        [
            'A. Nine of Swords',
            'B. Eight of Swords',
            'C. Page of Swords',
            'D. Two of Swords',
            0
        ],
    'Swords10.raw':
        [
            'A. King of Swords',
            'B. Queen of Swords',
            'C. Ten of Swords',
            'D. Page of Swords',
            2
        ],
    'Swords11.raw':
        [
            'A. Paige of Swords',
            'B. Queen of Swords',
            'C. Night of Swords',
            'D. Page of Swords',
            3
        ],
    'Swords12.raw':
        [
            'A. Queen of Swords',
            'B. Night of Swords',
            'C. Knight of Swords',
            'D. Page of Swords',
            2
        ],
    'Swords13.raw':
        [
            'A. Knight of Swords',
            'B. King of Swords',
            'C. Ace of Swords',
            'D. Queen of Swords',
            3
        ],
    'Swords14.raw':
        [
            'A. King of Swords',
            'B. Queen of Swords',
            'C. Page of Swords',
            'D. Ten of Swords',
            0
        ],
}

morse_code_game_practice_easy = {
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

morse_code_game_practice_medium = {
    'SOS': 'SOS',
    'HELLO': 'HELLO',
    'DEFCON30': 'DEFCON30',
    'ACE': 'ACE',
    'PAGE': 'PAGE',
    'KNIGHTS': 'KNIGHTS',
    'QUEEN': 'QUEEN',
    'KING': 'KING',
    'PENTACLES': 'PENTACLES',
    'SWORDS': 'SWORDS',
    'CUPS': 'CUPS',
    'WANDS': 'WANDS',
}

morse_code_game = {
    'MAJOR ARCANE': 'MAJOR ARCANE',
    'WHEEL OF FORTUNE': 'WHEEL OF FORTUNE',
    'THE HANGED MAN': 'THE HANGED MAN',
}

decryption_game_questions = {
    'Cipher 1': 'Cipher 1: Iwt rdchitaapixdc Pcsgdbtsp xh adrpits xc Vgddbqgxsvt ?',
    'Cipher 2': 'Cipher 2: dGhlIGFuc3dlciB0byB saWZlIHRoZSB1bml2ZX JzZSBhbmQgZXZl cnl0aGluZw==',
    'Cipher 3': 'Cipher 3: Mhv bnfbvf rhu rfx eofybgg wck bs kvx ttfabv nlauxr ft mbtrbbnm.',
}

decryption_game = {
    'Enter Game 9 Answer': b'\xc3\xc4\x1a\xa4\xb8`\x8bp\xa6[\xd2\x1bu\xcd\xf9\x17',
}

stego_game = {
    'Enter Game 1 Answer': b'\x9ax\xde\x90\xb3\xaa?\xe2\x81u1=\r\xa6xd',
}

reenactment_game = {
    'Enter Game 2 Answer': b'\x8fl\x07\xe1\xa5;=\xb9\'7\xabG\x86"b\xa4',
}

scavenger_hunt_game = {
    'Enter Game 3 Answer': b'\x0b\xf2\xc5\xec\x96s\xad\xa0\x8c%\xb0\xdc\xdf\xddS\xc7',
}

fun_deck_game = {
    'Enter Game 4 Answer': b'\x0b)\xa85\xcb\xf6\x89Wb\x1e2\xfd5.C\xa5',
}
