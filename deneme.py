import os

projectMainDirs = {
    # projectName:  [seriFolderName,      tdaFolderName]
    "GO CHARLIE":   ["GO",                  "GO"],
    "GO DELTA2":    ["GO_DELTA_2",          "GO_DELTA2"],
    "GY":           ["GY",                  "GY_GB_GT_GZ"],
}

projects = list(projectMainDirs.keys())
print(projects)
projectSelection = "GO DELTA2"

projectName = projectSelection[:2]
seriFolderName = projectMainDirs[projectSelection][0]
tdaFolderName = projectMainDirs[projectSelection][1]

brands = os.listdir("\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\")
print(brands)
brandSelection = "GRUNDIG"

pidNumber = "100000001"

fileServerPaths = {
    # projectName: [swFileServerPath,
    #               oemFileServerPath,
    #               factoryCusdataFileServerPath,
    #               customerCusdataFileServerPath,
    #               pidFileServerPath]
    "GO CHARLIE": ["\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\"+ projectName +"_upgrade_image_no_tvcertificate.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\"+ projectName +"_upgrade_image_oem.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\"+ projectName +"_upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\"+ projectName +"_upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\PROJECT_ID_YUKLEME\\"+ projectName +"_upgrade_image_project_id_"+ pidNumber +".pkg"],
    
    "GO DELTA2": ["\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\"+ projectName +"_upgrade_image_no_tvcertificate.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\"+projectName + "_upgrade_image_oem.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\"+ projectName +"_upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\"+ projectName +"_upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\PROJECT_ID_YUKLEME\\"+ projectName +"_upgrade_image_project_id_"+ pidNumber +".pkg"],

    "GY": ["\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\upgrade_image_no_tvcertificate.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\upgrade_image_oem.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\YAZILIM_YUKLEME\\"+ tdaFolderName +"\\USBDEN_YUKLEME\\BIRINCI_USB\\upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\OEM_YUKLEME\\"+brandSelection+"\\upgrade_image_cusdata.pkg",
                   "\\\\arcei34v\\SOFTWARE\\SERI\\"+ seriFolderName +"\\PROJECT_ID\\upgrade_image_project_id_"+ pidNumber +".pkg"]
}

# create swFileServerDir
swFileServerPath = fileServerPaths[projectSelection][0]
oemFileServerPath = fileServerPaths[projectSelection][1]
factoryCusdataFileServerPath = fileServerPaths[projectSelection][2]
customerCusdataFileServerPath = fileServerPaths[projectSelection][3]
pidFileServerPath = fileServerPaths[projectSelection][4]

if not os.path.exists(swFileServerPath):
    print("swFileServerPath not found")
if not os.path.exists(oemFileServerPath):
    print("oemFileServerPath not found")
if not os.path.exists(factoryCusdataFileServerPath):
    print("factoryCusdataFileServerPath not found")
if not os.path.exists(customerCusdataFileServerPath):
    print("customerCusdataFileServerPath not found")
if not os.path.exists(pidFileServerPath):
    print("pidFileServerPath not found")

print(f"projectName: {projectName}\nswFileServerPath: {swFileServerPath}\noemFileServerPath: {oemFileServerPath}\nfactoryCusdataFileServerPath: {factoryCusdataFileServerPath}\ncustomerCusdataFileServerPath: {customerCusdataFileServerPath}\npidFileServerPath: {pidFileServerPath}") 
