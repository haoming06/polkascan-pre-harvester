"""Changed index on log table

Revision ID: 1e6da577c3aa
Revises: 21fd70e7cbf6
Create Date: 2019-07-17 11:37:21.386880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6da577c3aa'
down_revision = '21fd70e7cbf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_data_log_type_id'), 'data_log', ['type_id'], unique=False)
    op.drop_index('ix_data_log_block_id', table_name='data_log')
    op.drop_index('ix_data_log_log_idx', table_name='data_log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_data_log_log_idx', 'data_log', ['log_idx'], unique=False)
    op.create_index('ix_data_log_block_id', 'data_log', ['block_id'], unique=False)
    op.drop_index(op.f('ix_data_log_type_id'), table_name='data_log')
    # ### end Alembic commands ###