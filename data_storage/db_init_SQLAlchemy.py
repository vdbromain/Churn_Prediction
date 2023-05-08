from sqlalchemy import Column, Integer, String, CHAR, Float
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import inspect
import pandas as pd

raw_path = 'datas/BankChurners.csv'
cleaned_data_path = "datas/cleaned_data.csv"

df = pd.read_csv(raw_path)
df_cleaned = pd.read_csv(cleaned_data_path)

#Deleting this column
del df_cleaned['Unnamed: 0']
print(df_cleaned.shape)

# Declare the base class
Base = declarative_base()

# Creating the first table of the DB called "Raw_data"
class Raw_data(Base):
    __tablename__ = "raw_data"

    clientnum = Column('CLIENTNUM', Integer, primary_key=True)
    attrition_flag = Column('Attrition_Flag', String, nullable=False)
    customer_age = Column('Customer_Age', Integer, nullable=False)
    #CHAR because it's a unique character and not a string
    gender = Column('Gender', CHAR, nullable=False)
    dependant_count = Column('Dependant_Count', Integer, nullable=False)
    education_level = Column('Education_Level', String, nullable=False)
    marital_status = Column('Marital_Status', String, nullable=False)
    income_category = Column('Income_Category', String, nullable=False)
    card_category = Column('Card_Category', String, nullable=False)
    month_on_book = Column('Month_On_Book', Integer, nullable=False)
    total_relationship_count = Column('Total_Relationship_Count', Integer, nullable=False)
    months_inactive_12_mon = Column('Months_Inactive_12_Mon', Integer, nullable=False)
    contacts_count_12_mon = Column('Contacts_Count_12_Mon', Integer, nullable=False)
    credit_limit = Column('Credit_Limit', Float, nullable=False)
    total_revolving_bal = Column('Total_Revolving_Bal', Integer, nullable=False)
    avg_open_to_buy = Column('Avg_Open_To_Buy', Float, nullable=False)
    total_amt_chng_Q4_Q1 = Column('Total_Amt_Chng_Q4_Q1', Float, nullable=False)
    total_trans_amt = Column('Total_Trans_Amt', Integer, nullable=False)
    total_trans_ct = Column('Total_Trans_Ct', Integer, nullable=False)
    total_ct_chng_Q4_Q1 = Column('Total_Ct_Chng_Q4_Q1', Float, nullable=False)
    avg_utilization_ratio = Column('Avg_Utilization_Ratio', Float, nullable=False)
    NBC1 = Column('Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', Float, nullable=False)
    NBC2 = Column('Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2', Float, nullable=False)
    
    def __init__(self, clientnum : int, attrition_flag : str, customer_age : int, gender : str, dependant_count : int, education_level : str,
                    marital_status : str, income_category : str, card_category : str, month_on_book : int, total_relationshiop_count : int,
                    months_inactive_12_mon : int, contacts_count_12_mon : int, credit_limit : float, total_revolving_bal : int, 
                    avg_open_to_buy : float, total_amt_chng_Q4_Q1 : float, total_trans_amt : int, total_trans_ct : int, total_ct_chng_Q4_Q1 : float,
                    avg_utilization_ratio : float, NBC1 : float, NBC2 : float):
        self.clientnum = clientnum
        self.attrition_flag = attrition_flag
        self.customer_age = customer_age
        self.gender = gender
        self.dependant_count = dependant_count
        self.education_level = education_level
        self.marital_status = marital_status
        self.income_category = income_category
        self.card_category = card_category
        self.month_on_book = month_on_book
        self.total_relationship_count = total_relationshiop_count
        self.months_inactive_12_mon = months_inactive_12_mon
        self.contacts_count_12_mon = contacts_count_12_mon
        self.credit_limit = credit_limit
        self.total_revolving_bal = total_revolving_bal
        self.avg_open_to_buy = avg_open_to_buy
        self.total_amt_chng_Q4_Q1 = total_amt_chng_Q4_Q1
        self.total_trans_amt = total_trans_amt
        self.total_trans_ct = total_trans_ct
        self.total_ct_chng_Q4_Q1 = total_ct_chng_Q4_Q1
        self.avg_utilization_ratio = avg_utilization_ratio
        self.NBC1 = NBC1
        self.NBC2 = NBC2
