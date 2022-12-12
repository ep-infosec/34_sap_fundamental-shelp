# SPDX-FileCopyrightText: 2014 SAP SE Srdjan Boskovic <srdjan.boskovic@sap.com>
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pyshlp import *
from abapsystems import *

c = get_connection(I64)

vih = valueInput(c)

#
# I64 CC_VBELN
#


def test_CC_VBELN():
    r = vih.get_shelp_descriptor("SH CC_VBELN")

    sel = [["ERNAM", "I", "BT", "H", "I"], ["VKORG", "I", "EQ", "3000", ""]]

    r = vih.search("SH VMVAA", sel)

    assert r["headers"] == [
        [u"BSTKD", u"Purchase order no.", 35],
        [u"VKORG", u"SOrg.", 4],
        [u"KUNNR", u"Sold-to pt", 10],
        [u"VTWEG", u"DChl", 2],
        [u"SPART", u"Dv", 2],
        [u"VKBUR", u"SOff.", 4],
        [u"VKGRP", u"SGrp", 3],
        [u"ERNAM", u"Created by", 12],
        [u"AUART", u"SaTy", 4],
        [u"BSTDK", u"PO date", 8],
        [u"TRVOG", u"TrG", 1],
        [u"VBELN", u"Document", 10],
        [u"POSNR", u"Item", 6],
    ]

    assert r["shlpoutput"] == u"VBELN"

    assert r["search_result"] == [
        {
            u"AUART": u"OR",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"7837",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"2192",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"OR",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"7829",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"2273",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"AT",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"60000049",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"22843",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"OR",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"7832",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"24384",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"AT",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"60000048",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"2827",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"AT",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"60000051",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"2929",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"AT",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"60000054",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HEYDT",
            u"BSTKD": u"8227",
            u"KUNNR": u"3000",
        },
        {
            u"AUART": u"OR",
            u"BSTDK": u"00.00.0000",
            u"VBELN": u"7831",
            u"POSNR": u"000000",
            u"SPART": u"00",
            u"VKGRP": u"311",
            u"VKORG": u"3000",
            u"VTWEG": u"10",
            u"VKBUR": u"3010",
            u"TRVOG": u"0",
            u"ERNAM": u"HARRISON",
            u"BSTKD": u"CJH",
            u"KUNNR": u"3000",
        },
    ]

    assert r["maxrows_exceeded"] == ""


def test_userparams():
    user_params = vih.get_user_params()
    assert [
        {u"PARID": u"8AP", u"PARTXT": u"FI-CA: Application in Contract Accounting", u"PARVA": u"S"},
        {u"PARID": u"AAT", u"PARTXT": u"Order type", u"PARVA": u"ZUII"},
        {u"PARID": u"CVR", u"PARTXT": u"CATS: Variant for time recording", u"PARVA": u"UHRCO001"},
        {u"PARID": u"KAR", u"PARTXT": u"Class type", u"PARVA": u""},
        {u"PARID": u"LGN", u"PARTXT": u"Warehouse number", u"PARVA": u"089"},
        {u"PARID": u"LGT", u"PARTXT": u"Storage type", u"PARVA": u"102"},
        {
            u"PARID": u"MANF_SETTINGS",
            u"PARTXT": u"Personal Settings for App. Request Master Data Maintenance",
            u"PARVA": u"1ZY S",
        },
        {u"PARID": u"POP", u"PARTXT": u"Plan Version (PD)", u"PARVA": u"01"},
        {u"PARID": u"RMA", u"PARTXT": u"Reference material", u"PARVA": u""},
        {
            u"PARID": u"SCL",
            u"PARTXT": u"Upper and lower case in source code: 'X' = lower, ' ' =upper",
            u"PARVA": u"G",
        },
        {
            u"PARID": u"SP01_WARN",
            u"PARTXT": u"Threshold Value for Number of Lines in Display",
            u"PARVA": u"0000002000",
        },
        {u"PARID": u"SPA", u"PARTXT": u"DIVISION", u"PARVA": u"00"},
        {u"PARID": u"VAG", u"PARTXT": u"SD: Sold-to party", u"PARVA": u"D_CUST_INT"},
        {u"PARID": u"VKO", u"PARTXT": u"Sales organization", u"PARVA": u"3000"},
        {u"PARID": u"VST", u"PARTXT": u"Shipping point", u"PARVA": u"3000"},
        {u"PARID": u"VTW", u"PARTXT": u"Distribution channel", u"PARVA": u"10"},
        {
            u"PARID": u"WLC",
            u"PARTXT": u"Workflow: User-specific settings",
            u"PARVA": u"X   X  XX   X 0000",
        },
    ] == user_params


