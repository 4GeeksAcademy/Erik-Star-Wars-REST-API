"""empty message

Revision ID: 28676f219680
Revises: 3d8cee0110fb
Create Date: 2025-01-07 14:57:41.022447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28676f219680'
down_revision = '3d8cee0110fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('climate', sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint(None, ['climate'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Planet', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('climate')

    # ### end Alembic commands ###