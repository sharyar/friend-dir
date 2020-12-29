import pytest
from datetime import date
from friend import Friend

# Happy Path Tests:
@pytest.mark.parametrize('fname,lname,phone_num,birth_date_iso',[
   ('Sharyar','Memon','780-293-2379','1992-07-05'),
   ('Rafsan', 'Jani', '780-000-0000', '1994-10-16') 
])
def test_friend_class(fname, lname, phone_num, birth_date_iso):
    f1 = Friend(fname, lname, phone_num, birth_date_iso) 
    assert f1.fname == fname
    assert f1.lname == lname
    assert f1.birthdate == date.fromisoformat(birth_date_iso)
    assert f1.last_contact == date.today()