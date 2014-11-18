import sys
import re
import csv
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1q2w3e4r5t6y7u8i', db='test')
cur = conn.cursor()
text = "a!34*vsfsdfsfsd^g"

count = 0;
csv_data = csv.reader(file('temp.csv'))

chk = False
for row in csv_data:
	count = count + 1
	print str(count)
	row[1] = row[1].replace("\"", "#");
	row[1] = row[1].replace("\'", "#");
	row[1] = row[1].replace("\u", "#");
	
	if (chk):
		if (cur.execute('SELECT title FROM title WHERE title = %s',str(row[1]))):
			### Found ###
			#print str(row[1])+"Found"
			cur.execute('UPDATE title SET lastdate = CURDATE() WHERE title = %s',str(row[1]))
						#print sql
			cond = "SELECT title_id FROM has_category WHERE title_id = (SELECT title_id FROM title WHERE title =\""+str(row[1])+"\") AND category_id ="+"(SELECT category_id FROM category WHERE category =\""+str(row[0])+"\")"
						# AND category_id =\""+str(row[0])+"\""
			#cur.execute(cond)
			
			#print str(cur.fetchone())
			if not (cur.execute(cond)):
			
				sql = "INSERT INTO has_category(title_id,category_id) VALUES ((SELECT title_id FROM title WHERE title =\""+str(row[1])+"\""+"),("+"SELECT category_id FROM category WHERE category =\""+str(row[0])+"\"))"
				cur.execute(sql)
			#cur.execute('SELECT title_id FROM title WHERE title = "row[1]"')
			#titleid = cur.fetchone()
			#cur.execute('SELECT category_id FROM category WHERE category = "row[0]"')
			#categoryid = cur.fetchone()
			#if not (cur.execute('SELECT title_id FROM has_category WHERE title_id = "titleid" AND category_id = "categoryid"')):
			#	cur.execute('INSERT INTO has_category(title_id)' 'VALUES(%s)',titleid)
			#	cur.execute('INSERT INTO has_category(category_id)' 'VALUES(%s)',categoryid)	
			conn.commit()
		else :
			### not found ###
			#print str(row[1])+"Not Found"
			cur.execute('INSERT INTO title(title_id,title,firstdate,lastdate) VALUES("",%s,CURDATE(),CURDATE())',str(row[1]))
			sql = "INSERT INTO has_category(title_id,category_id) VALUES ((SELECT title_id FROM title WHERE title =\""+str(row[1])+"\""+"),("+"SELECT category_id FROM category WHERE category =\""+str(row[0])+"\"))"
			#print sql
			cur.execute(sql)
	
			#cur.execute('SELECT title_id FROM title WHERE title = %s',row[1])
			#print str(cur.fetchone())
			#cur.execute('SET @title_id = LAST_INSERT_ID()')
			#titleid = cur.fetchone()
			#cur.execute('SELECT category_id FROM category WHERE category = %s',row[0])
			#print str(cur.fetchone())
			#cur.execute('SET @title_id = %s',str(cur.fetchone()))
			#categoryid = cur.fetchone()
			#sql = "INSERT INTO has_category(title_id,category_id) VALUES ((SELECT title_id FROM title WHERE title =\""+str(row[1])+"\""+"),("+"SELECT category_id FROM category WHERE category =\""+str(row[0])+"\"))"
			#print sql
			#cur.execute(sql)
			conn.commit()
			#cur.execute('INSERT INTO has_category(title_id,category_id) VALUES(%s,%s)',("1","20"))
	else :
		chk = True

   
conn.commit()
cur.close()
conn.close()
