from alembic import op
import sqlalchemy as sa

revision = 'your_revision_id'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'))
    )

def downgrade():
    op.drop_table('freebies')