def test_not_found():
    sel = [["ERNAM", "I", "EQ", "@", ""], ["VKORG", "I", "EQ", "SRDJ", ""]]

    r = vih.search("SH VMVAA", sel)
    assert r["search_result"] == []
    assert r["headers"] == []


def test_VMVAA_title():
    assert u"Sales document according to customer PO number" == vih.get_title("SH VMVAA")


def test_VMVAA_scrlenmax():
    assert 20 == vih._ElementaryHelp["SH VMVAA"]["SCRLENMAX"]


def test_VMVAA_params():
    params = vih.get_help_params("SH VMVAA")

    expected_params = [
        {
            u"F4AVAILABL": u"",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"CHAR35",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"01",
            u"FIELDTEXT": u"Customer PO number as matchcode field",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"Purchase order no.",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 1,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"",
            u"LENG": 35,
            u"OUTPUTLEN": 35,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"BSTKD",
            u"SIGN": u"",
            u"FIELDNAME": u"BSTKD",
            "DEFAULTVAL": u"",
            u"OFFSET": 6,
            u"ROLLNAME": u"BSTKD_M",
            "SHLPSELPOS": u"01",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"PO Number",
            u"SCRTEXT_L": u"Purchase order no.",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 70,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 35,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Pur. Order",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            u"DOMNAME": u"VKORG",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"02",
            u"FIELDTEXT": u"Sales Organization",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVKO",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"SOrg.",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 2,
            "PARVA": u"3000",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VKO",
            u"LENG": 4,
            u"OUTPUTLEN": 4,
            "TOPSHLPNAM": u"CC_VBELN",
            u"LFIELDNAME": u"VKORG",
            u"SIGN": u"",
            u"FIELDNAME": u"VKORG",
            "DEFAULTVAL": u"VKO",
            u"OFFSET": 76,
            u"ROLLNAME": u"VKORG",
            "SHLPSELPOS": u"02",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sales Org.",
            u"SCRTEXT_L": u"Sales Organization",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 8,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 5,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Sales org.",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"KUNNR",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"03",
            u"FIELDTEXT": u"Sold-to party",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"KNA1",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"ALPHA",
            u"REPTEXT": u"Sold-to pt",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 3,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VAG",
            u"LENG": 10,
            u"OUTPUTLEN": 10,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"KUNNR",
            u"SIGN": u"",
            u"FIELDNAME": u"KUNNR",
            "DEFAULTVAL": u"",
            u"OFFSET": 84,
            u"ROLLNAME": u"KUNAG",
            "SHLPSELPOS": u"03",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sold-to party",
            u"SCRTEXT_L": u"Sold-to party",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 20,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 10,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Sold-to pt",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"VTWEG",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"04",
            u"FIELDTEXT": u"Distribution Channel",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVKOV",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"DChl",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 4,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VTW",
            u"LENG": 2,
            u"OUTPUTLEN": 2,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"VTWEG",
            u"SIGN": u"",
            u"FIELDNAME": u"VTWEG",
            "DEFAULTVAL": u"",
            u"OFFSET": 104,
            u"ROLLNAME": u"VTWEG",
            "SHLPSELPOS": u"04",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Distr. Channel",
            u"SCRTEXT_L": u"Distribution Channel",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 4,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 4,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Distr. Chl",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"SPART",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"05",
            u"FIELDTEXT": u"Division",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVTA",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"Dv",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 5,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"SPA",
            u"LENG": 2,
            u"OUTPUTLEN": 2,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"SPART",
            u"SIGN": u"",
            u"FIELDNAME": u"SPART",
            "DEFAULTVAL": u"",
            u"OFFSET": 108,
            u"ROLLNAME": u"SPART",
            "SHLPSELPOS": u"05",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Division",
            u"SCRTEXT_L": u"Division",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 4,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 2,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Division",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"VKBUR",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"06",
            u"FIELDTEXT": u"Sales Office",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVKBZ",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"SOff.",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 6,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VKB",
            u"LENG": 4,
            u"OUTPUTLEN": 4,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"VKBUR",
            u"SIGN": u"",
            u"FIELDNAME": u"VKBUR",
            "DEFAULTVAL": u"",
            u"OFFSET": 112,
            u"ROLLNAME": u"VKBUR",
            "SHLPSELPOS": u"06",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sales Office",
            u"SCRTEXT_L": u"Sales Office",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 8,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 5,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Sales Off.",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"VKGRP",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"07",
            u"FIELDTEXT": u"Sales Group",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVBVK",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"SGrp",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 7,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VKG",
            u"LENG": 3,
            u"OUTPUTLEN": 3,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"VKGRP",
            u"SIGN": u"",
            u"FIELDNAME": u"VKGRP",
            "DEFAULTVAL": u"",
            u"OFFSET": 120,
            u"ROLLNAME": u"VKGRP",
            "SHLPSELPOS": u"07",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sales Group",
            u"SCRTEXT_L": u"Sales Group",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 6,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 4,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Sales Grp",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"USNAM",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"08",
            u"FIELDTEXT": u"Name of Person who Created the Object",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"Created by",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 8,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"",
            u"LENG": 12,
            u"OUTPUTLEN": 12,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"ERNAM",
            u"SIGN": u"",
            u"FIELDNAME": u"ERNAM",
            "DEFAULTVAL": u"",
            u"OFFSET": 126,
            u"ROLLNAME": u"ERNAM",
            "SHLPSELPOS": u"08",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Created by",
            u"SCRTEXT_L": u"Created by",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 24,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 12,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Created",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"AUART",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"09",
            u"FIELDTEXT": u"Sales Document Type",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"TVAK",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"AUART",
            u"REPTEXT": u"SaTy",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 9,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"AAT",
            u"LENG": 4,
            u"OUTPUTLEN": 4,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"AUART",
            u"SIGN": u"",
            u"FIELDNAME": u"AUART",
            "DEFAULTVAL": u"",
            u"OFFSET": 150,
            u"ROLLNAME": u"AUART",
            "SHLPSELPOS": u"09",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sales Doc. Type",
            u"SCRTEXT_L": u"Sales Document Type",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 8,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 4,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"SalesDocTy",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"DATUM",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"10",
            u"FIELDTEXT": u"Customer purchase order date",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"",
            u"DATATYPE": u"DATS",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"PO date",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 10,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"",
            u"LENG": 8,
            u"OUTPUTLEN": 10,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"BSTDK",
            u"SIGN": u"",
            u"FIELDNAME": u"BSTDK",
            "DEFAULTVAL": u"",
            u"OFFSET": 158,
            u"ROLLNAME": u"BSTDK",
            "SHLPSELPOS": u"10",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"PO date",
            u"SCRTEXT_L": u"Purchase order date",
            u"NOFORKEY": u"",
            u"INTTYPE": u"D",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 16,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"X",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 10,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"PO date",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"TRVOG",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"11",
            u"FIELDTEXT": u"Transaction group",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"",
            u"DATATYPE": u"CHAR",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"X",
            u"CONVEXIT": u"",
            u"REPTEXT": u"TrG",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 11,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"VTV",
            u"LENG": 1,
            u"OUTPUTLEN": 1,
            "TOPSHLPNAM": u"CC_VBELN",
            u"LFIELDNAME": u"TRVOG",
            u"SIGN": u"",
            u"FIELDNAME": u"TRVOG",
            "DEFAULTVAL": u"VTV",
            u"OFFSET": 174,
            u"ROLLNAME": u"TRVOG",
            "SHLPSELPOS": u"11",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Transact.group",
            u"SCRTEXT_L": u"Transaction group",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 2,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 3,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Trans.Grp",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"X",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"POSNR",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"13",
            u"FIELDTEXT": u"Item number of the SD document",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"VBUP",
            u"DATATYPE": u"NUMC",
            u"MASK": u"",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"",
            u"REPTEXT": u"Item",
            u"REFTABLE": u"",
            u"PRECFIELD": u"M_VMVAA",
            u"POSITION": 12,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"",
            u"LENG": 6,
            u"OUTPUTLEN": 6,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"POSNR",
            u"SIGN": u"",
            u"FIELDNAME": u"POSNR",
            "DEFAULTVAL": u"",
            u"OFFSET": 176,
            u"ROLLNAME": u"POSNR",
            "SHLPSELPOS": u"13",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Item",
            u"SCRTEXT_L": u"Item (SD)",
            u"NOFORKEY": u"",
            u"INTTYPE": u"N",
            u"KEYFLAG": u"X",
            u"SCRLEN1": 10,
            u"INTLEN": 12,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 6,
            u"DECIMALS": 0,
            u"COMPTYPE": u"E",
            u"SCRTEXT_S": u"Item",
            u"BIDICTRLC": u"",
        },
        {
            u"F4AVAILABL": u"",
            u"MASKLEN": u"0000",
            "PARTXT": "",
            u"DOMNAME": u"VBELN",
            u"REFFIELD": u"",
            "SHLPLISPOS": u"12",
            u"FIELDTEXT": u"Sales and Distribution Document Number",
            u"TABNAME": u"M_VMVAA",
            "SHLPOUTPUT": u"X",
            u"SCRLEN2": 15,
            "TOPSHLPFLD": u"",
            u"LOWERCASE": u"",
            u"CHECKTABLE": u"",
            u"DATATYPE": u"CHAR",
            u"MASK": u"  X",
            u"MAC": u"",
            u"NOAUTHCH": u"",
            u"VALEXI": u"",
            u"CONVEXIT": u"ALPHA",
            u"REPTEXT": u"Document",
            u"REFTABLE": u"",
            u"PRECFIELD": u"VBELN",
            u"POSITION": 13,
            "PARVA": "",
            u"LANGU": u"E",
            u"DYNPFLD": u"X",
            u"MEMORYID": u"AUN",
            u"LENG": 10,
            u"OUTPUTLEN": 10,
            "TOPSHLPNAM": u"",
            u"LFIELDNAME": u"",
            u"SIGN": u"",
            u"FIELDNAME": u"VBELN",
            "DEFAULTVAL": u"",
            u"OFFSET": 188,
            u"ROLLNAME": u"VBELN",
            "SHLPSELPOS": u"12",
            u"GENKEY": u"",
            u"SCRTEXT_M": u"Sales Document",
            u"SCRTEXT_L": u"Sales Document",
            u"NOFORKEY": u"",
            u"INTTYPE": u"C",
            u"KEYFLAG": u"",
            u"SCRLEN1": 10,
            u"INTLEN": 20,
            u"SCRLEN3": 20,
            u"AUTHORID": u"",
            u"LOGFLAG": u"",
            u"LTRFLDDIS": u"",
            u"HEADLEN": 10,
            u"DECIMALS": 0,
            u"COMPTYPE": u"D",
            u"SCRTEXT_S": u"SD Doc.",
            u"BIDICTRLC": u"",
        },
    ]

    assert len(params) == len(expected_params)

    for i in range(0, len(params)):
        assert params[i] == expected_params[i]


