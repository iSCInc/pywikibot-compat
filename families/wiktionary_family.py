# -*- coding: utf-8  -*-
import family

__version__ = '$Id$'


# The Wikimedia family that is known as Wiktionary
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wiktionary'

        self.languages_by_size = [
            'en', 'mg', 'fr', 'zh', 'lt', 'ru', 'es', 'el', 'pl', 'sv', 'ko',
            'nl', 'de', 'tr', 'ku', 'ta', 'io', 'kn', 'fi', 'vi', 'hu', 'pt',
            'chr', 'no', 'ml', 'my', 'id', 'it', 'li', 'ro', 'et', 'ja', 'te',
            'jv', 'fa', 'cs', 'ca', 'ar', 'eu', 'gl', 'lo', 'uk', 'br', 'fj',
            'eo', 'bg', 'hr', 'th', 'oc', 'is', 'vo', 'ps', 'zh-min-nan',
            'simple', 'cy', 'uz', 'scn', 'sr', 'af', 'ast', 'az', 'da', 'sw',
            'fy', 'tl', 'he', 'nn', 'wa', 'ur', 'la', 'sq', 'hy', 'sm', 'sl',
            'ka', 'pnb', 'nah', 'hi', 'tt', 'bs', 'lb', 'lv', 'tk', 'sk', 'hsb',
            'nds', 'kk', 'ky', 'be', 'km', 'mk', 'ga', 'wo', 'ms', 'ang', 'co',
            'sa', 'gn', 'mr', 'csb', 'ug', 'st', 'ia', 'sd', 'sh', 'si', 'mn',
            'tg', 'or', 'kl', 'vec', 'jbo', 'an', 'ln', 'fo', 'zu', 'gu', 'kw',
            'gv', 'rw', 'qu', 'ss', 'ie', 'mt', 'om', 'bn', 'pa', 'roa-rup',
            'iu', 'so', 'am', 'su', 'za', 'gd', 'mi', 'tpi', 'ne', 'yi', 'ti',
            'sg', 'na', 'dv', 'tn', 'ts', 'ha', 'ks', 'ay',
        ]

        self.langs = dict([(lang, '%s.wiktionary.org' % lang)
                           for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[14]['bn'] = [u'বিষয়শ্রেণী']
        self.namespaces[15]['bn'] = [u'বিষয়শ্রেণী আলোচনা']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Diskuse s uživatelkou', u'Uživatel diskuse', u'Uživatelka diskuse']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'BD', u'Benutzerin Diskussion']
        self.namespaces[2]['fa'] = [u'کاربر']
        self.namespaces[3]['fa'] = [u'بحث کاربر']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur', u'Discussion utilisatrice']
        self.namespaces[8]['hi'] = [u'मीडियाविकि']
        self.namespaces[9]['hi'] = [u'मीडियाविकि वार्ता']
        self.namespaces[10]['hi'] = [u'साँचा']
        self.namespaces[11]['hi'] = [u'साँचा वार्ता']
        self.namespaces[829]['ja'] = [u'モジュール・トーク']
        self.namespaces[2]['ko'] = [u'사용자']
        self.namespaces[3]['ko'] = [u'사용자토론']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[6]['vec'] = [u'File', u'Imagine']
        self.namespaces[2]['zh'] = [u'User', u'用戶', u'用户']
        self.namespaces[3]['zh'] = [u'User talk', u'用戶對話', u'用戶討論', u'用户对话', u'用户讨论']
        self.namespaces[10]['zh'] = [u'Template', u'样板', u'模板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'帮助', u'幫助']
        self.namespaces[13]['zh'] = [u'Help talk', u'帮助对话', u'帮助讨论', u'幫助對話', u'幫助討論']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'af': u'Wiktionary',
            'am': u'Wiktionary',
            'an': u'Wiktionary',
            'ang': [u'Wikiwordbōc', u'Wikiwordboc', u'Wiktionary'],
            'ar': [u'ويكاموس', u'Wiktionary'],
            'ast': [u'Uiccionariu', u'Wiktionary'],
            'ay': u'Wiktionary',
            'az': u'Wiktionary',
            'be': u'Wiktionary',
            'bg': [u'Уикиречник', u'Wiktionary'],
            'bn': [u'উইকিঅভিধান', u'Wiktionary'],
            'br': [u'Wikeriadur', u'Wiktionary'],
            'bs': [u'Vikirječnik', u'Wiktionary'],
            'ca': [u'Viccionari', u'Wiktionary'],
            'chr': u'Wiktionary',
            'co': u'Wiktionary',
            'cs': [u'Wikislovník', u'WS', u'WT', u'Wiktionary'],
            'csb': u'Wiktionary',
            'cy': [u'Wiciadur', u'Wiktionary'],
            'da': u'Wiktionary',
            'de': [u'Wiktionary', u'WT'],
            'dv': [u'ވިކިރަދީފު', u'Wiktionary'],
            'el': [u'Βικιλεξικό', u'Wiktionary'],
            'en': [u'Wiktionary', u'WT'],
            'eo': [u'Vikivortaro', u'Wiktionary'],
            'es': [u'Wikcionario', u'Wiktionary'],
            'et': [u'Vikisõnastik', u'Wiktionary'],
            'eu': u'Wiktionary',
            'fa': [u'ویکی‌واژه', u'Wiktionary', u'وو'],
            'fi': [u'Wikisanakirja', u'Wiktionary'],
            'fj': u'Wiktionary',
            'fo': u'Wiktionary',
            'fr': [u'Wiktionnaire', u'WT', u'Wiktionary'],
            'fy': u'Wiktionary',
            'ga': [u'Vicífhoclóir', u'Wiktionary'],
            'gd': u'Wiktionary',
            'gl': u'Wiktionary',
            'gn': u'Wiktionary',
            'gu': [u'વિક્શનરી', u'Wiktionary'],
            'gv': u'Wiktionary',
            'ha': u'Wiktionary',
            'he': [u'ויקימילון', u'Wiktionary'],
            'hi': [u'विक्षनरी', u'Wiktionary'],
            'hr': [u'Wječnik', u'Wiktionary'],
            'hsb': [u'Wikisłownik', u'Wiktionary'],
            'hu': [u'Wikiszótár', u'Wiktionary'],
            'hy': [u'Վիքիբառարան', u'Wiktionary'],
            'ia': [u'Wiktionario', u'Wiktionary'],
            'id': u'Wiktionary',
            'ie': u'Wiktionary',
            'io': [u'Wikivortaro', u'Wiktionary'],
            'is': [u'Wikiorðabók', u'Wiktionary'],
            'it': [u'Wikizionario', u'WZ', u'Wiktionary'],
            'iu': u'Wiktionary',
            'ja': u'Wiktionary',
            'jbo': u'Wiktionary',
            'jv': u'Wiktionary',
            'ka': [u'ვიქსიკონი', u'Wiktionary'],
            'kk': [u'Уикисөздік', u'Wiktionary'],
            'kl': u'Wiktionary',
            'km': u'Wiktionary',
            'kn': u'Wiktionary',
            'ko': [u'위키낱말사전', u'Wiktionary', u'낱'],
            'ks': u'Wiktionary',
            'ku': [u'Wîkîferheng', u'Wiktionary'],
            'kw': u'Wiktionary',
            'ky': u'Wiktionary',
            'la': [u'Victionarium', u'Wiktionary'],
            'lb': [u'Wiktionnaire', u'Wiktionary'],
            'li': u'Wiktionary',
            'ln': u'Wiktionary',
            'lo': u'Wiktionary',
            'lt': [u'Vikižodynas', u'Wiktionary'],
            'lv': u'Wiktionary',
            'mg': u'Wiktionary',
            'mi': u'Wiktionary',
            'mk': u'Wiktionary',
            'ml': [u'വിക്കിനിഘണ്ടു', u'Wiktionary', u'വിക്കി‌‌ നിഘണ്ടു'],
            'mn': u'Wiktionary',
            'mr': [u'विक्शनरी', u'Wiktionary'],
            'ms': u'Wiktionary',
            'mt': [u'Wikizzjunarju', u'Wiktionary'],
            'my': u'Wiktionary',
            'na': u'Wiktionary',
            'nah': [u'Wiktionary', u'Wikipedia'],
            'nds': u'Wiktionary',
            'ne': u'Wiktionary',
            'nl': [u'WikiWoordenboek', u'Wiktionary'],
            'nn': u'Wiktionary',
            'no': u'Wiktionary',
            'oc': [u'Wikiccionari', u'Wiktionary'],
            'om': u'Wiktionary',
            'or': u'Wiktionary',
            'pa': u'Wiktionary',
            'pl': [u'Wikisłownik', u'WS', u'Wiktionary'],
            'pnb': [u'وکشنری', u'Wiktionary'],
            'ps': [u'ويکيسيند', u'Wiktionary'],
            'pt': [u'Wikcionário', u'Wiktionary'],
            'qu': u'Wiktionary',
            'ro': [u'Wikționar', u'Wiktionary'],
            'roa-rup': u'Wiktionary',
            'ru': [u'Викисловарь', u'Wiktionary'],
            'rw': u'Wiktionary',
            'sa': u'Wiktionary',
            'scn': [u'Wikizziunariu', u'Wiktionary'],
            'sd': u'Wiktionary',
            'sg': u'Wiktionary',
            'sh': u'Wiktionary',
            'si': [u'වික්ෂනරි', u'Wiktionary'],
            'simple': [u'Wiktionary', u'WT'],
            'sk': [u'Wikislovník', u'Wiktionary'],
            'sl': [u'Wikislovar', u'Wiktionary'],
            'sm': u'Wiktionary',
            'so': u'Wiktionary',
            'sq': u'Wiktionary',
            'sr': [u'Викиречник', u'Wiktionary'],
            'ss': u'Wiktionary',
            'st': u'Wiktionary',
            'su': u'Wiktionary',
            'sv': [u'Wiktionary', u'WT'],
            'sw': u'Wiktionary',
            'ta': [u'விக்சனரி', u'Wiktionary', u'விக்கிபீடியா'],
            'te': [u'విక్షనరీ', u'Wiktionary'],
            'tg': u'Wiktionary',
            'th': [u'วิกิพจนานุกรม', u'Wiktionary'],
            'ti': u'Wiktionary',
            'tk': [u'Wikisözlük', u'Wiktionary'],
            'tl': u'Wiktionary',
            'tn': u'Wiktionary',
            'tpi': u'Wiktionary',
            'tr': [u'Vikisözlük', u'Wiktionary'],
            'ts': u'Wiktionary',
            'tt': u'Wiktionary',
            'ug': u'Wiktionary',
            'uk': [u'Вікісловник', u'Wiktionary', u'ВС'],
            'ur': [u'وکی لغت', u'Wiktionary'],
            'uz': [u'Vikilug‘at', u'Wiktionary'],
            'vec': [u'Wikisionario', u'Wiktionary'],
            'vi': u'Wiktionary',
            'vo': [u'Vükivödabuk', u'Wiktionary'],
            'wa': u'Wiktionary',
            'wo': u'Wiktionary',
            'yi': [u'װיקיװערטערבוך', u'Wiktionary', u'וויקיווערטערבוך'],
            'za': u'Wiktionary',
            'zh': u'Wiktionary',
            'zh-min-nan': u'Wiktionary',
            'zu': u'Wiktionary',
        }

        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'af': u'Wiktionarybespreking',
            'am': u'Wiktionary ውይይት',
            'an': u'Descusión Wiktionary',
            'ang': [u'Wikiwordbōcmōtung', u'Wikiwordbocmotung'],
            'ar': u'نقاش ويكاموس',
            'ast': [u'Uiccionariu alderique', u'Uiccionariu discusión'],
            'ay': u'Wiktionary discusión',
            'az': u'Wiktionary müzakirəsi',
            'be': [u'Размовы пра Wiktionary', u'Wiktionary размовы'],
            'bg': u'Уикиречник беседа',
            'bn': [u'উইকিঅভিধান আলোচনা', u'উইকিঅভিধান আলাপ'],
            'br': [u'Kaozeadenn Wikeriadur', u'Wiktionary talk'],
            'bs': u'Razgovor s Vikirječnikom',
            'ca': u'Viccionari Discussió',
            'chr': u'Wiktionary talk',
            'co': u'Wiktionary talk',
            'cs': [u'Diskuse k Wikislovníku', u'Wikislovník diskuse', u'Wiktionary diskuse', u'Wiktionary talk'],
            'csb': u'Diskùsëjô Wiktionary',
            'cy': u'Sgwrs Wiciadur',
            'da': [u'Wiktionary diskussion', u'Wiktionary-diskussion'],
            'de': u'Wiktionary Diskussion',
            'dv': [u'ވިކިރަދީފު ޚިޔާ', u'Wiktionary talk'],
            'el': [u'Συζήτηση βικιλεξικού', u'Βικιλεξικό συζήτηση'],
            'en': u'Wiktionary talk',
            'eo': [u'Vikivortaro-Diskuto', u'Vikivortaro diskuto'],
            'es': u'Wikcionario discusión',
            'et': [u'Vikisõnastiku arutelu', u'Vikisõnastik arutelu'],
            'eu': u'Wiktionary eztabaida',
            'fa': u'بحث ویکی‌واژه',
            'fi': u'Keskustelu Wikisanakirjasta',
            'fj': u'Wiktionary talk',
            'fo': [u'Wiktionary-kjak', u'Wiktionary kjak'],
            'fr': u'Discussion Wiktionnaire',
            'fy': u'Wiktionary oerlis',
            'ga': u'Plé Vicífhoclóra',
            'gd': u'An deasbaireachd aig Wiktionary',
            'gl': u'Conversa Wiktionary',
            'gn': u'Wiktionary myangekõi',
            'gu': u'વિક્શનરી ચર્ચા',
            'gv': u'Resooney Wiktionary',
            'ha': u'Wiktionary talk',
            'he': u'שיחת ויקימילון',
            'hi': u'विक्षनरी वार्ता',
            'hr': u'Razgovor Wječnik',
            'hsb': [u'Diskusija k Wikisłownikej', u'Wiktionary diskusija'],
            'hu': [u'Wikiszótár-vita', u'Wikiszótár vita'],
            'hy': u'Վիքիբառարանի քննարկում',
            'ia': u'Discussion Wiktionario',
            'id': u'Pembicaraan Wiktionary',
            'ie': u'Wiktionary Discussion',
            'io': u'Wikivortaro Debato',
            'is': [u'Wikiorðabókarspjall', u'Wikiorðabókspjall'],
            'it': u'Discussioni Wikizionario',
            'iu': u'Wiktionary talk',
            'ja': [u'Wiktionary・トーク', u'Wiktionary‐ノート'],
            'jbo': u'Wiktionary talk',
            'jv': u'Dhiskusi Wiktionary',
            'ka': u'ვიქსიკონი განხილვა',
            'kk': [u'Уикисөздік талқылауы', u'Уикисөздік talqılawı', u'Уикисөздік تالقىلاۋى'],
            'kl': [u'Wiktionary-p oqalliffia', u'Wiktionary-diskussion', u'Wiktionaryip oqalliffia'],
            'km': [u'ការពិភាក្សាអំពីWiktionary', u'Wiktionary ពិភាក្ស'],
            'kn': u'Wiktionary ಚರ್ಚೆ',
            'ko': u'위키낱말사전토론',
            'ks': u'Wiktionary بَحَژ',
            'ku': [u'Gotûbêja Wîkîferhengê', u'Wîkîferheng gotûbêj', u'Wîkîferheng nîqaş'],
            'kw': [u'Keskows Wiktionary', u'Cows Wiktionary', u'Kescows Wiktionary'],
            'ky': u'Wiktionary баарлашуу',
            'la': u'Disputatio Victionarii',
            'lb': [u'Wiktionnaire Diskussioun', u'Wiktionary Diskussioun'],
            'li': u'Euverlèk Wiktionary',
            'ln': u'Discussion Wiktionary',
            'lo': u'ສົນທະນາກ່ຽວກັບWiktionary',
            'lt': u'Vikižodyno aptarimas',
            'lv': u'Wiktionary diskusija',
            'mg': [u'Dinika amin\'ny Wiktionary', u'Discussion Wiktionary'],
            'mi': u'Wiktionary talk',
            'mk': u'Разговор за Wiktionary',
            'ml': [u'വിക്കിനിഘണ്ടു സംവാദം', u'വിക്കി‌‌ നിഘണ്ടു സംവാദം'],
            'mn': u'Wiktionary-н хэлэлцүүлэг',
            'mr': u'विक्शनरी चर्चा',
            'ms': [u'Perbincangan Wiktionary', u'Perbualan Wiktionary'],
            'mt': [u'Diskussjoni Wikizzjunarju', u'Wikizzjunarju diskussjoni', u'Wikizzjunarju diskuti'],
            'my': u'Wiktionary talk',
            'na': u'Wiktionary talk',
            'nah': [u'Wiktionary tēixnāmiquiliztli', u'Wikipedia Discusión'],
            'nds': [u'Wiktionary Diskuschoon', u'Wiktionary Diskussion'],
            'ne': u'Wiktionary वार्ता',
            'nl': u'Overleg WikiWoordenboek',
            'nn': u'Wiktionary-diskusjon',
            'no': u'Wiktionary-diskusjon',
            'oc': u'Discussion Wikiccionari',
            'om': u'Wiktionary talk',
            'or': [u'Wiktionary ଆଲୋଚନା', u'ଉଇକିପିଡ଼ିଆ ଆଲୋଚନା'],
            'pa': [u'Wiktionary ਗੱਲ-ਬਾਤ', u'Wiktionary ਚਰਚਾ'],
            'pl': u'Wikidyskusja',
            'pnb': u'گل ات',
            'ps': u'د ويکيسيند خبرې اترې',
            'pt': u'Wikcionário Discussão',
            'qu': u'Wiktionary rimanakuy',
            'ro': [u'Discuție Wikționar', u'Discuţie Wikționar'],
            'roa-rup': u'Wiktionary talk',
            'ru': u'Обсуждение Викисловаря',
            'rw': u'Wiktionary talk',
            'sa': [u'Wiktionaryसम्भाषणम्', u'Wiktionaryसंभाषणं'],
            'scn': u'Discussioni Wikizziunariu',
            'sd': u'Wiktionary بحث',
            'sg': u'Discussion Wiktionary',
            'sh': u'Razgovor o Wiktionary',
            'si': [u'වික්ෂනරි සාකච්ඡාව', u'Wiktionary talk'],
            'simple': u'Wiktionary talk',
            'sk': [u'Diskusia k Wikislovníku', u'Komentár k Wikipédii'],
            'sl': u'Pogovor o Wikislovarju',
            'sm': u'Wiktionary talk',
            'so': u'Wiktionary talk',
            'sq': u'Wiktionary diskutim',
            'sr': [u'Разговор о викиречнику', u'Razgovor o Викиречник'],
            'ss': u'Wiktionary talk',
            'st': u'Wiktionary talk',
            'su': u'Obrolan Wiktionary',
            'sv': [u'Wiktionarydiskussion', u'WT-diskussion'],
            'sw': [u'Majadiliano ya Wiktionary', u'Wiktionary majadiliano'],
            'ta': [u'விக்சனரி பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': [u'విక్షనరీ చర్చ', u'Wiktionary చర్చ'],
            'tg': [u'Баҳси Wiktionary', u'Wiktionary talk'],
            'th': [u'คุยเรื่องวิกิพจนานุกรม', u'คุยเรื่องWiktionary'],
            'ti': u'Wiktionary talk',
            'tk': u'Wikisözlük çekişme',
            'tl': u'Usapang Wiktionary',
            'tn': u'Wiktionary talk',
            'tpi': u'Wiktionary toktok',
            'tr': u'Vikisözlük tartışma',
            'ts': u'Wiktionary talk',
            'tt': [u'Wiktionary бәхәсе', u'Wiktionary bäxäse', u'Обсуждение Wiktionary'],
            'ug': [u'Wiktionaryمۇنازىرىسى', u'مۇنازىرىسىWiktionary'],
            'uk': u'Обговорення Вікісловника',
            'ur': u'تبادلۂ خیال وکی لغت',
            'uz': [u'Vikilug‘at munozarasi', u'Vikilug‘at talk'],
            'vec': u'Discussion Wikisionario',
            'vi': u'Thảo luận Wiktionary',
            'vo': [u'Bespik dö Vükivödabuk', u'Wiktionary talk'],
            'wa': u'Wiktionary copene',
            'wo': [u'Wiktionary waxtaan', u'Discussion Wiktionary'],
            'yi': [u'װיקיװערטערבוך רעדן', u'וויקיווערטערבוך רעדן'],
            'za': u'Wiktionary讨论',
            'zh': [u'Wiktionary talk', u'Wiktionary討論', u'Wiktionary讨论'],
            'zh-min-nan': u'Wiktionary討論',
            'zu': u'Wiktionary talk',
        }

        self.namespaces[90] = {
            'en': u'Thread',
        }

        self.namespaces[91] = {
            'en': u'Thread talk',
        }

        self.namespaces[92] = {
            'en': u'Summary',
        }

        self.namespaces[93] = {
            'en': u'Summary talk',
        }

        self.namespaces[100] = {
            'ang': u'Ætēaca',
            'bg': u'Словоформи',
            'bn': u'উইকিসরাস',
            'br': u'Stagadenn',
            'bs': u'Portal',
            'cs': u'Příloha',
            'cy': u'Atodiad',
            'el': u'Παράρτημα',
            'en': u'Appendix',
            'es': u'Apéndice',
            'fa': u'پیوست',
            'fi': u'Liite',
            'fr': u'Annexe',
            'ga': u'Aguisín',
            'gl': u'Apéndice',
            'he': u'נספח',
            'hu': u'Függelék',
            'id': u'Indeks',
            'it': u'Appendice',
            'ja': u'付録',
            'ko': u'부록',
            'ku': u'Pêvek',
            'lb': u'Annexen',
            'lt': u'Sąrašas',
            'lv': u'Pielikums',
            'mg': u'Rakibolana',
            'no': u'Tillegg',
            'oc': u'Annèxa',
            'pl': u'Aneks',
            'pt': u'Apêndice',
            'ro': u'Portal',
            'ru': [u'Приложение', u'Appendix'],
            'sr': u'Портал',
            'tr': u'Portal',
            'uk': u'Додаток',
            'zh': u'附录',
        }
        self.namespaces[101] = {
            'ang': u'Ætēacmōtung',
            'bg': u'Словоформи беседа',
            'bn': u'উইকিসরাস আলোচনা',
            'br': u'Kaozeadenn Stagadenn',
            'bs': u'Razgovor o Portalu',
            'cs': u'Diskuse k příloze',
            'cy': u'Sgwrs Atodiad',
            'el': u'Συζήτηση παραρτήματος',
            'en': u'Appendix talk',
            'es': u'Apéndice Discusión',
            'fa': u'بحث پیوست',
            'fi': u'Keskustelu liitteestä',
            'fr': u'Discussion Annexe',
            'ga': u'Plé aguisín',
            'gl': u'Conversa apéndice',
            'he': u'שיחת נספח',
            'hu': u'Függelékvita',
            'id': u'Pembicaraan Indeks',
            'it': u'Discussioni appendice',
            'ja': u'付録・トーク',
            'ko': u'부록 토론',
            'ku': u'Gotûbêja pêvekê',
            'lb': u'Annexen Diskussioun',
            'lt': u'Sąrašo aptarimas',
            'lv': u'Pielikuma diskusija',
            'mg': u'Dinika amin\'ny rakibolana',
            'no': u'Tilleggdiskusjon',
            'oc': u'Discussion Annèxa',
            'pl': u'Dyskusja aneksu',
            'pt': u'Apêndice Discussão',
            'ro': u'Discuție Portal',
            'ru': [u'Обсуждение приложения', u'Appendix talk'],
            'sr': u'Разговор о порталу',
            'tr': u'Portal tartışma',
            'uk': u'Обговорення додатка',
            'zh': u'附录讨论',
        }

        self.namespaces[102] = {
            'bs': u'Indeks',
            'cy': u'Odliadur',
            'de': u'Verzeichnis',
            'en': u'Concordance',
            'fr': u'Transwiki',
            'hu': u'Index',
            'ia': u'Appendice',
            'ku': u'Nimînok',
            'lt': u'Priedas',
            'pl': u'Indeks',
            'pt': u'Vocabulário',
            'ro': u'Apendice',
            'ru': [u'Конкорданс', u'Concordance'],
            'sv': u'Appendix',
            'uk': u'Індекс',
            'zh': u'Transwiki',
        }

        self.namespaces[103] = {
            'bs': u'Razgovor o Indeksu',
            'cy': u'Sgwrs Odliadur',
            'de': u'Verzeichnis Diskussion',
            'en': u'Concordance talk',
            'fr': u'Discussion Transwiki',
            'hu': u'Indexvita',
            'ia': u'Discussion Appendice',
            'ku': u'Gotûbêja nimînokê',
            'lt': u'Priedo aptarimas',
            'pl': u'Dyskusja indeksu',
            'pt': u'Vocabulário Discussão',
            'ro': u'Discuție Apendice',
            'ru': [u'Обсуждение конкорданса', u'Concordance talk'],
            'sv': u'Appendixdiskussion',
            'uk': u'Обговорення індексу',
            'zh': u'Transwiki talk',
        }

        self.namespaces[104] = {
            'bs': u'Dodatak',
            'cy': u'WiciSawrws',
            'de': [u'Thesaurus', u'WikiSaurus'],
            'en': u'Index',
            'fr': u'Portail',
            'ku': u'Portal',
            'mr': u'सूची',
            'pl': u'Portal',
            'pt': u'Rimas',
            'ru': [u'Индекс', u'Index'],
            'sv': u'Rimord',
        }

        self.namespaces[105] = {
            'bs': u'Razgovor o Dodatku',
            'cy': u'Sgwrs WiciSawrws',
            'de': [u'Thesaurus Diskussion', u'WikiSaurus Diskussion'],
            'en': u'Index talk',
            'fr': u'Discussion Portail',
            'ku': u'Gotûbêja portalê',
            'mr': u'सूची चर्चा',
            'pl': u'Dyskusja portalu',
            'pt': u'Rimas Discussão',
            'ru': [u'Обсуждение индекса', u'Index talk'],
            'sv': u'Rimordsdiskussion',
        }

        self.namespaces[106] = {
            'de': u'Reim',
            'en': u'Rhymes',
            'fr': u'Thésaurus',
            'is': u'Viðauki',
            'pt': u'Portal',
            'ru': [u'Рифмы', u'Rhymes'],
            'sv': u'Transwiki',
        }

        self.namespaces[107] = {
            'de': u'Reim Diskussion',
            'en': u'Rhymes talk',
            'fr': u'Discussion Thésaurus',
            'is': u'Viðaukaspjall',
            'pt': u'Portal Discussão',
            'ru': [u'Обсуждение рифм', u'Rhymes talk'],
            'sv': u'Transwikidiskussion',
        }

        self.namespaces[108] = {
            'en': u'Transwiki',
            'fr': u'Projet',
            'pt': u'Citações',
        }

        self.namespaces[109] = {
            'en': u'Transwiki talk',
            'fr': u'Discussion Projet',
            'pt': u'Citações Discussão',
        }

        self.namespaces[110] = {
            'en': [u'Wikisaurus', u'WS'],
            'is': u'Samheitasafn',
            'ko': u'미주알고주알',
        }

        self.namespaces[111] = {
            'en': u'Wikisaurus talk',
            'is': u'Samheitasafnsspjall',
            'ko': u'미주알고주알 토론',
        }

        self.namespaces[114] = {
            'en': u'Citations',
        }

        self.namespaces[115] = {
            'en': u'Citations talk',
        }

        self.namespaces[116] = {
            'en': u'Sign gloss',
        }

        self.namespaces[117] = {
            'en': u'Sign gloss talk',
        }

        # Global bot allowed languages on
        # http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'am', 'an', 'ang', 'ast', 'ay', 'az', 'be', 'bg', 'bn', 'br', 'bs',
            'ca', 'chr', 'co', 'cy', 'da', 'dv', 'eo', 'es', 'et', 'eu', 'fa',
            'fi', 'fj', 'fo', 'fy', 'ga', 'gd', 'gl', 'gn', 'gv', 'hu', 'ia',
            'id', 'ie', 'io', 'jv', 'ka', 'kl', 'kn', 'ku', 'ky', 'lb', 'lo',
            'lt', 'lv', 'mg', 'mk', 'ml', 'mn', 'my', 'ne', 'nl', 'no', 'oc',
            'or', 'pt', 'sh', 'simple', 'sk', 'sl', 'sm', 'su', 'tg', 'th',
            'ti', 'tk', 'tn', 'tpi', 'ts', 'ug', 'uk', 'vo', 'wa', 'wo', 'zh',
            'zh-min-nan', 'zu',
        ]

        # Other than most Wikipedias, page names must not start with a capital
        # letter on ALL Wiktionaries.
        self.nocapitalize = self.langs.keys()

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are
        # put after those, in code-alphabetical order.

        self.alphabetic_sv = [
            'aa', 'af', 'ak', 'als', 'an', 'roa-rup', 'ast', 'gn', 'ay', 'az',
            'id', 'ms', 'bm', 'zh-min-nan', 'jv', 'su', 'mt', 'bi', 'bo', 'bs',
            'br', 'ca', 'cs', 'ch', 'sn', 'co', 'za', 'cy', 'da', 'de', 'na',
            'mh', 'et', 'ang', 'en', 'es', 'eo', 'eu', 'to', 'fr', 'fy', 'fo',
            'ga', 'gv', 'sm', 'gd', 'gl', 'hr', 'io', 'ia', 'ie', 'ik', 'xh',
            'is', 'zu', 'it', 'kl', 'csb', 'kw', 'rw', 'rn', 'sw', 'ky', 'ku',
            'la', 'lv', 'lb', 'lt', 'li', 'ln', 'jbo', 'hu', 'mg', 'mi', 'mo',
            'my', 'fj', 'nah', 'nl', 'cr', 'no', 'nn', 'hsb', 'oc', 'om', 'ug',
            'uz', 'nds', 'pl', 'pt', 'ro', 'rm', 'qu', 'sg', 'sc', 'st', 'tn',
            'sq', 'scn', 'simple', 'ss', 'sk', 'sl', 'so', 'sh', 'fi', 'sv',
            'tl', 'tt', 'vi', 'tpi', 'tr', 'tw', 'vo', 'wa', 'wo', 'ts', 'yo',
            'el', 'av', 'ab', 'ba', 'be', 'bg', 'mk', 'mn', 'ru', 'sr', 'tg',
            'uk', 'kk', 'hy', 'yi', 'he', 'ur', 'ar', 'tk', 'sd', 'fa', 'ha',
            'ps', 'dv', 'ks', 'ne', 'pi', 'bh', 'mr', 'sa', 'hi', 'as', 'bn',
            'pa', 'pnb', 'gu', 'or', 'ta', 'te', 'kn', 'ml', 'si', 'th', 'lo',
            'dz', 'ka', 'ti', 'am', 'chr', 'iu', 'km', 'zh', 'ja', 'ko',
        ]

        self.interwiki_putfirst = {
            'da': self.alphabetic,
            'en': self.alphabetic,
            'et': self.alphabetic,
            'fi': self.alphabetic,
            'fy': self.fyinterwiki,
            'he': ['en'],
            'hu': ['en'],
            'ms': self.alphabetic_revised,
            'pl': self.alphabetic_revised,
            'sv': self.alphabetic_sv,
            'simple': self.alphabetic,
        }

        self.obsolete = {
            'aa': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Afar_Wiktionary
            'ab': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Abkhaz_Wiktionary
            'ak': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Akan_Wiktionary
            'als': None,  # http://als.wikipedia.org/wiki/Wikipedia:Stammtisch/Archiv_2008-1#Afterwards.2C_closure_and_deletion_of_Wiktionary.2C_Wikibooks_and_Wikiquote_sites
            'as': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Assamese_Wiktionary
            'av': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Avar_Wiktionary
            'ba': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bashkir_Wiktionary
            'bh': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bihari_Wiktionary
            'bi': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bislama_Wiktionary
            'bm': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bambara_Wiktionary
            'bo': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tibetan_Wiktionary
            'ch': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Chamorro_Wiktionary
            'cr': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nehiyaw_Wiktionary
            'dk': 'da',
            'dz': None,
            'ik': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Inupiak_Wiktionary
            'jp': 'ja',
            'mh': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Marshallese_Wiktionary
            'mo': 'ro',  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Moldovan_Wiktionary
            'minnan': 'zh-min-nan',
            'nb': 'no',
            'pi': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Pali_Bhasa_Wiktionary
            'rm': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Rhaetian_Wiktionary
            'rn': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kirundi_Wiktionary
            'sc': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Sardinian_Wiktionary
            'sn': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Shona_Wiktionary
            'to': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tongan_Wiktionary
            'tlh': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Klingon_Wiktionary
            'tw': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Twi_Wiktionary
            'tokipona': None,
            'xh': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Xhosa_Wiktionary
            'yo': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Yoruba_Wiktionary
            'zh-tw': 'zh',
            'zh-cn': 'zh'
        }

        self.interwiki_on_one_line = ['pl']

        self.interwiki_attop = ['pl']
