"""empty message

Revision ID: f1a4265171c5
Revises: f728305ae08c
Create Date: 2021-05-18 11:14:31.257223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1a4265171c5'
down_revision = 'f728305ae08c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rental',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('video', sa.Integer(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['video'], ['video.id'], ),
    sa.PrimaryKeyConstraint('id', 'customer', 'video')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental')
    # ### end Alembic commands ###