def test_VMVAA_defaults():
    defaults = vih.get_search_defaults("SH VMVAA")
    assert defaults == [{u"VKORG": u"VKO"}, {u"TRVOG": u"VTV"}]


def test_VMVAA_result_headers():
    result_headers = vih.get_search_result_headers("SH VMVAA")
    assert result_headers == {
        u"AUART": [u"SaTy", 4],
        u"BSTDK": [u"PO date", 8],
        u"BSTKD": [u"Purchase order no.", 35],
        u"ERNAM": [u"Created by", 12],
        u"KUNNR": [u"Sold-to pt", 10],
        u"POSNR": [u"Item", 6],
        u"SPART": [u"Dv", 2],
        u"TRVOG": [u"TrG", 1],
        u"VBELN": [u"Document", 10],
        u"VKBUR": [u"SOff.", 4],
        u"VKGRP": [u"SGrp", 3],
        u"VKORG": [u"SOrg.", 4],
        u"VTWEG": [u"DChl", 2],
    }


#
# SH H_T001
#


def test_multiple_SHLPOUTPUT():
    shlpname = "SH H_T001"
    # assert 'BUKRS' == vih.get_shelp_descriptor(shlpname)['elementary_helps'][shlpname]['SHLPOUTPUT']
    assert [u"BUKRS", u"BUTXT", u"ORT01", u"WAERS"] == vih.get_shelp_descriptor(shlpname)[
        "elementary_helps"
    ][shlpname]["ALLOUTPUTS"]

    shlpname = "SH H_T001W"
    # assert 'WERKS' == vih.get_shelp_descriptor(shlpname)['elementary_helps'][shlpname]['SHLPOUTPUT']
    assert ["NAME1", "WERKS"] == vih.get_shelp_descriptor(shlpname)["elementary_helps"][shlpname][
        "ALLOUTPUTS"
    ]


