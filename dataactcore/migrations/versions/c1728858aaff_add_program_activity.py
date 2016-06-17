"""add_program_activity

Revision ID: c1728858aaff
Revises: e7f8f4d5a1a2
Create Date: 2016-06-02 10:35:07.879000

"""

# revision identifiers, used by Alembic.
revision = 'c1728858aaff'
down_revision = '4195ae4623e1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('program_activity',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('program_activity_id', sa.Integer(), nullable=False),
    sa.Column('budget_year', sa.Text(), nullable=False),
    sa.Column('agency_id', sa.Text(), nullable=False),
    sa.Column('allocation_transfer_id', sa.Text(), nullable=True),
    sa.Column('account_number', sa.Text(), nullable=False),
    sa.Column('program_activity_code', sa.Text(), nullable=False),
    sa.Column('program_activity_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('program_activity_id')
    )
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('program_activity')
    ### end Alembic commands ###


def upgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
