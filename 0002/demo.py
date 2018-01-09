import uuid
import pymysql

def insertCode(codes):
	# 打开数据库连接
	db = pymysql.connect(host='192.168.10.130', port=3306, user='root', passwd='123456',db='test')
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	try:
		for code in codes:
			sql = "INSERT INTO uuid_table(uuid,datestr) VALUES ('%s', '%s')" % (code, '20180109')
		    # 执行sql语句
			cursor.execute(sql)
		    # 提交到数据库执行
			db.commit()
	except:
	   # 如果发生错误则回滚
		db.rollback()
	# 关闭数据库连接
	db.close()

def generateCode(num):
	list = []
	for i in range(num):
		list.append(uuid.uuid1())
	return list

if __name__ == "__main__":
	codes = generateCode(200)
	insertCode(codes)