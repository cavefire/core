"""Consts for OneDrive tests."""

from html import escape
from json import dumps

from onedrive_personal_sdk.models.items import (
    File,
    Hashes,
    IdentitySet,
    ItemParentReference,
    User,
)

CLIENT_ID = "1234"
CLIENT_SECRET = "5678"


BACKUP_METADATA = {
    "addons": [],
    "backup_id": "23e64aec",
    "date": "2024-11-22T11:48:48.727189+01:00",
    "database_included": True,
    "extra_metadata": {},
    "folders": [],
    "homeassistant_included": True,
    "homeassistant_version": "2024.12.0.dev0",
    "name": "Core 2024.12.0.dev0",
    "protected": False,
    "size": 34519040,
}

INSTANCE_ID = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0"

IDENTITY_SET = IdentitySet(
    user=User(
        display_name="John Doe",
        id="id",
        email="john@doe.com",
    )
)

MOCK_BACKUP_FILE = File(
    id="id",
    name="23e64aec.tar",
    size=34519040,
    parent_reference=ItemParentReference(
        drive_id="mock_drive_id", id="id", path="path"
    ),
    hashes=Hashes(
        quick_xor_hash="hash",
    ),
    mime_type="application/x-tar",
    created_by=IDENTITY_SET,
)

MOCK_METADATA_FILE = File(
    id="id",
    name="23e64aec.tar",
    size=34519040,
    parent_reference=ItemParentReference(
        drive_id="mock_drive_id", id="id", path="path"
    ),
    hashes=Hashes(
        quick_xor_hash="hash",
    ),
    mime_type="application/x-tar",
    description=escape(
        dumps(
            {
                "metadata_version": 2,
                "backup_id": "23e64aec",
                "backup_file_id": "id",
            }
        )
    ),
    created_by=IDENTITY_SET,
)
