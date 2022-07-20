
import configparser
import sys
import os
import hlpl_composer

def get_hlpl_composer__version(case):
    config = configparser.ConfigParser()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'setup.cfg')
    config.read(config_file_path)
    if case=='version':
       return config['hlpl_composer']['version']
    if case=='else':
       return config['hlpl_composer']['version']+'\n'+config['hlpl_composer']['author']+'\n'+config['hlpl_composer']['email']+'\n'+config['hlpl_composer']['url']+'\n'
 
def hlpl_get_name(st):
    if '\\' in st:
       return st.split('\\')[len(st.split('\\'))-1]   
    if '/' in st:
       return st.split('/')[len(st.split('/'))-1]   
    if '\/' in st:
       return st.split('\/')[len(st.split('\/'))-1] 
    
       
def main():
    st=hlpl_get_name(sys.argv[0])
    if st=='version':
        print('\n'+get_hlpl_composer__version('version'))
    if st=='hlpl_composer':
       hlpl_composer.main()
    else:
        print('\n'+get_hlpl_composer__version('else')+'\n'+'hlpl_composer under developement, it will be released next versions of HLPL')