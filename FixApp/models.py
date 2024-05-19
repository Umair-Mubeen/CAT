from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    rolType = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Employee(models.Model):
    Emp_Name = models.CharField(max_length=255)
    Emp_Pwd = models.CharField(max_length=255)
    Emp_Email = models.CharField(max_length=255)
    Emp_Age = models.IntegerField()
    Emp_Designation = models.CharField(max_length=255)
    EmpAddress = models.CharField(max_length=255)


class OrderEvent(models.Model):
    Order_Event = models.CharField(max_length=50)
    Fix_Col_0 = models.CharField(max_length=50)
    FirmROID = models.CharField(max_length=50)
    MsgType = models.CharField(max_length=50)
    CAT_IM_ID = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)
    Order_ID = models.CharField(max_length=50)
    Symbol = models.CharField(max_length=50)
    TimeStamp = models.CharField(max_length=50)
    Fix_Col_1 = models.CharField(max_length=50)
    Fix_Col_2 = models.CharField(max_length=50)
    Fix_Col_3 = models.CharField(max_length=50)
    Fix_Col_4 = models.CharField(max_length=50)
    Fix_Col_5 = models.CharField(max_length=50)
    Fix_Col_6 = models.CharField(max_length=50)
    Fix_Col_7 = models.CharField(max_length=50)
    Fix_Col_8 = models.CharField(max_length=50)
    SideType = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Fix_Col_9 = models.CharField(max_length=50)
    OrderType = models.CharField(max_length=50)
    TIF = models.CharField(max_length=50)
    Trading_Session = models.CharField(max_length=50)
    Fix_Col_10 = models.CharField(max_length=50)
    Fix_Col_11 = models.CharField(max_length=50)
    FD_ID = models.CharField(max_length=50)
    Acc_Type = models.CharField(max_length=50)
    Fix_Col_12 = models.CharField(max_length=50)
    Fix_Col_13 = models.CharField(max_length=50)
    Fix_Col_14 = models.CharField(max_length=50)
    Fix_Col_15 = models.CharField(max_length=50)
    Fix_Col_16 = models.CharField(max_length=50)
    Fix_Col_17 = models.CharField(max_length=50)
    Fix_Col_18 = models.CharField(max_length=50)
    Fix_Col_19 = models.CharField(max_length=50)
    Fix_Col_20 = models.CharField(max_length=50)
    Fix_Col_21 = models.CharField(max_length=50)
    Fix_Col_22 = models.CharField(max_length=50)
    Fix_Col_23 = models.CharField(max_length=50)
    Fix_Col_24 = models.CharField(max_length=50)
    Fix_Col_25 = models.CharField(max_length=50)
    Fix_Col_26 = models.CharField(max_length=50)
    Fix_Col_27 = models.CharField(max_length=50)
    Fix_Col_28 = models.CharField(max_length=50)


class Reports(models.Model):
    Report_Name = models.CharField(max_length=50)
    CAT_IMID = models.CharField(max_length=50)
    FD_ID = models.CharField(max_length=50)
    Train_Session = models.CharField(max_length=50)
    FileName = models.CharField(max_length=50)
    FileType = models.CharField(max_length=50)
    Status = models.CharField(max_length=50,default='')
