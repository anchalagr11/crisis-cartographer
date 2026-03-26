from enum import Enum

class CrisisType(Enum):
    WAR = "war"
    FAMINE = "famine"
    EPIDEMIC = "epidemic"
    DISASTER = "disaster"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"