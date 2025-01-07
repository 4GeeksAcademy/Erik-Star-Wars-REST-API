"""empty message

Revision ID: 9b95f91d6478
Revises: c8fc7b0dae4a
Create Date: 2025-01-07 15:22:58.561632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b95f91d6478'
down_revision = 'c8fc7b0dae4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('People',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('race', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('race')
    )
    with op.batch_alter_table('Planet', schema=None) as batch_op:
        batch_op.alter_column('population',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Planet', schema=None) as batch_op:
        batch_op.alter_column('population',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('People')
    # ### end Alembic commands ###