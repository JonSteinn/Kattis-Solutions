from main import inversions
import unittest

# Some of these may be repeated as they are randomly generated

class RandomizedTestCases(unittest.TestCase):
    def test_tdXbRfgtfYzdUUr(self):
        self.assertEqual(inversions('0'), 0)

    def test_SVgTHdiovdJS_xX(self):
        self.assertEqual(inversions('1'), 0)

    def test_NHvdFqcfBfdLkFn(self):
        self.assertEqual(inversions('?'), 0)

    def test_pkuHyOfZWboMeSy(self):
        self.assertEqual(inversions('00'), 0)

    def test_XMvyDWDyfJvCOUc(self):
        self.assertEqual(inversions('01'), 0)

    def test_vp_OnmfRWJtlxYy(self):
        self.assertEqual(inversions('0?'), 0)

    def test_gDEOQjkdNRHYMgh(self):
        self.assertEqual(inversions('10'), 1)

    def test_enMkVRIKgZEnbcW(self):
        self.assertEqual(inversions('11'), 0)

    def test_PzuuwMenmhdtpIk(self):
        self.assertEqual(inversions('1?'), 1)

    def test_lvWKwmEcKivEqQO(self):
        self.assertEqual(inversions('?0'), 1)

    def test_vyeYEwHNC_fhDCv(self):
        self.assertEqual(inversions('?1'), 0)

    def test_vQeDqZaiZgubopn(self):
        self.assertEqual(inversions('??'), 1)

    def test_eKBSFxQnDQaJEX_(self):
        self.assertEqual(inversions('000'), 0)

    def test_LyTpGRiaJUbb_fG(self):
        self.assertEqual(inversions('001'), 0)

    def test_xJDUhSVyUOQYdcx(self):
        self.assertEqual(inversions('00?'), 0)

    def test_dGoGaPjUAYobiOF(self):
        self.assertEqual(inversions('010'), 1)

    def test_jtGAKIVWMbqtdUN(self):
        self.assertEqual(inversions('011'), 0)

    def test_puBecxWlZeqZpTT(self):
        self.assertEqual(inversions('01?'), 1)

    def test_jbROLZYeevSxaPu(self):
        self.assertEqual(inversions('0?0'), 1)

    def test_mHpWlgFxtvgAXTm(self):
        self.assertEqual(inversions('0?1'), 0)

    def test_YWitzxzDzqAtsbh(self):
        self.assertEqual(inversions('0??'), 1)

    def test_eBsNDBMzgUOGdjn(self):
        self.assertEqual(inversions('100'), 2)

    def test_crnMhnYHmAQgeCA(self):
        self.assertEqual(inversions('101'), 1)

    def test_v_i_uPnKPkkPtVl(self):
        self.assertEqual(inversions('10?'), 3)

    def test_lmuoPeZAHyxIVjL(self):
        self.assertEqual(inversions('110'), 2)

    def test_sPrUUcGQzcbbmHL(self):
        self.assertEqual(inversions('111'), 0)

    def test_GHKpLBXDMtXrHsE(self):
        self.assertEqual(inversions('11?'), 2)

    def test_OTzDNznEsHJZpSZ(self):
        self.assertEqual(inversions('1?0'), 4)

    def test_rqzxxaEKdMKVDeu(self):
        self.assertEqual(inversions('1?1'), 1)

    def test_VqkmPGBYWUjoYND(self):
        self.assertEqual(inversions('1??'), 5)

    def test_Tsh_xtKrLIJPcoL(self):
        self.assertEqual(inversions('?00'), 2)

    def test_YepoDKMWvyrlFXZ(self):
        self.assertEqual(inversions('?01'), 1)

    def test_mzcJdioRVTp_ZKL(self):
        self.assertEqual(inversions('?0?'), 3)

    def test_TyMgTNQeLAWYyzJ(self):
        self.assertEqual(inversions('?10'), 3)

    def test_TkrVXHGl_dJkodb(self):
        self.assertEqual(inversions('?11'), 0)

    def test_SXnZOCm_VzyYbUQ(self):
        self.assertEqual(inversions('?1?'), 3)

    def test_fYVZrTytVtCEmzr(self):
        self.assertEqual(inversions('??0'), 5)

    def test_uldYAdtPpIBfyEg(self):
        self.assertEqual(inversions('??1'), 1)

    def test_gWSWOaACBlTBRjr(self):
        self.assertEqual(inversions('???'), 6)

    def test_lW_jOaaXnZTkmPG(self):
        self.assertEqual(inversions('????0???'), 928)

    def test_pDYvyAoOZEUVdhg(self):
        self.assertEqual(inversions('1???1?11??1011??1?0010'), 37376)

    def test_VgFoDrYZWfQQKaW(self):
        self.assertEqual(inversions('000?1?1?1'), 18)

    def test_E_SKqpFrbqgtRQF(self):
        self.assertEqual(inversions('?010100110100?1110?010?1?'), 2240)

    def test_ScFaRxsKrBoAwVG(self):
        self.assertEqual(inversions('??01?11?0?0??0000???1?1'), 131584)

    def test_IITaRFPbLdDTGPO(self):
        self.assertEqual(inversions('00?1?0?1?1?001?'), 1424)

    def test_caNJNKTPxnWwCSY(self):
        self.assertEqual(inversions('000011?10?101100?'), 230)

    def test_FtUXmAUIXpumCDq(self):
        self.assertEqual(inversions('0?1???01?001011?11?1?0??1??011'), 370688)

    def test_uKFqbPfQWmWRrit(self):
        self.assertEqual(inversions('101?00??'), 78)

    def test_DjaODwudUgLfHkV(self):
        self.assertEqual(inversions('00011???100??1?'), 1328)

    def test_LUq_EJJfMPS_Ddt(self):
        self.assertEqual(inversions('10000101??1000?000??1?00'), 4400)

    def test_wcgLxDENFJpPStA(self):
        self.assertEqual(inversions('?0??01111??'), 272)

    def test_XaWRLcxIxwWiluG(self):
        self.assertEqual(inversions('100?0010101100011????0???01?101000??100'), 390656)

    def test_ahKudVxjnIGvpyh(self):
        self.assertEqual(inversions('1011?01??10???11??00???01'), 183808)

    def test_OpOGEbCmqNwXfez(self):
        self.assertEqual(inversions('111?00???1?0??1?1?10???0000110?1?11?011?01?11110'), 33161216)

    def test_tUhRlsBTAzfEQcC(self):
        self.assertEqual(inversions('00011110010??11?0110'), 330)

    def test_bFkLdqgOBShGeIp(self):
        self.assertEqual(inversions('?0?01???011?1?100100??11?1010011?00??01?1??0?0'), 36372480)

    def test_v_pLVmkhQJawdGg(self):
        self.assertEqual(inversions('0001?000?11?0????1?10?10'), 25856)

    def test_bhwbRmpQqLesLHA(self):
        self.assertEqual(inversions('0010??11010??0?01?101??0111?1110?001110000?00010'), 648704)

    def test_IgAWxctmQVDzAes(self):
        self.assertEqual(inversions('0?1011?111?11011?01?01?0????1010100?1110??'), 1982464)

    def test_ZiQmnlorQflUwOR(self):
        self.assertEqual(inversions('??0?1000?0??1?100101110???1000?00?0'), 655360)

    def test_YbkiitlKVSJjqBM(self):
        self.assertEqual(inversions('100?'), 5)

    def test_zYERiysEmpREYHu(self):
        self.assertEqual(inversions('10?0110?1'), 33)

    def test_iB_moCGvPTHuiXG(self):
        self.assertEqual(inversions('01?110111???1100111'), 552)

    def test_YETjfwHWRvRofWU(self):
        self.assertEqual(inversions('11?011??10'), 118)

    def test_HFu_PjNgmzKnewM(self):
        self.assertEqual(inversions('0011101??011?01?000?1'), 1888)

    def test_WCGlFpxjAXXbuL_(self):
        self.assertEqual(inversions('1??11101?000'), 230)

    def test_SmQoDwKNUSePzoU(self):
        self.assertEqual(inversions('0?11??10?00????00?'), 24832)

    def test_XPx_zGIkLFnMFJG(self):
        self.assertEqual(inversions('0111?1100?111?1?11?01???1???010111?111?0'), 1495040)

    def test_cKoENtvyycAngSb(self):
        self.assertEqual(inversions('?00111?'), 11)

    def test_CwNwbAonwqxusot(self):
        self.assertEqual(inversions('0101?0?01?10'), 130)

    def test_uyeOuH_okVcOpAt(self):
        self.assertEqual(inversions('?0010?0?0?10???10?011????000?111???1'), 7733248)

    def test_esvELOrUemJQSuR(self):
        self.assertEqual(inversions('00?1011???0?00?1??10110'), 14336)

    def test_iJNDNZcOSevNJtD(self):
        self.assertEqual(inversions('1?00?001'), 33)

    def test_wXHbaWqpLUUvvZm(self):
        self.assertEqual(inversions('0?110?1?100011011??0?0010111?1??'), 58112)

    def test_HvrhDxFAdLGWUKF(self):
        self.assertEqual(inversions('110111?111??1?10??????11?110?1'), 442368)

    def test_SWxsRgcUpwfFBWB(self):
        self.assertEqual(inversions('1010??11?1?11?1?0'), 2032)

    def test_vEkCksLBiuQrAeC(self):
        self.assertEqual(inversions('?1??001000?00??101?1?10000???1?10?0'), 1167360)

    def test_hciqdstFKgeiChE(self):
        self.assertEqual(inversions('11111?1?1?1?1000???0?1011?110?0'), 155904)

    def test_BfliMNzysORwuSB(self):
        self.assertEqual(inversions('0??1010?1???11?1?101?001'), 33280)

    def test_RZcoQljeWoydcMT(self):
        self.assertEqual(inversions('11?10?0?01??10?110011?1?01?00011?101??100010'), 1112064)

    def test_hejvRqdTnCvEHzc(self):
        self.assertEqual(inversions('1?1???11001010??1???11?001??11?0??01?111101'), 13565952)

    def test_xfApGOMwpyjqdFK(self):
        self.assertEqual(inversions('??0?10111??1?00???0111?'), 59648)

    def test_RruifoXPoFIghN_(self):
        self.assertEqual(inversions('?00???0011101?100?000?10??1?011?001??0010011?11111'), 3731456)

    def test_GjofuZpzHKMpl_C(self):
        self.assertEqual(inversions('0111100?01100?01???00?1010?1??100?1?001?101110??01'), 4894720)

    def test_ThlsdpmaXYaSuIP(self):
        self.assertEqual(inversions('??1?001?1000?0?101110?0001??0'), 57088)

    def test_fQiremUJpJsbOp_(self):
        self.assertEqual(inversions('1??10?001101??1?110?1?0?'), 36608)

    def test_MNTxGChCajFxKIT(self):
        self.assertEqual(inversions('010000?0?0??10?1101?0??1?0??01??00?010??0110'), 13500416)

    def test_NCScGCRedUWwDCX(self):
        self.assertEqual(inversions('0011100?01?011?1?110??11101?011??0?1000001011'), 269056)

    def test_JNqgsBzXMBSNgjJ(self):
        self.assertEqual(inversions('00???11110111?101?0?11?1??0???0?10011?'), 3026944)

    def test_AdbuokNYdUaeiNv(self):
        self.assertEqual(inversions('101?0??1?00?0?0?10?0??0111100?1?101??0?11?1'), 12189696)

    def test_VXvemQqXoQCLKQv(self):
        self.assertEqual(inversions('??0?'), 14)

    def test_ozoaVGLFTIqLBbU(self):
        self.assertEqual(inversions('011011?0?01011?010??1?1??0110?1000'), 83456)

    def test_THHSEOSspgElJFr(self):
        self.assertEqual(inversions('?00?1?1?110??1'), 1040)

    def test_InDaJJXSiqwtoIm(self):
        self.assertEqual(inversions('1??01100000'), 93)

    def test_qMIkSAzmeDQKhUH(self):
        self.assertEqual(inversions('00??'), 1)

    def test_HcVvIikobjH_IkI(self):
        self.assertEqual(inversions('1101?00?11?1'), 122)

    def test_vuPvSkgzaDBHVJb(self):
        self.assertEqual(inversions('00?110??1?11??11111011111?01??0?000?00011?0?11'), 2387968)

    def test_xyMsWJIKCXnTEZi(self):
        self.assertEqual(inversions('111100?11?01????1?1010000???0?0?000??0'), 4222976)

    def test_sRBhoYcOUnRWDfA(self):
        self.assertEqual(inversions('0?100101??110?00?100011??001?1'), 26112)

    def test_pUgaKpSzSMBUxWX(self):
        self.assertEqual(inversions('001011??0???1'), 480)

    def test_nzYIrPtmPKgJtMf(self):
        self.assertEqual(inversions('0?101???0?1?0111'), 1328)

    def test_zQvpKnKiYYlchmA(self):
        self.assertEqual(inversions('1?10?1111010?101?0??11????101?1?0111??110'), 3190784)

    def test_KUpavdeySvTlqfr(self):
        self.assertEqual(inversions('1?111?1??00??1010?????10'), 184832)

    def test_fdJRWYBavrtqDRD(self):
        self.assertEqual(inversions('?0?01?011?010?1?1'), 1616)

    def test_UugNLdAjRVJIThg(self):
        self.assertEqual(inversions('11?1??10??010011??'), 6048)

    def test_jAeOiEbZWXiVtNv(self):
        self.assertEqual(inversions('?0???111010?0001?0?1011100?00?1???01?00001110'), 2146304)

    def test_puKzrWwMQoQtVi_(self):
        self.assertEqual(inversions('0????10?10000010??110?0101?0?1??1100101?110'), 1523712)

    def test__nTmfvniuvYQYUD(self):
        self.assertEqual(inversions('1?1010100000?001??1?0?1?0000?100??10??0111'), 802816)

    def test_OhFasqAXNNFzfDU(self):
        self.assertEqual(inversions('?11??1?1????1?0??0??0?1110???0?110111100100?01'), 153747456)

    def test_uMVPwCHHjxVgzLX(self):
        self.assertEqual(inversions('10?1?0??1????00?0?100??010?001'), 1032192)

    def test_iHHEPSsvAGUvuay(self):
        self.assertEqual(inversions('?01??1111?1?000011?10101?1?00?111'), 65792)

    def test_SGgoiehyvuFcjmL(self):
        self.assertEqual(inversions('0?1001?11???1?010010'), 3344)

    def test_IyBiaHuUZtFLFcP(self):
        self.assertEqual(inversions('??11110001'), 61)

    def test_kyDRYLMCLyujYSh(self):
        self.assertEqual(inversions('001?101111100?001?11??010111?000??1??0?100??000'), 2768896)

    def test_KkOtUuYCOqawIJw(self):
        self.assertEqual(inversions('???1'), 6)

    def test_zRyshnBgdFAokII(self):
        self.assertEqual(inversions('0101??010?00?11?1?0001?'), 8096)

    def test_aLgRkNvQBzXFqCw(self):
        self.assertEqual(inversions('?1??0?0?0'), 432)

    def test_aAxtChMZRsoBxfr(self):
        self.assertEqual(inversions('10000?0?1??0??0?00?11?????0?01??10'), 7536640)

    def test_EPVmoWjwTvzynwj(self):
        self.assertEqual(inversions('10?0??110?0?11??010?'), 12672)

    def test_FRMxBE_CH_TEOAt(self):
        self.assertEqual(inversions('01????01?100??0?10??100011?1?1011110?001000?1?11?0'), 19431424)

    def test_iVhYoTvOcqCNSMA(self):
        self.assertEqual(inversions('0000??01?0000?1?1?'), 1168)

    def test_hnCYadUdqKwAGyP(self):
        self.assertEqual(inversions('000?011?100'), 39)

    def test_LbTpbqQVmfopVev(self):
        self.assertEqual(inversions('?1110?10?0001111?0?0110?00110100?010?0100011?01??1'), 679424)

    def test_skuRjHKYWwuWoab(self):
        self.assertEqual(inversions('01?0?010?00?11000??1?01110'), 8480)

    def test_Y_RIiBVmiLOpswp(self):
        self.assertEqual(inversions('10011?11001?1'), 71)

    def test_cPxTddHqdEJzBPV(self):
        self.assertEqual(inversions('1?110?01?11?10?1100?10?0?1100100?1110110???1?11'), 2150400)

    def test_SdjX_MKtRCbYHtN(self):
        self.assertEqual(inversions('01111?111??10?0001100110100?1?110?0?'), 50048)

    def test_jNUbRppd_fh_xXI(self):
        self.assertEqual(inversions('1?0?01??1?11?111?01???10??11?01?101100111001?0'), 9117696)

    def test_cORcVZQBUNnqxsZ(self):
        self.assertEqual(inversions('0??001?01??0'), 448)

    def test_yPykFOQtiraNoWc(self):
        self.assertEqual(inversions('11?1?00011110???10001010?00?1111?0'), 40064)

    def test__FxAzVjXPvIBqjk(self):
        self.assertEqual(inversions('???1???1?10???1?010011101111???0'), 1953792)

    def test_FInJWMgzvr_YLsP(self):
        self.assertEqual(inversions('10001????00'), 264)

    def test_xwrdkQGybwscovd(self):
        self.assertEqual(inversions('??0?01?01?0?100?0?10001111?010?'), 106240)

    def test_KMWtfOoBYhhkFqU(self):
        self.assertEqual(inversions('0?11?010???101??110'), 5088)

    def test_ZreBRtXiRegCTzr(self):
        self.assertEqual(inversions('?1??1011?0?11?0?01?101??1??1'), 368640)

    def test_QyfVYNPubarXUnF(self):
        self.assertEqual(inversions('100?00'), 11)

    def test_RpDVgzYppTxegHC(self):
        self.assertEqual(inversions('?10?010?11?01?11'), 672)

    def test_ieeNboLQFHOxzYo(self):
        self.assertEqual(inversions('10100?0??01?????0'), 9088)

    def test_WRGvLcmspTaZgQW(self):
        self.assertEqual(inversions('?0?00??0110?0??0??11110??0?'), 290816)

    def test_gCFrTHcTNLwkaof(self):
        self.assertEqual(inversions('0??10?001010??0101110010100?11?01?10?010?01??1?1'), 1978368)

    def test_wondOsIeIrvqJEM(self):
        self.assertEqual(inversions('?1000?0?000111111?01??0?1'), 7136)

    def test_nGcvVdJhxE_zjdg(self):
        self.assertEqual(inversions('?010010?0011??10?0010?1?101?'), 20352)

    def test_odNjxJQPUMbfrLK(self):
        self.assertEqual(inversions('0????0?0??01?1?001111?0?1111?0?01?10??1?1101?0?00'), 148504576)

    def test_CgkSngufQBszplJ(self):
        self.assertEqual(inversions('?0?0011?010??11???1?????011'), 565248)

    def test_DYvlweLSj_WgDYW(self):
        self.assertEqual(inversions('??00000?11?0?0001110??011??0110?0'), 109824)

    def test_fxkDHcrXiOWylVB(self):
        self.assertEqual(inversions('01?1011?1??1?11?00?'), 6176)

    def test_sQdPdVuoiqEPVjS(self):
        self.assertEqual(inversions('0???0??00??0?110??010100?0?0?110'), 888832)

    def test_eyTwIaDKLVtfSVk(self):
        self.assertEqual(inversions('?0?01???001????0?01????101????10001101011011'), 50790400)

    def test_SUrISUPSUQNcruz(self):
        self.assertEqual(inversions('1?11???100?10???1?011?0010'), 105216)

    def test_XrtZXVUHSoNVhtZ(self):
        self.assertEqual(inversions('1??1'), 5)

    def test_wutIFyOpwlsiAPd(self):
        self.assertEqual(inversions('00??'), 1)

    def test_PAl_RMfJsGFtBCc(self):
        self.assertEqual(inversions('??11'), 1)

    def test_cLATTphYyifIhhW(self):
        self.assertEqual(inversions('??11'), 1)

    def test_DgVrfPEjtzkD_nT(self):
        self.assertEqual(inversions('110?01'), 11)

    def test_AxaDOhSOcCZClGw(self):
        self.assertEqual(inversions('1?1?0'), 19)

    def test__WPkacTuxOeaSxp(self):
        self.assertEqual(inversions('???110'), 34)

    def test_OZJNSGnJTZjmHgz(self):
        self.assertEqual(inversions('0101'), 1)

    def test_SAVmH_m_KenbIYb(self):
        self.assertEqual(inversions('??1?11'), 10)

    def test_TVsjprqwvwcoTun(self):
        self.assertEqual(inversions('?1101'), 5)

    def test_nAVNmeWvxPOAQgF(self):
        self.assertEqual(inversions('10110'), 4)

    def test_CgKRpPGtcXMegrR(self):
        self.assertEqual(inversions('00?10'), 3)

    def test_MyncAseDycOMGUX(self):
        self.assertEqual(inversions('10111'), 1)

    def test_ruZvwjMSzPrifOL(self):
        self.assertEqual(inversions('001?'), 1)

    def test_PAaMUaPVRcApYHN(self):
        self.assertEqual(inversions('1?11'), 1)

    def test_jnjBoGiwkzeKXdW(self):
        self.assertEqual(inversions('??10'), 9)

    def test_AoAVgqSOmrmmHNO(self):
        self.assertEqual(inversions('?111?'), 7)

    def test_x_saJVNYOipUvhk(self):
        self.assertEqual(inversions('???0'), 18)

    def test_vpNilojEOmrPMHC(self):
        self.assertEqual(inversions('00?1?'), 3)

    def test_WqbAuNvfFFeXrUf(self):
        self.assertEqual(inversions('?1?011'), 11)

    def test_cYvWwVAjQkozxO_(self):
        self.assertEqual(inversions('111100'), 8)

    def test_WgRAXSwsqnqCTds(self):
        self.assertEqual(inversions('00??00'), 9)

    def test_ZrCaXvTWtTyOpqn(self):
        self.assertEqual(inversions('01001'), 2)

    def test_wBrErhFgYgFmCsC(self):
        self.assertEqual(inversions('00??0'), 5)

    def test_CUIIOBEuDRzMHBK(self):
        self.assertEqual(inversions('?101?0'), 23)

    def test_txytvuGbqvalJL_(self):
        self.assertEqual(inversions('11?1'), 2)

    def test_kGMOiujVQZmuSZX(self):
        self.assertEqual(inversions('?10?'), 9)

    def test__HnEPrOeiIvNdjQ(self):
        self.assertEqual(inversions('010??'), 9)

    def test_hiOEtyyWsJkuZsT(self):
        self.assertEqual(inversions('?00101'), 5)

    def test_BmPagMtrXygbCQy(self):
        self.assertEqual(inversions('00100?'), 5)

    def test_mksDmUtI_Gl_nkt(self):
        self.assertEqual(inversions('1011'), 1)

    def test_mQDxSNndIdmklXF(self):
        self.assertEqual(inversions('10111?'), 6)

    def test_GPWaBsnGfnKpTkv(self):
        self.assertEqual(inversions('?00?1'), 5)

    def test_b_rqShcsnLBUHhK(self):
        self.assertEqual(inversions('00?1'), 0)

    def test_NgiXnioIjjpoYEo(self):
        self.assertEqual(inversions('1?0110'), 11)

    def test_kaWRsLINfVWhLGk(self):
        self.assertEqual(inversions('11?11?'), 13)

    def test_swuxEqpfHxcsZkZ(self):
        self.assertEqual(inversions('01?01'), 4)

    def test_NxztlKtipaNkNyy(self):
        self.assertEqual(inversions('?1110'), 7)

    def test_gcbKNOonAChCi_y(self):
        self.assertEqual(inversions('??00'), 9)

    def test_njEaurUcnrOWFmZ(self):
        self.assertEqual(inversions('1?10??'), 46)

    def test_dcRnlCTAINMNCsO(self):
        self.assertEqual(inversions('?01?1'), 5)

    def test_omXoKGacvuGtpPs(self):
        self.assertEqual(inversions('1111?'), 4)

    def test__xpAVtvhWfpKOKa(self):
        self.assertEqual(inversions('0011?0'), 7)

    def test_gJtKapBFzHOsiUG(self):
        self.assertEqual(inversions('?0??'), 10)

    def test_PnowQzg_nGMeMGr(self):
        self.assertEqual(inversions('0???'), 6)

    def test_kKUhYJYgkhSRkls(self):
        self.assertEqual(inversions('10?1'), 3)

    def test_aRLoXDyLaPsKMqF(self):
        self.assertEqual(inversions('0000?'), 0)

    def test_ViSplxcZbyCoSLk(self):
        self.assertEqual(inversions('01?0?'), 11)

    def test_RvCJudBWzCMatqm(self):
        self.assertEqual(inversions('0000'), 0)

    def test_gXaazTnOzdtwdYJ(self):
        self.assertEqual(inversions('01?010'), 9)

    def test_whJUfrdEchXdQKm(self):
        self.assertEqual(inversions('1??101'), 17)

    def test_EakAUYHEze_tmEo(self):
        self.assertEqual(inversions('0?0?'), 3)

    def test_sFLGjspUtDnMxdr(self):
        self.assertEqual(inversions('?1??'), 14)

    def test_vDRmBXODasByQkN(self):
        self.assertEqual(inversions('?10?'), 9)

    def test_KpCzjxPuooaLdAl(self):
        self.assertEqual(inversions('1?01'), 4)

    def test_otbktJfSTgdWhcf(self):
        self.assertEqual(inversions('?1?00?'), 46)

    def test_vwPNJsUMZboOEjb(self):
        self.assertEqual(inversions('010?1'), 3)

    def test_opMQboUuUnMLpVV(self):
        self.assertEqual(inversions('0?0??0'), 22)

    def test_jjliFNJInqeztzm(self):
        self.assertEqual(inversions('??111'), 1)

    def test_LuMBkMGKlmbwkuw(self):
        self.assertEqual(inversions('00?11?'), 5)

    def test_UXLhslznNGoSzsN(self):
        self.assertEqual(inversions('01011'), 1)

    def test_ahEnCaIeEigZNpm(self):
        self.assertEqual(inversions('1???'), 18)

    def test_iakAxjPoQgnfcWL(self):
        self.assertEqual(inversions('01101'), 2)

    def test_MAvAMOcWdRAoqmN(self):
        self.assertEqual(inversions('?1?1'), 3)

    def test_lCRgFULnBLyaebk(self):
        self.assertEqual(inversions('100?0'), 8)

    def test_zIlBlOTrhyydQdG(self):
        self.assertEqual(inversions('0?0??'), 10)

    def test_TiEjBlOAPkzsvWU(self):
        self.assertEqual(inversions('0?100'), 6)

    def test_QdUfGmqQujyMfMM(self):
        self.assertEqual(inversions('??0?0'), 26)

    def test_KQaPAFWmVDHsihI(self):
        self.assertEqual(inversions('?10110'), 10)

    def test_WroHnTovlQDFkaD(self):
        self.assertEqual(inversions('?011'), 1)

    def test_G_CRYzFMKXGzzgM(self):
        self.assertEqual(inversions('00???0'), 18)

    def test_wfFKZifyexOZ_Vu(self):
        self.assertEqual(inversions('0110'), 2)

    def test_TobrqDbUhmDKobD(self):
        self.assertEqual(inversions('??00'), 9)

    def test_KDHRIMVVWUurbon(self):
        self.assertEqual(inversions('0?00'), 2)

    def test_OyJhYOANmGxKvyh(self):
        self.assertEqual(inversions('11111'), 0)

    def test_UgQr_ohJcoBGchx(self):
        self.assertEqual(inversions('0110'), 2)

    def test_ZaEBcSwplOuJuSu(self):
        self.assertEqual(inversions('?01?'), 5)

    def test_rlTBkXiVvDWuU_b(self):
        self.assertEqual(inversions('001?00'), 7)

    def test_jRaOPUkMXSwUPsE(self):
        self.assertEqual(inversions('?01?0'), 13)

    def test_tLysVuAYQCUVbzC(self):
        self.assertEqual(inversions('01??1'), 5)

    def test_htRtwmRTkKAjUGK(self):
        self.assertEqual(inversions('00?11'), 0)

    def test_KqpFKnastVcDLkA(self):
        self.assertEqual(inversions('10?1'), 3)

    def test_RYLRODKMAIrT_Zk(self):
        self.assertEqual(inversions('1010'), 3)

    def test_iBrlwJVeF_TaJmv(self):
        self.assertEqual(inversions('11010?'), 13)

    def test_objS_OOEumXZbRU(self):
        self.assertEqual(inversions('?011'), 1)

    def test_WGqBmB_HtHFcTbV(self):
        self.assertEqual(inversions('1???'), 18)

    def test_m_PVGcedeWyEnXE(self):
        self.assertEqual(inversions('0001'), 0)

    def test_bfCULxPXkwrhGEu(self):
        self.assertEqual(inversions('?101'), 3)

    def test_frxaTPuqsCliNAD(self):
        self.assertEqual(inversions('00?1'), 0)

    def test_PrSyvauRuZTAdOM(self):
        self.assertEqual(inversions('1?1110'), 10)

    def test_qayCubuIZqvX_tc(self):
        self.assertEqual(inversions('??0100'), 21)

    def test_ONHNuDdrlbGMsfD(self):
        self.assertEqual(inversions('1?1000'), 16)

    def test_De_MoeZObDtOwrf(self):
        self.assertEqual(inversions('0101'), 1)

    def test_mNwPMmXzFyKtRhD(self):
        self.assertEqual(inversions('010?1'), 3)

    def test_AWTYAYqLhKhmwfM(self):
        self.assertEqual(inversions('?0?1?1'), 14)

    def test_hNIGdPDGMWUkbJw(self):
        self.assertEqual(inversions('?01?1'), 5)

    def test_VBaBXjZDfGXkYCp(self):
        self.assertEqual(inversions('00?0?1'), 3)

    def test_txJXtCBdDpsBgee(self):
        self.assertEqual(inversions('??101?'), 30)

    def test_LLaYgHagVPOnFYE(self):
        self.assertEqual(inversions('1?10'), 6)

    def test_AddUgdiTAXzdbDh(self):
        self.assertEqual(inversions('0??0'), 5)
    def test_lIhxGyedGOArTRD(self):
        self.assertEqual(inversions('??10??1001'), 200)

    def test_bLTtAVtBszgVpeR(self):
        self.assertEqual(inversions('1??0000?01?0110'), 392)

    def test_rqJmUZBOlpnCDzT(self):
        self.assertEqual(inversions('11001?001101'), 36)

    def test_iJqlDdgoTmCednp(self):
        self.assertEqual(inversions('0???0011101?'), 176)

    def test_VjdSbqLbkpdvppE(self):
        self.assertEqual(inversions('0?1101??0'), 86)

    def test_cRTMSdgFmmcjHpM(self):
        self.assertEqual(inversions('??111011?01111'), 110)

    def test_cYgiqohURpYmwPj(self):
        self.assertEqual(inversions('0??110111110?'), 122)

    def test_yNKKJeOmFCHDjku(self):
        self.assertEqual(inversions('011011010?'), 27)

    def test_SpAy_RWbHjmVxet(self):
        self.assertEqual(inversions('1?0?001?01???0'), 1616)

    def test_vefPIWBTDrDwq_l(self):
        self.assertEqual(inversions('011101?011001'), 45)

    def test__scBERhGwQLfrND(self):
        self.assertEqual(inversions('110?0???'), 160)

    def test_otXQSBxSovbSXdr(self):
        self.assertEqual(inversions('11?1111'), 2)

    def test_QWHDMK_FxsRyeQx(self):
        self.assertEqual(inversions('00100000???1?0'), 208)

    def test_VGNlwiRdQRJRnEK(self):
        self.assertEqual(inversions('0?10??????111'), 1248)

    def test_JpQCFyLKwbbdnmO(self):
        self.assertEqual(inversions('?00?0??'), 56)

    def test_fdElGLHqUQNOMNP(self):
        self.assertEqual(inversions('?11?0???010'), 624)

    def test_UCIZThWTbWocKAw(self):
        self.assertEqual(inversions('1?0?01??1'), 128)

    def test_iRItrZhJQImPwqq(self):
        self.assertEqual(inversions('111????10'), 216)

    def test_mi_uXYvCUxUToNx(self):
        self.assertEqual(inversions('??0?0?0??0010'), 1168)

    def test_iztuOGpeCezvEtD(self):
        self.assertEqual(inversions('0?10?01?0?101?'), 608)

    def test__xaUuqIUZaOhQFx(self):
        self.assertEqual(inversions('10110?11100?'), 87)

    def test_FGsZfxAVAfBFyIl(self):
        self.assertEqual(inversions('00?00???'), 40)

    def test_wepaFwgcyOVeJtw(self):
        self.assertEqual(inversions('10?1???00?1000'), 1040)

    def test_WwhsQAgEPnNEpsg(self):
        self.assertEqual(inversions('1?1???0'), 144)

    def test_OEGhUTtnxPqqiov(self):
        self.assertEqual(inversions('1?111100?'), 57)

    def test_VBTEtMwHvbcoZpi(self):
        self.assertEqual(inversions('0?01011??1??'), 368)

    def test_ODhUDhwrpVRkVvh(self):
        self.assertEqual(inversions('?1??0?10?100'), 720)

    def test_NrwDOGwaUJSSnkj(self):
        self.assertEqual(inversions('?11?0101111'), 33)

    def test_QHg_tnwGfeRHnYI(self):
        self.assertEqual(inversions('0?1001?'), 17)

    def test_ExLxLjtUXDIaSqQ(self):
        self.assertEqual(inversions('?001?00011'), 31)

    def test_cnlMtBxDVEBnqnw(self):
        self.assertEqual(inversions('00??0011??0?0'), 512)

    def test_wuwTIKwexKQUMnO(self):
        self.assertEqual(inversions('?1010000'), 23)

    def test_MOurMeA_FWUkdpe(self):
        self.assertEqual(inversions('1??111?0?001'), 384)

    def test_ihXtVYVbbxP_LBp(self):
        self.assertEqual(inversions('01010110'), 7)

    def test_UQARWlyDlOrZNGo(self):
        self.assertEqual(inversions('01110??0???0?'), 1616)

    def test_BEcjiCRGWWInMwh(self):
        self.assertEqual(inversions('?0110?11'), 17)

    def test__zwVxvYFFKliVL_(self):
        self.assertEqual(inversions('??0010??10?'), 400)

    def test_QOzwjZpXehtSVkD(self):
        self.assertEqual(inversions('0000?10'), 3)

    def test_yFjcYOVuUpGwmeB(self):
        self.assertEqual(inversions('10?10001?0??0'), 384)

    def test_TwtBmbCfhzTwSll(self):
        self.assertEqual(inversions('?011?1011'), 23)

    def test_ocuCpwGPZwEEGGt(self):
        self.assertEqual(inversions('0?0???101?11110'), 496)

    def test_Awjvei_VzEliWeq(self):
        self.assertEqual(inversions('10?01?1'), 17)

    def test_IhUvxF_wYxFCYCm(self):
        self.assertEqual(inversions('?0111000'), 22)

    def test_PpmVJXtliQAhVJP(self):
        self.assertEqual(inversions('11?11?1??'), 152)

    def test_WdwrrEPgEWjWULD(self):
        self.assertEqual(inversions('?001?0??10?0?'), 1200)

    def test_phiggfThXo_xiSI(self):
        self.assertEqual(inversions('1????100'), 184)

    def test_TTqXWWhzFDLA_Pu(self):
        self.assertEqual(inversions('111??10'), 33)

    def test_QvqgStkLaZlbabQ(self):
        self.assertEqual(inversions('010?010110'), 20)

    def test_mWJxPvptrIUCcnQ(self):
        self.assertEqual(inversions('?1??0010?0?1'), 576)

    def test__osZvEeMZkDNCjV(self):
        self.assertEqual(inversions('101???????'), 1696)

    def test_TKtRgABOuwNcUZU(self):
        self.assertEqual(inversions('01?11??0'), 70)

    def test_lvQuaFUirLtVsDV(self):
        self.assertEqual(inversions('11100?1000'), 42)

    def test_exUPeaHFiCj_kq_(self):
        self.assertEqual(inversions('1?0?0??10'), 176)

    def test_bpgSlWEQZzmsAUl(self):
        self.assertEqual(inversions('11?11??111'), 46)

    def test_zwhSZxbnFKvosFg(self):
        self.assertEqual(inversions('0??0?10000??0'), 576)

    def test_qRFGKRhpnk_KRgk(self):
        self.assertEqual(inversions('0?0???0'), 64)

    def test_GBHsdWXukqCorgu(self):
        self.assertEqual(inversions('?11?11000?0'), 194)

    def test_tysBlbHFHafDBQb(self):
        self.assertEqual(inversions('111?1?1?10?00?'), 1216)

    def test_PhiuwAABcIYhPtw(self):
        self.assertEqual(inversions('0?011?1?010'), 110)

    def test_zkUiauuYhZSasLR(self):
        self.assertEqual(inversions('0?10??0?0010?10'), 784)

    def test_dtAZOATpvLzsZpF(self):
        self.assertEqual(inversions('?0?1??0'), 96)

    def test_UBMqQfsWVzguBMx(self):
        self.assertEqual(inversions('00?11??1??10001'), 864)

    def test_EYLDiIAonxkvnQY(self):
        self.assertEqual(inversions('1?01?10001100?'), 242)

    def test_KKBXsdPdLhpJFgy(self):
        self.assertEqual(inversions('10?1110?10?'), 138)

    def test_ZsTFvlYCfAfbKgy(self):
        self.assertEqual(inversions('1?0?1??111??1?0'), 3488)

    def test_wHAsyrnuTZc_ztM(self):
        self.assertEqual(inversions('001??0?1100???'), 1328)

    def test_jERnzMsFbkJzvRK(self):
        self.assertEqual(inversions('001??10'), 17)

    def test_zOMoZLFqPCejvzj(self):
        self.assertEqual(inversions('?111000'), 21)

    def test_rQaxxWwWapScUTg(self):
        self.assertEqual(inversions('10101?10110001'), 57)

    def test_iLDItDqApyJUByn(self):
        self.assertEqual(inversions('?1?01?100'), 106)

    def test_RwPiHLPUCYtrzaF(self):
        self.assertEqual(inversions('01010010'), 8)

    def test_DsTDVlKAmjWMdUD(self):
        self.assertEqual(inversions('?0000100?100111'), 47)

    def test_sGVTonMbLWCUiNf(self):
        self.assertEqual(inversions('?10?110011'), 41)

    def test_bWMfnXopTttmdlz(self):
        self.assertEqual(inversions('00?1?000?1'), 62)

    def test_EQLMlqfKhGLoODz(self):
        self.assertEqual(inversions('0???1011100'), 114)

    def test_iCoMqgzyAKcqTAM(self):
        self.assertEqual(inversions('101????00?000?1'), 2064)

    def test_uNqnMGGHVmKggxi(self):
        self.assertEqual(inversions('01111?001?'), 55)

    def test_cgKjao_NSSfHXml(self):
        self.assertEqual(inversions('000?0011??00??'), 464)

    def test_WIYFvDdjJNzu_DV(self):
        self.assertEqual(inversions('1?1?00001'), 55)

    def test_muyNuJKLFPVKBPc(self):
        self.assertEqual(inversions('???000?00?'), 352)

    def test_RpfculOwyGBxcyB(self):
        self.assertEqual(inversions('1?00?1001'), 41)

    def test_TYkgQg_KrqKAJTD(self):
        self.assertEqual(inversions('0110?111010100?'), 135)

    def test_PawHVVPyleYYDrJ(self):
        self.assertEqual(inversions('0?1001?0?'), 70)

    def test_lbAGWcpfnSmkzog(self):
        self.assertEqual(inversions('111100???1?'), 288)

    def test_WthqZUTnUAmv_zM(self):
        self.assertEqual(inversions('110?000'), 21)

    def test_xdRojLfMpkfsKCS(self):
        self.assertEqual(inversions('0110??0110?'), 118)

    def test_HEbCMPB_EmqJabZ(self):
        self.assertEqual(inversions('?11?110?'), 70)

    def test_lETWsOcFNhECQuf(self):
        self.assertEqual(inversions('11101?1010100'), 64)

    def test_poCvKYvLqV_GfNH(self):
        self.assertEqual(inversions('?0?0?11?001001'), 352)

    def test_ZEMgSUQdyMWxetT(self):
        self.assertEqual(inversions('??0?00?11101'), 168)

    def test_EAXJUORnsYopEXV(self):
        self.assertEqual(inversions('00000111?10'), 12)

    def test_HI_FMMdjbAuRcWi(self):
        self.assertEqual(inversions('?0011111??10010'), 242)

    def test_LrhfnBHIXzLCzuZ(self):
        self.assertEqual(inversions('???000101'), 62)

    def test_nkiAyeImYZBqm_r(self):
        self.assertEqual(inversions('0011000010?0'), 32)

    def test_cwZCTvvtoBIyCyK(self):
        self.assertEqual(inversions('???11??'), 144)

    def test_FOsEmXRZByCseej(self):
        self.assertEqual(inversions('1001??00'), 41)

    def test_saVdIsRyylG_Ybp(self):
        self.assertEqual(inversions('00100?00?'), 25)

    def test_soxLejqiNkQBhAs(self):
        self.assertEqual(inversions('1011???'), 50)

    def test_GOlgTGJBkYmUqRq(self):
        self.assertEqual(inversions('1?101?0?1001000'), 330)

    def test_kALQsiQVfYbAtUW(self):
        self.assertEqual(inversions('??0010000'), 41)

    def test_wvpdjDlWXCOJmvv(self):
        self.assertEqual(inversions('00100?01110?1'), 43)

    def test_KcopinN_HOwOlDS(self):
        self.assertEqual(inversions('011101?0'), 19)

    def test_xlGjszLvopNfjMM(self):
        self.assertEqual(inversions('0?1?0??0??0?0'), 2784)

    def test_SlpSqHxNWUmYEaf(self):
        self.assertEqual(inversions('1????1101?'), 368)

    def test_IkwfkDQxVFm_DRR(self):
        self.assertEqual(inversions('?001?1011?'), 58)

    def test_eUiUHFbxZRKolkb(self):
        self.assertEqual(inversions('?0??0?010111??1'), 944)

    def test_QQUzqsdEiezWwag(self):
        self.assertEqual(inversions('0111?1?0'), 35)

    def test_PzutFLvscMYnEJo(self):
        self.assertEqual(inversions('1?100110?'), 49)

    def test_koLEegbbUS_uslt(self):
        self.assertEqual(inversions('10?10??1?0?'), 528)

    def test_pGvYdGPLkYgAJyp(self):
        self.assertEqual(inversions('0?1??1000'), 98)

    def test_keTJUraRoJSrnzx(self):
        self.assertEqual(inversions('1?0????'), 208)

    def test_zjOBIpeK_lnKpGD(self):
        self.assertEqual(inversions('?11?10?011???11'), 1424)

    def test_BfZkgxWZPvpnTPW(self):
        self.assertEqual(inversions('010?1??10??0'), 608)

    def test_uOVWKjBtAtUFQzU(self):
        self.assertEqual(inversions('?10?001?0?11???'), 2912)

    def test_qbcaAFNoDcXBrre(self):
        self.assertEqual(inversions('??1??011'), 88)

    def test_VkyMXYeTIfUbwEJ(self):
        self.assertEqual(inversions('1??0???'), 224)

    def test_kwfpbIdSCzPkJEo(self):
        self.assertEqual(inversions('???110110'), 78)

    def test_GgPKIFPClxumPvG(self):
        self.assertEqual(inversions('100?0?010?1'), 90)

    def test_rUmeHnkzjKQKqHW(self):
        self.assertEqual(inversions('?0??0??11'), 144)

    def test_mWGrnbmfGSSusvO(self):
        self.assertEqual(inversions('?10?1?1110'), 82)

    def test_rAARjRejiElIBqE(self):
        self.assertEqual(inversions('11?00?1?1??0'), 688)

    def test_ovbMMVuoyAVzMgI(self):
        self.assertEqual(inversions('??01001'), 21)

    def test_cUkAiZXBxxjme_e(self):
        self.assertEqual(inversions('?11???00?1'), 464)

    def test_eXOd_EDDxGyVfjJ(self):
        self.assertEqual(inversions('01?00110'), 14)

    def test_TfhtDgfFLM_OWeh(self):
        self.assertEqual(inversions('0??1?0110?00?'), 736)

    def test_SmyGFAnsAdtzeAs(self):
        self.assertEqual(inversions('00001001??001?1'), 98)

    def test_PWTpKuCrHLmTNfk(self):
        self.assertEqual(inversions('100??0?10?000'), 376)

    def test__HoEMuVFXXCCbae(self):
        self.assertEqual(inversions('???00?0010?01?'), 1200)

    def test_xlMwGJnRyWGDEFN(self):
        self.assertEqual(inversions('11?11?1111??101'), 376)

    def test_nuBzxiFtMIl_PxG(self):
        self.assertEqual(inversions('01?1?0111001?'), 162)

    def test_etAlkLLagDwwCjZ(self):
        self.assertEqual(inversions('?111??1??0'), 512)

    def test_nxZoDrZSZROwExO(self):
        self.assertEqual(inversions('?01??11?00100'), 424)

    def test_uQsLcPYXbwUoXJr(self):
        self.assertEqual(inversions('000010101?01?01'), 61)

    def test_JiKEbXdLSywHOZg(self):
        self.assertEqual(inversions('11?0110000?1?1'), 214)

    def test_ZdkwCqJZEleS_C_(self):
        self.assertEqual(inversions('1?0?0?1001?'), 240)

    def test_eqUwSkAKikBef_L(self):
        self.assertEqual(inversions('0?1?0?0?11?0?1'), 1168)

    def test_nEvcxQOYOtpbpaJ(self):
        self.assertEqual(inversions('??1??0?000100'), 848)

    def test_Q_xGmunYxJmnnof(self):
        self.assertEqual(inversions('110??10?01?00?0'), 1248)

    def test_udRRljN_RaEJPuz(self):
        self.assertEqual(inversions('1100??1??0?1'), 576)

    def test_opQcGolEAKQxNeN(self):
        self.assertEqual(inversions('000101??'), 13)

    def test_hrRzRlyjwxBnSnu(self):
        self.assertEqual(inversions('?000?10?1???'), 688)

    def test_cnMutPKGZbqTgqm(self):
        self.assertEqual(inversions('0?1?0??100?'), 480)

    def test_gVPGExHc_WclHGZ(self):
        self.assertEqual(inversions('1111001?010?'), 103)

    def test_tmuGqPbMRnBblrF(self):
        self.assertEqual(inversions('?1101?0?'), 82)

    def test_bZTDdteQYCMLxIk(self):
        self.assertEqual(inversions('1000???110??1?'), 1136)

    def test_rxReqfrCSXFvwVB(self):
        self.assertEqual(inversions('?0100?100010?00'), 226)

    def test_MAIvrwHuw_kdUEp(self):
        self.assertEqual(inversions('?10?010'), 29)

    def test_VHjTqWfpXNYQDzA(self):
        self.assertEqual(inversions('0100?000?11'), 31)

    def test_CYkfSXMaPAKffTB(self):
        self.assertEqual(inversions('0?0?1?0001'), 74)

    def test_vVOWkUVxgPkVxij(self):
        self.assertEqual(inversions('?000111?10110'), 61)

    def test_MYRmXpgkhPnAjGU(self):
        self.assertEqual(inversions('??01?001?1'), 144)

    def test_GrMpssStHMejCIH(self):
        self.assertEqual(inversions('10???0?11??0'), 1168)

    def test_EGxNNbjRGWNtxtH(self):
        self.assertEqual(inversions('01?100111??0?0'), 448)

    def test_ewwCnfjQIGDZaPM(self):
        self.assertEqual(inversions('0110?0110?0000'), 129)

    def test_MWyztCWaNiXzLQq(self):
        self.assertEqual(inversions('0010?011?0?001'), 158)

    def test_PsOmjsNyxHWNaQP(self):
        self.assertEqual(inversions('0100??0??001?1?'), 1168)

    def test_PQyYqqbRqrEIDLq(self):
        self.assertEqual(inversions('1?00?1010??1'), 248)

    def test_utJftgccjCjdkzG(self):
        self.assertEqual(inversions('111?1??110111??'), 784)

    def test_Jk_tqksARmjPHlj(self):
        self.assertEqual(inversions('1???1?0110000?0'), 1328)

    def test_YFvXJuIDipUrRuT(self):
        self.assertEqual(inversions('1101?101'), 16)

    def test_FlsHqBhtIEzKffV(self):
        self.assertEqual(inversions('?111000?1101'), 73)

    def test_oMQQmaicLVSDnPw(self):
        self.assertEqual(inversions('10??101?111'), 58)

    def test_ihhXdMMVJobrpRE(self):
        self.assertEqual(inversions('0?1???10?1?00?0'), 4256)

    def test_WCqhuccuqyVTRgH(self):
        self.assertEqual(inversions('?0100000?0?110?'), 296)

    def test_sjmpX_PZUiNZbTT(self):
        self.assertEqual(inversions('011010?0?0010?'), 218)

    def test_AdmHLUeq_SldUYC(self):
        self.assertEqual(inversions('1????00000??011'), 1648)

    def test_GazMkYJwaPKw_DY(self):
        self.assertEqual(inversions('0110100?0?1'), 59)

    def test_aqnEbafTUDMVikS(self):
        self.assertEqual(inversions('010???1111?101'), 232)

    def test_XIHHruKBNqwDZyz(self):
        self.assertEqual(inversions('0?11?1?0?1'), 160)

    def test_FDaYShGtbLnbVcG(self):
        self.assertEqual(inversions('1101?1??11'), 66)

    def test_VvPAf_MERlSeGZY(self):
        self.assertEqual(inversions('10?1100?010?11?'), 408)

    def test_IiYLAslkhiX_NYP(self):
        self.assertEqual(inversions('1?10????10?110?'), 3808)

    def test_Kp_vndYeWNHJK_y(self):
        self.assertEqual(inversions('110010?110??0'), 210)

    def test__kJgkblNbHUPUPc(self):
        self.assertEqual(inversions('1??001?'), 54)

    def test_TZoaVYwzUoJxxYS(self):
        self.assertEqual(inversions('?10?000'), 33)

    def test_azawqWWUdnmmspH(self):
        self.assertEqual(inversions('0??101??0'), 152)

    def test_miHaAukPoOotgXr(self):
        self.assertEqual(inversions('???0??00?011'), 848)

    def test_QZpSjLSuILy_qdr(self):
        self.assertEqual(inversions('1111011?1'), 14)

    def test_JdQytrlLHwNyXWf(self):
        self.assertEqual(inversions('1?1?0?11?011100'), 528)

    def test_ckAxTylmJEvQTtC(self):
        self.assertEqual(inversions('00?10?11'), 9)

    def test_gLcALOtlNHczJlD(self):
        self.assertEqual(inversions('100001?01?'), 37)

    def test_OaiFTzGWw_shVbi(self):
        self.assertEqual(inversions('0100?0?01001'), 51)

    def test_BjOuqbTEwdUZXSO(self):
        self.assertEqual(inversions('00??01111000?0'), 194)

    def test_ktli_DWbSPkVIus(self):
        self.assertEqual(inversions('111?00000?0000?'), 310)

    def test_NxtMzN_mbZyuB_P(self):
        self.assertEqual(inversions('0?000?0??0?01?'), 720)

    def test_PAvXGCwPuLkuVQw(self):
        self.assertEqual(inversions('01?0111001?10?1'), 194)

    def test_eLDCmAHzCxazAqJ(self):
        self.assertEqual(inversions('111???00?'), 264)

    def test_ilhrpdpdnhoGwph(self):
        self.assertEqual(inversions('01100?1'), 10)

    def test_ZxPtXYHkHzdfYiS(self):
        self.assertEqual(inversions('01??0????11?0?'), 5504)

    def test_UkteBJuWRqruCHa(self):
        self.assertEqual(inversions('111??00'), 45)

    def test_tmisRdNGdYVEKns(self):
        self.assertEqual(inversions('11?????'), 240)

    def test_zWHefnGKbmWNQhb(self):
        self.assertEqual(inversions('?0?011????'), 592)

    def test_QhjvJnKhCFfHrgN(self):
        self.assertEqual(inversions('?101?01??0000'), 480)

    def test_waxzjlJvAfskPTh(self):
        self.assertEqual(inversions('?1?1??1?11?'), 656)

    def test_V_BWRhcONbMUHYl(self):
        self.assertEqual(inversions('0000?1110100'), 25)

    def test_hxSGXHmjpxQqUsx(self):
        self.assertEqual(inversions('?1??1?0???'), 1824)

    def test_ogZRjEvDdhJIAoV(self):
        self.assertEqual(inversions('10?111101??011'), 170)

    def test_rNtokXXUpnBezFS(self):
        self.assertEqual(inversions('010?010?'), 27)

    def test_fyWsnfGqbklGksB(self):
        self.assertEqual(inversions('0101???101'), 74)

    def test_lAnxLKXJBbPtPiu(self):
        self.assertEqual(inversions('00000011?100010'), 32)

    def test_ErmUEaBOfXkIvRY(self):
        self.assertEqual(inversions('?01?01011?1001?0?1??10?11??101000?0000?1001001?111?11?0?10??1011?'), 259129344)

    def test_uxsUjaYKWiwYwIo(self):
        self.assertEqual(inversions('1?10?100110??1101?11?1111??1111011??01?0010??0??011?1011?1?0'), 121307136)

    def test_G_DHAqNDZinZZsT(self):
        self.assertEqual(inversions('00110110?011?01??0?0110?1?00111??00??110??1110?01?1110?0?00010?0?0'), 313917440)

    def test_hsXctVAhFRXPCEm(self):
        self.assertEqual(inversions('101010?1?1?111?101010?1?0?11?1011?1?0101??101?0?1?0?010???1?11?00?'), 505048050)

if __name__ == "__main__":
    unittest.main()