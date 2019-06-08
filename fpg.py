#-----------------------------------------------------------------------------------------------#
#Written by Dimitris Sinanis on 04/12/2017.
# Fake profil generator.
#Python version: 3.7.1 tested.
#-----------------------------------------------------------------------------------------------#
#To run this program correctly, you need to install these two libraries: random, names
#To install a library do the following:
#open terminal and excecute this command: sudo apt-get install *library_name*
#-----------------------------------------------------------------------------------------------#

"====================================The_code_begins_here======================================="
#imports
import random,names

def fake_profile_generator(ul,pc,pl):
    #username_and_password_generator
    list0=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0"]
    list1=["~","!","@","#","$","%","^","&","*","_","+","=","-","<",">","?"]
    list2=list0+list1
    username=""
    password=""
    for i in range(ul):
        username+=str(random.choice(list0))
    for i in range(pl):
        if pc=="Yes" or pc=="yes":
            password+=str(random.choice(list2))
        else:
            password+=str(random.choice(list0))
    #birthday_generator
    day=str(random.randint(1,28))
    month=str(random.randint(1,12))
    year=str(random.randint(1960,2000))# >18 years old.
    birthday=day+"/"+month+"/"+year
    #gene_generator
    list_gene=["male","female"]
    gene=random.choice(list_gene)
    #name_generator
    fn=str(names.get_first_name(gender=gene))
    ln=str(names.get_last_name())
    ###################################################
    print("==============================================")
    print("Username: ",username)
    print("Password: ",password)
    print("Gene: ",gene)
    print("First name: ",fn)
    print("Last name: ",ln)
    print("Birthday: ",birthday)
    print("==============================================")
    rp=input("Register Profile? (yes/no): ")
    if rp=="Yes" or rp=="yes":
        site=str(input("Register on site: "))
        F=open("profiles.txt","a")
        F.write("\nSite:  {}  |||  Username: {} ||| Password:  {}  |||  Gene:  {}  |||  First name:  {}  ||| Last name:  {}  |||  Birthday:  {}".format(site,username,password,gene,fn,ln,birthday))
        F.close()
    return ""


ul=int(input("Username length: "))
pc=input("Password unique characters (yes/no): ")
pl=int(input("Password length: "))           
print(fake_profile_generator(ul,pc,pl))
"==========================================The_end=============================================="
