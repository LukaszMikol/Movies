# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = None
        try:
            # creating database
            self.conn = sqlite3.connect('movies.db')
            self.c = self.conn.cursor()
            self.c.execute('''
                CREATE TABLE Movies (
                    Id INTEGER PRIMARY KEY,
                    Title TEXT,
                    Year TEXT,
                    Rating_value TEXT,
                    Rating_count TEXT,
                    Description TEXT,
                    Director TEXT,
                    Duration TEXT,
                    Genre TEXT,
                    Country TEXT,
                    Language TEXT,
                    Budget TEXT,
                    Box_office_USA TEXT,
                    Box_office_world TEXT,
                    Url TEXT
                )
            ''')


            # Save (commit) the changes
            self.conn.commit()

        except sqlite3.Error as e:
            print(e)


    def close_spider(self, spider):
        if self.conn != None:
            self.conn.close()

    def process_item(self, item, spider):
        self.conn.execute('''
        INSERT INTO Movies (Title, Year, Rating_value, Rating_count, Description, Director, Duration, 
                            Genre, Country, Language, Budget, Box_office_USA, Box_office_world, Url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);    
        ''', (
            item['Title'],
            item['Year'],
            item['Rating_value'],
            item['Rating_count'],
            item['Description'],
            item['Director'],
            item['Duration'],
            item['Genre'],
            item['Country'],
            item['Language'],
            item['Budget'],
            item['Box_office_USA'],
            item['Box_office_world'],
            item['Url']
        ))

        self.conn.commit()
        return item
