from website import create_api

#main allows us to use website as a python package
api = create_api()

if __name__ == '__main__':
    api.run(debug=True)

