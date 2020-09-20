"""user tokens

Revision ID: 3048302eb74d
Revises: 5988fcf60d97
Create Date: 2020-09-20 17:08:03.327719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3048302eb74d'
down_revision = '5988fcf60d97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###