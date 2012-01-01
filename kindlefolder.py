from __future__ import with_statement, division
import simplejson, tweepy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/braaaaains', methods=['GET', 'POST'])
def braaaaains():

	submitted_user = request.form['submitted_user']
	print ""	
	print submitted_user
	print "==============="
	if submitted_user[0] == "@":
		submitted_user == submitted_user[1:]

	user = tweepy.api.get_user(submitted_user)

	follower_ratio = user.followers_count/user.friends_count

	if follower_ratio > 3:
		follower_ratio_corrected = math.log10(follower_ratio)*2
	elif follower_ratio < 0.1:
		follower_ratio_corrected = 0.1
	else:
		follower_ratio_corrected = follower_ratio

	print 'follower_ratio'
	print follower_ratio
	chase_ratio = follower_ratio_corrected*11.1111111111

	#if talk of zombies++, death rate++
	#zombie_talk = API.search('zombie')
	#zombie_talk_number = API.search('zombie').length() + API.search('zombies').length() + API.search('zombiepocalypse')

	#if user hides geo info, death rate ++
	
	print 'chase_ratio'
	print chase_ratio
	if user.geo_enabled == True:
		geo = 33.3333333333
	else:
		geo = 0
	print 'geo'
	print geo

	now = datetime.datetime.now()
	before = user.created_at
	delta = now - before
	days_ago = delta.days
	
	loudness_ratio = user.statuses_count/days_ago
	print 'user.statuses_count'
	print user.statuses_count
	print 'loudness_ratio'
	print loudness_ratio
 
	if loudness_ratio > 20:
		loudness = 33.33
	if loudness_ratio > 10:
		loudness = 25
	elif loudness_ratio > 5:
		loudness = 20
	elif loudness_ratio > 1:
		loudness = 10
	elif loudness_ratio > 0.5:
		loudness = 5

        elif loudness_ratio <= 0.5:
		loudness = 0

	print 'loudness'
	print loudness
	#final percentage
	final_percentage = chase_ratio + geo + loudness
	print final_percentage
	final_percentage = int(final_percentage)
	final_percentage = 100-final_percentage
	print final_percentage
	return render_template('success.html', final_percentage=final_percentage, loudness=loudness, loudness_ratio=round(loudness_ratio,2), geo=geo, chase_ratio=chase_ratio, follower_ratio=round(follower_ratio,2))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404	

@app.errorhandler(400)
def bad_request(e):
    return render_template('index.html')	

@app.errorhandler(500)
def server_failure(e):
    return render_template('500.html'), 500		

if __name__ == "__main__":
	app.run()
