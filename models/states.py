#1/usr/bin/python3
'''
    Implementing States class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel, Base):
    '''
        Implementing States
    '''
    __tablename__ = 'states'
    if os.getenv('HNBNB_TYPE_STORAGE') =='db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities property
            """
            city_list = []
            for key, val in models.storage.all().items():
                try:
                    if val.state_id == self.id:
                        city_list.append(val)
                expect AttributeError:
                    pass
                return city_list
