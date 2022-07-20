
ar=list('أبجدهوزحطيكلمنسعفصقرشتثخذضظغ ')
har=['َ', 'ُ', 'ِ', 'ً', 'ٌ', 'ٍ', 'ّ', 'ْ']
ham= [ 'ء', 'ا']  
taa= ['ت','ة']   
alf= ['إ','أ', 'آ'] 
waw= ['و', 'ؤ']
lam= ['ل','لا','لأ','لإ'] 
yaa=['ي','ى','ئ']        
ar2=list('بجدهوزحطيكلمنسعفصقرشتثخذضظغ')
en=list('abcdefghijklmnopqrstuvwxyz')
num=list('1234567890')

import sqlite3
#from zipfile import ZipFile 
import os;from os import listdir;from os.path import isfile, join
#from shutil import copyfile
#from distutils.dir_util import copy_tree
#import math
#from geopy.distance import geodesic
#import cv2
#from moviepy.editor import *
#import datetime


def hlpl_copy_dir(dir1,dir2):
    copy_tree(dir1,dir2)

def hlpl_copy_file(f1,f2):
    copyfile(f1, f2)

def hlpl_dirs_list(xdir):
    lst=[x[0] for x in os.walk(xdir)]
    return lst
 
def hlpl_create_dir(hlpl_dir):
    if not os.path.exists(hlpl_dir):
       os.makedirs(hlpl_dir)

def hlpl_delete_dir(hlpl_dir):
    if os.path.exists(hlpl_dir):
       os.deletedirs(hlpl_dir)

def hlpl_get_file(xdir,lst,case):
    if case=='txt':
       lst2=[]
       for x in lst:
           if len(x)>4 and x[len(x)-4:len(x)]=='.txt' and isfile(join(xdir, x)): 
              lst2.append(x)
       return lst2[0]
    if case=='hlpl':
       lst2=[]
       for x in lst:
           if len(x)>5 and x[len(x)-5:len(x)]=='.hlpl' and isfile(join(xdir, x)): 
              lst2.append(x)
       return lst2
    if case=='kml':
       lst2=[]
       for x in lst:
           if len(x)>4 and x[len(x)-4:len(x)]=='.kml' and isfile(join(xdir, x)): 
              lst2.append(x)
       return lst2
  
def hlpl_remove_init(lst):
    lst2=[]
    for x in lst:
        if x not in ['__init__.py', '__pycache__']:
           lst2.append(x)
    return lst2           
  
def hlpl_files_list(xdir,case):
    filesnames=listdir(xdir)
    if case=='path':
       pathslist=[f for f in filesnames if isfile(join(xdir, f))]
       return pathslist 
    if case=='name':
       return filesnames
    if case=='resource':
       return hlpl_get_file(xdir,filesnames,'txt')      
    if case=='kml':
       return hlpl_get_file(xdir,filesnames,'kml') 
    if case=='hlpl':
       return hlpl_get_file(xdir,filesnames,'hlpl')
       
def hlpl_remover(st,lst):
    st2=''
    for x in st:
        if x not in lst:
           st2+=x
    return st2
    
 
def hlpl_lst_to_st(lst,s):
    st=''
    for x in lst:
        st+=x+s
    st=st[0:len(st)-len(s)]
    return st


def hlpl_code(letters,st,case):
    st2=''
    if case=='A':
       for x in lettes:
           st2+=st.count(x.upper())+st.count(x.lower())
    if case=='a':
       for x in lettes:
           st2+=st.count(x)
    return st           


t1='[';t2=']';t3=' '
def hlpl_phrase_template(st,lang='en'):
    st2=''
    lst=st.split()
    for x in lst:
        y=hlpl_word_template_en(x)
        st2+=t1+y+t2+t3
    st2=st2[0:len(st2)-1]
    return st2


def hlpl_database_create(filepath,lst):
    conn = sqlite3.connect(filepath) 
    cursor = conn.cursor() 
    for x in lst:
        x1=x[0]
        x2=x[1]
        st=''
        for y in x2:
            st+=y+' TEXT,'
        st=' '+st[0:len(st)-1]
        cursor.execute("CREATE TABLE IF NOT EXISTS "+x1+" ("+st+")")
     

