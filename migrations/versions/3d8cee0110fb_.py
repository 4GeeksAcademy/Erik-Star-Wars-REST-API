"""empty message

Revision ID: 3d8cee0110fb
Revises: 09e951862af4
Create Date: 2025-01-07 14:44:36.566694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d8cee0110fb'
down_revision = '09e951862af4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=40),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###
