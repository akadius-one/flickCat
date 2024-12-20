import sqlite3

from src.config import DATABASE_FILE

try:
	database = sqlite3.connect(DATABASE_FILE)
	database.row_factory = sqlite3.Row  # switch to dict like access.
except Exception as e:
	print(f"Can't connect to database `${DATABASE_FILE}`" )
	raise e


def get_database():
	return database


def create_table__sets(db) :

	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS 
		sets ("id" TEXT UNIQUE, "order" INT, "title" TEXT)
	''')


def create_table__medias(db) :
	"""
	"media" is photo or video
	:return:
	"""
	cursor = db.cursor()

	cursor.execute('''
		CREATE TABLE IF NOT EXISTS 
		medias (
			"id" TEXT UNIQUE,
			"title" TEXT,
			"media" TEXT,  
			"media_status" TEXT,
			"date_taken" DATETIME,   -- flickr datetaken
			"date_taken_granularity" INT, -- flickr datetakengranularity
			"date_taken_unknown" BOOLEAN, -- flickr datetakenunknown
			"url_sq" TEXT,
			"height_sq" INT,
			"width_sq" INT,
			"url_t" TEXT,
			"height_t" INT,
			"width_t" INT,
			"url_s" TEXT,
			"height_s" INT,
			"width_s" INT,
			"url_m" TEXT,
			"height_m" INT,
			"width_m" INT,
			"url_o" TEXT,
			"height_o" INT,
			"width_o" INT
		)
	''')

def create_table__media_sets(db) :

	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS 
		media_sets ("id" INT INCREMENT, "media_id" TEXT, "set_id" TEXT )
	''')

def insert_set( db, sets ):
	# [{'id':id,'title':title},...]

	print(sets)
	print([(s["id"],s["title"]) for s in sets])

	cursor = db.cursor()
	cursor.executemany('''INSERT INTO sets ("id", "order", "title") values (?, ?, ?)''', [(s["id"], s["order"], s["title"]) for s in sets] )


def insert_medias( db, medias ):

	print(medias)
	print([(m["id"], m["title"]) for m in medias])

	cursor = db.cursor()
	cursor.executemany(
		'''INSERT INTO  ("id", "title", "media", "media_status", 
							"date_taken", "date_taken_granularity", "date_taken_unknown",
							"url_sq", m["width_sq"],m["height_sq"],
							"url_t", m["width_t"],m["height_t"],
							"url_s", m["width_s"],m["height_s"],
							"url_m", m["width_m"],m["height_m"],
							"url_o",  m["width_o"],m["height_o"],
						)
	             values (?, ?, ?, ?, 
	                    ?, ?, ?, 
	                    ?, ?, ?,
	                    ?, ?, ?,
	                    ?, ?, ?,
	                    ?, ?, ?,
	                    ?, ?, ?
	                    )
		''',
		[
			(
				m["id"], m["title"], m["media"], m["media_status"],
				m["datetaken"], m["datetakengranularity"], m["datetakenunknown"],
				m["url_sq"], m["width_sq"],m["height_sq"],
				m["url_t"], m["width_t"], m["height_t"],
				m["url_s"], m["width_s"], m["height_s"],
				m["url_m"], m["width_m"], m["height_m"],
				m["url_o"], m["width_o"], m["height_o"]
			)
			for m in medias
		]
	)


def get_set_from_title( db, title ) :

	cursor = db.cursor()
	cursor.execute(
		'''SELECT * FROM sets WHERE title = ?''',
	    [title]
	)

	return cursor.fetchone()



if __name__ == "__main__":

	def main() :

		print("Setting up database")

		db = get_database()

		create_table__sets(db)
		create_table__medias(db)
		create_table__media_sets(db)

		db.commit()
		db.close()

	main()