def hlpl_database_drop(filepath,lst):     
    conn = sqlite3.connect(filepath) 
    cursor = conn.cursor() 
    for x in lst:
        cursor.execute("DROP TABLE IF EXISTS "+x+"")    


def hlpl_database_insert(filepath,table,lst1,lst2):
    hlpl_database_create(filepath,[[table,lst1]])
    conn = sqlite3.connect(filepath) 
    cursor = conn.cursor()  
    st1='';st2=''
    for x in lst1:
        st1+=x+','
    st1=st1[0:len(st1)-1]
    for x in lst2:
        st2+=x+','
    st2=st2[0:len(st2)-1] 
    stt="INSERT INTO "+table+"("+st1+") VALUES("+st2+")" 
    cursor.execute(stt)
    conn.commit()    


w1='hlpl_composer_settings.db'
def hlpl_settings_insert(table,st0=' '):
    hlpl_database_drop(w1,[table])
    hlpl_database_insert(w1,table,['i0','st0'],['0',st0])

    

def hlpl_database_import(filepath,table,lst,where):
    lst2=where.split('=');ttt=lst2[0].split()[0]
    lst.append(ttt)
    hlpl_database_create(filepath,[[table,lst]])
    conn = sqlite3.connect(filepath) 
    cursor = conn.cursor()
    st1=''
    for x in lst:
        st1+=x+','
    st1=st1[0:len(st1)-1]
    
    xxx=cursor.execute("SELECT "+st1+" FROM "+table+" WHERE "+where+"") .fetchall()
    return xxx    
    

def hlpl_settings_import(table):
    xxx=hlpl_database_import(w1,table,['st0'],'i0="0"')
    if len(xxx)!=0:
       xxx=xxx[0]
    else:
       xxx=''
    return xxx
    
    
def hlpl_sum_of_2_dct(dct1,dct2):
    dct12=dct1
    lst2=list(dct2.keys())
    for x in lst2:
        dct12[x]=dct2[x]
    return dct12
    
      
            
 
def hlpl_line_data(lst):
            dct={}
            for z in lst:
                z2=z.split('=')
                if len(z2)==2:
                   q1=z2[0].split()[0]
                   q2=z2[1].split()[0] 
                   dct[q1]=q2
            return dct                
         

wx1='longitude1';wx2='longitude2';wx3='latitude1';wx4='latitude2';wx5='atitude1';wx6='atitude2' 
def hlpl_data_path_loader(path):
    fr=open(path,'r',encoding='utf-8').readlines()
    lst1=[]
    lst2=[]
    dct={}
    for i in range(len(fr)):
         x=fr[i]
         if 'HLPL_resource; Type=path;' in x:
            lst1.append(i)
         if '</HLPL_resource>' in x:
            lst2.append(i)
    for j in range(len(lst1)):
        xi=lst1[j];yi=hlpl_next(xi,lst2)
        lst4=fr[xi].split(';')
        dct3=hlpl_line_data(lst4)
        st=dct3[wx1]+'_'+dct3[wx3]+'__'+dct3[wx5]+'___'+dct3[wx2]+'____'+dct3[wx4]+'_____'+dct3[wx6]
        dct2={}
        for k in range(xi+1,yi):
            lst3=fr[k].split(',')
            dct2[k]=hlpl_line_data(lst3)
        dct[st]=dct2
    return dct
            

def hlpl_data_paths_loader(main_dir):
    dirs=hlpl_dirs_list(main_dir);dirs2=[]
    for x in dirs:
        if '__pycache__' not in x and x!=main_dir:
           dirs2.append(x)
    dct={}  
    for x in dirs2:
        file=join(x, 'HLPL_resource.txt')
        dctt=hlpl_data_path_loader(file)
        #dct=hlpl_sum_of_2_dct(dct,dctt)
        dct[x]=dctt
    return dct
 
def hlpl_next(i,lst2):
    k=0
    for j in lst2:
        if j>i:
           k=j
           break
    return k  

wy1='longitude';wy2='latitude';wy3='atitude'
def hlpl_data_view_loader(path):
    fr=open(path,'r',encoding='utf-8').readlines()
    lst1=[]
    lst2=[]
    dct={}
    for i in range(len(fr)):
         x=fr[i]  
         if 'HLPL_resource; Type=view;' in x:
            lst1.append(i)  
         if '</HLPL_resource>' in x:
            lst2.append(i) 
            
    for j in range(len(lst1)):
        xi=lst1[j];yi=hlpl_next(xi,lst2)
        lst4=fr[xi].split(';')
        dct3=hlpl_line_data(lst4)
        st=dct3[wy1]+'_'+dct3[wy2]+'__'+dct3[wy3]
        dct2={}
        for k in range(xi+1,yi):
            lst3=fr[k].split(',')
            dct2[k]=hlpl_line_data(lst3)
        dct[st]=dct2
        
    return dct    
    

