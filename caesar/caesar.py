import string

cipher = "zh zrxog qhyhu pdnh lw wkdw hdvb.. rxu hqfubswlrq lv rqh vwhs dkhdg!livi mw er mrgvihmfpi xlsyklx sj geiwevr alex ai amwl, ai viehmpc fipmizi, erh alex ai syvwipziw xlmro, ai mqekmri sxlivw xlmro epws. ai amwl xli jpek mw jpek{xairxc_xlvii_wxefw_evi_aec_xss_qerc}"
charset = string.ascii_lowercase

def rot_n(n, cipher):
    shifter = string.maketrans(charset, charset[n:] + charset[:n])
    return string.translate(cipher, shifter)

for shift in range(-1, -10, -1):
    print shift
    print rot_n(shift, cipher)
    print ""
