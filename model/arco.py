from dataclasses import dataclass

from model.driver import Driver


@dataclass
class Arco:
    vincente: Driver
    perdente: Driver
    peso: int