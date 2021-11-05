"""updating type.

Revision ID: c36c83a0bf92
Revises: 
Create Date: 2021-09-17 13:58:51.702821

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c36c83a0bf92'
down_revision = 'bc8aee16d308'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.get_bind().connect() as conn:
        result = conn.execute("""SELECT 1 FROM pg_type t
                               JOIN pg_class c ON c.oid = t.typrelid
                               JOIN pg_attribute a ON a.attrelid = c.oid
                               WHERE t.typname = 'dataset_type'
                               AND a.attname = 'created_at'
                           """)
        if not result:
            conn.execute('ALTER TYPE dataset_type ADD ATTRIBUTE created_at TIMESTAMP CASCADE;')
            conn.execute('ALTER TYPE dataset_type ADD ATTRIBUTE updated_at TIMESTAMP CASCADE;')

        conn.execute('COMMIT')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.get_bind().connect() as conn:
        conn.execute('ALTER TYPE dataset_type DROP ATTRIBUTE IF EXISTS created_at CASCADE;')
        conn.execute('ALTER TYPE dataset_type DROP ATTRIBUTE IF EXISTS updated_at CASCADE;')

        conn.execute('COMMIT')

    # ### end Alembic commands ###
