        data = [['Alex',10],['Bob',12],['Clarke',13], ['Rana', 60]]
        df = pd.DataFrame(data,columns=['Firstname','Age'], index = ['rank1','rank2','rank3', 'rank4'], dtype = float)
        print df
        
""""    
Its output is as follows −
           Firstname   Age
rank1      Alex  10.0
rank2       Bob  12.0
rank3    Clarke  13.0
rank4      Rana  60.0
""""     
        print "How to add new rows"
        data = [['Alexa',10]]
        df1 = pd.DataFrame (data,columns=['Firstname','Age'], index = ['rank5'] )
        df=df.append(df1)
        print df 
 """"    
Its output is as follows −
 Firstname   Age
rank1      Alex  10.0
rank2       Bob  12.0
rank3    Clarke  13.0
rank4      Rana  60.0
rank5     Alexa  10.0

"""
        print "Adding new coloumns"
        df ['phone'] = pd.Series([10,15,16,11, 3], index=df.index)
        print df 
 """"    
Its output is as follows −
Adding new coloumns
      Firstname   Age  phone
rank1      Alex  10.0     10
rank2       Bob  12.0     15
rank3    Clarke  13.0     16
rank4      Rana  60.0     11
rank5     Alexa  10.0      3

"""
