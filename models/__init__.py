from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class UserRole(Enum):
    FARMER           = "Farmer"
    EXTENSION_OFFICER = "Extension Officer"
    COOPERATIVE_LEADER = "Cooperative Leader"
    ADMINISTRATOR    = "Administrator"

class TransactionType(Enum):
    REVENUE = "Revenue"
    COST    = "Cost"

@dataclass
class User:
    user_id:       int
    full_name:     str
    phone:         str
    password_hash: str
    role:          UserRole = UserRole.FARMER
    region:        str      = "Kigali"
    village:       str      = ""
    language:      str      = "English"
    created_at:    datetime = field(default_factory=datetime.now)
    is_active:     bool     = True

@dataclass
class FinancialRecord:
    record_id:        int
    user_id:          int
    season:           str
    transaction_type: TransactionType
    category:         str
    description:      str
    amount:           float
    recorded_at:      datetime = field(default_factory=datetime.now)
    is_synced:        bool     = False  # offline-first (NFR6)

@dataclass
class PestReport:
    report_id:             int
    user_id:               int
    pest_name:             str
    symptoms:              str
    diagnosis_result:      str
    recommended_treatment: str
    reported_at:           datetime = field(default_factory=datetime.now)
    is_synced:             bool     = False

@dataclass
class PlantingAdvisory:
    advisory_id:          int
    user_id:              int
    region:               str
    bean_variety:         str
    weather_summary:      str
    soil_preparation_tips:str
    generated_at:         datetime = field(default_factory=datetime.now)