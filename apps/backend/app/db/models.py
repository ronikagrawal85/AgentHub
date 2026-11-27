"""Central ORM model import registry used by Alembic discovery.

Business modules will import their owned models here when those modules are
implemented. Importing this module from Alembic ensures every registered model
is attached to ``Base.metadata`` before autogeneration runs.
"""
