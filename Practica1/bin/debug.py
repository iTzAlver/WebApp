import es_func as es

usuario = 'alverciito@gmail.com'
contra = '131314'
#response = es.storeRegister(usuario,contra)
response = es.searchLogin(usuario,contra)
print(response)
es.delete_all_users()