"""Adding user.

Revision ID: 9f4a4b16344f
Revises: 90f91c523f48
Create Date: 2022-11-11 14:59:20.900082

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f4a4b16344f'
down_revision = '90f91c523f48'
branch_labels = ()
depends_on = '561ebe6266ad' # LCCS-DB stable 0.8.1


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('institution', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('users_pkey')),
    sa.UniqueConstraint('email', name=op.f('users_email_key')),
    schema='sampledb'
    )
    op.create_index(op.f('idx_sampledb_users_email'), 'users', ['email'], unique=False, schema='sampledb')
    op.create_index(op.f('idx_sampledb_users_institution'), 'users', ['institution'], unique=False, schema='sampledb')
    op.create_index(op.f('idx_sampledb_users_name'), 'users', ['name'], unique=False, schema='sampledb')
    op.create_foreign_key(op.f('datasets_user_id_users_fkey'), 'datasets', 'users', ['user_id'], ['user_id'], source_schema='sampledb', referent_schema='sampledb', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('datasets_user_id_users_fkey'), 'datasets', schema='sampledb', type_='foreignkey')
    op.drop_index(op.f('idx_sampledb_users_name'), table_name='users', schema='sampledb')
    op.drop_index(op.f('idx_sampledb_users_institution'), table_name='users', schema='sampledb')
    op.drop_index(op.f('idx_sampledb_users_email'), table_name='users', schema='sampledb')
    op.drop_table('users', schema='sampledb')
    # ### end Alembic commands ###
