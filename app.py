from xml.dom import minidom 
import os 


root = minidom.Document() 

xml = root.createElement('databaseChangeLog')
xml.setAttribute("xmlns","http://www.liquibase.org/xml/ns/dbchangelog")
xml.setAttribute("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
xml.setAttribute("xmlns:pro","http://www.liquibase.org/xml/ns/pro")
xml.setAttribute("xsi:schemaLocation","http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-latest.xsd http://www.liquibase.org/xml/ns/pro http://www.liquibase.org/xml/ns/pro/liquibase-pro-latest.xsd ")
root.appendChild(xml) 

def create_changeSet(xml,id,author,label="",context=""):
	chset=root.createElement('changeSet')
	chset.setAttribute("id",id)
	chset.setAttribute("author",author)
	xml.appendChild(chset)
	return chset

def create_sqlFile(chset,path):
	sqlfile=root.createElement('sqlFile')
	sqlfile.setAttribute("path",path)
	chset.appendChild(sqlfile)
      

def get_relative_file_paths(root_folder):
    id=1
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            relative_path = os.path.relpath(os.path.join(root_folder,dirpath, filename), root_folder)
            changeset=create_changeSet(xml,str(id),"vaishnavi")
            id=id+1
            create_sqlFile(changeset,relative_path)


root_folder = 'Release 1'
get_relative_file_paths(root_folder)
	

xml_str = root.toprettyxml(indent ="\t") 

save_path_file = "root_changelog_file.xml"

with open(save_path_file, "w") as f: 
	f.write(xml_str) 
