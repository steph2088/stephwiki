from flask import Flask, send_from_directory
import jinja2
application = Flask(__name__)

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

@application.route('/')
def index():
  TEMPLATE_FILE = "index.html"
  template = templateEnv.get_template(TEMPLATE_FILE)
  return template.render()

@application.route('/infos/<path:path>')
def send_info(path):
  TEMPLATE_FILE = "./infos/"+path
  try: template = templateEnv.get_template(TEMPLATE_FILE)
  except: return TEMPLATE_FILE
  return template.render()

@application.route('/static/<path:path>')
def send_static(path):
  return send_from_directory('', path)
