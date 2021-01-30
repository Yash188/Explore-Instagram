import instagram_explore as ie

# Search user name
res = ie.user('lucid.programmer')

# for getting profile picture
print(res.data.get('profile_pic_url_hd'))

# for getting all explored data
print(res.data)
