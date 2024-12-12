#vytvor slovnik
user_1 = {}

#dopln slovnik
user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'

#rozsir slovnik
user_email = {'email': 'marek.parek@gmail.com'}
user_1.update(user_email)

#vypis
print('User #01:', user_1)