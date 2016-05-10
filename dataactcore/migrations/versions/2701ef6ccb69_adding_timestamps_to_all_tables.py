"""adding timestamps to all tables

Revision ID: 2701ef6ccb69
Revises: 19c18c1545c3
Create Date: 2016-04-20 14:19:25.366380

"""

# revision identifiers, used by Alembic.
revision = '2701ef6ccb69'
down_revision = '19c18c1545c3'
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
    op.add_column('error_data', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('error_data', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('error_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('error_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('file', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('file', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('updated_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('status', 'updated_at')
    op.drop_column('status', 'created_at')
    op.drop_column('file', 'updated_at')
    op.drop_column('file', 'created_at')
    op.drop_column('error_type', 'updated_at')
    op.drop_column('error_type', 'created_at')
    op.drop_column('error_data', 'updated_at')
    op.drop_column('error_data', 'created_at')
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('file_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('job_dependency', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('job_dependency', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('job_status', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('job_status', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('submission', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('submission', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('type', 'updated_at')
    op.drop_column('type', 'created_at')
    op.drop_column('submission', 'updated_at')
    op.drop_column('submission', 'created_at')
    op.drop_column('status', 'updated_at')
    op.drop_column('status', 'created_at')
    op.drop_column('job_status', 'updated_at')
    op.drop_column('job_status', 'created_at')
    op.drop_column('job_dependency', 'updated_at')
    op.drop_column('job_dependency', 'created_at')
    op.drop_column('file_type', 'updated_at')
    op.drop_column('file_type', 'created_at')
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_template', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('email_template', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('email_template_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('email_template_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('email_token', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('email_token', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('permission_type', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('permission_type', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('user_status', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user_status', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('user_status', 'updated_at')
    op.drop_column('user_status', 'created_at')
    op.drop_column('permission_type', 'updated_at')
    op.drop_column('permission_type', 'created_at')
    op.drop_column('email_token', 'updated_at')
    op.drop_column('email_token', 'created_at')
    op.drop_column('email_template_type', 'updated_at')
    op.drop_column('email_template_type', 'created_at')
    op.drop_column('email_template', 'updated_at')
    op.drop_column('email_template', 'created_at')
    ### end Alembic commands ###

def upgrade_validation():
    pass

def downgrade_validation():
    pass
