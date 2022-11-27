from flask import Flask, render_template, redirect, url_for,g, request
#from flask_bootstrap import Bootstrap
import sqlite3
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

##############################################################################
   #  Development flag, 1 for DEV , 0 for Production
#################################################################################
Dev_Flag=0
if Dev_Flag==1:
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hive.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:/home/tomsenska/mysite/hive.db'


#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Flask/Hive_math/hm4sql/hive.db'
#app.config['SECRET_KEY'] = 'Thisisasecret!'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hive.db'

db=SQLAlchemy(app)
########################  BEEHIVES  TABLE #########################################
class suppliers(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date_created=db.Column(db.String(12),nullable=False)
    country = db.Column(db.String(80), nullable=False)
    supplier_name = db.Column(db.String(200), nullable=False)
    supplier_link = db.Column(db.String(200), nullable=False)
    hive_type = db.Column(db.String(80), nullable=False)
    hive_link = db.Column(db.String(200), unique=True, nullable=False)
    number_frames = db.Column(db.Integer, nullable=False)
    hive_price = db.Column(db.String(10),nullable=False)
    price_date=db.Column(db.String(12),nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    link = db.Column(db.String(30), nullable=False)


########################  BLOG TABLE #########################################
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    tags = db.Column(db.String(200))


# Create table
#  c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

##############################################################################

   #  routes
#################################################################################
################################################################################


#################################################################################
         #  Tests
@app.route('/index2')

def index2():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')



        cursor = conn.cursor()

        cursor.execute('SELECT * FROM suppliers ORDER BY id ')
        suppl=cursor.fetchall()
        conn.close()

    #######################    UK LIST #########################################################
        #declare lists
        UK_INDEX_LIST=[]
        UK_Var=0
        List_of_UK_beehives=[]
        #step 0. declare country UK list ( repeat for every country)

        for row in suppl:
            if "UK" in row:
                List_of_UK_beehives.append(row) #  Country  list with all beehives
    #########################  UK Warre type  #######################################################
        UK_Warre_MIN_List=[]
        Warre_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Warre' in row:

                Warre_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Warre_UK_Data:

            UK_Warre_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Warre_MIN_List)

        #find row with the minimum value
        for row in Warre_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)


    #########################  UK WBC type  #######################################################
        UK_WBC_MIN_List=[]
        WBC_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'WBC' in row:

                WBC_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in WBC_UK_Data:

            UK_WBC_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_WBC_MIN_List)

        #find row with the minimum value
        for row in WBC_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Top Bar type  #######################################################
        UK_Topbar_MIN_List=[]
        Topbar_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Top Bar' in row:

                Topbar_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Topbar_UK_Data:

            UK_Topbar_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Topbar_MIN_List)

        #find row with the minimum value
        for row in Topbar_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Smith  type  #######################################################
        UK_Smith_MIN_List=[]
        Smith_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Smith' in row:

                Smith_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Smith_UK_Data:

            UK_Smith_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Smith_MIN_List)

        #find row with the minimum value
        for row in Smith_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)


    #########################  UK Skep  type  #######################################################
        UK_Skep_MIN_List=[]
        Skep_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Skep' in row:

                Skep_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Skep_UK_Data:

            UK_Skep_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Skep_MIN_List)

        #find row with the minimum value
        for row in Skep_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK National  type  #######################################################
        UK_National_MIN_List=[]
        National_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'National' in row:

                National_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in National_UK_Data:

            UK_National_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_National_MIN_List)

        #find row with the minimum value
        for row in National_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Loghive  type  #######################################################
        UK_Loghive_MIN_List=[]
        Loghive_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Log Hive' in row:

                Loghive_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Loghive_UK_Data:

            UK_Loghive_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Loghive_MIN_List)

        #find row with the minimum value
        for row in Loghive_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Layens  type  #######################################################
        UK_Layens_MIN_List=[]
        Layens_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Layens' in row:

                Layens_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Layens_UK_Data:

            UK_Layens_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Layens_MIN_List)

        #find row with the minimum value
        for row in Layens_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Langstroth  type  #######################################################
        UK_Langstroth_MIN_List=[]
        Langstroth_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Langstroth' in row:

                Langstroth_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Langstroth_UK_Data:

            UK_Langstroth_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Langstroth_MIN_List)

        #find row with the minimum value
        for row in Langstroth_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Drayton  type  #######################################################
        UK_Drayton_MIN_List=[]
        Drayton_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Drayton' in row:

                Drayton_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Drayton_UK_Data:

            UK_Drayton_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Drayton_MIN_List)

        #find row with the minimum value
        for row in Drayton_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)

    #########################  UK Dadant type  #######################################################
        UK_Dadant_MIN_List=[]
        Dadant_UK_Data=[]

        #step 1. declare beehive type's list
        for row in List_of_UK_beehives:
            if 'Dadant' in row:

                Dadant_UK_Data.append(row)

        #step 2. find minimum value in the beehive type's list
        for row in Dadant_UK_Data:

            UK_Dadant_MIN_List.append(row[8])

        #step 3. add minimum value to variable
        UK_Var=min(UK_Dadant_MIN_List)

        #find row with the minimum value
        for row in Dadant_UK_Data:
            if UK_Var in row[8]:
                UK_INDEX_LIST.append(row)





                return render_template('index2.html', UK_INDEX_LIST=UK_INDEX_LIST)






