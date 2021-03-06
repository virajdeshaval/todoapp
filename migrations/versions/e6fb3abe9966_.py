"""empty message

Revision ID: e6fb3abe9966
Revises: f2801cba82ea
Create Date: 2021-05-15 11:51:19.765659

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import nullslast


# revision identifiers, used by Alembic.
revision = 'e6fb3abe9966'
down_revision = 'f2801cba82ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed=False WHERE completed IS NULL;')
    
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
