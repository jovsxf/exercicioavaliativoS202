from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI


motoristaDAO = MotoristaDAO("atlas_cluster","usuarios")

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()