def hlpl_data_views_loader(main_dir):
    dirs=hlpl_dirs_list(main_dir);dirs2=[]
    for x in dirs:
        if '__pycache__' not in x and x!=main_dir:
           dirs2.append(x)
    dct={} 
    for x in dirs2: 
        file=join(x, 'HLPL_resource.txt')
        dctt=hlpl_data_view_loader(file)
        dct=hlpl_sum_of_2_dct(dct,dctt)
    return dct



def hlpl_data_map_loader(path):
    fr=open(path,'r',encoding='utf-8').readlines()
    lst1=[]
    lst2=[]
    dct={}
    for i in range(len(fr)):
         x=fr[i]  
         if 'HLPL_resource; Type=map;' in x:
            lst1.append(i)  
         if '</HLPL_resource>' in x:
            lst2.append(i)   
    for j in range(len(lst1)):
        xi=lst1[j];yi=hlpl_next(xi,lst2)
        lst4=fr[xi].split(';')
        dct3=hlpl_line_data(lst4)
        st=dct3[wy1]+'_'+dct3[wy2]
        dct2={}                       
        for k in range(xi+1,yi):
            lst3=fr[k].split(',')
            dct2[k]=hlpl_line_data(lst3)
        dct[st]=dct2
    return dct  


def hlpl_data_maps(dir_maps): 
    dirs=hlpl_dirs_list(dir_maps);dirs2=[]
    for x in dirs:
        if '__pycache__' not in x and x!=dir_maps:
           dirs2.append(x)
    dct={}
    for x in dirs2:  
        file=file=join(x, 'HLPL_resource.txt')
        dctt=hlpl_data_map_loader(file)
        dct=hlpl_sum_of_2_dct(dct,dctt)
    return dct


 

def hlpl_data_view_global(fr,case):
    fr=open(fr,'r',encoding='utf-8').readlines()
    lst1=[]
    lst2=[];dct2={}
    if case=='view':
       for i in range(len(fr)):
         x=fr[i]
         if 'HLPL_resource; Type=view' in x:
            lst1.append(i)
         if '</HLPL_resource>' in x:
            lst2.append(i)
    if case=='path':
       for i in range(len(fr)):
         x=fr[i]
         if 'HLPL_resource; Type=path' in x:
            lst1.append(i)
         if '</HLPL_resource>' in x:
            lst2.append(i)            
    m=0
    for j in range(len(lst1)):
        xi=lst1[j];yi=lst2[j]
        for k in range(xi+1,yi):
            lst3=fr[k].split(',')
            dct2[m]=hlpl_line_data(lst3)
            m+=1
    return dct2 

def hlpl_hide_show(lst1=[],lst2=[]):
    for x in lst1:
        x.show()
    for x in lst2:
        x.hide()   
    
    

def hlpl_chech_uncheck(lst1,lst2):
    for x in lst1:
        x.setChecked(True)     
    for x in lst2:
        x.setChecked(False)          
         
             
  
def get_all_file_paths(directory): 
    file_paths = [] 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
    return file_paths  

    
def hlpl_export_as_zip(directory,zip_name): 
    file_paths = get_all_file_paths(directory) 
    with ZipFile(zip_name,'w') as zip: 
         for file in file_paths: 
             zip.write(file) 
       
  
                 
def hlpl_create_dirs(lst_dirs):
    for x in lst_dirs:
        try:
           os.mkdir(x)          
        except:
           pass        
         

def hlpl_remove_repeated(lst):
    lst2=[]
    for x in lst:
        if x not in lst2:
           lst2.append(x)
    return lst2           

    
def hlpl_spherical_to_cartesian(r,the,phi):
    x=r*math.cos(the)*math.cos(phi);y=r*math.cos(the)*math.sin(phi);z=r*math.sin(the)
    return x,y,z