################################################################################




@app.route('/')
def index():
    if Dev_Flag==1:
        conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')




    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers ORDER BY id ')
    suppl=cursor.fetchall()
    conn.close()


#######################    UK LIST #########################################################
    #declare lists
    UK_INDEX_LIST=[]
    UK_Var=0
    List_of_UK_beehives=[]
    #step 0. declare country UK list ( repeat for every country)

    for row in suppl:
        if "UK" in row:
            List_of_UK_beehives.append(row) #  Country  list with all beehives
#########################  UK Warre type  #######################################################
    UK_Warre_MIN_List=[]
    Warre_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Warre' in row:

            Warre_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Warre_UK_Data:

        UK_Warre_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Warre_MIN_List)

    #find row with the minimum value
    for row in Warre_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)


#########################  UK WBC type  #######################################################
    UK_WBC_MIN_List=[]
    WBC_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'WBC' in row:

            WBC_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in WBC_UK_Data:

        UK_WBC_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_WBC_MIN_List)

    #find row with the minimum value
    for row in WBC_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Top Bar type  #######################################################
    UK_Topbar_MIN_List=[]
    Topbar_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Top Bar' in row:

            Topbar_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Topbar_UK_Data:

        UK_Topbar_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Topbar_MIN_List)

    #find row with the minimum value
    for row in Topbar_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Smith  type  #######################################################
    UK_Smith_MIN_List=[]
    Smith_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Smith' in row:

            Smith_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Smith_UK_Data:

        UK_Smith_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Smith_MIN_List)

    #find row with the minimum value
    for row in Smith_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)


#########################  UK Skep  type  #######################################################
    UK_Skep_MIN_List=[]
    Skep_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Skep' in row:

            Skep_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Skep_UK_Data:

        UK_Skep_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Skep_MIN_List)

    #find row with the minimum value
    for row in Skep_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK National  type  #######################################################
    UK_National_MIN_List=[]
    National_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'National' in row:

            National_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in National_UK_Data:

        UK_National_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_National_MIN_List)

    #find row with the minimum value
    for row in National_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Loghive  type  #######################################################
    UK_Loghive_MIN_List=[]
    Loghive_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Log Hive' in row:

            Loghive_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Loghive_UK_Data:

        UK_Loghive_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Loghive_MIN_List)

    #find row with the minimum value
    for row in Loghive_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Layens  type  #######################################################
    UK_Layens_MIN_List=[]
    Layens_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Layens' in row:

            Layens_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Layens_UK_Data:

        UK_Layens_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Layens_MIN_List)

    #find row with the minimum value
    for row in Layens_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Langstroth  type  #######################################################
    UK_Langstroth_MIN_List=[]
    Langstroth_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Langstroth' in row:

            Langstroth_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Langstroth_UK_Data:

        UK_Langstroth_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Langstroth_MIN_List)

    #find row with the minimum value
    for row in Langstroth_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Drayton  type  #######################################################
    UK_Drayton_MIN_List=[]
    Drayton_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Drayton' in row:

            Drayton_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Drayton_UK_Data:

        UK_Drayton_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Drayton_MIN_List)

    #find row with the minimum value
    for row in Drayton_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)

#########################  UK Dadant type  #######################################################
    UK_Dadant_MIN_List=[]
    Dadant_UK_Data=[]

    #step 1. declare beehive type's list
    for row in List_of_UK_beehives:
        if 'Dadant' in row:

            Dadant_UK_Data.append(row)

    #step 2. find minimum value in the beehive type's list
    for row in Dadant_UK_Data:

        UK_Dadant_MIN_List.append(row[8])

    #step 3. add minimum value to variable
    UK_Var=min(UK_Dadant_MIN_List)

    #find row with the minimum value
    for row in Dadant_UK_Data:
        if UK_Var in row[8]:
            UK_INDEX_LIST.append(row)









    return render_template('index.html',UK_INDEX_LIST=UK_INDEX_LIST)
#################################################################################


@app.route('/contact')
def contactpage():
    return render_template("contact.html")
##############################################################################

   # beehive type routes