# Creating the second table of the DB called "Cleaned_data"        
class Cleaned_data(Base):
    __tablename__ = "cleaned_data"

    clientnum = Column('CLIENTNUM', Integer, primary_key=True)
    attrition_flag = Column('Attrition_Flag', String, nullable=False)
    customer_age = Column('Customer_Age', Integer, nullable=False)
    #CHAR because it's a unique character and not a string
    gender = Column('Gender', CHAR, nullable=False)
    dependant_count = Column('Dependant_Count', Integer, nullable=False)
    education_level = Column('Education_Level', String, nullable=False)
    marital_status = Column('Marital_Status', String, nullable=False)
    income_category = Column('Income_Category', String, nullable=False)
    card_category = Column('Card_Category', String, nullable=False)
    month_on_book = Column('Month_On_Book', Integer, nullable=False)
    total_relationship_count = Column('Total_Relationship_Count', Integer, nullable=False)
    months_inactive_12_mon = Column('Months_Inactive_12_Mon', Integer, nullable=False)
    contacts_count_12_mon = Column('Contacts_Count_12_Mon', Integer, nullable=False)
    credit_limit = Column('Credit_Limit', Float, nullable=False)
    total_revolving_bal = Column('Total_Revolving_Bal', Integer, nullable=False)
    total_amt_chng_Q4_Q1 = Column('Total_Amt_Chng_Q4_Q1', Float, nullable=False)
    total_trans_amt = Column('Total_Trans_Amt', Integer, nullable=False)
    total_trans_ct = Column('Total_Trans_Ct', Integer, nullable=False)
    total_ct_chng_Q4_Q1 = Column('Total_Ct_Chng_Q4_Q1', Float, nullable=False)
    avg_utilization_ratio = Column('Avg_Utilization_Ratio', Float, nullable=False)
    
    def __init__(self, clientnum : int, attrition_flag : str, customer_age : int, gender : str, dependant_count : int, education_level : str,
                    marital_status : str, income_category : str, card_category : str, month_on_book : int, total_relationshiop_count : int,
                    months_inactive_12_mon : int, contacts_count_12_mon : int, credit_limit : float, total_revolving_bal : int, 
                    total_amt_chng_Q4_Q1 : float, total_trans_amt : int, total_trans_ct : int, total_ct_chng_Q4_Q1 : float,
                    avg_utilization_ratio : float):
        self.clientnum = clientnum
        self.attrition_flag = attrition_flag
        self.customer_age = customer_age
        self.gender = gender
        self.dependant_count = dependant_count
        self.education_level = education_level
        self.marital_status = marital_status
        self.income_category = income_category
        self.card_category = card_category
        self.month_on_book = month_on_book
        self.total_relationship_count = total_relationshiop_count
        self.months_inactive_12_mon = months_inactive_12_mon
        self.contacts_count_12_mon = contacts_count_12_mon
        self.credit_limit = credit_limit
        self.total_revolving_bal = total_revolving_bal
        self.total_amt_chng_Q4_Q1 = total_amt_chng_Q4_Q1
        self.total_trans_amt = total_trans_amt
        self.total_trans_ct = total_trans_ct
        self.total_ct_chng_Q4_Q1 = total_ct_chng_Q4_Q1
        self.avg_utilization_ratio = avg_utilization_ratio
# Create the engine to interact with the DB
engine = create_engine('sqlite:///data_storage/DB/Churn_prediction_DB.db')

# Create database following parameters defined on `Base` => this step close the creation of the DB but it's empty !
Base.metadata.create_all(engine)

def open_session(engine):
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    return session

def get_table_name (engine):
    inspector = inspect(engine)
    # Get the tables'list in the DB
    return print(inspector.get_table_names())

def get_first (session, table_name):
    first_entry = session.query(table_name).limit(1).all()
    session.close()

    for row in first_entry :
        return print(row.__dict__)

def insert_raw_data():
    session = open_session(engine)
    # Going trough the whole df to enter each df's column in the DB's related column where each column is a tuple with the iterrows function
    for row in df.iterrows():
        raw_data = Raw_data(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6],row[1][7],row[1][8],row[1][9],row[1][10],row[1][11],
        row[1][12],row[1][13],row[1][14],row[1][15],row[1][16],row[1][17],row[1][18],row[1][19],row[1][20],row[1][21],row[1][22])
        session.add(raw_data)
        session.commit()
        session.close()

def insert_cleaned_data():
    session = open_session(engine)
    # Going trough the whole df to enter each df's column in the DB's related column where each column is a tuple with the iterrows function
    for row in df_cleaned.iterrows():
        cleaned_data = Cleaned_data(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6],row[1][7],row[1][8],row[1][9],row[1][10],row[1][11],
        row[1][12],row[1][13],row[1][14],row[1][15],row[1][16],row[1][17],row[1][18],row[1][19])
        session.add(cleaned_data)
        session.commit()
        session.close()

def main():
    get_table_name(engine)
    insert_raw_data()
    insert_cleaned_data()
    session = open_session(engine)
    print("Raw_data :")
    get_first(session, Raw_data)
    print("Cleaned data :")
    get_first(session, Cleaned_data)

if __name__ == "__main__":
    main() 