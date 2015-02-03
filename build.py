import glob
import os

from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'

def Main():
  env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
      extensions=['jinja2.ext.with_'])
  page = "index"
  template = env.get_template('%s.html' % page)
  html = template.render()
  with open('site/%s.html' % page, 'w') as f:
    f.write(html.encode('utf8'))
    f.close()

if __name__ == '__main__':
  Main()