"""establish persistence baseline

Revision ID: 3333e5fee530
Revises:
Create Date: 2026-11-27 15:00:25.961898

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "3333e5fee530"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