#################################################################################
################################################################################
@app.route('/warre')
def warre():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')


    cursor = conn.cursor()


    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Warre" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Warre_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Warre_List.append(row)



    conn.close()
    return render_template("hives/warre.html",UK_Warre_List=UK_Warre_List)
#########################################################################################################################

@app.route('/langstroth')
def langstroth():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()


    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Langstroth" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Langstroth_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Langstroth_List.append(row)


    conn.close()
    return render_template("hives/langstroth.html",UK_Langstroth_List=UK_Langstroth_List)


###########################################################################################################""

@app.route('/national')
def national():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="National" ORDER BY id')
    suppl = cursor.fetchall()

    UK_National_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_National_List.append(row)

    conn.close()
    return render_template("hives/national.html",UK_National_List=UK_National_List)

################################################################################################
@app.route('/wbc')
def wbc():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="WBC" ORDER BY id')
    suppl = cursor.fetchall()

    UK_WBC_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_WBC_List.append(row)

    conn.close()
    return render_template("hives/wbc.html",UK_WBC_List=UK_WBC_List)

##################################################################################################""
@app.route('/alltypes')
#have a look at the link later
#https://flask-table.readthedocs.io/en/stable/
def alltypes():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM suppliers WHERE country="UK" ORDER BY id')
    suppl = cursor.fetchall()
    conn.close()

    return render_template("hives/alltypes.html",suppl = suppl)
#############################################################################################################

@app.route('/topbar')
def topbar():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Top Bar" ORDER BY id')
    suppl = cursor.fetchall()

    UK_TopBar_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_TopBar_List.append(row)


    conn.close()

    return render_template("hives/topbar.html",UK_TopBar_List=UK_TopBar_List)


#############################################################################################################

@app.route('/loghive')
def loghive():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Log Hive" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Loghive_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Loghive_List.append(row)

    conn.close()
    return render_template("hives/loghive.html",UK_Loghive_List=UK_Loghive_List)


#############################################################################################################

@app.route('/smith')
def smith():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Smith" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Smith_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Smith_List.append(row)

    conn.close()
    return render_template("hives/smith.html",UK_Smith_List=UK_Smith_List)



#############################################################################################################

@app.route('/layens')
def layens():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Layens" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Layens_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Layens_List.append(row)

    conn.close()
    return render_template("hives/layens.html",UK_Layens_List=UK_Layens_List)

#############################################################################################################

@app.route('/dadant')
def dadant():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Dadant" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Dadant_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Dadant_List.append(row)

    conn.close()
    return render_template("hives/dadant.html",UK_Dadant_List=UK_Dadant_List)


#############################################################################################################

@app.route('/skep')
def skep():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Skep" ORDER BY id')
    suppl = cursor.fetchall()

    UK_Skep_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Skep_List.append(row)

    conn.close()
    return render_template("hives/skep.html",UK_Skep_List=UK_Skep_List)


#############################################################################################################

@app.route('/drayton')
def drayton():
    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM suppliers WHERE hive_type="Drayton" ORDER BY id')
    suppl = cursor.fetchall()



    UK_Drayton_List=[]
    for row in suppl:
        if 'UK' in row[2]:
            UK_Drayton_List.append(row)

    conn.close()
    return render_template("hives/drayton.html",UK_Drayton_List=UK_Drayton_List)

##################################################################################

    #legal / other legal / about
#############################################################################
#############################################################################
@app.route('/tandc')
def tandc():
    return render_template("legal/tandc.html")


@app.route('/legal')
def legal():
    return render_template("legal/legal.html")


@app.route('/privacy')
def privacy():
    return render_template("legal/privacy.html")

@app.route('/cookies')
def cookies():
    return render_template("legal/privacy.html")

@app.route('/about')
def about():
    return render_template("about.html")
##################################################################################
#######################  BLOG ROUTES     #####################################
@app.route('/blog')
def blog():
    #posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()


    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM blogpost ORDER BY date_posted ASC')
    bposts = cursor.fetchall()

    return render_template('blog.html',bposts=bposts)


@app.route('/post/<int:post_id>')
def post(post_id):
    #post = Blogpost.query.filter_by(id=post_id).one()

    if Dev_Flag==1:
            conn = sqlite3.connect('hive.db')
    else:
        conn = sqlite3.connect('/home/tomsenska/mysite/hive.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM blogpost WHERE id=(?)' ,[post_id])
    bpost = cursor.fetchall()




    return render_template('post.html', bpost=bpost)

#@app.route('/add')
#def add():
#    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    tags = request.form['tags']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content,tags=tags, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('blog'))
#######################  END OF  BLOG ROUTES     #####################################
if __name__ == '__main__':
    app.run(debug=True)