def hlpl_closest_point_sphere(p0,lst):
    x0,y0,z0=hlpl_spherical_to_cartesian(1,p0[0],p0[1])
    dct={}
    for xx in lst:
        x,y,z=hlpl_spherical_to_cartesian(1,xx[0],xx[1])
        d=(x-x0)**2+(y-y0)**2+(z-z0)**2
        dct[d]=xx
    m=min(list(dct.keys()))
    closest_point=dct[m]
    return closest_point
    


def hlpl_distance_2gps(point1,point2):
    return geodesic(point1, point2).meters


def hlpl_closest_point_plan(p0,lst):
    dct={}
    for xx in lst:
        d=hlpl_distance_2gps(p0,xx)
        dct[d]=xx
    m=min(list(dct.keys()))
    closest_point=dct[m]
    return closest_point


def hlpl_points_between_2gps_data(x1,x2,num):
       lst=[];
       x1=int(x1);
       x2=int(x2);
       num=int(num)
       dx=(x1-x2)/num;yy=x2
       lst.append(x2)
       for i in range(num):
           yy+=dx
           lst.append(yy)  
       return lst           


def hlpl_points_between_2gps(p1,p2,num):
    lo1=p1[0];la1=p1[1];at1=p1[2];lo2=p2[0];la2=p2[1];at2=p2[2];lstlo=[];lstla=[];lstat=[]
    if lo1>=lo2:
       lstlo=hlpl_points_between_2gps_data(lo1,lo2,num)
    if lo2>lo1:
       lstlo=hlpl_points_between_2gps_data(lo2,lo1,num)
    if la1>=la2:
       lstla=hlpl_points_between_2gps_data(la1,la2,num)
    if la2>la1:
       lstla=hlpl_points_between_2gps_data(la2,la1,num)
    if at1>=at2:
       lstat=hlpl_points_between_2gps_data(at1,at2,num)
    if at2>at1:
       lstat=hlpl_points_between_2gps_data(at2,at1,num)
    lst=[]
    for i in range(num+1):
        lst.append([lstlo[i],lstla[i],lstat[i]])
    return lst




def hlpl_getFrame_data(sec,vidcap,count,hlpl_dir):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image=vidcap.read()
    path=join(hlpl_dir,"image"+str(count)+".jpg")
    if hasFrames:
        cv2.imwrite(path, image)     
    return hasFrames,path
        

def hlpl_getFrame(video,dt,hlpl_dir):
    lst=[]
    vidcap=cv2.VideoCapture(video)
    sec=0;count=1
    success=hlpl_getFrame_data(sec,vidcap,count,hlpl_dir)
    while success:
          count=count+1
          sec=sec+dt
          sec=round(sec,2)
          success,path=hlpl_getFrame_data(sec,vidcap,count,hlpl_dir)
          lst.append(path)
    return lst



def hlpl_video_editor(video,case,cut=(0, 1)):
    clip = VideoFileClip(video) 
    if case=='duration':
       return clip.duration 
    if case=='cut':
       clip = clip.subclip(cut[0], cut[1]) 
    if case=='nframes':
       return clip.reader.nframes



def hlpl_closest_in_list(x0,lst):
    dct={}
    for xx in lst:
        d=abs(x0-xx)
        dct[d]=xx
    m=min(list(dct.keys()))
    closest_point=dct[m]
    return closest_point


def hlpl_time_to_number(lst):
    lst2=[]
    for x in lst:
        lst2.append(int(hlpl_remover(x,['.'])))
    return lst2

    
def hlpl_time_to_number_2(time):
    n=int(hlpl_remover(time,['.',':',' ','/']))
    return n


def hlpl_date_time():
    xx=str(datetime.datetime.now())
    st=xx[0:4]+'.'+xx[5:7]+'.'+xx[8:10]+'.'+xx[11:13]+'.'+xx[14:16]+'.'+xx[17:19]+'.'+xx[20:len(xx)]
    return st


def hlpl_angle_period(w):
    x0=2*math.pi
    x1=w/x0;x2=int(x1)
    x3=x1-x2
    return x3


def hlpl_points_between_2angles(w1,w2,num):
    lst=[];w1=int(w1);w2=int(w2);num=int(num)
    Dw=w2-w1;dw=Dw/num
    ww=w1
    for i in range(num+1):
        lst.append(ww)
        ww+=dw
    return lst
    








































1
