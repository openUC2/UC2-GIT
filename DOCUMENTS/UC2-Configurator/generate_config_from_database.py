# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 07:23:47 2020

@author: bene
"""
# install pandas: pip install pandas, pip install xlrd
import string
import json as json
import os

import xlrd

from UC2_classes import *

# check if files exists
stlfolder = '/Users/bene/Dropbox/Dokumente/Promotion/PROJECTS/UC2-GIT/CAD/RAW/STL/'
filesnonexist = []
NAME_CUBE_EMPTY = 'ASSEMBLY_CUBE_empty'
github_prefx = 'UC2_'
# This file converts the UC2 modules/parts database into a JSON-file ready for the 
# Online UC2 Selector 

sheetname = 'v3' #'Complete overview' # change it to your sheet name
ucs_database_filename = 'UC2_ReadyToUse_Boxes_Modules_Parts.xlsx' # change it to the name of your excel file

#%% Define entries in Database
alphabet=string.ascii_lowercase

my_root = '/Users/bene/Dropbox/Dokumente/Promotion/PROJECTS/UC2-GIT' # save json.config files inside..
    
is_debug = False
# need to be lower case! 
col_first_app = 'k' # chr(ord('K'))
col_last_app = 'v'
col_all_app = range(alphabet.find(col_first_app), alphabet.find(col_last_app))

row_app_name = 2
row_app_imagelink = 4
row_app_githublink = 3
row_app_briefdescription = 5
row_app_price = 7


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

# 0.) find empty cube
# search for empty cube since it's only a reference in each assemlby:
# we need to replace it..dirty. Sorry. 
all_modules_indices = [i_module for i_module, x in enumerate(worksheet.col(col_assembly_index)) if type(x.value)==float]
all_modules = []
my_empty_cube_index_start = - 1
for row_module in (all_modules_indices):
    module_name = worksheet.cell(row_module, col_assembly_index+1).value

    if my_empty_cube_index_start>0:
        # this is the next module..very dirty hack..
        my_empty_cube_index_end = row_module
        break
        
    # the empty module is not well defined..
    if module_name == NAME_CUBE_EMPTY:
        my_empty_cube_index_start = row_module+1
        print("is empty cube: " + str(module_name == NAME_CUBE_EMPTY) + " Name: "+module_name)
        


        
# 1.) find all Assemblies 
i_module = 0
for row_module in (all_modules_indices):
    #% row_module=6; i_module=0 # debug
    module_name = worksheet.cell(row_module, col_assembly_index+1).value
    if(module_name==""):
        print('bla')
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
        is_add_empty_cube = part_name==NAME_CUBE_EMPTY
        
        if is_add_empty_cube:
            # we need to replace the reference link of the empty cube with the 
            # parts of the cube
            for i_part in range(my_empty_cube_index_start,my_empty_cube_index_end):
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
                
                # addpart to module
                mymodule.addpart(mypart)

                if(is_debug): mymodule.print()

        else:
            part_name = worksheet.cell(i_part, col_assembly_module_part_name).value
            print(part_name)
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
                

            # addpart to module
            mymodule.addpart(mypart)
            if(is_debug): mymodule.print()
        
        if part_isprintable and not os.path.isfile(stlfolder+github_prefx+part_name+".stl"):
            filesnonexist.append(part_name)

        
    # add all modules to the list
    all_modules.append(mymodule)
    print("Reading....: " + mymodule.name)

    # just an iterator 
    i_module+=1



# first iterate over all applications from K...V
#for i_application in col_all_app:

'''
DEBUG: We want to have only one application to see if it works

We also want to build a json file directly! 
'''

#%%
# export Assemblies to JSON in /root/APPLICATIONS
# Hierachy:
#   Application    
#   |
#   --->Modules
#       |
#       Module 1 ---> Parts ----> Part 1
#                          |
#                          |----> Part 2



for i_application in range(10,100):# range(10,100):

    # read application properties
    if i_application >= worksheet.ncols: break
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

    # create json from class and fill it with stuff
    my_application_json = json.loads(json.dumps(my_application.__dict__, default=lambda o: '<not serializable>'))

    
    # now we need to fuse applications and modules
    # 1.) - we need to go through each module and check how many times we need that 
    module_iterator = 0
    
    for i_module in all_modules_indices:
        my_cellvalue = worksheet.cell(i_module, i_application).value
        if my_cellvalue == '': break # scan for last value in cell
        n_modules = int(my_cellvalue)


        
        # 2.) - if this module is part of the application, add it! 
        if(is_debug): print('adding module '+str(i_module)+'  '+str(n_modules)+'-times')
        for i_add in range(n_modules):
            my_module = all_modules[module_iterator]
            
            my_application.addmodule(my_module) # make sure to add n-modules   
            my_application_json['modules'].append(json.loads(json.dumps(my_module.__dict__, default=lambda o: '<not serializable>')))
            
            # add all parts
            n_parts = len(my_application_json['modules'][-1]['partslist'])
            my_partslist = []
            for i_part in range(n_parts):
                my_partslist.append(my_application.modules[-1].__dict__['partslist'][i_part].__dict__)

            my_application_json['modules'][-1]['partslist']=json.loads(json.dumps(my_partslist))     
                
        # just some iterator
        module_iterator += 1            
        
    # 3.) Test if this works 
    my_application.print()
   
    # 4.) Save this! 
    if my_application.is_box: 
        # boxes have a different location
        my_approot = '/TheBOX'
    else:
        my_approot = '/APPLICATIONS'
        
    my_appprefix = '/'
    my_appnpath = application_name
    

    my_jsonpath = my_root+my_approot+my_appprefix+my_appnpath
    
    if(is_debug): print('should save to: '+my_jsonpath)

    with open(my_jsonpath+'/config.json', "w") as j:
        json.dump(my_application_json, j, indent=4)
    print("config written!\n\n")
    
#%%
# export Modules to JSON in /root/CAD
# Hierachy:
#   --->Modules
#       |
#       Module 1 ---> Parts ----> Part 1
#                          |
#                          |----> Part 2


for i_module in range(len(all_modules)):

    # read module
    my_module = all_modules[i_module]
    
    # add all parts
    n_parts = len(my_module.partslist)
    
    # convert list to json object and replace parts since they are not serialisizbel asdlkfj
    my_module_json = json.loads(json.dumps(my_module.__dict__, default=lambda o: '<not serializable>'))
    
    my_partslist = []
    for i_part in range(n_parts):
        my_partslist.append(my_module.partslist[i_part].__dict__)

    # add all parts to the module again.
    my_module_json['partslist'] = json.loads(json.dumps(my_partslist))
    
    
    # 4.) Save this! 
    my_cadroot = '/CAD'
    my_cadprefix = '/'
    my_cadpath = os.path.split(my_module.githublink)[-1]
    my_jsonpath = my_root+my_cadroot+my_cadprefix+my_cadpath
    print('should save to: '+my_jsonpath)
    
    # Write out file to the module folder    
    with open(my_jsonpath+'/config.json', "w") as j:
        json.dump(my_module_json, j, indent=4)
    print("config written!\n\n")

workbook.release_resources()
del workbook


# PRINT MISSING FILES
for i in filesnonexist:
    print(i+" is missing")
