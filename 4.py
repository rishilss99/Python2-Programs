#Restaurant

meal = 600
GST = 18.0/100
meal = meal + meal*GST

tip = (2.0/100)*meal

print "Thank you for visiting Jon's Restaurant your is bill is for Rs %0.2f and your tip is Rs %0.2f" % (meal,tip)