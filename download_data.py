import pylast

def generate_api_object():
  API_KEY = 'b8c4f4dc4574a73a1281e8e3408ca8ca'
  API_SECRET = 'a13bb7eda2a20553f6342c2d2961b0f5'
  return pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)


def get_artist_tags(last, artist):
    tag_weight = {}
    result = last.get_artist(artist).get_top_tags()

    for tag in result:
        tag_weight[str(tag.item.get_name())] = str(tag.weight) 

    tag_weight = {k: int(v) for k, v in tag_weight.items()}

    return sorted(tag_weight.items(), key=lambda x: x[1], reverse=True)

def get_artist_wiki(last, artist):
    return last.get_artist(artist).get_bio_content()

def get_track_tags(last, artist, track):
    tag_weight = {}
    result = last.get_track(artist, track).get_top_tags()

    for tag in result:
        tag_weight[str(tag.item.get_name())] = str(tag.weight) 

    tag_weight = {k: int(v) for k, v in tag_weight.items()}

    return sorted(tag_weight.items(), key=lambda x: x[1], reverse=True)

def get_loved_tracks(last, user, number):
    return last.get_user(user).get_loved_tracks(limit=number)

def get_last_tracks(last, user, number):
    return last.get_user(user).get_recent_tracks(limit=number)

def get_user_top_tracks(last, user, period, number):
        return last.get_user(user).get_top_tracks(period=period,limit=number)

def get_user_top_artists(last, user, period, number):
        return last.get_user(user).get_top_artists(period=period,limit=number)

def get_user_top_artists(last, user, period, number):
        return last.get_user(user).get_top_albums(period=period,limit=number)

def get_artist_tracks(last, user, artist):
    	return last.get_user(user).get_artist_tracks(artist=artist)

def get_track_scrobbles(last, user, artist, track):
    return last.get_user(user).get_track_scrobbles(artist,track)

def get_user_last_scrobbles(last,user):
    return last.get_user(user).get_recent_tracks(limit = 10)