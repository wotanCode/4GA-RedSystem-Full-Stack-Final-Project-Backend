"""empty message

Revision ID: f9eafb7dc2f4
Revises: 
Create Date: 2021-09-20 01:05:23.202368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9eafb7dc2f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contrato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_project', sa.String(length=255), nullable=False),
    sa.Column('region', sa.String(length=100), nullable=True),
    sa.Column('comuna', sa.String(length=100), nullable=True),
    sa.Column('sector', sa.String(length=100), nullable=True),
    sa.Column('plano', sa.String(length=120), nullable=True),
    sa.Column('obra_descripcion', sa.String(length=200), nullable=True),
    sa.Column('planta_matriz', sa.String(length=120), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=True),
    sa.Column('tecnicos', sa.String(length=255), nullable=True),
    sa.Column('comentario', sa.String(length=120), nullable=True),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_project')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('rut', sa.String(length=12), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('lastname', sa.String(length=100), nullable=True),
    sa.Column('contact', sa.String(length=120), nullable=True),
    sa.Column('perfil', sa.String(length=40), nullable=True),
    sa.Column('fecha_nacimiento', sa.String(length=200), nullable=True),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ordentrabajo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_nombre', sa.String(length=100), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=255), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=True),
    sa.Column('tecnicos', sa.String(length=255), nullable=True),
    sa.Column('id_contrato', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_contrato'], ['contrato.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalleordentrabajo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('id_ordentrabajo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ordentrabajo'], ['ordentrabajo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userorden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_orden', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_orden'], ['ordentrabajo.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('acreditacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_foto', sa.String(length=255), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('id_userorden', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_userorden'], ['userorden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statusorden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inicio_fecha', sa.String(length=100), nullable=False),
    sa.Column('final_fecha', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.Column('minutostrabajados', sa.String(length=120), nullable=False),
    sa.Column('url_foto_epp', sa.String(length=120), nullable=False),
    sa.Column('url_foto_referencia', sa.String(length=200), nullable=False),
    sa.Column('geo_lat', sa.String(length=120), nullable=False),
    sa.Column('geo_lon', sa.String(length=120), nullable=False),
    sa.Column('id_userorden', sa.Integer(), nullable=True),
    sa.Column('id_contrato', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_contrato'], ['contrato.id'], ),
    sa.ForeignKeyConstraint(['id_userorden'], ['userorden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('statusorden')
    op.drop_table('acreditacion')
    op.drop_table('userorden')
    op.drop_table('detalleordentrabajo')
    op.drop_table('ordentrabajo')
    op.drop_table('user')
    op.drop_table('contrato')
    # ### end Alembic commands ###
