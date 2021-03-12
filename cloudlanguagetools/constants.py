
import enum

class Service(enum.Enum):
    Azure = enum.auto()
    Google = enum.auto()
    MandarinCantonese = enum.auto()
    EasyPronunciation = enum.auto()
    Watson = enum.auto()
    Naver = enum.auto()
    Amazon = enum.auto()

class RequestType(enum.Enum):
    translation = enum.auto()
    transliteration = enum.auto()
    audio = enum.auto()

class UsageScope(enum.Enum):
    def __init__(self, key_str):
        self.key_str = key_str 
    User = ("user")
    Global = ("global")

class UsagePeriod(enum.Enum):
    daily = enum.auto()
    monthly = enum.auto()
    lifetime = enum.auto()

class Gender(enum.Enum):
    Male = enum.auto()
    Female = enum.auto()

class Language(enum.Enum):
    af = ("Afrikaans")
    sq = ("Albanian")
    am = ("Amharic")
    ar = ("Arabic")
    hy = ("Armenian")
    az = ("Azerbaijani")
    eu = ("Basque")
    be = ("Belarusian")
    bn = ("Bangla")
    bs = ("Bosnian")
    bg = ("Bulgarian")
    ca = ("Catalan")
    ceb = ("Cebuano")
    ny = ("Chichewa")
    co = ("Corsican")
    hr = ("Croatian")
    cs = ("Czech")
    da = ("Danish")
    nl = ("Dutch")
    en = ("English")
    eo = ("Esperanto")
    et = ("Estonian")
    tl = ("Filipino")
    fi = ("Finnish")
    fr = ("French")
    fy = ("Frisian")
    gl = ("Galician")
    ka = ("Georgian")
    de = ("German")
    el = ("Greek")
    gu = ("Gujarati")
    ht = ("Haitian Creole")
    ha = ("Hausa")
    haw = ("Hawaiian")
    iw = ("Hebrew")
    iu = ("Inuktitut")
    hi = ("Hindi")
    hmn = ("Hmong")
    hu = ("Hungarian")
    is_ = ("Icelandic")
    ig = ("Igbo")
    id_ = ("Indonesian")
    ga = ("Irish")
    it = ("Italian")
    ja = ("Japanese")
    jw = ("Javanese")
    kn = ("Kannada")
    kk = ("Kazakh")
    km = ("Khmer")
    rw = ("Kinyarwanda")
    ko = ("Korean")
    ku = ("Kurdish (Central)")
    ky = ("Kyrgyz")
    lo = ("Lao")
    la = ("Latin")
    lv = ("Latvian")
    lt = ("Lithuanian")
    lb = ("Luxembourgish")
    mk = ("Macedonian")
    mg = ("Malagasy")
    ms = ("Malay")
    ml = ("Malayalam")
    mt = ("Maltese")
    mi = ("Maori")
    mr = ("Marathi")
    mn = ("Mongolian")
    cnr = ("Montenegrin")
    my = ("Myanmar (Burmese)")
    ne = ("Nepali")
    no = ("Norwegian")
    or_ = ("Odia")
    ps = ("Pashto")
    fa = ("Persian")
    pl = ("Polish")
    pt_br = ("Portuguese (Brazil)")
    pa = ("Punjabi")
    ro = ("Romanian")
    ru = ("Russian")
    sm = ("Samoan")
    gd = ("Scots Gaelic")
    st = ("Sesotho")
    sn = ("Shona")
    sd = ("Sindhi")
    si = ("Sinhala")
    sk = ("Slovak")
    sl = ("Slovenian")
    so = ("Somali")
    es = ("Spanish")
    es_mx = ("Spanish (Mexico)")
    su = ("Sundanese")
    sw = ("Swahili")
    sv = ("Swedish")
    tg = ("Tajik")
    ta = ("Tamil")
    tt = ("Tatar")
    te = ("Telugu")
    th = ("Thai")
    ti = ("Tigrinya")
    tr = ("Turkish")
    tk = ("Turkmen")
    uk = ("Ukrainian")
    ur = ("Urdu")
    ug = ("Uyghur")
    uz = ("Uzbek")
    vi = ("Vietnamese")
    cy = ("Welsh")
    xh = ("Xhosa")
    yi = ("Yiddish")
    yo = ("Yoruba")
    zu = ("Zulu")
    he = ("Hebrew")
    as_ = ("Assamese")
    fil = ("Filipino")
    fj = ("Fijian")
    fr_ca = ("French (Canada)")
    kmr = ("Kurdish (Northern)")
    mww = ("Hmong Daw")
    nb = ("Norwegian")
    otq = ("Querétaro Otomi")
    prs = ("Dari")
    pt_pt = ("Portuguese (Portugal)")
    sr_cyrl = ("Serbian (Cyrillic)")
    sr_latn = ("Serbian (Latin)")
    tlh_latn = ("Klingon (Latin)")
    tlh_piqd = ("Klingon (pIqaD)")
    to = ("Tongan")
    ty = ("Tahitian")
    yua = ("Yucatec Maya")
    yue = ("Chinese (Cantonese, Traditional)")
    zh_cn = ("Chinese (Simplified)")
    zh_tw = ("Chinese (Traditional)")


    def __init__(self, lang_name):
        self.lang_name = lang_name        

