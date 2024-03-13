import os
import shutil
import pandas as pd
import global_variables
import cls_Transaction
import database

class InputSelector():

    def __init__(self, filePath):
        if os.path.exists(filePath):
            if os.access(filePath, os.W_OK):
                self.__handleFile(filePath)
            else:
                print(f'No access to file:  {filePath}')

    def __handleFile(self, filePath):
        split_tup = os.path.splitext(filePath)
        ext = split_tup[1]
        print(ext)
        if ext == ".pdf":
            self.__moveFile(filePath,"Processed")
        elif ext == ".xls":
            self.__validateExcel(filePath)
        elif ext == ".xlsx":
            self.__validateExcel(filePath)
        elif ext == ".csv":
            self.__validateTextFiles(filePath,",")
        elif ext == ".txt":
            self.__validateTextFiles(filePath,"|")
        else:
            self.__moveFile(filePath, "Errors")

    def __validateExcel(self,filePath):
        # open file
        xl = pd.read_excel(filePath)

        # validate headers (move to errors folder)
        if not set(global_variables.inputHeaderList).issubset(xl.head()):
            self.__moveFile(filePath, "Errors")
            return

        # load data to class and append list of objects
        for index in xl.index:
            trans = cls_Transaction.Transaction(xl.loc[index, 'Price'],
                                                xl.loc[index, 'Product'],
                                                xl.loc[index, 'Amount'],
                                                xl.loc[index, 'Date'],
                                                xl.loc[index, 'Group'],
                                                xl.loc[index, 'Color'],
                                                xl.loc[index, 'Material'],
                                                xl.loc[index, 'Country'])

            global_variables.list_transactions.append(trans)
            #print(trans.ProductPrice)

        self.__moveFile(filePath, "Processed")

        #database.saveTradesIntoDb(global_variables.list_transactions)
        database.saveInputDfIntoDb(xl)
        print("database updated")

        #print(len(global_variables.list_transactions))

    def __validateTextFiles(self, filePath, separator):

        # open file
        try:
            txt = pd.read_csv(filePath, header=0, sep=separator, decimal=",")
        except:
            self.__moveFile(filePath, "Errors")

        # TODO - create database and load data there

        # validate headers (move to errors folder)
        if not set(global_variables.inputHeaderList).issubset(txt.head()):
            self.__moveFile(filePath, "Errors")
            return

        # load data to class and append list of objects
        for index in xl.index:
            trans = cls_Transaction.Transaction(txt.loc[index, 'Price'],
                                                txt.loc[index, 'Product'],
                                                txt.loc[index, 'Amount'],
                                                txt.loc[index, 'Date'],
                                                txt.loc[index, 'Group'],
                                                txt.loc[index, 'Color'],
                                                txt.loc[index, 'Material'],
                                                txt.loc[index, 'Country'])

            global_variables.list_transactions.append(trans)



    def __moveFile(self, filePath, directFolder):
        file_name = os.path.basename(filePath)
        if directFolder == "Errors":
            print("Err")
            shutil.move(filePath, global_variables.folderPathError + file_name)
        elif directFolder =="Processed":
            print("Proc")
            shutil.move(filePath, global_variables.folderPathProcessed + file_name)




