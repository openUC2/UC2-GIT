#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 07:23:47 2020

@author: bene
"""
# install pandas: pip install pandas, pip install xlrd
from pandas import read_excel
import pandas as pd
import string
import xlrd


class uc2_application:
    def __init__(self, name, description, githublink, image, price):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        
        self.modulelist = []
        

    def addmodule(self, module):
        self.modulelist.append(module)

    def print(self):
        print("App Name: " + self.name)
        print("App description: " + self.description)
        print("App githublink: " + self.githublink)
        print("App image: " + self.image)
        print("App Parts: ".join(str(x) for x in ([i.name for i in self.modulelist]))) 

class uc2_module: # also called assembly
    def __init__(self, name, description, githublink, image, price):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        
        self.partslist = []
        
    def addpart(self, part):
        self.partslist.append(part)

    def print(self):
        print("Module Name: " + self.name)
        print("Module description: " + self.description)
        print("Module githublink: " + self.githublink)
        print("Module image: " + self.image)
        print("Module Parts: ".join(str(x) for x in ([i.name for i in self.partslist]))) 


class uc2_part:
    def __init__(self, name, description, githublink, image, price, is_printable, n_parts):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        self.is_printable = is_printable
        self.n_parts = n_parts
        
    def print(self):
        print("App Name: " + self.name)
        print("App description: " + self.description)
        print("App githublink: " + self.githublink)
        print("App image: " + self.image)
        print("App Modules: " + self.Modules.value)        




# This file converts the UC2 modules/parts database into a JSON-file ready for the 
# Online UC2 Selector 

sheetname = 'Complete overview' # change it to your sheet name
ucs_database_filename = 'UC2_ReadyToUse_Boxes_Modules_Parts.xlsx' # change it to the name of your excel file

#%% Define entries in Database
alphabet=string.ascii_lowercase

# need to be lower case! 
col_first_app = 'k' # chr(ord('K'))
col_last_app = 'v'
col_all_app = range(alphabet.find(col_first_app), alphabet.find(col_last_app))

row_app_name = 2
row_app_imagelink = 4
row_app_githublink = 3
row_app_briefdescription = 5
row_app_price = 6


col_assembly_index = alphabet.find('a')
col_assembly =  alphabet.find('b')
col_assembly_module_part_name =  alphabet.find('c')
col_assembly_module_part_isprintable =  alphabet.find('d')
col_assembly_module_part_n =  alphabet.find('e')
col_assembly_module_part_name_githublink =  alphabet.find('f')
col_assembly_module_part_name_price =  alphabet.find('g')

#%%
# open XLXS file
workbook = xlrd.open_workbook(ucs_database_filename)
worksheet = workbook.sheet_by_name(sheetname)

# 1.) find all Assemblies 
all_modules_indices = [i_module for i_module, x in enumerate(worksheet.col(col_assembly_index)) if type(x.value)==float]
all_modules = []
i_module = 0
for row_module in (all_modules_indices):
    #%% row_module=6; i_module=0 # debug
    module_name = worksheet.cell(row_module, col_assembly_index+1).value
    module_githublink = worksheet.cell(row_module+1, col_assembly_index+1).value
    module_price = worksheet.cell(row_module+2, col_assembly_index+1).value
    module_imagelink = ''
    module_description = '' 
    
    # create module
    mymodule = uc2_module(module_name,
               module_description, 
               module_githublink, 
               module_imagelink, 
               module_price)
    

    # collecting parts inside modules and add them to modules
    try:
        all_part_indices = range(row_module+1, all_modules_indices[i_module+1])
    except:
        print('reached end of the list')
        break
            
            
    # 2.) find all parts per Assembly
    for i_part in (all_part_indices):
        part_name = worksheet.cell(i_part, col_assembly_module_part_name).value
        part_isprintable = bool(worksheet.cell(i_part, col_assembly_module_part_isprintable).value)
        part_githublink = worksheet.cell(i_part, col_assembly_module_part_name_githublink).value
        part_price = worksheet.cell(i_part, col_assembly_module_part_name_price).value
        part_imagelink = '' 
        part_description = ''
        part_n_parts = worksheet.cell(i_part, col_assembly_module_part_n).value
        
        # create part
        mypart = uc2_part(part_name, 
                          part_description, 
                          part_githublink, 
                          part_imagelink, 
                          part_price, 
                          part_isprintable, 
                          part_n_parts)
    
        part_name = worksheet.cell(i_part, col_assembly_module_part_name+1).value
        print("Reading Part....: " + mypart.name)


        # addpart to module
        mymodule.addpart(mypart)
        mymodule.print()
        
    # add all modules to the list
    all_modules.append(mymodule)
    print("Reading....: " + mymodule.name)

    # just an iterator 
    i_module+=1



# first iterate over all applications from K...V
#for i_application in col_all_app:

#%% DEBUG: We want to have only one application to see if it works
if(True):
    i_application=10
    
    # read application properties
    application_name = worksheet.cell(row_app_name-1, i_application).value
    application_imagelink = worksheet.cell(row_app_imagelink-1, i_application).value
    application_description = worksheet.cell(row_app_briefdescription-1, i_application).value
    application_githublink = worksheet.cell(row_app_githublink-1, i_application).value
    application_price = 0
    
    #create application
    my_application = uc2_application(application_name, 
                                     application_description, 
                                     application_githublink, 
                                     application_imagelink, 
                                     application_price)
    
    # now we need to fuse applications and modules
    # 1.) - we need to go through each module and check how many times we need that 
    module_iterator = 0
    try:
        for i_module in all_modules_indices:
            n_add = int(worksheet.cell(i_module, i_application).value)
         
            # 2.) - if this module is part of the application, add it! 
            for i_add in range(n_add):
                my_application.addmodule(all_modules[module_iterator]) # make sure to add n-modules     
                
            # just some iterator
            module_iterator += 1            
    except:
        print('Error, but we are probably done...')
        
    # 3.) Test if this works 
    my_application.print()



# %% Now transform it to compatible JSON code using code from :
# https://github.com/AlecVercruysse/UC2-GIT/blob/master/APPLICATIONS/APP_Incubator_Microscope/config.json
# def get_modules(dirname):
#     """ Basically look through the STL names to try to find a unique match in the CAD subfolder. just an estimate for now, this needs to be gone through manually"""
#     modules = []
#     try:
#         fs = os.scandir(dirname + "/STL")
#     except FileNotFoundError: # some incomplete applications
#         fs = []
#         print("file not found :( no module completion")
#     for f in fs:
#         matches = glob.glob("../CAD/ASSEMBLY_*/STL/" + f.name)
#         if len(matches) == 1:
#             modname = re.search(r"ASSEMBLY.*?(?=/)", matches[0]).group(0)
#             modules.append({
#                 "name":modname,
#                 "fixedOptions": {}
#             })
#     modules_no_duplicates = []
#     [modules_no_duplicates.append(x) for x in modules if x not in modules_no_duplicates]
#     return modules_no_duplicates

    
# sentence = re.compile(r"[A-Z][a-z]+.*\.")
# dirs = [x for x in os.scandir() if "APP" in x.name]
# for d in dirs:
#     print(d.name)
#     with open(glob.glob(d.name + "/*.md")[0], "r") as f:
#         f.readline()
#         x = ""
#         while not sentence.match(x): x = f.readline()
#         desc = x.replace("This is the repository for ", "").replace("The stl-files can be found in the folder [STL](./STL).", "").replace("\n", "") # quick and dirty estimate.
#         if "STL" in desc: desc = "TODO: This, and the readme, needs more documentation."
#         #print(desc)
#         with open(d.name + "/config.json", "w") as j:
#             data = {
#                 "type":"application",
#                 "description" : desc,
#                 "modules": get_modules(d.name)
#                 }
#             json.dump(data, j, indent=2)