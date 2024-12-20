import json

from src.config import USER_ID


def swap_photo_set(flickr) :
	set_id_called_random = "72177720320728991"
	set_id_called_tosort = "72177720320964111"

	response = flickr.photosets.getPhotos(photoset_id=set_id_called_random)

	first_photo = response["photoset"]["photo"][0]

	print("Transferring photo between sets")
	flickr.photosets.removePhoto(photoset_id=set_id_called_random, photo_id=first_photo['id'])
	flickr.photosets.addPhoto(photoset_id=set_id_called_tosort, photo_id=first_photo['id'])

	print(json.dumps(response))


def print_set_names(flickr):

	sets = flickr.photosets.getList(user_id='14280458@N05')

	sets_length = len(sets['photosets'])
	title  = sets['photosets']['photoset'][0]['title']['_content']

	for set in sets['photosets']['photoset']:
		print( set["title"]["_content"])


def get_medias_in_set(flickr, set_id, per_page=1, page=1 ):

	photos = flickr.photosets.getPhotos(
		user_id=USER_ID,
		photoset_id=set_id,
		per_page=per_page,
		page=page,
		extras="date_taken,media,url_sq,url_t,url_s,url_m,url_o"
	)

	# with open("photos.json", "w") as f:
	# 	json.dump(photos, f )
	return photos

def get_set_names_with_ids(flickr):

	sets = flickr.photosets.getList(user_id=USER_ID)

	name_ids = []
	for i, set in enumerate(sets['photosets']['photoset']):
		name_ids.append( {
			'id' : set['id'],
			'order' : i,
			'title' : set['title']['_content']
		})

	# json.dump(name_ids, open("sets.json", "w") )

	return name_ids
