#My class
rahul = {"name":"Rahul" , "tests":[25.0,82.0],"internals":18.0}
rohan = {"name":"Rohan" , "tests":[23.0,89.0],"internals":12.0}
rishil = {"name":"Rishil", "tests":[26.5,94.0],"internals":19.5}
students = [rahul , rohan , rishil]


def all_info(given_list):
  print "Well the record are as follows:"
  for each1 in given_list:
    print each1["name"]
    print each1["tests"]
    print each1["internals"]

def total_score(new):
  for each2 in new:
    total = each2["tests"][0] + each2["tests"][1]*0.5 + each2["internals"]
    print "So %s has scored %.2f" % (each2["name"],total)

def grade(new1):
  for each3 in new1:
      total = each3["tests"][0] + each3["tests"][1] * 0.5 + each3["internals"]
      if total >= 90:
          print  "So %s has scored A" % (each3["name"])
      elif total < 90 and total >= 80:
          print  "So %s has scored B" % (each3["name"])
      elif total < 80 and total >= 70:
          print  "So %s has scored C" % (each3["name"])
      elif total < 70 and total >= 60:
          print  "So %s has scored D" % (each3["name"])
      else:
          print  "So %s has scored F" % (each3["name"])

grade(students)