class AudioLanguage(enum.Enum):
    af_ZA = (Language.af, "Afrikaans (South Africa)")
    ar_EG = (Language.ar, "Arabic (Egypt)")
    ar_SA = (Language.ar, "Arabic (Saudi Arabia)")
    ar_XA = (Language.ar, "Arabic")
    bg_BG = (Language.bg, "Bulgarian")
    bn_IN = (Language.bn, "Bengali (India)")
    ca_ES = (Language.ca, "Catalan")
    cs_CZ = (Language.cs, "Czech")
    cy_GB = (Language.cy, "Welsh")
    da_DK = (Language.da, "Danish")
    de_AT = (Language.de, "German (Austria)")
    de_CH = (Language.de, "German (Switzerland)")
    de_DE = (Language.de, "German (Germany)")
    el_GR = (Language.el, "Greek")
    en_AU = (Language.en, "English (Australia)")
    en_CA = (Language.en, "English (Canada)")
    en_GB = (Language.en, "English (UK)")
    en_GB_WLS = (Language.en, "English (Welsh)")
    en_IE = (Language.en, "English (Ireland)")
    en_IN = (Language.en, "English (India)")
    en_US = (Language.en, "English (US)")
    es_ES = (Language.es, "Spanish (Spain)")
    es_MX = (Language.es, "Spanish (Mexico)")
    es_LA = (Language.es, "Spanish (Latin America)")
    es_US = (Language.es, "Spanish (North America)")
    et_EE = (Language.et, "Estonian")
    fi_FI = (Language.fi, "Finnish")
    fil_PH = (Language.tl, "Filipino (Philippines)")
    fr_CA = (Language.fr_ca, "French (Canada)")
    fr_CH = (Language.fr, "French (Switzerland)")
    fr_FR = (Language.fr, "French (France)")
    ga_IE = (Language.ga, "Irish (Ireland)")
    gu_IN = (Language.gu, "Gujarati (India)")
    he_IL = (Language.he, "Hebrew (Israel)")
    hi_IN = (Language.hi, "Hindi (India)")
    hr_HR = (Language.hr, "Croatian")
    hu_HU = (Language.hu, "Hungarian")
    id_ID = (Language.id_, "Indonesian")
    is_IS = (Language.is_, "Icelandic")
    it_IT = (Language.it, "Italian")
    ja_JP = (Language.ja, "Japanese")
    ko_KR = (Language.ko, "Korean")
    kn_IN = (Language.kn, "Kannada (India)")
    lt_LT = (Language.lt, "Lithuanian")
    lv_LV = (Language.lv, "Latvian")
    ml_IN = (Language.ml, "Malayalam (India)")
    ms_MY = (Language.ms, "Malay")
    mt_MT = (Language.mt, "Maltese (Malta)")
    nb_NO = (Language.nb, "Norwegian")
    nl_NL = (Language.nl, "Dutch")
    pl_PL = (Language.pl, "Polish")
    pt_BR = (Language.pt_br, "Portuguese (Brazil)")
    pt_PT = (Language.pt_pt, "Portuguese (Portugal)")
    ro_RO = (Language.ro, "Romanian")
    ru_RU = (Language.ru, "Russian")
    sk_SK = (Language.sk, "Slovak")
    sl_SI = (Language.sl, "Slovenian")
    sr_RS = (Language.sr_cyrl, "Serbian (Serbia)")
    sv_SE = (Language.sv, "Swedish")
    ta_IN = (Language.ta, "Tamil (India)")
    te_IN = (Language.te, "Telugu (India)")
    th_TH = (Language.th, "Thai")
    tr_TR = (Language.tr, "Turkish (Turkey)")
    uk_UA = (Language.uk, "Ukrainian (Ukraine)")
    vi_VN = (Language.vi, "Vietnamese")
    zh_CN = (Language.zh_cn, "Chinese (Mandarin, Simplified)")
    zh_HK = (Language.yue, "Chinese (Cantonese, Traditional)")
    zh_TW = (Language.zh_tw, "Chinese (Taiwanese Mandarin)")

    def __init__(self, lang, audio_lang_name):
        self.lang = lang
        self.audio_lang_name = audio_lang_name    