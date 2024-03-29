"""empty message

Revision ID: 2f006dc658c5
Revises: 853eeb4bba7a
Create Date: 2019-09-16 17:07:48.757690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f006dc658c5'
down_revision = '853eeb4bba7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('ticket', sa.Column('order_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ticket', 'orders', ['order_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ticket', type_='foreignkey')
    op.drop_column('ticket', 'order_id')
    op.drop_table('orders')
    # ### end Alembic commands ###
