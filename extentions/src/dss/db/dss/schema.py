from sqlalchemy import (
    Integer,
    ForeignKey,
    PrimaryKeyConstraint,
    String,
    Binary,
    CHAR,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, declarative_base

from diracx.db.utils import Column

USER_CODE_LENGTH = 8

DSSDBBase = declarative_base()


class Releases(DSSDBBase):
    __tablename__ = "Releases"
    releaseID = Column("releaseID", Integer, primary_key=True, autoincrement=True, nullable=False)
    releaseName = Column("releaseName", String(32), unique=True, nullable=False)

class GlobalTags(DSSDBBase):
    __tablename__ = "GlobalTags"
    dbGlobalTagID = Column("dbGlobalTagID", Integer, primary_key=True, autoincrement=True, nullable=False)
    dbGlobalTag = Column("dbGlobalTag", String(32), unique=True, nullable=False)

class MCEventTypes(DSSDBBase):
    __tablename__ = "MCEventTypes"
    mcEventTypeID = Column("mcEventTypeID", Integer, primary_key=True, autoincrement=True, nullable=False)
    mcEventType = Column("mcEventType", String(32), unique=True, nullable=False)

class GeneralSkimNames(DSSDBBase):
    __tablename__ = "GeneralSkimNames"
    generalSkimNameID = Column("generalSkimNameID", Integer, primary_key=True, autoincrement=True, nullable=False)
    skimDecayMode = Column("skimDecayMode", String(32), unique=True, nullable=False)

class MCCampaigns(DSSDBBase):
    __tablename__ = "MCCampaigns"
    mcCampaignID = Column("mcCampaignID", Integer, primary_key=True, autoincrement=True, nullable=False)
    mcCampaign = Column("mcCampaign", String(32), unique=True, nullable=False)

class DataTypes(DSSDBBase):
    __tablename__ = "DataTypes"
    dataTypeID = Column("dataTypeID", Integer, primary_key=True, autoincrement=True, nullable=False)
    dataType = Column("dataType", String(32), unique=True, nullable=False)

class DataLevels(DSSDBBase):
    __tablename__ = "DataLevels"
    dataLevelID = Column("dataLevelID", Integer, primary_key=True, autoincrement=True, nullable=False)
    dataLevel = Column("dataLevel", String(32), unique=True, nullable=False)

class BeamEnergies(DSSDBBase):
    __tablename__ = "BeamEnergies"
    beamEnergyID = Column("beamEnergyID", Integer, primary_key=True, autoincrement=True, nullable=False)
    beamEnergy = Column("beamEnergy", String(32), unique=True, nullable=False)

class BkgLevels(DSSDBBase):
    __tablename__ = "BkgLevels"
    bkgLevelID = Column("bkgLevelID", Integer, primary_key=True, autoincrement=True, nullable=False)
    bkgLevel = Column("bkgLevel", String(32), unique=True, nullable=False)

class Datasets(DSSDBBase):
    __tablename__ = "Datasets"
    datasetID = Column("datasetID", Integer, primary_key=True, autoincrement=True, nullable=False)
    lpn = Column("lpn", String(1018), nullable=False)
    lpnHash = Column("lpnHash", Binary(20), nullable=True)
    lpnHashHex = Column("lpnHashHex", CHAR(40), nullable=False)
    experimentLow = Column("experimentLow", Integer, nullable=False)
    experimentHigh = Column("experimentHigh", Integer, nullable=False)
    runLow = Column("runLow", Integer, nullable=False)
    runHigh = Column("runHigh", Integer, nullable=False)
    productionId = Column("productionId", Integer, nullable=False)

    # Define foreign key constraints for the other tables
    releasesID = Column(Integer, ForeignKey('Releases.releaseID'))
    releases = relationship('Releases', foreign_keys=[releasesID])

    globalTagsID = Column(Integer, ForeignKey('GlobalTags.dbGlobalTagID'))
    global_tags = relationship('GlobalTags', foreign_keys=[globalTagsID])

    mcEventTypesID = Column(Integer, ForeignKey('MCEventTypes.mcEventTypeID'))
    mc_event_types = relationship('MCEventTypes', foreign_keys=[mcEventTypesID])

    generalSkimNamesID = Column(Integer, ForeignKey('GeneralSkimNames.generalSkimNameID'))
    general_skim_names = relationship('GeneralSkimNames', foreign_keys=[generalSkimNamesID])

    mcCampaignsID = Column(Integer, ForeignKey('MCCampaigns.mcCampaignID'))
    mc_campaigns = relationship('MCCampaigns', foreign_keys=[mcCampaignsID])

    dataTypesID = Column(Integer, ForeignKey('DataTypes.dataTypeID'))
    data_types = relationship('DataTypes', foreign_keys=[dataTypesID])

    dataLevelsID = Column(Integer, ForeignKey('DataLevels.dataLevelID'))
    data_levels = relationship('DataLevels', foreign_keys=[dataLevelsID])

    beamEnergiesID = Column(Integer, ForeignKey('BeamEnergies.beamEnergyID'))
    beam_energies = relationship('BeamEnergies', foreign_keys=[beamEnergiesID])

    bkgLevelsID = Column(Integer, ForeignKey('BkgLevels.bkgLevelID'))
    bkg_levels = relationship('BkgLevels', foreign_keys=[bkgLevelsID])

    __table_args__ = (UniqueConstraint('lpnHashHex', name='DH_HEX_INDEX'),)






class DatasetResponse(DSSDBBase):
    datasetID: int
    lpn: str
    experimentLow: int
    experimentHigh: int
    runLow: int
    runHigh: int
    productionId: int
    releaseName: str
    # Define other fields similarly
