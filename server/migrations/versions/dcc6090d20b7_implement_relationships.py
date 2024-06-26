"""implement relationships

Revision ID: dcc6090d20b7
Revises: b1523b8f4739
Create Date: 2024-04-14 18:23:37.254809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc6090d20b7'
down_revision = 'b1523b8f4739'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signups', sa.Column('camper_id', sa.Integer(), nullable=True))
    op.add_column('signups', sa.Column('activity_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_signups_activity_id_activities'), 'signups', 'activities', ['activity_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_signups_camper_id_campers'), 'signups', 'campers', ['camper_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_signups_camper_id_campers'), 'signups', type_='foreignkey')
    op.drop_constraint(op.f('fk_signups_activity_id_activities'), 'signups', type_='foreignkey')
    op.drop_column('signups', 'activity_id')
    op.drop_column('signups', 'camper_id')
    # ### end Alembic commands ###
