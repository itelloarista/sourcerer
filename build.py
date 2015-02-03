import glob
import os
import yaml

from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = 'templates'
CASE_STUDIES = yaml.load(open('data/case-studies-en.yaml'))
ENUMS = yaml.load(open('data/enums.yaml'))
template_data = {
	'title': 'Crowdsourcing Advisor - a GovLab production',
	'case_studies': CASE_STUDIES, 
	'enums': ENUMS,
	'total_case_studies': len(CASE_STUDIES)
}

def Main():
	env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
		extensions=['jinja2.ext.with_'])
	pages = ["index", 'advisor']
	for page in pages:
		template = env.get_template('%s.html' % page)
		html = template.render(template_data)
		with open('site/%s.html' % page, 'w') as f:
			f.write(html.encode('utf8'))
			f.close()
	projects = {}
	for case in CASE_STUDIES:
		projects[case['title'].replace(" ","-").lower()] = case
	for key, value in projects.items():
		template = env.get_template('project.html')
		html = template.render(value)
		with open('site/ajax/{}.html'.format(key), 'w') as f:
			f.write(html.encode('utf8'))
			f.close()

if __name__ == '__main__':
  Main()