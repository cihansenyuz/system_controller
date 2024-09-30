
'''
TDA klasörü ile Seri klasöründeki isimlendirmeler tutmadığından aşağıdaki dictionary oluşturulmuştur.
Yeni proje geldikçe ve eski projeler öldükçe aşağıdan düzeltmeler yapılmalıdır
'''
projectMainDirs = {
    # projectName:      [seriFolderName,        tdaFolderName]
    "GO CHARLIE 3":     ["GO",                  "GO"],
    "GO DELTA 2":       ["GO_DELTA_2",          "GO_DELTA2"],
    "GO DELTA SE":      ["GO_DELTA_SE",         "GO_DELTA_SE"],
    "GO DELTA SE 2A":   ["GO_DELTASE2A",        "GO_DELTASE2A"],
    "GO ECHO 2":        ["GO_ECHO2",            "GO_ECHO2"],
    "GY":               ["GY",                  "GY_GB_GT_GZ"],
    "GT":               ["GT",                  "GY_GB_GT_GZ"],
    "GB":               ["GB",                  "GY_GB_GT_GZ"],
    "GZ":               ["GZ",                  "GY_GB_GT_GZ"],
    "GX CHARLIE 2":     ["GX",                  "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
    "GX BETA 2":        ["GX_BETA2",            "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
    "GX HOTEL":         ["GX_HOTEL_TV",         "GX_HOTEL_TV"],
    "GX OPTIMUS":       ["GX_OPTIMUS",          "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
    "GX OLED":          ["GX_OLED",             "GX_BETA2_OPTIMUS_CHARLIE_OLED"],
    "AN BETA 2":        ["AN_BETA2",            "AN_BETA2"],
    "AN CHARLIE":       ["AN_CHARLIE",          "AN-OPTIMUS-CHARLIE-CHARM"],
    "AN CHARM":         ["AN_CHARM",            "AN-OPTIMUS-CHARLIE-CHARM"],
    "AN OPTIMUS":       ["AN_OPTIMUS",          "AN-OPTIMUS-CHARLIE-CHARM"],
    }

'''
marka klasörlerinin bulunduğu adres aşağıdaki class'a ait dictonary'de tanımlanmalıdır.
'''
class BrandPaths():
    def __init__(self, OS_SEP, ROOT_DIR, SERI_FOLDER, TDA_FOLDER) -> None:
        self.brandPaths = {
            "GO CHARLIE 3":     ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GO DELTA 2":       ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GO DELTA SE":      ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GO DELTA SE 2A":   ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GO ECHO 2":        ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GY":               ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GT":               ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GB":               ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GZ":               ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GX CHARLIE 2":     ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GX BETA 2":        ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GX HOTEL":         ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GX OPTIMUS":       ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "GX OLED":          ROOT_DIR + SERI_FOLDER + OS_SEP + "OEM_YUKLEME" + OS_SEP,
            "AN BETA 2":        ROOT_DIR + "YAZILIM_YUKLEME" + OS_SEP + TDA_FOLDER + OS_SEP + "USBDEN_YUKLEME",
            "AN CHARLIE":       ROOT_DIR + "YAZILIM_YUKLEME" + OS_SEP + TDA_FOLDER + OS_SEP + "USBDEN_YUKLEME",
            "AN CHARM":         ROOT_DIR + "YAZILIM_YUKLEME" + OS_SEP + TDA_FOLDER + OS_SEP + "USBDEN_YUKLEME",
            "AN OPTIMUS":       ROOT_DIR + "YAZILIM_YUKLEME" + OS_SEP + TDA_FOLDER + OS_SEP + "USBDEN_YUKLEME"
        }