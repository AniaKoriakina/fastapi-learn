from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON, Boolean

metadata = MetaData()

operation = Table(
    "operation",
    metadata,

)