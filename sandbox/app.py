from flask import Flask, jsonify, request

app = Flask(__name__)

proj_updates = {

}

projects = [
  {
    'id': 1,
    'name': 'TESTE',
    'creator': 'Ciclano',
    'description': 'RESTfulAPI',
    'publication': '12/12/12'
  }
]

# pagination --------------------------------------------------------

step = 2
hashmap = {

}

for ind in range(len(projects)):
  if ind == 0:
    hashmap[ind] = projects[0:step]
  else:
    start_ind = step * ind
    end_ind = ((ind + 1) * step)
    sample = projects[start_ind:end_ind]
    hashmap[ind] = sample
  

# homepage ----------------------------------------------------------

@app.route('/')
def index():
  return 'Index Page'

# authentication ----------------------------------------------------



# @app.route('/login', methods=['GET','POST'])
# def login():
#   if request.method == 'POST':
#     #check user details from db
#     login_user()
#   elif request.method == 'GET':
#     #serve login page
#     serve_login_page()

# post project ------------------------------------------------------

@app.route('/projects', methods=['POST'])
def create_project():
  new_project = request.get_json()
  projects.append(new_project)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         static_file = request.files['the_file']
#         # here you can send this static_file to a storage service
#         # or save it permanently to the file system
#         static_file.save('/var/www/uploads/profilephoto.png')

# search project and return json ------------------------------------

@app.route('/projects', methods=['GET'])
def get_project():
  return jsonify(projects)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#   #returns the post, the post_id should be an int
#   return str(post_id)

# filter project by name -----------------------------------------

@app.route('/projects/<str:name>', methods=['GET'])
def get_project_by_name(name):
  for proj in projects:
    if proj.get('name') == name:
      return jsonify(proj)

# filter project by creator --------------------------------------------

@app.route('/projects/<str:creator>', methods=['GET'])
def get_project_by_creator(creator):
  for proj in projects:
    if proj.get('creator') == creator:
      return jsonify(proj)

# #adding variables
# @app.route('/user/<username>')
# def show_user(username):
#   #returns the username
#   return 'Username: %s' % username

# filter project by data of publication -----------------------------

# Update some project -----------------------------------------------

# by ID
@app.route('/projects/<int:id>', methods=['PUT'])
def update_project_by_name(id):
  project_updated = request.get_json()
  for ind, proj in enumerate(projects):
    if proj.get('id') == id:
      projects[ind].update(project_updated)

# Exclude some project ----------------------------------------------

# by ID
@app.route('/projects/<int:id>', methods=['DELETE'])
def exclude_project_by_name(id):
  for ind, proj in enumerate(projects):
    if proj.get('id') == id:
      del projects[ind]

  return jsonify(projects)

# Run ---------------------------------------------------------------

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)