import arrow 

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiprofile = namedtuple("chaiprofile", ["flavor", "aroma"])

# this is just a bonus lecture.

#there are some advance data types like counter for counting, defaultdict, deque for fast insertion or removal, namedtuple for tuple with meaningful names
# and also one orderdDict