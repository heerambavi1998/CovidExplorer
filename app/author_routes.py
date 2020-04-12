from flask import render_template
from app import app
from .elasticSearch import  author_findpapers, paper_namefromid


@app.route('/author/<author_name>', methods = ['GET'])
def get_author_page_new(author_name):
	#must return author individual page

	# author_name = ' '.join(author_id.split('-')).title()
	# print(author_name)
	paper_data = list(author_findpapers(author_name))
	paper_yearwise={}
	for pid in paper_data:
		pdata = paper_namefromid(pid)
		year = int(pdata['ptime'][:4])
		if year in paper_yearwise:
			paper_yearwise[year].append(pdata)
		else:
			paper_yearwise[year] = [pdata]
	paper_yearwise = sorted(paper_yearwise.items(), reverse=True)

	return render_template('author_pg.html', items=paper_yearwise, keyword=author_name)