from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import UUID4, BaseModel, Field, PositiveInt


class OrganizationsListSchema(BaseModel):
    id: PositiveInt
    tin: PositiveInt
    description: str
    is_body_empty: bool
    region_id: PositiveInt
    form: str
    format_id: Optional[str] = None
    site_url: str
    updated_at: datetime
    base_year: Optional[PositiveInt] = None
    uuid: str


class UserListSchema(BaseModel):
    id: PositiveInt
    updated_at: datetime
    last_name: str
    first_name: str
    middle_name: str
    birth_date: Optional[datetime] = None
    sex: Optional[str] = None
    phone_number: str
    email: str
    organization_id: PositiveInt
    organization_inn: str
    is_active: bool
    position: str
    uuid: Optional[str] = None
    consent_personal_data: bool


class NameValuePair(BaseModel):

    name: str
    value: Any


class LeadSchema(BaseModel):
    vp_date_modified: Optional[NameValuePair] = Field(default=None)
    last_name: Optional[NameValuePair] = Field(default=None)
    first_name: Optional[NameValuePair] = Field(default=None)
    second_name: Optional[NameValuePair] = Field(default=None)
    phone_mobile: Optional[NameValuePair] = Field(default=None)
    email1: Optional[NameValuePair] = Field(default=None)
    acc_portal_id: Optional[NameValuePair] = Field(default=None)
    account_name: Optional[NameValuePair] = Field(default=None)
    acc_portal_inn: Optional[NameValuePair] = Field(default=None)
    portal_user: Optional[NameValuePair] = Field(default=None)
    lead_source: Optional[NameValuePair] = Field(default=None)
    status: Optional[NameValuePair] = Field(default=None)


class AppealsSchema(BaseModel):
    id: str
    entry_list: Dict[str, Dict[str, Any]]


class ChatMessageSchema(BaseModel):
    id: str
    entry_list: Dict[str, Dict[str, Any]]