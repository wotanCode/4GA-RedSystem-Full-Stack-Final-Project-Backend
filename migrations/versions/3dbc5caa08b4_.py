"""empty message

Revision ID: 3dbc5caa08b4
Revises: ba94cd78e207
Create Date: 2021-08-27 18:23:45.759767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dbc5caa08b4'
down_revision = 'ba94cd78e207'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ordentrabajo', sa.Column('id_nombre', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ordentrabajo', 'id_nombre')
    # ### end Alembic commands ###