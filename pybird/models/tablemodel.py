
class TableModel:

    def __init__(self) -> None:
        setattr(self,'root', self.return_name())
        setattr(self,'map', self.return_attrs())
        pass
    
    @classmethod
    def return_name(cls):
        return cls.__name__

    @classmethod
    def return_attrs(cls):
        return cls.__annotations__

    


    @classmethod
    def __create_query(cls):

        list = cls.__annotations__
        query = f'create table "{str(cls.__name__)}" ('
        ID = ''
        for key in list:
            if key[0:2].upper() == 'ID':
                ID = str(key)
                query += f' {str(key)} {cls.to_type(list[key])} not null,'
                query += f' constraint "PK_{str(cls.__name__)}" primary key ("{str(key)}") '
            elif cls.to_type(list[key]) != 'None Type':
                query += f', {str(key)} {cls.to_type(list[key])}'
            else:
                ...
        
        query += ");"


        return query

    @classmethod
    def create_table(cls, con):
        
        query = cls.__create_query()
        print(query)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        
    
    @classmethod
    @staticmethod
    def to_type(type):

        if type == int:
            return 'Integer'
        elif type == str:
            return 'VARCHAR(50)'
        elif type == float:
            return 'FLOAT'
        else:
            return 'None Type' 

        