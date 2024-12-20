import flickrapi

import config
from database import get_database, insert_set, create_table__sets, get_set_from_title
from flickr import get_set_names_with_ids, get_medias_in_set
from auth import create_auth_if_necessary
from src.database import insert_medias

flickr = flickrapi.FlickrAPI(config.API_KEY, config.API_SECRET, format='parsed-json')
create_auth_if_necessary(flickr)

# print("setting up database...")
# create_table__sets()
#
# print("retrieving sets...")
# sets = get_set_names_with_ids(flickr)
#
# print("adding to database")
# database = insert_set( sets )
# database.commit()
#
# print("done")

db = get_database()
auto_upload_set = get_set_from_title(db, "Auto Upload")  # "72157703486909305"

medias = get_medias_in_set(flickr, auto_upload_set["id"], 2, 1)
insert_medias(db, medias)