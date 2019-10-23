from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    return(namedtuple("blog", dict_.keys())(*dict_.values()))


def nt2json(nt):
    def jsondatetimeconverter(o):
        """To avoid TypeError: datetime.datetime(...) is not JSON serializable"""

        if isinstance(o, datetime):
            return o.__str__()
    return json.dumps(nt._asdict(), default=jsondatetimeconverter)

nt = dict2nt(blog)
output=nt2json(nt)
print(type(output))
data = json.loads(output)
print (data['name'])