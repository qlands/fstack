"""Initial version

Revision ID: 9147a676fbff
Revises: 
Create Date: 2020-09-06 22:55:09.999025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9147a676fbff"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("user_id", sa.Unicode(length=120), nullable=False),
        sa.Column("user_name", sa.Unicode(length=120), nullable=True),
        sa.Column("user_email", sa.Unicode(length=120), nullable=True),
        sa.Column("user_password", sa.UnicodeText(), nullable=True),
        sa.Column("user_about", sa.UnicodeText(), nullable=True),
        sa.Column("user_cdate", sa.DateTime(), nullable=True),
        sa.Column("user_llogin", sa.DateTime(), nullable=True),
        sa.Column(
            "user_super", sa.INTEGER(), server_default=sa.text("'0'"), nullable=True
        ),
        sa.Column(
            "user_active", sa.INTEGER(), server_default=sa.text("'1'"), nullable=True
        ),
        sa.Column("user_apikey", sa.Unicode(length=64), nullable=True),
        sa.Column("tags", sa.UnicodeText(), nullable=True),
        sa.Column("extras", sa.UnicodeText(), nullable=True),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_user")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