"""
def test_KREDA_title():
    vih.get_shelp_descriptor('KREDA')
    assert u'Vendors (General)' == vih.get_title('KREDA')

def test_KREDA_scrlenmax():
    assert 20 == r.Help['KREDA']['SCRLENMAX']

def test_KREDA_params():
    Params = r.get_help_params('KREDA')
    assert 5 == len(Params)
    assert 'SORTL' == Params [0]['FIELDNAME']
    assert 'PSTLZ' == Params [1]['FIELDNAME']
    assert 'MCOD3' == Params [2]['FIELDNAME']
    assert 'MCOD1' == Params [3]['FIELDNAME']
    assert 'LIFNR' == Params [4]['FIELDNAME']

def test_KREDA_defaults():
    defaults = r.get_search_defaults('KREDA')
    assert defaults == []

def test_KREDA_search_headers():
    headers = r.get_search_result_headers('KREDA')

    assert headers['LIFNR'] == [u'Vendor', 10]
    assert headers['MCOD1'] == [u'Name 1', 25]
    assert headers['MCOD3'] == [u'City', 25]
    assert headers['PSTLZ'] == [u'PostalCode', 10]
    assert headers['SORTL'] == [u'SearchTerm', 10]

def test_KREDA_search():
    sel = [['PSTLZ', 'I', 'BT', '13', '200000']]

    result = r.search('KREDA', sel, 2)
    search_result = result['search_result']
    headers = result['headers']
    assert 2 == len(search_result)

    assert search_result == [
        {u'LIFNR': u'1234', u'MCOD3': u'BERLIN', u'MCOD1': u'K.F.W. BERLIN', u'SORTL': u'MECH', u'PSTLZ': u'13403'},
        {u'LIFNR': u'1080', u'MCOD3': u'MARSEILLES', u'MCOD1': u'G\xc9N\xc9RALE ELECTRONIQUE SA', u'SORTL': u'SCHULUNG', u'PSTLZ': u'13020'} ]

    assert headers == [
        [u'SORTL', u'SearchTerm', 10],
        [u'PSTLZ', u'PostalCode', 10],
        [u'MCOD3', u'City', 25],
        [u'MCOD1', u'Name 1', 25],
        [u'LIFNR', u'Vendor', 10] ]


def test_KREDA_search_compact():
    [[u'MECH',     u'13403', u'BERLIN',     u'K.F.W. BERLIN',                  u'1234'],
     [u'SCHULUNG', u'13020', u'MARSEILLES', u'G\xc9N\xc9RALE ELECTRONIQUE SA', u'1080']]
"""


#
# tear down
#
