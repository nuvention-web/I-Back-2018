"""empty message

Revision ID: 366e11dec3cc
Revises: 
Create Date: 2018-06-09 11:43:46.355361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '366e11dec3cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bought', sa.Column('quiz_id', sa.Integer(), nullable=True))
    op.add_column('notbought', sa.Column('quiz_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notbought', 'quiz_id')
    op.drop_column('bought', 'quiz_id')
    # ### end Alembic commands ###
