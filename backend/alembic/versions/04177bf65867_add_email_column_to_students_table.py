"""Add email column to students table

Revision ID: 04177bf65867
Revises: 
Create Date: 2025-02-15 21:00:21.792718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04177bf65867'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the "email" column to the "students" table.
    op.add_column('students', sa.Column('email', sa.String(100), nullable=True))
    # Optionally, create a unique constraint for the email column.
    op.create_unique_constraint('uq_students_email', 'students', ['email'])


def downgrade() -> None:
    # Remove the unique constraint and drop the "email" column.
    op.drop_constraint('uq_students_email', 'students', type_='unique')
    op.drop_column('students', 'email')
