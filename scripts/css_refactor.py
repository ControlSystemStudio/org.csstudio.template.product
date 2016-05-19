import os
import fileinput
from sets import Set
from xml.dom import minidom

# The python script is not complete, please use the bash script css_refactor.sh

g_textToSearch="template"
g_textToReplace="han"
# g_featureToSearch=""
# g_featureToReplace=""


def replaceProjectName(filename, parent_name, name, text_to_replace):
    
    dom=minidom.parse(filename)
    namelist = dom.getElementsByTagName(name)
    for  a in namelist:
        if a.parentNode.nodeName == parent_name :
            print(a.firstChild.data)
            a.firstChild.data =text_to_replace
            print(a.firstChild.data)

    # print dom.toxml()
    print ("")

    
# # replaceProjectName(file0, "project", "artifactId", target_name)
# # replaceProjectName(file1, "parent",  "artifactId", target_name)
# # replaceProjectName(file2, "parent",  "artifactId", target_name)

# def rename_with_path(root, name):
#     old = os.path.join(root,name)
#     new = old.replace(g_textToSearch, g_textToReplace)
#     # print(old, "was renamed to ", new)
#     os.rename(old, new)   
    


                   
# def getXmlFiles(path):
#     fileList = []
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(".xml"):
#                 fileList.append(os.path.join(root,file))
#     return fileList


# ## 1. Rename directories which has the han sub-name
# ## 2. Rename files which have the han sub-name


# renameAll()



# # ## 3. Replace han in all files
# # # xml files

# xmlList = getXmlFiles("./")

# print "------------------------"
# print g_featureToReplace
# print g_featureToSearch
# print "------------------------"

# for xmlfile in xmlList:
# #    print xmlfile
#     id_name = ""
#     product_name = ""
    

#     if "features/pom.xml" in xmlfile:
#         id_name = "parent"
#         product_name = g_textToReplace + "-product"
#         replaceProjectName(xmlfile, id_name, "artifactId", product_name)
#     elif "repository/pom.xml" in xmlfile:
#         id_name = "parent"
#         product_name = g_textToReplace + "-product"
#         replaceProjectName(xmlfile, id_name, "artifactId", product_name)
#     elif "pom.xml" in xmlfile:
#         id_name = "project"
#         product_name =  g_textToReplace + "-product"
#         replaceProjectName(xmlfile, id_name, "artifactId", product_name)

def change_name(root, name):
    old_file_path = os.path.join(root, name)
    new_name      = name.replace(g_textToSearch, g_textToReplace)
    new_file_path = os.path.join(root, new_name)
    os.rename(old_file_path, new_file_path)

if __name__ == '__main__':
    for path, dirs, files in os.walk("./"):
        for f_name in files:
            if g_textToSearch in f_name:
                change_name(path, f_name)
        for d_name in dirs:
            if g_textToSearch in d_name:
                change_name(path, d_name)



# 2
# ./pom.xml,             project,            artifactId, han-product, g_textToReplace-product
# features/pom.xml,      parent,             artifactId, han-product, g_textToReplace-product

# repository/pom.xml,    parent,             artifactId, han-product, g_textToReplace-product
# .project,              projectDescription, name,       han-product, g_textToReplace-product

# features/org.csstudio.g_textToReplace.product.configuration.feature/pom.xml, project, artifactId, org.csstudio.han.product.configuration.feature, org.csstudio.g_textToReplace.product.configuration.feature
# features/org.csstudio.g_textToReplace.product.configuration.feature/.project, projectDescription, name, org.csstudio.han.product.configuration.feature, org.csstudio.g_textToReplace.product.configuration.feature
# features/pom.xml,      modules,            module, org.csstudio.han.product.configuration.feature, org.csstudio.g_textToReplace.product.configuration.feature

target_name = g_textToReplace + "-product"
replaceProjectName("pom.xml", "project", "artifactId", target_name)
