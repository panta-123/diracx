from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from sqlalchemy import insert, select

from diracx.db.utils import BaseDB

from sqlalchemy.orm import joinedload


from .schema import DSSDBBase, Datasets, Releases, GlobalTags, MCEventTypes, GeneralSkimNames, MCCampaigns, DataTypes, DataLevels, BeamEnergies, BkgLevels


class DSSDB(BaseDB):
    metadata = DSSDBBase.metadata

    def insert_datasets(self, dataset_list):
        with self.transaction() as session:
            for dataset_data in dataset_list:
                stmt = insert(Datasets).values(**dataset_data)
                session.execute(stmt)

    def search_datasets(self, filters=None):
        with self.transaction() as session:
            query = select(Datasets)
            if filters:
                query = query.filter_by(**filters)
            result = session.execute(query)
            return result.fetchall()
    
    def update_dataset(self, dataset_id, update_data):
        with self.transaction() as session:
            stmt = update(Datasets).where(Datasets.datasetID == dataset_id).values(**update_data)
            session.execute(stmt)
    

    def insert_release(self, release_data):
        with self.transaction() as session:
            stmt = insert(Releases).values(**release_data)
            session.execute(stmt)

    def search_releases(self, filters=None):
        with self.transaction() as session:
            query = select(Releases)
            if filters:
                query = query.filter_by(**filters)
            result = session.execute(query)
            return result.fetchall()

    # Example of updating data in other tables:
    def update_release(self, release_id, update_data):
        with self.transaction() as session:
            stmt = update(Releases).where(Releases.releaseID == release_id).values(**update_data)
            session.execute(stmt)

    def get_lpn_by_foreign_key_value(session, foreign_key_table, foreign_key_column, foreign_key_value):
        subquery = session.query(Datasets.lpn).join(foreign_key_table).filter(foreign_key_table.c[foreign_key_column] == foreign_key_value).subquery()
        lpn_values = session.query(subquery.c.lpn).all()
        return [row.lpn for row in lpn_values]
    
    def get_dataset_info_with_foreign_keys(session, lpn_to_search):
        dataset_info = session.query(Datasets).filter_by(lpn=lpn_to_search).\
        options(joinedload('*')).first()
        return dataset_info
