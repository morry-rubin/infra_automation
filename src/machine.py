from pydantic import BaseModel, PositiveInt, ValidationError
from typing import Literal
import logging

logger = logging.getLogger("infra_sim")


class Machine(BaseModel):

    name: str
    os: Literal["ubuntu", "centos"]
    cpu: PositiveInt
    ram: PositiveInt

    def to_dict(self):
        return {
        "name": self.name,
        "os": self.os,
        "cpu": self.cpu,
        "ram": self.ram
        }
    
    def log_creation(self):
        """this function will log the creation of new machine objects.
          it will log and print to the user"""
        msg = f"Provisioning {self.name}: {self.os}, {self.cpu}, {self.ram}"
        logger.info(msg)
        print(msg + "\n")


if __name__ == "__main__":
    try:
        name = "blabla"
        machine = Machine(name=name, os="CENTO".lower(), cpu="-4", ram="4")
        machine.log_creation()
        print(machine.to_dict())
    except ValidationError as e:
        print(e)
