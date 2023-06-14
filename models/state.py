#!/usr/bin/python3
""" State module for the HBNB project """
from models.base_model import BaseModel, Base
from models import storage


class State(BaseModel, Base):
    """ State class to store state information """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type != "db":
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id"""
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
