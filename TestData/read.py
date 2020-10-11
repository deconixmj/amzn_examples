import xlrd

wb=xlrd.open_workbook("D:\\amzn_testcases\TestData\\amazon.xlsx")
# sheet1=wb.sheet_by_name("Categories")

sheet1=wb.sheet_by_name("Categories")

"""
In this readexcel file , we need to read column first and row second as the data for one category is entered in a column-wise , one column will contain 
categorynames for one main category

"""

def get_categories():
    list=[]

    for i in range(0,sheet1.ncols):
        data=[]
        for j in range(0,sheet1.nrows):
            # data = []
            data.append(sheet1.cell_value(j,i))
        # print(data)
        list.append(data)

    return list

# L=get_categories()
# print(L[0])
