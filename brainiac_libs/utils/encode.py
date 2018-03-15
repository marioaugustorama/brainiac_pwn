import codecs
class Encode:
    """
suport para encode
    =>suport para encode
    =>cp874
    =>cp875
    =>cp932
    =>cp949 cp950
    =>cp1006
    =>cp1026
    =>cp1140
    =>cp1250
    =>cp1251
    =>cp1252
    =>cp1253
    =>cp1254
    =>cp1255
    =>cp1256
    =>cp1257
    =>cp1258
    =>euc_jp
    =>euc_jis_2004
    =>euc_jisx0213
    =>euc_kr
    =>gb2312
    =>gbk
    =>gb18030
    =>hz
    =>iso2022_jp
    =>iso2022_jp_1
    =>iso2022_jp_2
    =>iso2022_jp_2004
    =>iso2022_jp_3
    =>iso2022_jp_ext
    =>iso2022_kr
    =>iso8859_2,
    =>iso8859_3
    =>iso8859_4
    =>iso8859_5
    =>iso8859_6
    =>iso8859_7
    =>iso8859_8
    =>iso8859_9,
    =>iso8859_10
    =>iso8859_11
    =>iso8859_13
    =>iso8859_14
    =>iso8859_15
    =>iso8859_16
    =>johab
    =>koi8_r
    =>koi8_u
    =>mac_cyrillic
    =>mac_greek
    =>mac_iceland
    =>mac_latin2
    =>mac_roman
    =>mac_turkish
    =>ptcp154
    =>shift_jis
    =>shift_jis_2004
    =>shift_jisx0213
    =>utf_32
    =>utf_32_be
    =>utf_32_le
    =>utf_16
    =>utf_16_be
    =>utf_16_le
    =>utf_7
    =>utf_8
    =>utf_8_sig
    =>idna
    =>mbcs
    =>palmos
    =>punycode
    =>raw_unicode_escape
    =>rot_13
    =>undefined
    =>unicode_escape
    =>unicode_internal
    =>base64_codec
    =>bz2_codec
    =>hex_codec
    =>quopri_codec
    =>string_escape
    =>zlib_codec

    """
    def __init__(self, cp874, cp875, cp932, cp949, cp950, cp1006, cp1026, cp1140, cp1250, cp1251, cp1252, cp1253,
                 cp1254, cp1255, cp1256, cp1257, cp1258, euc_jp, euc_jis_2004, euc_jisx0213, euc_kr, gb2312, gbk,
                 gb18030, hz, iso2022_jp, iso2022_jp_1, iso2022_jp_2, iso2022_jp_2004, iso2022_jp_3, iso2022_jp_ext,
                 iso2022_kr, iso8859_2, iso8859_3, iso8859_4, iso8859_5, iso8859_6, iso8859_7, iso8859_8, iso8859_9,
                 iso8859_10, iso8859_11, iso8859_13, iso8859_14, iso8859_15, iso8859_16, johab, koi8_r, koi8_u,
                 mac_cyrillic, mac_greek, mac_iceland, mac_latin2, mac_roman, mac_turkish, ptcp154, shift_jis,
                 shift_jis_2004, shift_jisx0213, utf_32, utf_32_be, utf_32_le, utf_16, utf_16_be, utf_16_le, utf_7,
                 utf_8, utf_8_sig, idna, mbcs, palmos, punycode, raw_unicode_escape, rot_13, undefined, unicode_escape,
                 unicode_internal, base64_codec, bz2_codec, hex_codec, quopri_codec, string_escape, zlib_codec):
        self.cp874 = cp874
        self.cp875 = cp875
        self.cp932 = cp932
        self.cp949 = cp949
        self.cp950 = cp950
        self.cp1006 = cp1006
        self.cp1026 = cp1026
        self.cp1140 = cp1140
        self.cp1250 = cp1250
        self.cp1251 = cp1251
        self.cp1252 = cp1252
        self.cp1253 = cp1253
        self.cp1254 = cp1254
        self.cp1255 = cp1255
        self.cp1256 = cp1256
        self.cp1257 = cp1257
        self.cp1258 = cp1258
        self.euc_jp = euc_jp
        self.euc_jis_2004 = euc_jis_2004
        self.euc_jisx0213 = euc_jisx0213
        self.euc_kr = euc_kr
        self.gb2312 = gb2312
        self.gbk = gbk
        self.gb18030 = gb18030
        self.hz = hz
        self.iso2022_jp = iso2022_jp
        self.iso2022_jp_1 = iso2022_jp_1
        self.iso2022_jp_2 = iso2022_jp_2
        self.iso2022_jp_2004 = iso2022_jp_2004
        self.iso2022_jp_3 = iso2022_jp_3
        self.iso2022_jp_ext = iso2022_jp_ext
        self.iso2022_kr = iso2022_kr
        self.iso8859_2 = iso8859_2
        self.iso8859_3 = iso8859_3
        self.iso8859_4 = iso8859_4
        self.iso8859_5 = iso8859_5
        self.iso8859_6 = iso8859_6
        self.iso8859_7 = iso8859_7
        self.iso8859_8 = iso8859_8
        self.iso8859_9 = iso8859_9
        self.iso8859_10 = iso8859_10
        self.iso8859_11 = iso8859_11
        self.iso8859_13 = iso8859_13
        self.iso8859_14 = iso8859_14
        self.iso8859_15 = iso8859_15
        self.iso8859_16 = iso8859_16
        self.johab = johab
        self.koi8_r = koi8_r
        self.koi8_u = koi8_u
        self.mac_cyrillic = mac_cyrillic
        self.mac_greek = mac_greek
        self.mac_iceland = mac_iceland
        self.mac_latin2 = mac_latin2
        self.mac_roman = mac_roman
        self.mac_turkish = mac_turkish
        self.ptcp154 = ptcp154
        self.shift_jis = shift_jis
        self.shift_jis_2004 = shift_jis_2004
        self.shift_jisx0213 = shift_jisx0213
        self.utf_32 = utf_32
        self.utf_32_be = utf_32_be
        self.utf_32_le = utf_32_le
        self.utf_16 = utf_16
        self.utf_16_be = utf_16_be
        self.utf_16_le = utf_16_le
        self.utf_7 = utf_7
        self.utf_8 = utf_8
        self.utf_8_sig = utf_8_sig
        self.idna = idna
        self.mbcs = mbcs
        self.palmos = palmos
        self.punycode = punycode
        self.raw_unicode_escape = raw_unicode_escape
        self.rot_13 = rot_13
        self.undefined = undefined
        self.unicode_escape = unicode_escape
        self.unicode_internal = unicode_internal
        self.base64_codec = base64_codec
        self.bz2_codec = bz2_codec
        self.hex_codec = hex_codec
        self.quopri_codec = quopri_codec
        self.cp874 = cp874
        self.cp875 = cp875
        self.cp932 = cp932
        self.cp949 = cp949
        self.cp950 = cp950
        self.cp1006 = cp1006
        self.cp1026 = cp1026
        self.cp1140 = cp1140
        self.cp1250 = cp1250
        self.cp1251 = cp1251
        self.cp1252 = cp1252
        self.cp1253 = cp1253
        self.cp1254 = cp1254
        self.cp1255 = cp1255
        self.cp1256 = cp1256
        self.cp1257 = cp1257
        self.cp1258 = cp1258
        self.euc_jp = euc_jp
        self.euc_jis_2004 = euc_jis_2004
        self.euc_jisx0213 = euc_jisx0213
        self.euc_kr = euc_kr
        self.gb2312 = gb2312
        self.gbk = gbk
        self.gb18030 = gb18030
        self.hz = hz
        self.iso2022_jp = iso2022_jp
        self.iso2022_jp_1 = iso2022_jp_1
        self.iso2022_jp_2 = iso2022_jp_2
        self.iso2022_jp_2004 = iso2022_jp_2004
        self.iso2022_jp_3 = iso2022_jp_3
        self.iso2022_jp_ext = iso2022_jp_ext
        self.iso2022_kr = iso2022_kr
        self.iso8859_2 = iso8859_2
        self.iso8859_3 = iso8859_3
        self.iso8859_4 = iso8859_4
        self.iso8859_5 = iso8859_5
        self.iso8859_6 = iso8859_6
        self.iso8859_7 = iso8859_7
        self.iso8859_8 = iso8859_8
        self.iso8859_9 = iso8859_9
        self.iso8859_10 = iso8859_10
        self.iso8859_11 = iso8859_11
        self.iso8859_13 = iso8859_13
        self.iso8859_14 = iso8859_14
        self.iso8859_15 = iso8859_15
        self.iso8859_16 = iso8859_16
        self.johab, koi8_r = johab, koi8_r
        self.koi8_u = koi8_u
        self.mac_cyrillic = mac_cyrillic
        self.mac_greek = mac_greek
        self.mac_iceland = mac_iceland
        self.mac_latin2 = mac_latin2
        self.mac_roman = mac_roman
        self.mac_turkish = mac_turkish
        self.ptcp154 = ptcp154
        self.shift_jis = shift_jis
        self.shift_jis_2004 = shift_jis_2004
        self.shift_jisx0213 = shift_jisx0213
        self.utf_32 = utf_32
        self.utf_32_be = utf_32_be
        self.utf_32_le = utf_32_le
        self.utf_16 = utf_16
        self.utf_16_be = utf_16_be
        self.utf_16_le = utf_16_le
        self.utf_7 = utf_7
        self.utf_8 = utf_8
        self.utf_8_sig = utf_8_sig
        self.idna = idna
        self.mbcs = mbcs
        self.palmos = palmos
        self.punycode = punycode
        self.raw_unicode_escape = raw_unicode_escape
        self.rot_13 = rot_13
        self.undefined = undefined
        self.unicode_escape = unicode_escape
        self.unicode_internal = unicode_internal
        self.base64_codec = base64_codec
        self.bz2_codec = bz2_codec
        self.hex_codec = hex_codec
        self.quopri_codec = quopri_codec
        self.string_escape = string_escape
        self.zlib_codec = zlib_codec
        self.string_escape = string_escape
        self.zlib_codec = zlib_codec

    def cp874(self):
        enc = codecs.encode(self, encoding='cp874')
        print(str(enc)[2:-1])

    def cp875(self):
        enc = codecs.encode(self, encoding='cp875')
        print(str(enc)[2:-1])

    def cp932(self):
        enc = codecs.encode(self, encoding='cp932')
        print(str(enc)[2:-1])

    def cp949(self):
        enc = codecs.encode(self, encoding='cp949')
        print(str(enc)[2:-1])

    def cp950(self):
        enc = codecs.encode(self, encoding='cp950')
        print(str(enc)[2:-1])

    def cp1006(self):
        enc = codecs.encode(self, encoding='cp1006')
        print(str(enc)[2:-1])

    def cp1026(self):
        enc = codecs.encode(self, encoding='cp1026')
        print(str(enc)[2:-1])

    def cp1140(self):
        enc = codecs.encode(self, encoding='cp1140')
        print(str(enc)[2:-1])

    def cp1250(self):
        enc = codecs.encode(self, encoding='cp1250')
        print(str(enc)[2:-1])

    def cp1251(self):
        enc = codecs.encode(self, encoding='cp1251')
        print(str(enc)[2:-1])

    def cp1252(self):
        enc = codecs.encode(self, encoding='cp1252')
        print(str(enc)[2:-1])

    def cp1253(self):
        enc = codecs.encode(self, encoding='cp1253')
        print(str(enc)[2:-1])

    def cp1254(self):
        enc = codecs.encode(self, encoding='cp1254')
        print(str(enc)[2:-1])

    def cp1255(self):
        enc = codecs.encode(self, encoding='cp1255')
        print(str(enc)[2:-1])

    def cp1256(self):
        enc = codecs.encode(self, encoding='cp1256')
        print(str(enc)[2:-1])

    def cp1257(self):
        enc = codecs.encode(self, encoding='cp1257')
        print(str(enc)[2:-1])

    def cp1258(self):
        enc = codecs.encode(self, encoding='cp1258')
        print(str(enc)[2:-1])

    def euc_jp(self):
        enc = codecs.encode(self, encoding='euc_jp')
        print(str(enc)[2:-1])

    def euc_jis_2004(self):
        enc = codecs.encode(self, encoding='euc_jis_2004')
        print(str(enc)[2:-1])

    def euc_jisx0213(self):
        enc = codecs.encode(self, encoding='euc_jisx0213')
        print(str(enc)[2:-1])

    def euc_kr(self):
        enc = codecs.encode(self, encoding='euc_kr')
        print(str(enc)[2:-1])

    def gb2312(self):
        enc = codecs.encode(self, encoding='gb2312')
        print(str(enc)[2:-1])

    def gbk(self):
        enc = codecs.encode(self, encoding='gbk')
        print(str(enc)[2:-1])

    def gb18030(self):
        enc = codecs.encode(self, encoding='gb18030')
        print(str(enc)[2:-1])

    def hz(self):
        enc = codecs.encode(self, encoding='hz')
        print(str(enc)[2:-1])

    def iso2022_jp(self):
        enc = codecs.encode(self, encoding='iso2022_jp')
        print(str(enc)[2:-1])

    def iso2022_jp_1(self):
        enc = codecs.encode(self, encoding='iso2022_jp_1')
        print(str(enc)[2:-1])

    def iso2022_jp_2(self):
        enc = codecs.encode(self, encoding='iso2022_jp_2')
        print(str(enc)[2:-1])

    def iso2022_jp_2004(self):
        enc = codecs.encode(self, encoding='iso2022_jp_2004')
        print(str(enc)[2:-1])

    def iso2022_jp_3(self):
        enc = codecs.encode(self, encoding='iso2022_jp_3')
        print(str(enc)[2:-1])

    def iso2022_jp_ext(self):
        enc = codecs.encode(self, encoding='iso2022_jp_ext')
        print(str(enc)[2:-1])

    def iso2022_kr(self):
        enc = codecs.encode(self, encoding='iso2022_kr')
        print(str(enc)[2:-1])

    def iso8859_2(self):
        enc = codecs.encode(self, encoding='iso8859_2')
        print(str(enc)[2:-1])

    def iso8859_3(self):
        enc = codecs.encode(self, encoding='iso8859_3')
        print(str(enc)[2:-1])

    def iso8859_4(self):
        enc = codecs.encode(self, encoding='iso8859_4')
        print(str(enc)[2:-1])

    def iso8859_5(self):
        enc = codecs.encode(self, encoding='iso8859_5')
        print(str(enc)[2:-1])

    def iso8859_6(self):
        enc = codecs.encode(self, encoding='iso8859_6')
        print(str(enc)[2:-1])

    def iso8859_7(self):
        enc = codecs.encode(self, encoding='iso8859_7')
        print(str(enc)[2:-1])

    def iso8859_8(self):
        enc = codecs.encode(self, encoding='iso8859_8')
        print(str(enc)[2:-1])

    def iso8859_9(self):
        enc = codecs.encode(self, encoding='iso8859_9')
        print(str(enc)[2:-1])

    def iso8859_10(self):
        enc = codecs.encode(self, encoding='iso8859_10')
        print(str(enc)[2:-1])

    def iso8859_11(self):
        enc = codecs.encode(self, encoding='iso8859_11')
        print(str(enc)[2:-1])

    def iso8859_13(self):
        enc = codecs.encode(self, encoding='iso8859_13')
        print(str(enc)[2:-1])

    def iso8859_14(self):
        enc = codecs.encode(self, encoding='iso8859_14')
        print(str(enc)[2:-1])

    def iso8859_15(self):
        enc = codecs.encode(self, encoding='iso8859_15')
        print(str(enc)[2:-1])

    def iso8859_16(self):
        enc = codecs.encode(self, encoding='iso8859_16')
        print(str(enc)[2:-1])

    def johab(self):
        enc = codecs.encode(self, encoding='johab')
        print(str(enc)[2:-1])

    def koi8_r(self):
        enc = codecs.encode(self, encoding='koi8_r')
        print(str(enc)[2:-1])

    def koi8_u(self):
        enc = codecs.encode(self, encoding='koi8_u')
        print(str(enc)[2:-1])

    def mac_cyrillic(self):
        enc = codecs.encode(self, encoding='mac_cyrillic')
        print(str(enc)[2:-1])

    def mac_greek(self):
        enc = codecs.encode(self, encoding='mac_greek')
        print(str(enc)[2:-1])

    def mac_iceland(self):
        enc = codecs.encode(self, encoding='mac_iceland')
        print(str(enc)[2:-1])

    def mac_latin2(self):
        enc = codecs.encode(self, encoding='mac_latin2')
        print(str(enc)[2:-1])

    def mac_roman(self):
        enc = codecs.encode(self, encoding='mac_roman')
        print(str(enc)[2:-1])

    def mac_turkish(self):
        enc = codecs.encode(self, encoding='mac_turkish')
        print(str(enc)[2:-1])

    def ptcp154(self):
        enc = codecs.encode(self, encoding='ptcp154')
        print(str(enc)[2:-1])

    def shift_jis(self):
        enc = codecs.encode(self, encoding='shift_jis')
        print(str(enc)[2:-1])

    def shift_jis_2004(self):
        enc = codecs.encode(self, encoding='shift_jis_2004')
        print(str(enc)[2:-1])

    def shift_jisx0213(self):
        enc = codecs.encode(self, encoding='shift_jisx0213')
        print(str(enc)[2:-1])

    def utf_32(self):
        enc = codecs.encode(self, encoding='utf_32')
        print(str(enc)[2:-1])

    def utf_32_be(self):
        enc = codecs.encode(self, encoding='utf_32_be')
        print(str(enc)[2:-1])

    def utf_32_le(self):
        enc = codecs.encode(self, encoding='utf_32_le')
        print(str(enc)[2:-1])

    def utf_16(self):
        enc = codecs.encode(self, encoding='utf_16')
        print(str(enc)[2:-1])

    def utf_16_be(self):
        enc = codecs.encode(self, encoding='utf_16_be')
        print(str(enc)[2:-1])

    def utf_16_le(self):
        enc = codecs.encode(self, encoding='utf_16_le')
        print(str(enc)[2:-1])

    def utf_7(self):
        enc = codecs.encode(self, encoding='utf_7')
        print(str(enc)[2:-1])

    def utf_8(self):
        enc = codecs.encode(self, encoding='utf_8')
        print(str(enc)[2:-1])

    def utf_8_sig(self):
        enc = codecs.encode(self, encoding='utf_8_sig')
        print(str(enc)[2:-1])

    def idna(self):
        enc = codecs.encode(self, encoding='idna')
        print(str(enc)[2:-1])

    def mbcs(self):
        enc = codecs.encode(self, encoding='mbcs')
        print(str(enc)[2:-1])

    def palmos(self):
        enc = codecs.encode(self, encoding='palmos')
        print(str(enc)[2:-1])

    def punycode(self):
        enc = codecs.encode(self, encoding='punycode')
        print(str(enc)[2:-1])

    def raw_unicode_escape(self):
        enc = codecs.encode(self, encoding='raw_unicode_escape')
        print(str(enc)[2:-1])

    def rot_13(self):
        enc = codecs.encode(self, encoding='rot_13')
        print(str(enc)[2:-1])

    def undefined(self):
        enc = codecs.encode(self, encoding='undefined')
        print(str(enc)[2:-1])

    def unicode_escape(self):
        enc = codecs.encode(self, encoding='unicode_escape')
        print(str(enc)[2:-1])

    def unicode_internal(self):
        enc = codecs.encode(self, encoding='unicode_internal')
        print(str(enc)[2:-1])

    def base64_codec(self):
        enc = codecs.encode(self, encoding='base64_codec')
        print(str(enc)[2:-1])

    def bz2_codec(self):
        enc = codecs.encode(self, encoding='bz2_codec')
        print(str(enc)[2:-1])

    def hex_codec(self):
        enc = codecs.encode(self, encoding='hex_codec')
        print(str(enc)[2:-1])

    def quopri_codec(self):
        enc = codecs.encode(self, encoding='quopri_codec')
        print(str(enc)[2:-1])

    def cp874(self):
        enc = codecs.encode(self, encoding='cp874')
        print(str(enc)[2:-1])

    def cp875(self):
        enc = codecs.encode(self, encoding='cp875')
        print(str(enc)[2:-1])

    def cp932(self):
        enc = codecs.encode(self, encoding='cp932')
        print(str(enc)[2:-1])

    def cp949(self):
        enc = codecs.encode(self, encoding='cp949')
        print(str(enc)[2:-1])

    def cp950(self):
        enc = codecs.encode(self, encoding='cp950')
        print(str(enc)[2:-1])

    def cp1006(self):
        enc = codecs.encode(self, encoding='cp1006')
        print(str(enc)[2:-1])

    def cp1026(self):
        enc = codecs.encode(self, encoding='cp1026')
        print(str(enc)[2:-1])

    def cp1140(self):
        enc = codecs.encode(self, encoding='cp1140')
        print(str(enc)[2:-1])

    def cp1250(self):
        enc = codecs.encode(self, encoding='cp1250')
        print(str(enc)[2:-1])

    def cp1251(self):
        enc = codecs.encode(self, encoding='cp1251')
        print(str(enc)[2:-1])

    def cp1252(self):
        enc = codecs.encode(self, encoding='cp1252')
        print(str(enc)[2:-1])

    def cp1253(self):
        enc = codecs.encode(self, encoding='cp1253')
        print(str(enc)[2:-1])

    def cp1254(self):
        enc = codecs.encode(self, encoding='cp1254')
        print(str(enc)[2:-1])

    def cp1255(self):
        enc = codecs.encode(self, encoding='cp1255')
        print(str(enc)[2:-1])

    def cp1256(self):
        enc = codecs.encode(self, encoding='cp1256')
        print(str(enc)[2:-1])

    def cp1257(self):
        enc = codecs.encode(self, encoding='cp1257')
        print(str(enc)[2:-1])

    def cp1258(self):
        enc = codecs.encode(self, encoding='cp1258')
        print(str(enc)[2:-1])

    def euc_jp(self):
        enc = codecs.encode(self, encoding='euc_jp')
        print(str(enc)[2:-1])

    def euc_jis_2004(self):
        enc = codecs.encode(self, encoding='euc_jis_2004')
        print(str(enc)[2:-1])

    def euc_jisx0213(self):
        enc = codecs.encode(self, encoding='euc_jisx0213')
        print(str(enc)[2:-1])

    def euc_kr(self):
        enc = codecs.encode(self, encoding='euc_kr')
        print(str(enc)[2:-1])

    def gb2312(self):
        enc = codecs.encode(self, encoding='gb2312')
        print(str(enc)[2:-1])

    def gbk(self):
        enc = codecs.encode(self, encoding='gbk')
        print(str(enc)[2:-1])

    def gb18030(self):
        enc = codecs.encode(self, encoding='gb18030')
        print(str(enc)[2:-1])

    def hz(self):
        enc = codecs.encode(self, encoding='hz')
        print(str(enc)[2:-1])

    def iso2022_jp(self):
        enc = codecs.encode(self, encoding='iso2022_jp')
        print(str(enc)[2:-1])

    def iso2022_jp_1(self):
        enc = codecs.encode(self, encoding='iso2022_jp_1')
        print(str(enc)[2:-1])

    def iso2022_jp_2(self):
        enc = codecs.encode(self, encoding='iso2022_jp_2')
        print(str(enc)[2:-1])

    def iso2022_jp_2004(self):
        enc = codecs.encode(self, encoding='iso2022_jp_2004')
        print(str(enc)[2:-1])

    def iso2022_jp_3(self):
        enc = codecs.encode(self, encoding='iso2022_jp_3')
        print(str(enc)[2:-1])

    def iso2022_jp_ext(self):
        enc = codecs.encode(self, encoding='iso2022_jp_ext')
        print(str(enc)[2:-1])

    def iso2022_kr(self):
        enc = codecs.encode(self, encoding='iso2022_kr')
        print(str(enc)[2:-1])

    def iso8859_2(self):
        enc = codecs.encode(self, encoding='iso8859_2')
        print(str(enc)[2:-1])

    def iso8859_3(self):
        enc = codecs.encode(self, encoding='iso8859_3')
        print(str(enc)[2:-1])

    def iso8859_4(self):
        enc = codecs.encode(self, encoding='iso8859_4')
        print(str(enc)[2:-1])

    def iso8859_5(self):
        enc = codecs.encode(self, encoding='iso8859_5')
        print(str(enc)[2:-1])

    def iso8859_6(self):
        enc = codecs.encode(self, encoding='iso8859_6')
        print(str(enc)[2:-1])

    def iso8859_7(self):
        enc = codecs.encode(self, encoding='iso8859_7')
        print(str(enc)[2:-1])

    def iso8859_8(self):
        enc = codecs.encode(self, encoding='iso8859_8')
        print(str(enc)[2:-1])

    def iso8859_9(self):
        enc = codecs.encode(self, encoding='iso8859_9')
        print(str(enc)[2:-1])

    def iso8859_10(self):
        enc = codecs.encode(self, encoding='iso8859_10')
        print(str(enc)[2:-1])

    def iso8859_11(self):
        enc = codecs.encode(self, encoding='iso8859_11')
        print(str(enc)[2:-1])

    def iso8859_13(self):
        enc = codecs.encode(self, encoding='iso8859_13')
        print(str(enc)[2:-1])

    def iso8859_14(self):
        enc = codecs.encode(self, encoding='iso8859_14')
        print(str(enc)[2:-1])

    def iso8859_15(self):
        enc = codecs.encode(self, encoding='iso8859_15')
        print(str(enc)[2:-1])

    def iso8859_16(self):
        enc = codecs.encode(self, encoding='iso8859_16')
        print(str(enc)[2:-1])

    def johab(self):
        enc = codecs.encode(self, encoding='johab')
        print(str(enc)[2:-1])

    def koi8_r(self):
        enc = codecs.encode(self, encoding='koi8_r')
        print(str(enc)[2:-1])

    def koi8_u(self):
        enc = codecs.encode(self, encoding='koi8_u')
        print(str(enc)[2:-1])

    def mac_cyrillic(self):
        enc = codecs.encode(self, encoding='mac_cyrillic')
        print(str(enc)[2:-1])

    def mac_greek(self):
        enc = codecs.encode(self, encoding='mac_greek')
        print(str(enc)[2:-1])

    def mac_iceland(self):
        enc = codecs.encode(self, encoding='mac_iceland')
        print(str(enc)[2:-1])

    def mac_latin2(self):
        enc = codecs.encode(self, encoding='mac_latin2')
        print(str(enc)[2:-1])

    def mac_roman(self):
        enc = codecs.encode(self, encoding='mac_roman')
        print(str(enc)[2:-1])

    def mac_turkish(self):
        enc = codecs.encode(self, encoding='mac_turkish')
        print(str(enc)[2:-1])

    def ptcp154(self):
        enc = codecs.encode(self, encoding='ptcp154')
        print(str(enc)[2:-1])

    def shift_jis(self):
        enc = codecs.encode(self, encoding='shift_jis')
        print(str(enc)[2:-1])

    def shift_jis_2004(self):
        enc = codecs.encode(self, encoding='shift_jis_2004')
        print(str(enc)[2:-1])

    def shift_jisx0213(self):
        enc = codecs.encode(self, encoding='shift_jisx0213')
        print(str(enc)[2:-1])

    def utf_32(self):
        enc = codecs.encode(self, encoding='utf_32')
        print(str(enc)[2:-1])

    def utf_32_be(self):
        enc = codecs.encode(self, encoding='utf_32_be')
        print(str(enc)[2:-1])

    def utf_32_le(self):
        enc = codecs.encode(self, encoding='utf_32_le')
        print(str(enc)[2:-1])

    def utf_16(self):
        enc = codecs.encode(self, encoding='utf_16')
        print(str(enc)[2:-1])

    def utf_16_be(self):
        enc = codecs.encode(self, encoding='utf_16_be')
        print(str(enc)[2:-1])

    def utf_16_le(self):
        enc = codecs.encode(self, encoding='utf_16_le')
        print(str(enc)[2:-1])

    def utf_7(self):
        enc = codecs.encode(self, encoding='utf_7')
        print(str(enc)[2:-1])

    def utf_8(self):
        enc = codecs.encode(self, encoding='utf_8')
        print(str(enc)[2:-1])

    def utf_8_sig(self):
        enc = codecs.encode(self, encoding='utf_8_sig')
        print(str(enc)[2:-1])

    def idna(self):
        enc = codecs.encode(self, encoding='idna')
        print(str(enc)[2:-1])

    def mbcs(self):
        enc = codecs.encode(self, encoding='mbcs')
        print(str(enc)[2:-1])

    def palmos(self):
        enc = codecs.encode(self, encoding='palmos')
        print(str(enc)[2:-1])

    def punycode(self):
        enc = codecs.encode(self, encoding='punycode')
        print(str(enc)[2:-1])

    def raw_unicode_escape(self):
        enc = codecs.encode(self, encoding='raw_unicode_escape')
        print(str(enc)[2:-1])

    def rot_13(self):
        enc = codecs.encode(self, encoding='rot_13')
        print(str(enc)[2:-1])

    def undefined(self):
        enc = codecs.encode(self, encoding='undefined')
        print(str(enc)[2:-1])

    def unicode_escape(self):
        enc = codecs.encode(self, encoding='unicode_escape')
        print(str(enc)[2:-1])

    def unicode_internal(self):
        enc = codecs.encode(self, encoding='unicode_internal')
        print(str(enc)[2:-1])

    def base64_codec(self):
        enc = codecs.encode(self, encoding='base64_codec')
        print(str(enc)[2:-1])

    def bz2_codec(self):
        enc = codecs.encode(self, encoding='bz2_codec')
        print(str(enc)[2:-1])

    def hex_codec(self):
        enc = codecs.encode(self, encoding='hex_codec')
        print(str(enc)[2:-1])

    def quopri_codec(self):
        enc = codecs.encode(self, encoding='quopri_codec')
        print(str(enc)[2:-1])

    def string_escape(self):
        enc = codecs.encode(self, encoding='string_escape')
        print(str(enc)[2:-1])

    def zlib_codec(self):
        enc = codecs.encode(self, encoding='zlib_codec')
        print(str(enc)[2:-1])

    def string_escape(self):
        enc = codecs.encode(self, encoding='string_escape')
        print(str(enc)[2:-1])

    def zlib_codec(self):
        enc = codecs.encode(self, encoding='zlib_codec')
        print(str(enc)[2:-1])
