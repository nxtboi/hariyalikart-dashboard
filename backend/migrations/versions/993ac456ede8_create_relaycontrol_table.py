"""Create RelayControl table

Revision ID: 993ac456ede8
Revises: e332238d476d
Create Date: 2024-09-01 01:24:28.581518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '993ac456ede8'
down_revision = 'e332238d476d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relay_control',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.String(length=64), nullable=True),
    sa.Column('moisture_threshold', sa.Float(), nullable=True),
    sa.Column('temperature_threshold', sa.Float(), nullable=True),
    sa.Column('relay_status', sa.String(length=64), nullable=True),
    sa.Column('switch_status', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)

    op.drop_table('relay_control')
    # ### end Alembic commands ###
